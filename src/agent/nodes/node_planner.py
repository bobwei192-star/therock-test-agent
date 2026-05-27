from typing import Any, Optional
from ..state import AgentState, AgentContext
from ..prompts import get_planner_prompt
from .utils import _invoke_llm


def get_llm(agent: Any = None) -> Any:
    """Module-level LLM accessor — patchable in tests."""
    return agent


def get_memory_manager(runtime: Any = None) -> Any:
    """Module-level MemoryManager accessor — patchable in tests."""
    if runtime is None:
        return None
    from ..memory_manager import MemoryManager
    return MemoryManager(runtime)


def planner(state: AgentState, runtime: Any = None, agent: Any = None, interrupt_enabled: bool = True) -> dict:
    memory = get_memory_manager(runtime)

    if runtime is not None:
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

    memories = []
    memory_hints = ""
    if memory is not None:
        memories = memory.search("plans", query=state.get("requirement", ""), limit=3)
        raw_hints = memory.format_hints(memories)
        memory_hints = raw_hints if isinstance(raw_hints, str) else ""

        try:
            print(f"[DEBUG planner] Retrieved {len(memories)} memories:")
            for i, m in enumerate(memories):
                data = m.value.get("data", "")[:100] if hasattr(m, "value") else str(m)[:100]
                print(f"  [{i}] key={m.key}, data={data}...")
        except Exception:
            pass
        print(f"[DEBUG planner] Formatted hints length: {len(memory_hints) if isinstance(memory_hints, str) else '?'} chars")
    if runtime is not None:
        print(f"{'=' * 60}\n")

    prompt = get_planner_prompt(
        requirement=state.get("requirement", "") or state.get("parsed_requirement", ""),
        context=state.get("context", {}),
        memory_hints=memory_hints,
        feedback=state.get("feedback", ""),
        execution_result=state.get("execution_result", {}),
    )

    # Use get_llm so tests can patch this module's get_llm
    llm = get_llm(agent)
    if llm is not None:
        response = llm.invoke({"messages": [{"role": "user", "content": prompt}]})
        case_plan = response.content if hasattr(response, "content") else str(response)
    else:
        case_plan = _invoke_llm(agent, prompt, node_name="planner")

    if memory is not None:
        memory_key = memory.save_plan(
            requirement=state.get("requirement", ""),
            case_plan=case_plan,
        )
        # Also call save_memory for backward compatibility
        if hasattr(memory, "save_memory"):
            memory.save_memory(data=case_plan, key=memory_key)
        print(f"\n[DEBUG planner] ✅ Wrote memory: key={memory_key}")

    return {
        "case_plan": case_plan,
        "messages": [
            {"role": "assistant", "content": f"Case plan generated.\n{case_plan[:500]}"}
        ],
    }