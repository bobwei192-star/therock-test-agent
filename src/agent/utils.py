import ast
import re
from typing import Any

from ..state import AgentState, AgentContext
from ..message_utils import get_message_content, get_last_user_message


def _message_content(message: Any) -> str:
    """统一获取消息内容（兼容新旧调用方式）。"""
    return get_message_content(message)


def _last_user_message(state: AgentState) -> str:
    """获取最后一条用户消息（兼容新旧调用方式）。"""
    msgs = state.get("messages", [])
    if not msgs:
        return ""
    return get_last_user_message(msgs)


def _invoke_llm(agent: Any, prompt: str, node_name: str = "LLM") -> str:
    if agent is None:
        raise RuntimeError(
            "LLM node requires a model-backed agent. Pass model to build_graph()."
        )

    print(f"\n[{node_name}] Invoking LLM ({len(prompt)} chars prompt)...")
    try:
        result = agent.invoke({"messages": [{"role": "user", "content": prompt}]})
        last_msg = result["messages"][-1]
        content = _message_content(last_msg)
        print(f"[{node_name}] LLM response: {len(content)} chars")
        return content
    except PermissionError:
        import sys

        print(f"\n[{node_name}] ❌ 文件写入权限不足", file=sys.stderr)
        raise
    except Exception:
        import os, sys, traceback

        exc_name = type(sys.exc_info()[1]).__name__
        exc_msg = str(sys.exc_info()[1])[:200]
        provider = os.environ.get("TEST_CASE_AGENT_MODEL_PROVIDER", "unknown")
        model = (
            os.environ.get("LLM_MODEL") or os.environ.get("DEEPSEEK_MODEL") or "unknown"
        )
        base_url = (
            os.environ.get("LLM_BASE_URL")
            or os.environ.get("DEEPSEEK_BASE_URL")
            or "unknown"
        )
        print(
            f"\n[{node_name}] ❌ Agent invoke 失败: {exc_name}: {exc_msg}",
            file=sys.stderr,
        )
        print(
            f"  provider={provider}  model={model}  base_url={base_url}",
            file=sys.stderr,
        )
        traceback.print_exc(file=sys.stderr)
        raise


def _looks_like_python_code(text: str) -> tuple[bool, str]:
    """严格检查：返回 (是否有效, 原因)。不做截断修复。"""
    stripped = text.strip()
    if not stripped:
        return False, "代码为空"
    if not any(kw in stripped for kw in ("import ", "def ", "class ")):
        return False, "缺少 Python 基本语法特征（import/def/class）"
    if "def test_" not in stripped:
        return False, "缺少 pytest 测试函数（def test_...）"
    try:
        ast.parse(stripped)
        return True, ""
    except SyntaxError as exc:
        return False, f"语法错误: {exc}"


def _fix_code_by_truncation(code: str) -> str | None:
    """截断代码到最长可解析前缀，修复尾部未闭合 f-string 等错误。"""
    lines = code.split("\n")
    for i in range(len(lines), 0, -1):
        snippet = "\n".join(lines[:i])
        try:
            ast.parse(snippet)
            return snippet
        except SyntaxError:
            pass
    return None


def _extract_code(text: str) -> tuple[str, str, str]:
    """返回 (code, explanation, status)。新增截断修复能力。"""
    original = text.strip()
    if not original:
        return "", "", "空回复"

    candidates = []

    python_blocks = re.findall(r"```python\s*(.*?)\s*```", text, re.DOTALL)
    candidates.extend(block.strip() for block in python_blocks)

    if not candidates:
        generic_blocks = re.findall(r"```\s*(.*?)\s*```", text, re.DOTALL)
        candidates.extend(block.strip() for block in generic_blocks)

    if not candidates and "```python" in text:
        unclosed = text.split("```python", 1)[1].strip()
        candidates.append(unclosed)

    explanation = re.sub(
        r"```(?:python)?\s*.*?\s*```", "", text, flags=re.DOTALL
    ).strip()
    explanation = re.sub(r"```python\s*.*$", "", explanation, flags=re.DOTALL).strip()

    best_code = ""
    best_status = "未找到有效代码块"

    for candidate in candidates:
        is_valid, reason = _looks_like_python_code(candidate)
        if is_valid:
            best_code = candidate
            best_status = "成功提取有效代码"
            break
        else:
            # 尝试截断修复尾部语法错误
            fixed = _fix_code_by_truncation(candidate)
            if fixed:
                is_valid_fixed, _ = _looks_like_python_code(fixed)
                if is_valid_fixed:
                    best_code = fixed
                    best_status = "成功提取并截断修复代码"
                    break
            if best_status == "未找到有效代码块":
                best_code = candidate
                best_status = f"代码块提取成功但验证失败: {reason}"

    if not best_code:
        is_valid, reason = _looks_like_python_code(original)
        if is_valid:
            best_code = original
            best_status = "成功提取有效代码（无围栏）"
            explanation = ""
        else:
            fixed = _fix_code_by_truncation(original)
            if fixed:
                is_valid_fixed, _ = _looks_like_python_code(fixed)
                if is_valid_fixed:
                    best_code = fixed
                    best_status = "成功提取并截断修复代码（无围栏）"
                    explanation = ""
                else:
                    best_status = f"无围栏代码验证失败: {reason}"
            else:
                best_status = f"无围栏代码验证失败: {reason}"

    return best_code, explanation, best_status


def _validate_real_test_code(code: str) -> list[str]:
    issues: list[str] = []
    if not code or not code.strip():
        issues.append("No generated code extracted.")
        return issues

    lowered = code.lower()

    if "def test_" not in code:
        issues.append(
            "Generated pytest code must contain at least one test function (def test_...)."
        )

    try:
        ast.parse(code)
    except SyntaxError as exc:
        issues.append(f"Syntax error in generated code: {exc}")

    if "pytest.mark.dry_run_only" in code:
        issues.append("Generated pytest code must not be marked dry_run_only.")

    if re.search(r"^\s*#\s*.*subprocess\.run", code, flags=re.MULTILINE):
        issues.append("subprocess.run appears to be commented out.")

    has_subprocess = "subprocess" in lowered or "subprocess.run" in lowered
    has_popen = "popen" in lowered
    has_run_cmd = "run_cmd" in lowered or "execute" in lowered
    if not (has_subprocess or has_popen or has_run_cmd):
        issues.append(
            "Generated pytest code should execute the target command with subprocess or equivalent."
        )

    if re.search(r"output\s*=\s*(?:'''|\"\"\")", code):
        issues.append(
            "Generated pytest code must not use hard-coded successful command output."
        )

    if "mock" in lowered or "fake output" in lowered:
        issues.append(
            "Generated pytest code must not use mock or fake output for real tests."
        )

    return issues



