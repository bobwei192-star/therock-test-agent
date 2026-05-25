from typing import Any, Optional
from langgraph.runtime import Runtime
from ..state import AgentState, AgentContext
from ..prompts import get_planner_prompt
from ..memory_manager import MemoryManager
from .utils import _invoke_llm


def planner(state: AgentState, runtime: Runtime[AgentContext], agent: Any, interrupt_enabled: bool = True) -> dict:
    memory = MemoryManager(runtime)

    print(f"\n{'=' * 60}")
    print(
        f"[DEBUG planner] Runtime context: user_id={runtime.context.user_id}, project_id={runtime.context.project_id}"
    )
    print(f"[DEBUG planner] Query: {state.get('requirement', '')[:80]}...")
    if state.get("feedback"):
        print(
            "[DEBUG planner] Re-plan mode from sandbox feedback: "
            f"{state.get('feedback', '')[:160]}..."
        )

    memories = memory.search("plans", query=state.get("requirement", ""), limit=3)
    memory_hints = memory.format_hints(memories)

    print(f"[DEBUG planner] Retrieved {len(memories)} memories:")
    for i, m in enumerate(memories):
        data = m.value.get("data", "")[:100] if hasattr(m, "value") else str(m)[:100]
        print(f"  [{i}] key={m.key}, data={data}...")
    print(f"[DEBUG planner] Formatted hints length: {len(memory_hints)} chars")
    print(f"{'=' * 60}\n")

    prompt = get_planner_prompt(
        requirement=state.get("requirement", ""),
        context=state.get("context", {}),
        memory_hints=memory_hints,
        feedback=state.get("feedback", ""),
        execution_result=state.get("execution_result", {}),
    )
    case_plan = _invoke_llm(agent, prompt, node_name="planner")

    memory_key = memory.save_plan(
        requirement=state.get("requirement", ""),
        case_plan=case_plan,
    )

    print(f"\n[DEBUG planner] ✅ Wrote memory: key={memory_key}")

    # CLI 模式下不使用 interrupt，直接继续执行
    # 人机交互确认将在 CLI 层单独处理

    return {
        "case_plan": case_plan,
        "messages": [
            {"role": "assistant", "content": f"Case plan generated.\n{case_plan[:500]}"}
        ],
    }