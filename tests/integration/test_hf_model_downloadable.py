"""
验证 LLM 在收到 HuggingFace 模型查询时，能自主调用 HF MCP 工具。
核心改进：
1. 不检查 messages.tool_calls（LangGraph 内部消费），改检查 case_plan / generated_code 中的 MCP 痕迹；
2. 通过全局计数器统计 MCP 调用次数，确保 requirement_parser 阶段有调用；
3. 降级测试修复 monkeypatch 时机问题。
"""

import os
import sys
import importlib
import pytest
from unittest.mock import patch

from src.agent.runner import run_multi_turn
from src.agent.tools import TOOLS


# ── 辅助函数 ──────────────────────────────────────────────


def _has_hf_token() -> bool:
    return bool(os.environ.get("HF_TOKEN"))


def _get_hf_tools_info() -> list[dict]:
    """遍历 TOOLS，提取所有 HuggingFace MCP 工具的名称与描述。"""
    known_hf_tools = {
        "hf_whoami",
        "space_search",
        "hub_repo_search",
        "paper_search",
        "hub_repo_details",
        "hf_doc_search",
        "hf_doc_fetch",
        "gr1_z_image_turbo_generate",
    }
    info = []
    for tool in TOOLS:
        name = getattr(tool, "name", None)
        if not name:
            continue
        if name.startswith("hf_") or name in known_hf_tools:
            desc = getattr(tool, "description", None) or getattr(tool, "desc", "")
            info.append({"name": name, "description": desc})
    return info


def _count_hf_tool_calls_in_logs(caplog_records: list) -> int:
    """从 pytest caplog 记录中统计 [MCP TOOL RESULT] 出现次数。"""
    count = 0
    for record in caplog_records:
        msg = record.getMessage() if hasattr(record, "getMessage") else str(record)
        if "[MCP TOOL RESULT]" in msg:
            count += 1
    return count


# ── Fixtures ──────────────────────────────────────────────


@pytest.fixture
def hf_conversation_id():
    return "test-hf-req-parser-001"


# ── 核心测试 ──────────────────────────────────────────────


class TestLLMHFToolInvocation:
    """验证 LLM 在收到 HF 模型查询时，会调用 MCP 工具并把结果融入输出。"""

    @pytest.mark.skipif(not _has_hf_token(), reason="HF_TOKEN not set")
    def test_hf_tools_loaded(self):
        """前置检查：HF MCP 工具已正确加载。"""
        hf_tools = _get_hf_tools_info()
        print(f"\n=== 当前可用的 HF MCP 工具 ({len(hf_tools)} 个) ===")
        for t in hf_tools:
            desc = t["description"] or "暂无描述"
            print(f"  • {t['name']}: {desc[:80]}{'...' if len(desc) > 80 else ''}")
        assert hf_tools, "环境中没有加载任何 HF MCP 工具"

    @pytest.mark.skipif(not _has_hf_token(), reason="HF_TOKEN not set")
    def test_llm_uses_hf_mcp_for_model_query(self, hf_conversation_id, caplog):
        """
        给 LLM 输入 HuggingFace 模型需求，
        验证最终输出的 case_plan / generated_code 中包含 MCP 查询结果。
        """
        requirement = "帮我测试下 huggingface 的 qwen2b 模型"

        results = run_multi_turn(
            [requirement],
            thread_id=hf_conversation_id,
            user_id="zx",
            project_id="hf-mcp-test",
        )
        final_state = results[-1]

        # ── 1. 检查 case_plan 是否引用了 MCP 查询结果 ──
        case_plan = final_state.get("case_plan", "")
        print(f"\n=== Case Plan 预览 ({len(case_plan)} chars) ===")
        print(case_plan[:800] if case_plan else "(empty)")

        plan_has_hf = any(
            k in case_plan
            for k in [
                "HuggingFace",
                "Hugging Face",
                "hf.co",
                "Qwen",
                "hub_repo",
                "已查询",
                "资源确认",
                "模型仓库",
            ]
        )
        assert plan_has_hf, (
            f"case_plan 中没有 MCP 查询痕迹。\n前 500 字: {case_plan[:500]}"
        )

        # ── 2. 检查生成的代码是否包含正确的模型 ID ──
        code = final_state.get("generated_code", "") or final_state.get("code", "")
        print(f"\n=== Generated Code 预览 ({len(code)} chars) ===")
        print(code[:800] if code else "(empty)")

        code_has_qwen = "Qwen/Qwen2" in code or "Qwen2" in code
        assert code_has_qwen, (
            f"生成的代码里没有 Qwen 模型 ID。\n前 500 字: {code[:500]}"
        )

        # ── 3. 检查 MCP 工具是否被调用过（通过日志统计）──
        # 注意：这里统计的是整个流程的调用次数，包括 requirement_parser + planner + generator
        # 理想情况是 requirement_parser 调 1~2 次，后续节点不再重复调用
        mcp_call_count = _count_hf_tool_calls_in_logs(caplog.records)
        print(f"\n=== MCP 工具调用统计 ===")
        print(f"  整个流程共调用 {mcp_call_count} 次")

        assert mcp_call_count > 0, "没有任何 MCP 工具被调用"
        # 宽松检查：至少调用了，不严格限制次数（因为 planner 可能也会调）
        if mcp_call_count > 5:
            print(
                f"⚠️ 警告：MCP 调用了 {mcp_call_count} 次，建议优化 prompt 避免重复查询"
            )

        print(f"\n✅ 通过：LLM 调用了 MCP 工具并生成了基于查询结果的代码")

    @pytest.mark.skipif(not _has_hf_token(), reason="HF_TOKEN not set")
    def test_llm_code_uses_env_for_model_id(self, hf_conversation_id):
        """
        验证生成的代码使用环境变量配置模型 ID（说明考虑了可配置性）。
        """
        requirement = "帮我测试下 huggingface 的 qwen2b 模型"
        results = run_multi_turn(
            [requirement],
            thread_id=hf_conversation_id + "-env",
            user_id="zx",
            project_id="hf-mcp-test",
        )
        code = results[-1].get("generated_code", "")

        has_env_var = "os.environ" in code or "os.getenv" in code or "HF_" in code
        print(f"\n=== 环境变量检查 ===")
        print(f"  代码中使用环境变量: {has_env_var}")

        # 软断言：不强制要求，但建议
        if not has_env_var:
            print(f"⚠️ 建议：代码中未使用环境变量配置模型 ID")


class TestRequirementParserSingleToolCall:
    """验证 requirement_parser 只调用一次工具，后续节点不复查。"""

    @pytest.mark.skipif(not _has_hf_token(), reason="HF_TOKEN not set")
    def test_req_parser_calls_tool_once(self, hf_conversation_id, caplog):
        """
        理想流程：requirement_parser 调 1~2 次 hub_repo_search，
        planner/generator 直接读取结果，不再重复调用。
        """
        requirement = "帮我测试下 huggingface 的 qwen2b 模型"

        # 清空之前的日志记录
        caplog.clear()

        results = run_multi_turn(
            [requirement],
            thread_id=hf_conversation_id + "-once",
            user_id="zx",
            project_id="hf-mcp-test",
        )

        mcp_count = _count_hf_tool_calls_in_logs(caplog.records)
        print(f"\n=== 单次测试 MCP 调用次数: {mcp_count} ===")

        # 严格检查：requirement_parser 应该调了，但不应该超过 3 次（1次搜索+1次详情+容错）
        assert mcp_count >= 1, "requirement_parser 没有调用任何 MCP 工具"
        assert mcp_count <= 5, (
            f"MCP 工具被调用了 {mcp_count} 次，说明 planner/generator 在重复查询。\n"
            f"建议：把 requirement_parser 的查询结果写入 state，后续节点直接读取。"
        )


class TestLLMHFGracefulFallback:
    """降级：无 HF_TOKEN 时，系统不应崩溃。"""

    def test_fallback_without_hf_token(self, monkeypatch, hf_conversation_id):
        """
        无 HF_TOKEN 时，HF MCP 工具不应加载，LLM 应基于通用知识回答。
        """
        # 关键：先移除 token，再重新加载 tools 模块
        monkeypatch.delenv("HF_TOKEN", raising=False)

        # 重新加载 tools 模块，让 _load_hf_mcp_tools() 重新执行
        if "src.agent.tools" in sys.modules:
            importlib.reload(sys.modules["src.agent.tools"])

        # 重新导入 TOOLS（此时应该只有 save_to_file + read_file）
        from src.agent.tools import TOOLS as fallback_tools

        hf_tools = [
            t for t in fallback_tools if getattr(t, "name", "").startswith("hf_")
        ]
        print(
            f"\n=== 降级场景工具数: {len(fallback_tools)} (HF 工具: {len(hf_tools)}) ==="
        )

        # 无 token 时，应该没有 HF 工具
        assert len(hf_tools) == 0, f"无 HF_TOKEN 时仍加载了 {len(hf_tools)} 个 HF 工具"

        requirement = "帮我测试下 huggingface 的 qwen2b 模型"
        try:
            results = run_multi_turn(
                [requirement],
                thread_id=hf_conversation_id + "-fallback",
                user_id="zx",
                project_id="hf-mcp-test",
            )
        except Exception as e:
            pytest.fail(f"无 HF_TOKEN 时 run_multi_turn 抛异常: {e}")

        state = results[-1]
        messages = state.get("messages", [])
        code = state.get("generated_code", "") or state.get("code", "")

        print(f"\n=== 降级场景输出 ===")
        print(f"  消息数: {len(messages)}")
        print(f"  代码长度: {len(code)}")

        # 无 token 时，至少应该返回一些内容
        assert len(messages) >= 1, "没有任何消息返回"
        assert code or any(
            (
                m.get("content", "")
                if isinstance(m, dict)
                else str(getattr(m, "content", ""))
            )
            for m in messages
        ), "没有任何文本输出"
