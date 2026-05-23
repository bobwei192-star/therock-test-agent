"""测试 RAG 检索节点"""

import json
import pytest
from pathlib import Path
from unittest.mock import MagicMock, patch

from src.agent.nodes import node_context_retriever as rag
from src.agent.state import AgentState


# ---------- 工具函数 ----------
def make_state(requirement: str = "", messages: list = None) -> AgentState:
    return {
        "requirement": requirement,
        "messages": messages or [],
    }


# ---------- _get_requirement 测试 ----------
class TestGetRequirement:
    def test_from_state_requirement(self):
        state = make_state(requirement="test rocm-smi")
        assert rag._get_requirement(state) == "test rocm-smi"

    def test_fallback_to_messages_dict(self):
        state = make_state(
            messages=[
                {"role": "assistant", "content": "hi"},
                {"role": "user", "content": "from msg"},
            ]
        )
        assert rag._get_requirement(state) == "from msg"

    def test_fallback_skips_assistant_messages(self):
        state = make_state(
            messages=[
                {"role": "user", "content": "real"},
                {"role": "assistant", "content": "noise"},
            ]
        )
        assert rag._get_requirement(state) == "real"

    def test_empty_when_nothing(self):
        assert rag._get_requirement(make_state()) == ""


# ---------- context_retriever 集成测试 ----------
class TestContextRetriever:
    def test_placeholder_when_no_chroma_db(self):
        """chroma_db 不存在时应优雅降级"""
        with patch.object(rag, "_CHROMA_DIR", Path("/nonexistent")):
            result = rag.context_retriever(make_state(requirement="test"))
        ctx = result["context"]
        assert ctx["phase"] == "phase_one_placeholder"
        assert "rag_error" in ctx

    def test_rag_error_in_message(self):
        with patch.object(rag, "_CHROMA_DIR", Path("/nonexistent")):
            result = rag.context_retriever(make_state(requirement="test"))
        msg = result["messages"][0]["content"]
        assert "知识库未就绪" in msg or "检索" in msg or "不存在" in msg

    def test_context_is_serializable(self):
        with patch.object(rag, "_CHROMA_DIR", Path("/nonexistent")):
            result = rag.context_retriever(make_state(requirement="test"))
        # 确保能 JSON 序列化（LangGraph 状态需要）
        json.dumps(result["context"])
        json.dumps(result["messages"])


# ---------- 真实向量库测试（需要提前建好索引） ----------
@pytest.mark.skipif(not Path("./chroma_db").exists(), reason="chroma_db 未建立")
class TestWithRealVectorstore:
    def test_real_retrieval_returns_docs(self):
        state = make_state(requirement="rocm-smi 温度")
        result = rag.context_retriever(state)
        ctx = result["context"]
        # 如果文档里有相关内容，应进入 rag_enabled
        if ctx.get("phase") == "rag_enabled":
            assert "retrieved_knowledge" in ctx
            assert ctx["retrieved_count"] > 0
            assert "🔍" in result["messages"][0]["content"]
            # 检查来源标签格式
            assert "【来源:" in ctx["retrieved_knowledge"]
        else:
            pytest.skip("向量库中无匹配文档")

    def test_requirement_preserved(self):
        state = make_state(requirement="rocm-smi")
        result = rag.context_retriever(state)
        assert result["context"]["requirement"] == "rocm-smi"
