"""LangGraph 状态图定义模块 - TestCaseAgent 的核心编排逻辑。

本文件定义了 Agent 的有向状态图（StateGraph），将各个处理节点
（需求解析、上下文检索、计划生成、代码生成、沙盒执行）串联为完整的工作流。

调用的框架/库：
- langgraph: 状态图编排框架，提供 StateGraph、条件边、RetryPolicy
- deepagents: 深度 Agent 创建库，封装 LLM + Tools 为可调用 Agent
- functools.partial: 用于为节点函数绑定额外参数（model、agent）
"""

from functools import partial
from langgraph.graph import StateGraph, START, END
from langgraph.types import RetryPolicy
from .tools import TOOLS

from .state import AgentState, AgentContext
from .nodes import (
    context_retriever,
    generator,
    planner,
    requirement_parser,
    sandbox_executor,
)


# Agent 的系统提示词，定义角色和行为约束
DEFAULT_SYSTEM_PROMPT = (
    "你是一个测试用例生成专家。"
    "你会先规划测试用例，再生成最小可执行的测试草案。"
    "当涉及外部资源（如 HuggingFace 模型、GitHub 仓库, Docker 镜像，Artifactory ）时，你必须先调用相应工具确认资源存在及最新状态，禁止凭记忆假设"
)

# 沙盒执行节点的重试策略：最大重试 3 次，指数退避（1s → 2s → 4s），上限 10s
SANDBOX_RETRY_POLICY = RetryPolicy(
    max_attempts=3,
    initial_interval=1.0,
    backoff_factor=2.0,
    max_interval=10.0,
)


def route_after_sandbox(state: AgentState) -> str:
    """沙盒执行后的条件路由函数。

    根据执行结果决定下一步走向：
    - 成功 → 结束图（END）
    - 失败且未超过最大重试次数 → 回到 planner 重新规划
    - 失败且已耗尽重试 → 终止（END，表示终端失败）
    """
    result = state.get("execution_result", {})
    if result.get("status") == "success":
        return END
    # RetryPolicy 会自动处理重试，这里只需决定是否进入修复流程
    if state.get("sandbox_retry_count", 0) < state.get("max_sandbox_retries", 3):
        return "planner"
    return END


def build_graph(
    model=None,
    tools=None,
    checkpointer=None,
    store=None,
    system_prompt: str | None = None,
):
    """构建并编译 LangGraph 状态图。

    参数:
        model: ChatOpenAI 兼容的 LLM 实例，为 None 时构建结构图（无 LLM 能力）
        tools: Agent 可使用的工具列表，默认使用全局 TOOLS
        checkpointer: 检查点持久化后端（如 MemorySaver），用于支持多轮对话
        store: 长期记忆存储后端（如 InMemoryStore），用于跨会话记忆
        system_prompt: 自定义系统提示词，覆盖默认值

    返回:
        编译后的 LangGraph CompiledGraph 实例
    """
    # 创建 deepagents Agent（封装了 LLM + Tools + System Prompt）
    agent = None
    if model is not None:
        from deepagents import create_deep_agent

        all_tools = tools if tools is not None else TOOLS
        agent = create_deep_agent(
            model=model,
            tools=all_tools,
            system_prompt=system_prompt or DEFAULT_SYSTEM_PROMPT,
        )

    # 使用 partial 为各节点函数绑定 agent/model 参数
    requirement_parser_with_agent = partial(requirement_parser, agent=agent)
    planner_with_agent = partial(planner, agent=agent)
    generator_with_model = partial(generator, model=model)

    # 构建状态图，指定状态类型和上下文 schema
    builder = StateGraph(AgentState, context_schema=AgentContext)

    # 注册各处理节点
    builder.add_node("requirement_parser", requirement_parser_with_agent)
    builder.add_node("context_retriever", context_retriever)
    builder.add_node("planner", planner_with_agent)
    builder.add_node("generator", generator_with_model)
    builder.add_node("sandbox_executor", sandbox_executor, retry_policy=SANDBOX_RETRY_POLICY)

    # 定义节点间的线性边（顺序执行流）
    builder.add_edge(START, "requirement_parser")
    builder.add_edge("requirement_parser", "context_retriever")
    builder.add_edge("context_retriever", "planner")
    builder.add_edge("planner", "generator")
    builder.add_edge("generator", "sandbox_executor")

    # 沙盒执行后的条件路由：成功则结束，失败则回到 planner 重新规划
    builder.add_conditional_edges(
        "sandbox_executor",
        route_after_sandbox,
        {
            "planner": "planner",
            END: END,
        },
    )

    # 编译图，注入持久化组件
    compile_kwargs = {}
    if checkpointer is not None:
        compile_kwargs["checkpointer"] = checkpointer
    if store is not None:
        compile_kwargs["store"] = store

    return builder.compile(**compile_kwargs)
