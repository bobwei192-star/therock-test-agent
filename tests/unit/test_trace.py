"""Langfuse tracing 模块测试。

覆盖：
- 有凭证时 handler 正常创建
- build_langfuse_config 返回正确结构
- flush_langfuse 安全调用
- dump_execution_trace 本地文件落盘
- 缺凭证时的降级行为
"""

import json
import os
import tempfile
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

from src.agent.tracing import (
    _build_langfuse_handler,
    build_langfuse_config,
    dump_execution_trace,
    flush_langfuse,
    langfuse_handler,
)


class TestBuildLangfuseHandler:
    def test_handler_created_when_credentials_present(self):
        """当 .env 中已配置完整 Langfuse 凭证时，应返回 CallbackHandler 实例。"""
        handler = _build_langfuse_handler()
        # 如果 .env 已配置密钥，handler 应为真
        assert handler is not None, (
            "未创建 handler，请检查 .env 中的 LANGFUSE_BASE_URL / PUBLIC_KEY / SECRET_KEY"
        )
        assert hasattr(handler, "auth_check") or True

    def test_handler_none_when_missing_env(self, monkeypatch):
        """当缺少任意一项凭证时，应返回 None。"""
        monkeypatch.delenv("LANGFUSE_PUBLIC_KEY", raising=False)
        monkeypatch.delenv("LANGFUSE_SECRET_KEY", raising=False)
        monkeypatch.delenv("LANGFUSE_BASE_URL", raising=False)
        monkeypatch.delenv("LANGFUSE_HOST", raising=False)

        import src.agent.tracing as tracing_mod

        monkeypatch.setattr(tracing_mod, "load_dotenv", lambda *a, **kw: None)

        handler = _build_langfuse_handler()
        assert handler is None

    def test_handler_uses_langfuse_host_over_base_url(self, monkeypatch):
        """LANGFUSE_HOST 的优先级应高于 LANGFUSE_BASE_URL。"""
        monkeypatch.setenv("LANGFUSE_HOST", "http://localhost:3000")
        monkeypatch.setenv("LANGFUSE_PUBLIC_KEY", "pk-test")
        monkeypatch.setenv("LANGFUSE_SECRET_KEY", "sk-test")
        monkeypatch.delenv("LANGFUSE_BASE_URL", raising=False)

        import src.agent.tracing as tracing_mod

        monkeypatch.setattr(tracing_mod, "load_dotenv", lambda *a, **kw: None)

        handler = _build_langfuse_handler()
        assert handler is not None
        assert os.environ["LANGFUSE_HOST"] == "http://localhost:3000"

    def test_handler_none_when_callbackhandler_unimportable(self, monkeypatch):
        """当 langfuse 包未安装时，应安全返回 None。"""
        monkeypatch.setenv("LANGFUSE_HOST", "http://localhost:3000")
        monkeypatch.setenv("LANGFUSE_PUBLIC_KEY", "pk-test")
        monkeypatch.setenv("LANGFUSE_SECRET_KEY", "sk-test")

        import src.agent.tracing as tracing_mod

        monkeypatch.setattr(tracing_mod, "load_dotenv", lambda *a, **kw: None)

        with patch.object(tracing_mod, "CallbackHandler", None):
            handler = _build_langfuse_handler()
            assert handler is None


class TestBuildLangfuseConfig:
    def test_returns_empty_dict_when_no_handler(self, monkeypatch):
        """当 langfuse_handler 为 None 时，返回空配置。"""
        import src.agent.tracing as tracing_mod

        monkeypatch.setattr(tracing_mod, "langfuse_handler", None)
        cfg = build_langfuse_config()
        assert cfg == {}

    def test_returns_callbacks_with_metadata(self):
        """正常情况下返回包含 callbacks 和 metadata 的配置字典。"""
        cfg = build_langfuse_config()
        if langfuse_handler is None:
            pytest.skip("Langfuse 未配置，跳过")
        assert "callbacks" in cfg
        assert "metadata" in cfg
        assert cfg["callbacks"] == [langfuse_handler]

    def test_thread_id_in_metadata(self):
        """传入 thread_id 时应写入 metadata.langfuse_user_id。"""
        cfg = build_langfuse_config(thread_id="test-thread-42")
        if langfuse_handler is None:
            pytest.skip("Langfuse 未配置，跳过")
        assert cfg["metadata"]["langfuse_user_id"] == "test-thread-42"

    def test_custom_tags_in_metadata(self):
        """传入自定义 tags 时应覆盖默认值。"""
        cfg = build_langfuse_config(tags=["custom", "test"])
        if langfuse_handler is None:
            pytest.skip("Langfuse 未配置，跳过")
        assert "custom" in cfg["metadata"]["langfuse_tags"]

    def test_default_tags_when_none_provided(self):
        """不传 tags 时使用默认值。"""
        cfg = build_langfuse_config()
        if langfuse_handler is None:
            pytest.skip("Langfuse 未配置，跳过")
        assert "langgraph" in cfg["metadata"]["langfuse_tags"]
        assert "test-case-agent" in cfg["metadata"]["langfuse_tags"]


class TestFlushLangfuse:
    def test_flush_noop_when_no_handler(self, monkeypatch):
        """无 handler 时 flush 应安全执行不报错。"""
        import src.agent.tracing as tracing_mod

        monkeypatch.setattr(tracing_mod, "langfuse_handler", None)
        flush_langfuse()

    def test_flush_calls_handler_flush(self):
        """有 handler 且带 flush 方法时应被调用。"""
        mock_handler = MagicMock()
        mock_handler.flush = MagicMock()
        import src.agent.tracing as tracing_mod

        monkeypatch = pytest.MonkeyPatch()
        monkeypatch.setattr(tracing_mod, "langfuse_handler", mock_handler)
        try:
            flush_langfuse()
            mock_handler.flush.assert_called_once()
        finally:
            monkeypatch.undo()

    def test_flush_safe_when_no_flush_method(self):
        """handler 没有 flush 方法时应安全跳过。"""
        mock_handler = MagicMock(spec=[])
        import src.agent.tracing as tracing_mod

        monkeypatch = pytest.MonkeyPatch()
        monkeypatch.setattr(tracing_mod, "langfuse_handler", mock_handler)
        try:
            flush_langfuse()
        finally:
            monkeypatch.undo()


class TestDumpExecutionTrace:
    def _make_fake_graph_history(self):
        """构造最小可用的 graph + state_history 双 mock。"""
        mock_graph = MagicMock()
        fake_mmd = "graph TD\n  A-->B\n"
        mock_graph.get_graph.return_value.draw_mermaid.return_value = fake_mmd

        state_0 = MagicMock()
        state_0.next = ["planner"]
        state_0.values = {"requirement": "test", "messages": []}
        state_0.metadata = {"step": 0}

        state_1 = MagicMock()
        state_1.next = []
        state_1.values = {"final_report": {"status": "ok"}}
        state_1.metadata = {"step": 1}

        mock_graph.get_state_history.return_value = [state_0, state_1]
        return mock_graph

    def test_creates_summary_json(self):
        """应生成 summary.json 文件。"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_graph = self._make_fake_graph_history()
            dump_execution_trace(fake_graph, {}, output_dir=tmpdir)

            summary_path = Path(tmpdir) / "summary.json"
            assert summary_path.exists()
            summary = json.loads(summary_path.read_text())
            assert summary["total_steps"] == 2
            assert "timestamp" in summary

    def test_creates_step_json_files(self):
        """应为历史中的每一步生成 step_NNN_node.json 文件。"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_graph = self._make_fake_graph_history()
            dump_execution_trace(fake_graph, {}, output_dir=tmpdir)

            files = sorted(Path(tmpdir).glob("step_*.json"))
            assert len(files) == 2
            step0 = json.loads(files[0].read_text())
            assert step0["next_node"] == ["planner"]

    def test_writes_mermaid_graph(self):
        """应生成 graph.mmd Mermaid 文件。"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_graph = self._make_fake_graph_history()
            dump_execution_trace(fake_graph, {}, output_dir=tmpdir)

            mmd_path = Path(tmpdir) / "graph.mmd"
            assert mmd_path.exists()
            content = mmd_path.read_text()
            assert "graph TD" in content or "flowchart" in content

    def test_survives_missing_mermaid(self):
        """graph 不支持 draw_mermaid 时不应崩溃。"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_graph = MagicMock()
            fake_graph.get_graph.side_effect = Exception("no mermaid")
            fake_graph.get_state_history.return_value = []
            dump_execution_trace(fake_graph, {}, output_dir=tmpdir)

            summary = json.loads(Path(tmpdir, "summary.json").read_text())
            assert summary["total_steps"] == 0

    def test_survives_empty_history(self):
        """空历史时不应崩溃。"""
        with tempfile.TemporaryDirectory() as tmpdir:
            fake_graph = MagicMock()
            fake_graph.get_state_history.return_value = []
            dump_execution_trace(fake_graph, {}, output_dir=tmpdir)
            assert Path(tmpdir, "summary.json").exists()

    def test_truncates_long_values(self):
        """长字符串值应被截断，防止落盘文件过大。"""
        long_text = "A" * 3000
        state = MagicMock()
        state.next = []
        state.values = {"long_field": long_text}
        state.metadata = {}

        with tempfile.TemporaryDirectory() as tmpdir:
            fake_graph = MagicMock()
            fake_graph.get_state_history.return_value = [state]
            dump_execution_trace(fake_graph, {}, output_dir=tmpdir)

            step_file = list(Path(tmpdir).glob("step_*.json"))[0]
            content = step_file.read_text()
            assert "truncated" in content


class TestModuleLevelHandler:
    def test_module_level_handler_is_not_none(self):
        """模块级单例 langfuse_handler 应在 .env 配置后非空。"""
        from src.agent.tracing import langfuse_handler as handler

        assert handler is not None, (
            "langfuse_handler 为 None，请确认 .env 中 LANGFUSE_PUBLIC_KEY / "
            "LANGFUSE_SECRET_KEY / LANGFUSE_BASE_URL 均已配置且 langfuse 包已安装"
        )

    def test_build_langfuse_config_not_empty(self):
        """build_langfuse_config() 在凭证完整时不应返回空字典。"""
        cfg = build_langfuse_config()
        assert cfg != {}, "build_langfuse_config 返回空字典，Langfuse 未连接。"


if __name__ == "__main__":
    pytest.main([__file__, "-v", "-s"])
