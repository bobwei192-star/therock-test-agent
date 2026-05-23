"""
测试 HuggingFace MCP 工具集成（极简版）

对应极简版 __init__.py：TOOLS = [原生工具, *_load_hf_mcp_tools()]
测试目标：
1. TOOLS 列表能正常构建（含/不含 HF_TOKEN）
2. MCP 工具可调用（get_model_info, search_models 等）
3. 原生工具不受 MCP 影响
"""

import os
import pytest

from langchain_core.tools import BaseTool


# ========== 辅助函数 ==========


def _has_hf_token() -> bool:
    return bool(os.environ.get("HF_TOKEN"))


def _get_tool_names() -> list[str]:
    """获取当前 TOOLS 里所有工具名"""
    from src.agent.tools import TOOLS

    return [t.name for t in TOOLS]


def _find_tool(name_keyword: str) -> BaseTool | None:
    """按关键词查找工具"""
    from src.agent.tools import TOOLS

    keyword = name_keyword.lower()
    for t in TOOLS:
        if keyword in t.name.lower():
            return t
    return None


# ========== 测试：工具列表构建 ==========


class TestToolsList:
    """测试 TOOLS 列表正确构建"""

    @pytest.mark.skipif(not _has_hf_token(), reason="HF_TOKEN not set")
    def test_mcp_tools_loaded_with_token(self):
        """有 HF_TOKEN 时 MCP 工具应该加载"""
        names = _get_tool_names()

        # # 至少有一些含 model 的工具（HF Server 提供的）
        # model_tools = [n for n in names if "model" in n.lower()]
        # assert len(model_tools) > 0, f"No MCP model tools. All tools: {names}"
        # print(f"\nMCP tools loaded: {model_tools}")

        # 方案 1：检查是否加载了任何 HF 工具（以 hf_ 开头或数量明显多于基础工具）
        hf_tools = [
            n
            for n in names
            if n.startswith("hf_")
            or n
            in (
                "space_search",
                "hub_repo_search",
                "paper_search",
                "hub_repo_details",
                "hf_doc_search",
                "hf_doc_fetch",
                "gr1_z_image_turbo_generate",
            )
        ]
        assert len(hf_tools) > 0, f"No HF MCP tools loaded. All tools: {names}"
        print(f"\nMCP tools loaded: {hf_tools}")

    def test_mcp_tools_not_loaded_without_token(self):
        """无 HF_TOKEN 时不应该加载 MCP 工具（降级测试）"""
        # 临时移除 token
        original = os.environ.pop("HF_TOKEN", None)
        try:
            # 强制重新导入（Python 会重新执行 _load_hf_mcp_tools）
            import importlib
            from src.agent import tools as tools_mod

            importlib.reload(tools_mod)

            names = [t.name for t in tools_mod.TOOLS]

            # 只有原生工具
            model_tools = [n for n in names if "model" in n.lower()]
            # check_model_downloadable 是原生工具，不算 MCP
            mcp_only = [n for n in model_tools if n != "check_model_downloadable"]

            assert len(mcp_only) == 0, f"Unexpected MCP tools without token: {mcp_only}"
            print(f"\nGraceful fallback OK: {names}")

        finally:
            if original:
                os.environ["HF_TOKEN"] = original


# ========== 测试：MCP 工具调用 ==========


@pytest.mark.skipif(not _has_hf_token(), reason="HF_TOKEN not set")
class TestMCPtoolCalls:
    """测试 MCP 工具实际调用"""

    def test_get_model_info_exists(self):
        """测试检查存在的模型"""
        tool = _find_tool("model_info") or _find_tool("get_model")

        if not tool:
            # 列出所有可用工具帮助调试
            names = _get_tool_names()
            pytest.skip(f"No model_info tool. Available: {names}")

        print(f"\nUsing tool: {tool.name}")
        result = tool.invoke({"model_id": "Qwen/Qwen2.5-7B-Instruct"})

        print(f"Result: {str(result)[:500]}")

        # 结果应该包含模型信息（字符串或 dict）
        result_str = str(result).lower()
        assert any(
            k in result_str for k in ["qwen", "instruct", "id", "author", "downloads"]
        ), f"Unexpected result: {result}"

    def test_get_model_info_not_exists(self):
        """测试检查不存在的模型"""
        tool = _find_tool("model_info") or _find_tool("get_model")

        if not tool:
            pytest.skip("No model_info tool available")

        result = tool.invoke({"model_id": "FakeUser/NotExist12345"})

        print(f"\nResult: {str(result)[:500]}")

        # 应该返回不存在或错误
        result_str = str(result).lower()
        assert any(
            k in result_str for k in ["not found", "error", "404", "not exist", "false"]
        ), f"Expected not-found, got: {result}"

    def test_search_models(self):
        """测试搜索模型"""
        tool = _find_tool("search") or _find_tool("list")

        if not tool:
            names = _get_tool_names()
            pytest.skip(f"No search tool. Available: {names}")

        print(f"\nUsing tool: {tool.name}")
        result = tool.invoke({"query": "qwen2.5", "limit": 3})

        print(f"Result: {str(result)[:500]}")

        # 验证返回了结果
        assert result is not None
        result_str = str(result).lower()
        assert (
            "qwen" in result_str or "model" in result_str or "result" in result_str
        ), f"Unexpected search result: {result}"

    def test_trending_models(self):
        """测试获取 trending 模型（like 数最多）"""
        # HF MCP Server 可能有 trending 或 list_models 工具
        tool = _find_tool("trending") or _find_tool("list") or _find_tool("search")

        if not tool:
            pytest.skip("No trending/list tool available")

        print(f"\nUsing tool: {tool.name}")

        # 尝试调用 trending（参数取决于具体工具）
        try:
            result = tool.invoke({"sort": "likes", "limit": 5})
        except Exception:
            # fallback：普通搜索
            result = tool.invoke({"query": "", "limit": 5})

        print(f"Result: {str(result)[:500]}")
        assert result is not None
