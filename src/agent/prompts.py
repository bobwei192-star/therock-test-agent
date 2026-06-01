"""从 src/agent/promot/ 加载提示词模板并格式化。

根据 guide/09_promot优化.md 设计：
- 支持多意图提示词模板：create_intent/update_intent/query_intent/external_intent/build_intent
- create_intent: GENERATE/APPEND（创建类）
- update_intent: UPDATE/REFACTOR（修改类）
- query_intent: DIAGNOSE/COVERAGE/PROBE（查询诊断类）
- external_intent: EXECUTE_EXTERNAL（外部执行类）
- build_intent: ENV_BUILD（环境构建类）
"""

from pathlib import Path
from typing import Any

_PROMPT_DIR = Path(__file__).resolve().parent / "promots"


def _load_prompt_text(name: str) -> str:
    """读取 .md 文件并返回去除了首尾空白的文本。"""
    filepath = _PROMPT_DIR / name
    if not filepath.exists():
        raise FileNotFoundError(f"Prompt file not found: {filepath}")
    return filepath.read_text(encoding="utf-8").strip()


def get_requirement_parser_prompt(raw_requirement: str) -> str:
    """格式 requirement_parser 节点的提示词。"""
    tmpl = _load_prompt_text("node_requirement_parser.md")
    return tmpl.replace("{raw_requirement}", raw_requirement)


def get_planner_prompt(
    requirement: str,
    context: dict[str, Any],
    memory_hints: str,
    feedback: str = "",
    execution_result: dict[str, Any] | None = None,
) -> str:
    """格式 planner 节点的提示词。"""
    tmpl = _load_prompt_text("node_planner.md")
    return (
        tmpl.replace("{requirement}", requirement)
        .replace("{context}", str(context))
        .replace("{memory_hints}", memory_hints)
        .replace("{feedback}", feedback or "无")
        .replace("{execution_result}", str(execution_result or {}))
    )


def get_generator_prompt(
    case_plan: str,
    memory_hints: str,
    previous_code_hint: str,
) -> str:
    """格式 generator 节点的提示词。"""
    tmpl = _load_prompt_text("node_generator.md")
    return (
        tmpl.replace("{case_plan}", case_plan)
        .replace("{memory_hints}", memory_hints)
        .replace("{previous_code_hint}", previous_code_hint)
    )


def get_prompt_by_template(template_name: str, **kwargs: Any) -> str:
    """根据模板名称获取格式化的提示词。

    Args:
        template_name: 模板名称（create_intent/update_intent/query_intent/external_intent/build_intent/chat_intent）
        **kwargs: 模板中需要替换的占位符参数

    Returns:
        格式化后的提示词文本
    """
    # 模板文件名映射
    template_file_map = {
        "create_intent": "create_intent.md",
        "update_intent": "update_intent.md",
        "query_intent": "query_intent.md",
        "external_intent": "external_intent.md",
        "build_intent": "build_intent.md",
        "chat_intent": "chat_intent.md",
    }

    filename = template_file_map.get(template_name)
    if not filename:
        raise ValueError(f"Unknown template name: {template_name}")

    tmpl = _load_prompt_text(filename)

    # 替换所有占位符
    result = tmpl
    for key, value in kwargs.items():
        placeholder = "{" + key + "}"
        result = result.replace(placeholder, str(value) if value is not None else "")

    return result
