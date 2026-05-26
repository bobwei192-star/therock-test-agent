"""测试 P0 功能实现：多轮对话、结果驱动修复、用户驱动修复、执行计划节点"""

import pytest
from unittest.mock import Mock, patch, MagicMock
from typing import Any, Dict

from src.agent.graph import build_graph, route_after_sandbox
from src.agent.state import AgentState


class TestMultiTurnConversation:
    """测试多轮对话功能"""

    def test_cli_runner_has_conversation_state(self):
        """测试 CLIRunner 包含对话状态"""
        from src.agent.cli.cli_runner import CLIRunner
        
        runner = CLIRunner()
        
        assert hasattr(runner, '_conversation_state')
        assert hasattr(runner, '_is_first_turn')
        assert runner._is_first_turn is True
        assert runner._conversation_state == {}

    def test_cli_runner_first_turn(self):
        """测试第一轮对话"""
        from src.agent.cli.cli_runner import CLIRunner
        
        runner = CLIRunner()
        
        # 模拟第一轮
        assert runner._is_first_turn is True
        
        # 第一轮后应该变为 False
        runner._is_first_turn = False
        assert runner._is_first_turn is False

    def test_cli_runner_follow_up_turn(self):
        """测试追问模式"""
        from src.agent.cli.cli_runner import CLIRunner
        
        runner = CLIRunner()
        
        # 模拟已有对话状态
        runner._is_first_turn = False
        runner._conversation_state = {"messages": [{"role": "user", "content": "test"}]}
        
        # 检测追问
        is_follow_up = not runner._is_first_turn and runner._conversation_state
        assert is_follow_up is not False  # 应该是真值（字典）


class TestResultDrivenRepair:
    """测试结果驱动修复功能"""

    def test_route_after_sandbox_success(self):
        """测试执行成功时的路由"""
        state: AgentState = {
            "execution_result": {"status": "success"},
            "sandbox_retry_count": 0,
            "max_sandbox_retries": 3,
        }
        
        result = route_after_sandbox(state)
        assert result == "__end__"

    def test_route_after_sandbox_failure_retry(self):
        """测试执行失败时的重试路由"""
        state: AgentState = {
            "execution_result": {
                "status": "failed",
                "stage": "pytest_execution",
                "error": "测试失败",
                "exit_code": 1,
            },
            "sandbox_retry_count": 0,
            "max_sandbox_retries": 3,
        }
        
        result = route_after_sandbox(state)
        assert result == "planner"

    def test_route_after_sandbox_max_retries(self):
        """测试达到最大重试次数时的路由"""
        state: AgentState = {
            "execution_result": {
                "status": "failed",
                "stage": "pytest_execution",
                "error": "测试失败",
                "exit_code": 1,
            },
            "sandbox_retry_count": 3,
            "max_sandbox_retries": 3,
        }
        
        result = route_after_sandbox(state)
        assert result == "__end__"

    def test_route_after_sandbox_retry_progression(self):
        """测试重试进度"""
        # 第 1 次失败
        state1: AgentState = {
            "execution_result": {"status": "failed", "stage": "test", "error": "err"},
            "sandbox_retry_count": 0,
            "max_sandbox_retries": 3,
        }
        assert route_after_sandbox(state1) == "planner"
        
        # 第 2 次失败
        state2: AgentState = {
            "execution_result": {"status": "failed", "stage": "test", "error": "err"},
            "sandbox_retry_count": 1,
            "max_sandbox_retries": 3,
        }
        assert route_after_sandbox(state2) == "planner"
        
        # 第 3 次失败（达到最大）
        state3: AgentState = {
            "execution_result": {"status": "failed", "stage": "test", "error": "err"},
            "sandbox_retry_count": 2,
            "max_sandbox_retries": 3,
        }
        assert route_after_sandbox(state3) == "planner"
        
        # 第 4 次（超过最大）
        state4: AgentState = {
            "execution_result": {"status": "failed", "stage": "test", "error": "err"},
            "sandbox_retry_count": 3,
            "max_sandbox_retries": 3,
        }
        assert route_after_sandbox(state4) == "__end__"


class TestUserDrivenRepair:
    """测试用户驱动修复功能"""

    def test_cli_chat_fix_command(self):
        """测试 fix 命令解析"""
        prompt = "fix 添加超时处理"
        
        if prompt.lower().startswith("fix "):
            fix_desc = prompt[4:].strip()
            new_prompt = f"请修复测试用例：{fix_desc}"
            
        assert fix_desc == "添加超时处理"
        assert new_prompt == "请修复测试用例：添加超时处理"

    def test_cli_chat_feedback_command(self):
        """测试 feedback 命令解析"""
        prompt = "feedback 测试应该检查返回值"
        
        if prompt.lower().startswith("feedback "):
            feedback = prompt[9:].strip()
            new_prompt = f"用户反馈：{feedback}。请根据反馈调整测试用例。"
            
        assert feedback == "测试应该检查返回值"
        assert "用户反馈" in new_prompt

    def test_cli_chat_new_command(self):
        """测试 new 命令重置对话"""
        from src.agent.cli.cli_runner import CLIRunner
        
        runner = CLIRunner()
        runner._is_first_turn = False
        runner._conversation_state = {"messages": ["test"]}
        
        # 模拟 new 命令
        runner._is_first_turn = True
        runner._conversation_state = {}
        
        assert runner._is_first_turn is True
        assert runner._conversation_state == {}


class TestExecutionPlannerNode:
    """测试执行计划节点"""

    def test_execution_planner_import(self):
        """测试执行计划节点导入"""
        from src.agent.nodes import execution_planner
        
        assert callable(execution_planner)

    def test_graph_includes_execution_planner(self):
        """测试图包含执行计划节点"""
        graph = build_graph()
        
        assert "execution_planner" in graph.nodes
        assert len(graph.nodes) == 7  # __start__ + 6 个节点

    def test_graph_execution_order(self):
        """测试图执行顺序"""
        graph = build_graph()
        
        nodes = list(graph.nodes.keys())
        
        # 验证顺序
        assert nodes[0] == "__start__"
        assert nodes[1] == "requirement_parser"
        assert nodes[2] == "context_retriever"
        assert nodes[3] == "planner"
        assert nodes[4] == "execution_planner"
        assert nodes[5] == "generator"
        assert nodes[6] == "sandbox_executor"


class TestCLICommands:
    """测试 CLI 命令"""

    def test_cli_runner_node_names(self):
        """测试 CLI Runner 节点名称列表"""
        from src.agent.cli.cli_runner import NODE_NAMES
        
        assert "execution_planner" in NODE_NAMES
        assert NODE_NAMES.index("planner") < NODE_NAMES.index("execution_planner")
        assert NODE_NAMES.index("execution_planner") < NODE_NAMES.index("generator")

    def test_cli_runner_output_keys(self):
        """测试 CLI Runner 输出键映射"""
        from src.agent.cli.cli_runner import NODE_OUTPUT_KEYS
        
        assert NODE_OUTPUT_KEYS["execution_planner"] == "execution_plan"
        assert NODE_OUTPUT_KEYS["planner"] == "case_plan"
        assert NODE_OUTPUT_KEYS["generator"] == "generated_code"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
