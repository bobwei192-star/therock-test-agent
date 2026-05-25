"""用户输入清洗过滤器。

在 CLI 和 Chat UI 的输入管道前插入，过滤掉无效内容和重复字符，
减少无效 token 消耗，提升 Agent 体验。

用法: from src.agent.input_filter import clean_input
"""

import re
import unicodedata


def clean_input(text: str, max_length: int = 4000) -> str:
    """清洗用户输入，返回干净的文本。

    过滤规则（按顺序）：
    1. 去除控制字符（保留换行和制表）
    2. 折叠重复字符（3 个以上 → 2 个）
    3. 删除全重复行（同一行出现 3 次以上 → 只保留前 2 次）
    4. 规范化 Unicode
    5. 压缩多余空白行
    6. 截断超长输入

    Args:
        text: 原始用户输入
        max_length: 最大允许长度，超过则截断并保留头尾

    Returns:
        清洗后的文本
    """
    if not text or not text.strip():
        return ""

    # 1. 移除不可见字符（保留换行 \n、制表 \t）
    cleaned = ""
    for ch in text:
        cat = unicodedata.category(ch)
        if cat == "Cc" and ch not in ("\n", "\t"):
            cleaned += " "
        elif cat in ("Cf", "Cs", "Co", "Cn"):
            cleaned += " "
        elif ch == "\r":
            cleaned += "\n"
        else:
            cleaned += ch

    # 2. 折叠重复字符：同一非空白字符连续出现 3 次以上压缩到 2 个
    cleaned = re.sub(r"(\S)\1{2,}", r"\1\1", cleaned)

    # 3. 删除全重复行（完全相同的行出现 3 次以上 → 只保留前 2 次）
    lines = cleaned.split("\n")
    seen: dict[str, int] = {}
    deduped: list[str] = []
    for line in lines:
        stripped = line.strip()
        if not stripped:
            deduped.append(line)
            continue
        count = seen.get(stripped, 0)
        if count < 2:
            deduped.append(line)
            seen[stripped] = count + 1
    cleaned = "\n".join(deduped)

    # 4. Unicode 规范化 (NFC)
    cleaned = unicodedata.normalize("NFC", cleaned)

    # 5. 压缩多余空白行（连续 3 行以上空行 → 2 行）
    cleaned = re.sub(r"\n{3,}", "\n\n", cleaned)

    # 6. 截断超长输入
    stripped = cleaned.strip()
    if not stripped:
        return ""
    if len(stripped) > max_length:
        head = stripped[:max_length // 2]
        tail = stripped[-(max_length // 2):]
        stripped = head + "\n\n... (输入过长已截断) ...\n\n" + tail
    return stripped


def is_meaningful(text: str, min_chars: int = 3) -> bool:
    """判断输入是否有意义（非空且不全是垃圾字符）。"""
    cleaned = clean_input(text)
    if not cleaned:
        return False
    # 至少包含一个中文字符、字母或数字
    if not re.search(r"[\u4e00-\u9fff\w]", cleaned):
        return False
    # 长度不足
    if len(cleaned) < min_chars:
        return False
    # 超过 90% 是同一个字符（如 "kkkkkkkkkkkkk"）
    from collections import Counter
    chars = [c for c in cleaned if not c.isspace()]
    if not chars:
        return False
    most_common_ratio = Counter(chars).most_common(1)[0][1] / len(chars)
    if most_common_ratio > 0.8:
        return False
    return True
