"""测试代码生成节点 —— 使用底层 model 避免 HITL

根据 guide/09_promot优化.md 设计：
- 支持多种意图：GENERATE/APPEND/UPDATE/REFACTOR/EXECUTE_EXTERNAL/DIAGNOSE/COVERAGE/PROBE/ENV_BUILD
- 根据意图选择不同的提示词模板
- ENV_BUILD 意图生成 Dockerfile，其他意图生成测试代码
"""

import os
from datetime import datetime
from pathlib import Path
from typing import Any

from langgraph.runtime import Runtime

from ..prompts import get_generator_prompt, get_prompt_by_template
from ..state import AgentState, AgentContext
from ..memory_manager import MemoryManager
from ..code_output import parse_llm_response
from ..intent_router import IntentType
from .utils import (
    _validate_real_test_code,
    _looks_like_python_code,
)

OUTPUT_DIR = os.environ.get(
    "TEST_CASE_OUTPUT_DIR",
    str(Path(__file__).resolve().parents[3] / "test_case"),
)


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
    
    根据意图选择不同的生成策略：
    - GENERATE/APPEND/UPDATE/REFACTOR: 生成测试代码
    - ENV_BUILD: 生成 Dockerfile
    - EXECUTE_EXTERNAL: 生成外部执行脚本
    - DIAGNOSE/COVERAGE/PROBE: 查询类，不生成代码
    
    Args:
        model: 底层 ChatOpenAI 实例（从 graph.py 传入）
    """
    memory = MemoryManager(runtime)

    # 获取意图信息
    parsed_intent: IntentType = state.get("parsed_intent", "GENERATE")
    template_name = state.get("template_name", "template_a")

    print(f"\n{'=' * 60}")
    print(f"[DEBUG generator] Intent: {parsed_intent}, Template: {template_name}")
    print(f"[DEBUG generator] case_plan length: {len(state.get('case_plan', ''))} chars")
    print(f"[DEBUG generator] case_plan preview: {state.get('case_plan', '')[:100]}...")
    
    # 检查状态完整性
    if not state.get("case_plan"):
        print(f"[DEBUG generator] ⚠️ WARNING: case_plan is empty or None!")
        print(f"[DEBUG generator] Available state keys: {list(state.keys())}")

    # 意图特定的记忆搜索
    memories = []
    memory_hints = ""
    if parsed_intent == "ENV_BUILD":
        memories = memory.search("env_builds", query=state.get("case_plan", ""), limit=2)
    else:
        memories = memory.search("generations", query=state.get("case_plan", ""), limit=2)
    memory_hints = memory.format_hints(memories)

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
    
    # 根据意图确定操作模式
    intent_to_action = {
        "APPEND": ("补充/追加", "保留所有历史测试函数，在其下方追加新函数"),
        "UPDATE": ("修改", "保留所有未修改的测试函数，只修改指定的部分"),
        "REFACTOR": ("重构", "保留测试逻辑，优化代码结构"),
    }
    
    action_desc, keep_desc = intent_to_action.get(parsed_intent, ("修改或补充", "保留所有历史测试函数，根据需求修改或追加"))

    if previous_code:
        truncated = previous_code
        if len(previous_code) > _MAX_PREVIOUS_CODE_CHARS:
            truncated = (
                previous_code[:_MAX_PREVIOUS_CODE_CHARS]
                + "\n# ... (已截断，上述代码太长)"
            )

        previous_code_hint = (
            f"\n\n【历史代码 - 必须在此基础上{action_desc}】\n"
            f"```python\n{truncated}\n```\n"
            f"注意：用户要求对代码进行{action_desc}操作。你必须输出修改后的**完整文件**，不要只返回差异或新增部分。\n"
            f"注意：{keep_desc}。禁止删除已有的测试函数。\n"
            f"注意：必须保持原始测试目标不变。如果原始代码测试的是 rocm-smi，修改后仍然必须测试 rocm-smi，"
            f"禁止把测试目标改成测试 helper 函数或内部封装。\n"
        )

    # 根据意图选择提示词模板
    if parsed_intent == "ENV_BUILD":
        # 使用 ENV_BUILD 专用模板
        prompt = get_prompt_by_template(
            template_name,
            intent=parsed_intent,
            case_plan=state.get("case_plan", ""),
            memory_hints=memory_hints,
        )
    elif parsed_intent in ["DIAGNOSE", "COVERAGE", "PROBE"]:
        # 查询类意图，使用简化模板
        prompt = get_prompt_by_template(
            template_name,
            intent=parsed_intent,
            case_plan=state.get("case_plan", ""),
        )
    else:
        # 测试代码生成意图
        prompt = get_generator_prompt(
            case_plan=state.get("case_plan", ""),
            memory_hints=memory_hints,
            previous_code_hint=previous_code_hint,
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

    # 使用 Pydantic 友好的解析器（优先 JSON，失败回退正则）
    generated_code, explanation, extraction_status = parse_llm_response(reply)
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
    memory_key = memory.save_generation(
        requirement=state.get("requirement", ""),
        code=final_code,
        saved_filepath=saved_filepath,
    )

    print(f"\n[DEBUG generator] ✅ Wrote memory: key={memory_key}")

    return {
        "code": final_code,
        "generated_code": final_code,
        "explanation": explanation,
        "validation_result": validation_result,
        "saved_filepath": saved_filepath,
        "messages": [{"role": "assistant", "content": reply}],
    }