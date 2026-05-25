"""统一消息处理工具 - 使用 LangChain BaseMessage"""

from typing import Any, List, Dict, Optional
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, ToolMessage


def ensure_message(obj: Any) -> BaseMessage:
    """将任意对象转换为 BaseMessage。"""
    if isinstance(obj, BaseMessage):
        return obj
    if isinstance(obj, dict):
        role = obj.get("role", "assistant")
        content = obj.get("content", "")
        if role in ("user", "human"):
            return HumanMessage(content=content)
        elif role == "tool":
            return ToolMessage(content=content, tool_call_id=obj.get("tool_call_id", ""))
        else:
            return AIMessage(content=content)
    return AIMessage(content=str(obj))


def get_message_content(msg: Any) -> str:
    """统一获取消息内容。"""
    if isinstance(msg, BaseMessage):
        return str(msg.content)
    if isinstance(msg, dict):
        return str(msg.get("content", ""))
    return str(getattr(msg, "content", msg))


def get_last_user_message(messages: List[Any]) -> str:
    """从消息列表中获取最后一条用户消息。"""
    for msg in reversed(messages):
        if isinstance(msg, BaseMessage):
            if msg.type == "human":
                return str(msg.content)
        elif isinstance(msg, dict):
            role = msg.get("role", "")
            if role in ("user", "human"):
                return str(msg.get("content", ""))
    return ""


def create_ai_message(content: str) -> AIMessage:
    """创建 AI 消息。"""
    return AIMessage(content=content)


def create_human_message(content: str) -> HumanMessage:
    """创建人类消息。"""
    return HumanMessage(content=content)