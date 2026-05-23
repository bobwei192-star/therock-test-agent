"""冒烟测试 —— 端到端验证 Agent 可正常执行。"""

import os

import pytest
from dotenv import load_dotenv

load_dotenv()


@pytest.mark.skipif(
    not bool(os.environ.get("DEEPSEEK_API_KEY")),
    reason="未配置 DEEPSEEK_API_KEY，跳过冒烟测试",
)
class TestAgentSmoke:
    def test_simple_prompt_returns_result(self):
        from src.agent.runner import run_once

        state = run_once("say hello in one sentence")
        assert state is not None
        assert state.get("messages")

    def test_generates_code_for_pytest_request(self):
        from src.agent.runner import run_once

        state = run_once("写一个 pytest 测试函数 test_one，断言 1+1==2")
        code = state.get("generated_code") or state.get("code", "")
        assert code, "generator 未生成代码"
        assert "def test_" in code, f"代码中应包含测试函数，实际: {code[:200]}"

    def test_planner_produces_case_plan(self):
        from src.agent.runner import run_once

        state = run_once("测试 rocminfo 是否存在")
        plan = state.get("case_plan", "")
        assert plan, "planner 未生成测试计划"


@pytest.mark.skipif(
    bool(os.environ.get("DEEPSEEK_API_KEY")),
    reason="API Key 已配置，无密钥测试跳过",
)
class TestAgentSmokeNoKey:
    def test_graph_compiles_without_model(self):
        from src.agent.graph import build_graph

        g = build_graph()
        nodes = list(g.get_graph().nodes.keys())
        assert len(nodes) >= 6, f"即使无模型也应编译: {nodes}"

    def test_no_key_does_not_crash(self):
        import os

        old_key = os.environ.pop("DEEPSEEK_API_KEY", None)
        try:
            from src.agent.graph import build_graph

            g = build_graph()
            nodes = [n for n in g.get_graph().nodes.keys() if not n.startswith("__")]
            assert len(nodes) == 4
        finally:
            if old_key:
                os.environ["DEEPSEEK_API_KEY"] = old_key
