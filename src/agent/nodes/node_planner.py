import uuid
from typing import Any
from langgraph.runtime import Runtime
from ..state import AgentState, AgentContext
from .utils import _invoke_llm, _memory_namespace, _format_memories


def planner(state: AgentState, runtime: Runtime[AgentContext], agent: Any) -> dict:
    ns = _memory_namespace(runtime, "plans")

    print(f"\n{'=' * 60}")
    print(
        f"[DEBUG planner] Runtime context: user_id={runtime.context.user_id}, project_id={runtime.context.project_id}"
    )
    print(f"[DEBUG planner] Memory namespace: {ns}")
    print(f"[DEBUG planner] Query: {state.get('requirement', '')[:80]}...")

    memories = runtime.store.search(ns, query=state.get("requirement", ""), limit=3)
    memory_hints = _format_memories(memories)

    print(f"[DEBUG planner] Retrieved {len(memories)} memories:")
    for i, m in enumerate(memories):
        data = m.value.get("data", "")[:100] if hasattr(m, "value") else str(m)[:100]
        print(f"  [{i}] key={m.key}, data={data}...")
    print(f"[DEBUG planner] Formatted hints length: {len(memory_hints)} chars")
    print(f"{'=' * 60}\n")

    prompt = (
        "你是 Test Case Agent 的规划器。基于上游提供的测试规格，输出可执行的工程计划。"
        "不要重复解释等价类理论或 AAAC 原则（上游已分析），直接引用规格中的测试点做编排决策。\n\n"
        f"原始需求:\n{state.get('requirement', '')}\n\n"
        f"上下文:\n{state.get('context', {})}\n"
        f"{memory_hints}\n"
        "按以下格式输出执行计划（不要解释，只输出结构）:\n"
        "1. 测试目标: <一句话，引用或确认规格中的目标>\n"
        "2. Suite 划分与类名映射:\n"
        "   - Suite: <冒烟/功能/边界/错误处理> | 类名: <TestXxx> | 包含测试点: <引用规格中的测试点编号/名称>\n"
        "3. 前置条件:\n"
        "   - 环境: <ROCm版本/GPU型号/驱动要求/命令PATH要求>\n"
        "   - 数据: <需要预置的文件/配置/环境变量>\n"
        "   - 权限: <root/普通用户/特定组权限>\n"
        "4. 执行顺序与依赖:\n"
        "   - 步骤1: <存在性探测/命令可用性检查，失败则后续skip>\n"
        "   - 步骤2: <有效等价类测试执行，串行或并行策略>\n"
        "   - 步骤3: <边界值测试执行，建议串行避免GPU状态干扰>\n"
        "   - 步骤4: <无效等价类/降级测试执行>\n"
        "5. 预期结果映射:\n"
        "   - 有效类: <返回码0/输出包含关键词/数值在规格给定范围内>\n"
        "   - 无效类: <pytest.skip/非零返回码/异常信息包含指定关键词>\n"
        "6. 风险与应对:\n"
        "   - 风险: <GPU被占用导致状态干扰/温度波动导致精确数值断言失败/ROCm版本差异导致输出格式变化>\n"
        "   - 应对: <串行执行标记/范围断言替代精确匹配/多版本关键词兼容>\n"
        "7. Fixture 复用与作用域方案:\n"
        "   - 共享Fixture: <命令执行器(scope=module)/GPU计数(scope=module)>\n"
        "   - 独占Fixture: <临时文件(scope=function)/环境隔离(scope=class)>\n"
        "   - Skip逻辑集中点: <在共享Fixture内统一处理命令缺失/无GPU，避免每个测试重复检查>\n"
    )
    case_plan = _invoke_llm(agent, prompt, node_name="planner")

    memory_key = f"plan_{uuid.uuid4().hex[:8]}"
    memory_value = {
        "data": f"需求: {state.get('requirement', '')[:120]}... | 计划摘要: {case_plan[:200]}...",
        "requirement": state.get("requirement", ""),
        "full_plan": case_plan,
    }
    runtime.store.put(ns, memory_key, memory_value)

    print(f"\n[DEBUG planner] ✅ Wrote memory: key={memory_key}, namespace={ns}")
    print(f"[DEBUG planner] Memory value preview: {memory_value['data'][:100]}...")

    return {
        "case_plan": case_plan,
        "messages": [
            {"role": "assistant", "content": f"Case plan generated.\n{case_plan[:500]}"}
        ],
    }
