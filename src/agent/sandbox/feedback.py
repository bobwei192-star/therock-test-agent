"""Build compact planner feedback from sandbox execution failures."""

from __future__ import annotations

from .base import CommandResult

_MAX_LOG_CHARS = 2000


def _truncate(text: str, limit: int = _MAX_LOG_CHARS) -> str:
    """Return a bounded log snippet for LLM feedback."""
    if len(text) <= limit:
        return text
    return f"{text[:limit]}\n... <truncated {len(text) - limit} chars>"


def classify_failure(stage: str, error: str, output: str = "") -> str:
    """Classify a sandbox failure into a planner-friendly category."""
    haystack = f"{stage}\n{error}\n{output}".lower()

    if "modulenotfounderror" in haystack or "no module named" in haystack:
        return "ModuleNotFoundError"
    if "importerror" in haystack:
        return "ImportError"
    if "syntaxerror" in haystack:
        return "SyntaxError"
    if "collection failed" in haystack or "error collecting" in haystack:
        return "pytest collection failed"
    if "command not found" in haystack or "not found" in haystack:
        return "command not found"
    if "filenotfounderror" in haystack:
        return "FileNotFoundError"
    if "timeout" in haystack or "timed out" in haystack:
        return "timeout"
    if stage == "dependency":
        return "dependency installation failed"
    if stage == "pytest":
        return "pytest failed"
    return "sandbox failure"


def build_feedback(
    *,
    stage: str,
    error: str,
    retry_count: int,
    max_retries: int,
    command_result: CommandResult | None = None,
    output: str = "",
) -> str:
    """Create feedback for planner re-planning after sandbox failure."""
    stdout = command_result.stdout if command_result else ""
    stderr = command_result.stderr if command_result else ""
    exit_code = command_result.exit_code if command_result else None
    combined_output = output or "\n".join(part for part in (stderr, stdout) if part)
    failure_type = classify_failure(stage, error, combined_output)

    lines = [
        f"[{stage}] 沙盒验证失败。",
        f"错误类型: {failure_type}",
    ]
    if exit_code is not None:
        lines.append(f"退出码: {exit_code}")
    if error:
        lines.append(f"错误摘要: {_truncate(error, 800)}")
    if combined_output:
        lines.append(f"关键日志:\n{_truncate(combined_output)}")

    next_retry = retry_count + 1
    if next_retry < max_retries:
        lines.append(
            f"这是第 {next_retry} 次重试，请重新评估测试计划并输出完整新计划。"
        )
    else:
        lines.append(
            f"已达到最大重试次数 {max_retries}，请保留完整失败原因供人工介入。"
        )

    lines.append("不要只输出 diff；需要重新给出完整测试策略和执行计划。")
    return "\n".join(lines)
