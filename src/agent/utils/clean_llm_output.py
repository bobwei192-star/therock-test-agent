"""清洗 LLM 输出内容，移除调试信息和技术性内容。

用于清理 requirement_parser 等节点的 LLM 输出，提升前端展示质量。
"""

import re


def clean_llm_output(content: str) -> str:
    """清洗 LLM 输出，移除不必要的技术性内容。

    清理规则：
    1. 移除 HumanMessage/AIMessage 等 LangChain 内部对象表示
    2. 移除原始 prompt 模板内容
    3. 移除 JSON 格式的原始消息对象
    4. 保留实际的回复内容（包括意图标识）

    Args:
        content: LLM 原始输出

    Returns:
        清洗后的内容
    """
    if not content or not isinstance(content, str):
        return content or ""

    # 先检查是否只有空白字符
    if content.strip() == "":
        return ""

    cleaned = content

    # 规则 1: 移除 HumanMessage/AIMessage/SystemMessage 对象表示
    # 匹配模式：HumanMessage(content=...), AIMessage(content=...) 等
    message_pattern = r'(HumanMessage|AIMessage|SystemMessage)\(content=[\s\S]*?\)'
    cleaned = re.sub(message_pattern, '', cleaned)

    # 规则 2: 移除包含 "你是 ROCm 测试需求解析专家" 的 prompt 模板段落
    # 这些是重复的 prompt 内容，不应该展示给用户
    prompt_header_pattern = r'你是 ROCm 测试需求解析专家[\s\S]*?(?=## 意图识别|意图：|测试目标:|$)'
    cleaned = re.sub(prompt_header_pattern, '', cleaned)

    # 规则 3: 移除 "用户需求：[{'type': 'text', 'text': ...}]" 这种原始输入复述
    user_input_pattern = r"用户需求：\s*\[\{[\s\S]*?'type':\s*'text'[\s\S]*?\}\]"
    cleaned = re.sub(user_input_pattern, '', cleaned)

    # 规则 4: 移除包含 "messages" 的 JSON 对象（可能是调试信息）
    # 使用更宽松的模式匹配以 {"messages": 开头的行或块
    # 匹配 {"messages": ...} 格式，包括嵌套结构
    json_pattern = r'\{"messages":\s*\[.*?\](?:\s*,\s*"[^"]+":\s*\{?[^}]*\}?)*\s*\}'
    cleaned = re.sub(json_pattern, '[调试信息已隐藏]', cleaned, flags=re.DOTALL)

    # 规则 5: 移除 "## 意图识别（必选其一）" 等 prompt 模板说明
    template_instruction_pattern = r'## 意图识别（必选其一）[\s\S]*?(?=意图：|意图:|测试规格输出|$)'
    cleaned = re.sub(template_instruction_pattern, '', cleaned)

    # 规则 6: 移除意图选项列表（- GENERATE: ... - CHAT: ... 等）
    # 匹配以 "- " 开头的意图列表行，但不匹配 "意图：GENERATE" 这样的结果行
    # 只匹配列表项，不匹配 "意图：XXX" 格式
    intent_list_pattern = r'(?:^|\n)(?:-[\s]+(?:GENERATE|APPEND|UPDATE|REFACTOR|EXECUTE_EXTERNAL|DIAGNOSE|COVERAGE|PROBE|CHAT|ENV_BUILD):[^\n]*(?:\n|$))+'
    cleaned = re.sub(intent_list_pattern, '', cleaned)

    # 规则 7: 移除 "分析用户输入，判断属于以下哪种意图：" 等选项列表
    # 但保留 "意图：XXX" 这一行
    intent_options_pattern = r'分析用户输入[\s\S]*?(?=\n意图：|意图：|$)'
    cleaned = re.sub(intent_options_pattern, '', cleaned)

    # 规则 8: 移除多余的 "意图：" 标题（只保留带实际意图值的行）
    # 匹配单独一行的 "意图："（后面没有具体意图值）
    intent_header_pattern = r'^意图[\s]*[:：]\s*$'
    cleaned = re.sub(intent_header_pattern, '', cleaned, flags=re.MULTILINE)

    # 规则 9: 清理多余的空白行（连续 3 个以上空行）
    cleaned = re.sub(r'\n{3,}', '\n\n', cleaned)

    # 规则 10: 移除行首行尾的空白
    cleaned = cleaned.strip()

    # 如果清洗后内容为空，返回原始内容（避免完全丢失信息）
    if not cleaned:
        return content

    return cleaned


def extract_intent_from_llm_response(content: str) -> str | None:
    """从 LLM 响应中提取意图。

    尝试从 LLM 输出中解析出意图标识（GENERATE/APPEND/UPDATE 等）

    Args:
        content: LLM 原始输出

    Returns:
        提取的意图标识，如果未找到则返回 None
    """
    if not content:
        return None

    # 尝试匹配 "意图：XXX" 格式（支持中英文冒号）
    intent_pattern = r'意图[\s]*[:：][\s]*(GENERATE|APPEND|UPDATE|REFACTOR|EXECUTE_EXTERNAL|DIAGNOSE|COVERAGE|PROBE|CHAT|ENV_BUILD)'
    match = re.search(intent_pattern, content, re.IGNORECASE)

    if match:
        return match.group(1).upper()

    # 尝试匹配单独出现的意图标识（可能在列表中）
    standalone_pattern = r'(?:^|\s|\-)(GENERATE|APPEND|UPDATE|REFACTOR|EXECUTE_EXTERNAL|DIAGNOSE|COVERAGE|PROBE|CHAT|ENV_BUILD)(?:$|\s|:|-)'
    match = re.search(standalone_pattern, content, re.IGNORECASE)

    if match:
        return match.group(1).upper()

    return None
