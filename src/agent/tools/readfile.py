from langchain_core.tools import tool

from pathlib import Path


@tool
def read_file(filepath: str) -> str:
    """读取文件内容。

    Args:
        filepath: 文件路径
    """
    path = Path(filepath)
    if not path.exists():
        return f"\u274c 文件不存在: {filepath}"
    return path.read_text(encoding="utf-8")
