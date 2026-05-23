"""测试代码生成节点 —— 使用底层 model 避免 HITL"""

import uuid
import os
from datetime import datetime
from typing import Any

from langgraph.runtime import Runtime

from ..state import AgentState, AgentContext
from .utils import (
    _invoke_llm,
    _extract_code,
    _validate_real_test_code,
    _memory_namespace,
    _format_memories,
    _looks_like_python_code,
)

OUTPUT_DIR = "/home/zx/TestCaseAgent/output"


def _save_test_file(code: str) -> str:
    """保存测试代码到文件，返回文件路径。"""
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"test_generated_{timestamp}.py"
    filepath = os.path.join(OUTPUT_DIR, filename)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(code)

    print(f"\n[DEBUG generator] ✅ 测试文件已保存: {filepath}")
    return filepath


def generator(state: AgentState, runtime: Runtime[AgentContext], model: Any) -> dict:
    """
    使用底层 ChatOpenAI model 直接调用，避免 Agent 的 HITL 拦截。
    
    Args:
        model: 底层 ChatOpenAI 实例（从 graph.py 传入）
    """
    ns = _memory_namespace(runtime, "generations")

    print(f"\n{'=' * 60}")
    print(f"[DEBUG generator] Memory namespace: {ns}")
    print(f"[DEBUG generator] Query (case_plan): {state.get('case_plan', '')[:80]}...")

    memories = runtime.store.search(ns, query=state.get("case_plan", ""), limit=2)
    memory_hints = _format_memories(memories)

    print(f"[DEBUG generator] Retrieved {len(memories)} memories:")
    for i, m in enumerate(memories):
        data = m.value.get("data", "")[:100] if hasattr(m, "value") else str(m)[:100]
        print(f"  [{i}] key={m.key}, data={data}...")
    print(f"[DEBUG generator] Formatted hints length: {len(memory_hints)} chars")
    print(f"{'=' * 60}\n")

    # ========== 历史代码处理（修改/追加模式） ==========
    _MAX_PREVIOUS_CODE_CHARS = 5000
    previous_code = state.get("generated_code") or state.get("code", "")
    previous_code_hint = ""
    if previous_code:
        truncated = previous_code
        if len(previous_code) > _MAX_PREVIOUS_CODE_CHARS:
            truncated = (
                previous_code[:_MAX_PREVIOUS_CODE_CHARS]
                + "\n# ... (已截断，上述代码太长)"
            )

        requirement = state.get("requirement", "").lower()
        is_append_mode = any(
            kw in requirement for kw in ("补充", "追加", "添加", "增加", "新增")
        )
        is_modify_mode = any(
            kw in requirement for kw in ("修改", "改成", "改为", "调整", "修复")
        )

        if is_append_mode:
            action_desc = "补充/追加"
            keep_desc = "保留所有历史测试函数，在其下方追加新函数"
        elif is_modify_mode:
            action_desc = "修改"
            keep_desc = "保留所有未修改的测试函数，只修改指定的部分"
        else:
            action_desc = "修改或补充"
            keep_desc = "保留所有历史测试函数，根据需求修改或追加"

        previous_code_hint = (
            f"\n\n【历史代码 - 必须在此基础上{action_desc}】\n"
            f"```python\n{truncated}\n```\n"
            f"注意：用户要求对代码进行{action_desc}操作。你必须输出修改后的**完整文件**，不要只返回差异或新增部分。\n"
            f"注意：{keep_desc}。禁止删除已有的测试函数。\n"
            f"注意：必须保持原始测试目标不变。如果原始代码测试的是 rocm-smi，修改后仍然必须测试 rocm-smi，"
            f"禁止把测试目标改成测试 helper 函数或内部封装。\n"
        )

    # ========== 核心 Prompt（建设性原则 + 紧凑防御约束） ==========
    prompt = (
        "你是 ROCm 测试代码生成器。将测试计划转化为完整、可执行的 pytest 代码。\n\n"
        f"测试计划:\n{state.get('case_plan', '')}\n"
        f"{memory_hints}\n"
        f"{previous_code_hint}\n\n"
        "## 代码生成原则（必须遵循）\n"
        "1. AAAC 四阶段：每个测试函数用注释标记 # Arrange / # Act / # Assert / # Cleanup，"
        "Cleanup 只在有副作用（写文件、改配置）时需要，只读测试写 '# Cleanup: 无'。\n"
        "2. Fixture 复用：命令探测、GPU 计数等重复 Arrange 逻辑必须抽成 @pytest.fixture(scope='module')，"
        "Fixture 内自动执行 pytest.skip() 处理命令缺失/无 GPU 场景。\n"
        "3. 等价类覆盖：按测试计划中的有效/无效/边界等价类分别生成独立测试函数，"
        "无效等价类使用 pytest.skip() 优雅降级，不抛异常。\n"
        "4. 边界值断言：数值类测试使用范围断言（如 0 <= temp <= 120），禁止断言精确等于具体数值。"
        "禁止断言精确字符串匹配（输出格式可能随 ROCm 版本变化）。\n"
        "5. 错误诊断：每个 assert 必须带诊断消息，包含 returncode、stderr[:500]、stdout[:500]。\n"
        "6. 真实执行：所有测试必须通过 subprocess.run 或等价方式执行真实命令，timeout=30，"
        "禁止 mock、patch、fake output、硬编码输出、注释掉真实执行代码。\n\n"
        "## 强制约束（不可违反）\n"
        "- 输出必须是完整可执行的 Python 文件，包含所有 import 和全部测试函数。\n"
        "- 代码用 ```python ... ``` 包裹，除代码块外不输出任何文字、diff、文件路径或总结。\n"
        "- 修改/追加模式下必须输出完整文件，禁止只返回修改部分或新增部分。\n"
        "- 代码中禁止使用绝对路径（/home/、/tmp/），不使用 save_to_file 调用。\n"
    )

    # ========== 直接调用底层 model ==========
    print(f"\n[generator] 直接调用底层 ChatOpenAI model...")
    try:
        if model is None:
            raise RuntimeError("generator 需要传入底层 model 实例")
        
        response = model.invoke([{"role": "user", "content": prompt}])
        
        if hasattr(response, "content"):
            reply = response.content
        else:
            reply = str(response)

        print(f"[generator] Model response: {len(reply)} chars")

    except Exception as exc:
        print(f"[generator] ❌ Model invoke 失败: {type(exc).__name__}: {exc}")
        import traceback
        traceback.print_exc()
        return {
            "code": "",
            "generated_code": "",
            "explanation": f"Error: {exc}",
            "validation_result": {"status": "failed", "errors": [str(exc)]},
            "messages": [{"role": "assistant", "content": f"生成失败: {exc}"}],
        }

    print(f"\n[DEBUG generator] Raw reply length: {len(reply)} chars")
    print(f"[DEBUG generator] Raw reply preview: {reply[:200]}...")

    generated_code, explanation, extraction_status = _extract_code(reply)
    print(f"[DEBUG generator] Extracted code length: {len(generated_code)} chars")
    print(f"[DEBUG generator] Extraction status: {extraction_status}")
    if explanation:
        print(f"[DEBUG generator] Explanation length: {len(explanation)} chars")

    # 验证新代码
    if not generated_code:
        validation_result = {
            "status": "failed",
            "quality_gate": "real_pytest_code",
            "errors": ["LLM did not return valid Python code block."],
        }
    else:
        quality_issues = _validate_real_test_code(generated_code)
        validation_result = {
            "status": "failed" if quality_issues else "passed",
            "quality_gate": "real_pytest_code",
            "errors": quality_issues,
        }

    # 验证失败时保留上一轮有效代码
    old_code = state.get("generated_code") or state.get("code", "")
    final_code = generated_code

    if validation_result["status"] == "failed":
        if old_code and _looks_like_python_code(old_code)[0]:
            print(
                f"\n[DEBUG generator] 新代码验证失败({len(generated_code)} chars)，保留上一轮有效代码({len(old_code)} chars)"
            )
            final_code = old_code
            validation_result["errors"].insert(
                0,
                f"New generation failed ({extraction_status}). Kept previous {len(old_code)} chars code.",
            )
        else:
            print(f"\n[DEBUG generator] 新代码验证失败，且无旧代码可保留")

    # 保存文件
    saved_filepath = None
    if final_code:
        saved_filepath = _save_test_file(final_code)
        print(f"\n[DEBUG generator] 📁 文件已保存: {saved_filepath}")
    else:
        print(f"\n[DEBUG generator] ⚠️ 没有有效代码可保存")

    # 写入记忆
    memory_key = f"gen_{uuid.uuid4().hex[:8]}"
    memory_value = {
        "data": f"为需求 [{state.get('requirement', '')[:80]}...] 最终保留 {len(final_code)} 字符代码",
        "code_preview": final_code[:500] if final_code else "EXTRACTION_FAILED",
        "saved_filepath": saved_filepath,
    }
    runtime.store.put(ns, memory_key, memory_value)

    print(f"\n[DEBUG generator] ✅ Wrote memory: key={memory_key}, namespace={ns}")

    return {
        "code": final_code,
        "generated_code": final_code,
        "explanation": explanation,
        "validation_result": validation_result,
        "saved_filepath": saved_filepath,
        "messages": [{"role": "assistant", "content": reply}],
    }