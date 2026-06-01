"""需求解析节点 —— 解析用户需求并识别意图

根据 guide/09_promot优化.md 设计：
- 从状态中提取用户原始需求
- 使用规则匹配识别意图类型（9种意图）
- 调用 LLM 将自然语言需求转换为结构化需求
- 将解析结果保存到长期记忆

支持的意图类型：GENERATE/APPEND/UPDATE/REFACTOR/EXECUTE_EXTERNAL/DIAGNOSE/COVERAGE/PROBE/ENV_BUILD
"""

from typing import Any, Optional
from langchain_core.messages import HumanMessage, AIMessage

from ..state import AgentState, AgentContext
from ..prompts import get_requirement_parser_prompt
from ..intent_router import route_intent, get_intent_cluster, get_template_name
from ..logging_config import get_logger
from .utils import _last_user_message
from ..utils.clean_llm_output import clean_llm_output, extract_intent_from_llm_response

_logger = get_logger("nodes.requirement_parser")


def get_llm(agent: Any = None) -> Any:
    """模块级 LLM 访问器 —— 测试时可被 patch"""
    return agent


def get_memory_manager(runtime: Any = None) -> Any:
    """模块级 MemoryManager 访问器 —— 测试时可被 patch"""
    if runtime is None:
        return None
    from ..memory_manager import MemoryManager
    return MemoryManager(runtime)


def requirement_parser(
    state: AgentState, runtime: Any = None, agent: Any = None
) -> dict:
    """需求解析节点主函数

    执行流程：
    1. 从状态中提取用户原始需求（优先使用 state.requirement，回退到最后一条用户消息）
    2. 使用规则匹配识别意图类型
    3. 获取意图聚类和对应的提示词模板名称
    4. 调用 LLM 将自然语言需求转换为结构化需求
    5. 将解析结果保存到长期记忆

    Args:
        state: Agent 运行时状态
        runtime: LangGraph 运行时实例（用于访问长期记忆）
        agent: deepagents Agent 实例

    Returns:
        更新后的状态字段字典
    """
    # 提取用户原始需求
    raw_requirement = state.get("requirement") or _last_user_message(state)

    # 意图识别（规则匹配，无需 LLM）
    parsed_intent = route_intent(raw_requirement)
    intent_cluster = get_intent_cluster(parsed_intent)
    template_name = get_template_name(parsed_intent)

    _logger.info(
        "intent_detected",
        raw=raw_requirement[:50],
        intent=parsed_intent,
        cluster=intent_cluster,
        template=template_name,
    )
    
    # DEBUG: 追踪 CHAT 意图处理
    if parsed_intent == "CHAT":
        _logger.info("chat_intent_detected", 
                    raw_input=raw_requirement,
                    action="Preparing friendly response for chat intent")

    # 获取需求解析提示词并调用 LLM
    prompt = get_requirement_parser_prompt(raw_requirement)

    # 使用可 patch 的 LLM 访问器，便于测试
    llm = get_llm(agent)
    if llm is not None:
        llm_result = llm.invoke({"messages": [HumanMessage(content=prompt)]})
    else:
        from .utils import _invoke_llm
        llm_result = _invoke_llm(agent, prompt, node_name="requirement_parser")

    # 提取 LLM 响应内容
    if hasattr(llm_result, "content"):
        content = llm_result.content
    elif isinstance(llm_result, dict):
        # 允许测试中使用 dict 格式覆盖意图字段
        if "intent" in llm_result:
            parsed_intent = llm_result["intent"]
            intent_cluster = llm_result.get("cluster", intent_cluster)
        content = llm_result.get("raw_spec", str(llm_result))
    else:
        content = str(llm_result)

    # 清洗 LLM 输出，移除调试信息和技术性内容
    content = clean_llm_output(content)

    # 尝试从清洗后的内容中提取意图（如果之前规则匹配失败）
    if parsed_intent not in ["GENERATE", "APPEND", "UPDATE", "REFACTOR", "EXECUTE_EXTERNAL", "DIAGNOSE", "COVERAGE", "PROBE", "ENV_BUILD", "CHAT"]:
        extracted_intent = extract_intent_from_llm_response(content)
        if extracted_intent:
            parsed_intent = extracted_intent
            intent_cluster = get_intent_cluster(parsed_intent)
            template_name = get_template_name(parsed_intent)
            _logger.info("intent_extracted_from_llm", intent=parsed_intent)

    # 保存到长期记忆
    memory = get_memory_manager(runtime)
    if memory is not None:
        memory.save_requirement(
            raw_requirement=raw_requirement,
            parsed_requirement=content,
        )

    # 返回更新的状态字段
    return {
        "requirement": raw_requirement,
        "parsed_requirement": content,
        "parsed_intent": parsed_intent,
        "intent": parsed_intent,
        "intent_cluster": intent_cluster,
        "cluster": intent_cluster,
        "template_name": template_name,
        "messages": [AIMessage(content=content)],
    }
