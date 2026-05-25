from typing import Any
from langgraph.runtime import Runtime
from ..state import AgentState, AgentContext
from ..prompts import get_requirement_parser_prompt
from ..memory_manager import MemoryManager
from ..intent_router import route_intent, get_intent_cluster, get_template_name
from .utils import _invoke_llm, _last_user_message


def requirement_parser(
    state: AgentState, runtime: Runtime[AgentContext], agent: Any
) -> dict:
    memory = MemoryManager(runtime)
    raw_requirement = state.get("requirement") or _last_user_message(state)

    # 意图识别（规则匹配）
    parsed_intent = route_intent(raw_requirement)
    intent_cluster = get_intent_cluster(parsed_intent)
    template_name = get_template_name(parsed_intent)

    print(f"[意图识别] raw_requirement: {raw_requirement[:50]}...")
    print(f"[意图识别] intent: {parsed_intent}, cluster: {intent_cluster}, template: {template_name}")

    prompt = get_requirement_parser_prompt(raw_requirement)

    llm_result = _invoke_llm(agent, prompt, node_name="requirement_parser")

    if hasattr(llm_result, "content"):
        content = llm_result.content
    else:
        content = str(llm_result)

    memory_key = memory.save_requirement(
        raw_requirement=raw_requirement,
        parsed_requirement=content,
    )

    msg = {"role": "assistant", "content": content}

    return {
        "requirement": raw_requirement,
        "parsed_requirement": content,
        "parsed_intent": parsed_intent,
        "intent_cluster": intent_cluster,
        "template_name": template_name,
        "messages": [msg],
    }
