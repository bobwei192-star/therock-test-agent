"""Agent 运行器模块 —— 提供图执行的高层封装接口

本模块提供：
1. create_initial_state(): 创建初始状态字典
2. build_runnable_graph(): 构建可执行的图实例（带模型）
3. build_runtime_config(): 构建运行时配置（含追踪元数据）
4. run_once(): 单轮执行入口
5. run_multi_turn(): 多轮对话执行入口

持久化策略：
- 开发环境: 使用 MemorySaver（内存存储）
- 生产环境: 设置 TEST_CASE_AGENT_POSTGRES_URL 启用 PostgreSQL 持久化

多轮对话策略：
- 第一轮：传入完整初始状态
- 后续轮：只传增量更新，Checkpointer 自动恢复历史状态
"""

import copy
import os
import time
from collections.abc import Iterable
from typing import Any

from langchain_core.messages import HumanMessage

from .graph import build_graph
from .model import build_model
from .state import AgentState, AgentContext
from .tools import TOOLS
from .tracing import build_langfuse_config, flush_langfuse
from .logging_config import get_logger
from .config import get_config, print_config_warnings

# 初始化日志器
logger = get_logger("runner")


def create_initial_state(user_prompt: str) -> AgentState:
    """创建 Agent 的初始状态字典。

    Args:
        user_prompt: 用户输入的初始提示词

    Returns:
        AgentState: 包含所有必需字段的初始状态
    """
    return {
        "messages": [HumanMessage(content=user_prompt)],
        "requirement": user_prompt,
        "context": {},
        "case_plan": "",
        "code": "",
        "generated_code": "",
        "explanation": "",
        "validation_result": {},
        "execution_plan": {},
        "execution_result": {},
        "parsed_result": {},
        "repair_suggestion": "",
        "final_report": {},
        "retry": 0,
        "repair_count": 0,
        "saved_filepath": "",
        "sandbox_config": {
            "provider": os.environ.get(
                "TEST_CASE_AGENT_SANDBOX_PROVIDER", "remote_ssh_docker"
            ),
            "image": os.environ.get(
                "TEST_CASE_AGENT_SANDBOX_IMAGE",
                "rocm/dev-ubuntu-22.04:6.0",
            ),
            "block_network": False,
            "timeout": 120,
            "remote_host": os.environ.get(
                "TEST_CASE_AGENT_REMOTE_HOST", ""
            ),
            "remote_user": os.environ.get("TEST_CASE_AGENT_REMOTE_USER", "jenkins"),
            "remote_work_dir": os.environ.get(
                "TEST_CASE_AGENT_REMOTE_WORK_DIR", "/tmp/testcase_agent"
            ),
            "device_name": os.environ.get(
                "TEST_CASE_AGENT_DEVICE_NAME", "/dev/kfd,/dev/dri"
            ),
        },
        "sandbox_id": "",
        "sandbox_retry_count": 0,
        "max_sandbox_retries": 3,
        "feedback": "",
        "error_log": [],
        "session_id": "",
    }


def build_runnable_graph(
    provider: str | None = None,
    tools: list[Any] | None = None,
    enable_checkpoint: bool = True,
    enable_store: bool = True,
):
    """构建带模型的可执行图实例。

    Args:
        provider: LLM Provider 名称（amd/deepseek/openai/ark/yuanyuai/generic）
        tools: Agent 可用的工具列表
        enable_checkpoint: 是否启用检查点（短期记忆）
        enable_store: 是否启用存储（长期记忆）

    Returns:
        编译后的 LangGraph CompiledGraph 实例
    """
    model = build_model(provider=provider)
    # ✅ 恢复原生持久化存储能力
    # graph.py 内部自动选择 MemorySaver 或 PostgreSQL Checkpointer/Store
    # - 开发环境: InMemoryStore（内存存储）
    # - 生产环境: 设置 TEST_CASE_AGENT_POSTGRES_URL 启用 PostgreSQL
    return build_graph(
        model=model,
        tools=tools if tools is not None else TOOLS,
        checkpointer=None,  # 在 build_graph 中自动选择
        store=None,  # 在 build_graph 中自动选择
        use_persistence=True,  # ✅ 启用持久化，恢复长期记忆能力
    )


def build_runtime_config(thread_id: str) -> dict[str, Any]:
    """构建 LangGraph 运行时配置（含追踪元数据）。

    Args:
        thread_id: 会话/线程标识

    Returns:
        运行时配置字典
    """
    config: dict[str, Any] = {"configurable": {"thread_id": thread_id}}
    config.update(build_langfuse_config(thread_id=thread_id))
    return config


def run_once(
    user_prompt: str,
    provider: str | None = None,
    thread_id: str = "test-case-agent-debug",
    enable_checkpoint: bool = True,
    enable_store: bool = True,
    user_id: str = "default_user",
    project_id: str | None = None,
) -> AgentState:
    """单轮执行入口 —— 执行完整的测试用例生成流程。

    Args:
        user_prompt: 用户输入需求
        provider: LLM Provider 名称
        thread_id: 会话标识（用于检查点和追踪）
        enable_checkpoint: 是否启用检查点
        enable_store: 是否启用长期记忆存储
        user_id: 用户标识（用于记忆隔离）
        project_id: 项目标识（可选，用于记忆隔离）

    Returns:
        AgentState: 执行完成后的最终状态

    Raises:
        Exception: 执行过程中的任何异常
    """
    # 启动时校验配置，打印警告
    print_config_warnings()

    start_time = time.time()
    logger.info(
        "run_once_start",
        user_prompt=user_prompt[:100] + "..." if len(user_prompt) > 100 else user_prompt,
        provider=provider,
        thread_id=thread_id,
        user_id=user_id,
        project_id=project_id,
    )

    try:
        # 构建可执行图
        graph = build_runnable_graph(
            provider=provider,
            enable_checkpoint=enable_checkpoint,
            enable_store=enable_store,
        )
        logger.debug("graph_built", provider=provider)

        # 构建运行时配置和上下文
        config = build_runtime_config(thread_id=thread_id)
        context = AgentContext(user_id=user_id, project_id=project_id)

        # 执行图
        logger.debug("invoking_graph", thread_id=thread_id)
        result = graph.invoke(
            create_initial_state(user_prompt), config=config, context=context
        )

        # 记录执行结果
        elapsed = time.time() - start_time
        generated_code = result.get("generated_code", "") or result.get("code", "")
        logger.info(
            "run_once_complete",
            elapsed=round(elapsed, 2),
            code_length=len(generated_code),
            has_code=bool(generated_code),
            validation_status=result.get("validation_result", {}).get("status"),
            errors=result.get("error_log", []),
        )

        return result
    except Exception as e:
        elapsed = time.time() - start_time
        logger.exception(
            "run_once_failed",
            elapsed=round(elapsed, 2),
            error=str(e),
            user_prompt=user_prompt[:100] if user_prompt else "",
        )
        raise
    finally:
        flush_langfuse()


def run_multi_turn(
    turns: list[str],
    provider: str | None = None,
    thread_id: str = "multi-turn-test",
    user_id: str = "default_user",
    project_id: str | None = None,
) -> list[AgentState]:
    """多轮对话执行入口 —— 在同一线程中执行多轮对话，Agent 记住上下文。

    多轮对话策略：
    1. 第一轮：传入完整初始状态
    2. 后续轮：只传入增量更新（新消息 + requirement），
       让 Checkpointer 自动恢复历史状态，避免 messages 重复累积
    3. 每轮结束后深拷贝保存结果，避免引用污染

    Args:
        turns: 用户输入的多轮对话列表
        provider: LLM Provider 名称
        thread_id: 会话标识（必须保持一致以维护上下文）
        user_id: 用户标识
        project_id: 项目标识（可选）

    Returns:
        每轮对话的状态列表
    """
    graph = build_runnable_graph(
        provider=provider,
        enable_checkpoint=True,  # ✅ 启用短期记忆（检查点）
        enable_store=True,  # ✅ 启用长期记忆（存储）
    )
    config = build_runtime_config(thread_id=thread_id)
    context = AgentContext(user_id=user_id, project_id=project_id)

    results = []
    try:
        for i, prompt in enumerate(turns):
            print(f"\n{'=' * 60}")
            print(f"TURN {i + 1}: {prompt[:50]}...")
            print(f"{'=' * 60}")

            if i == 0:
                # 第一轮：传入完整初始状态
                state = create_initial_state(prompt)
            else:
                # 后续轮次：只传增量更新
                # Checkpointer 会自动恢复该 thread_id 的历史状态，
                # messages 通过 add_messages reducer 追加，requirement 直接覆盖
                state = {
                    "messages": [HumanMessage(content=prompt)],
                    "requirement": prompt,
                }

            # 调用图执行
            final_state = graph.invoke(state, config=config, context=context)
            # ✅ 深拷贝后再追加，避免 results 里全是同一对象引用
            results.append(copy.deepcopy(final_state))

            # 打印本轮响应摘要
            last_msg = final_state["messages"][-1]
            content = (
                last_msg.content
                if hasattr(last_msg, "content")
                else str(last_msg)
            )
            print(f"Assistant: {content[:300]}...")

        return results
    finally:
        flush_langfuse()
