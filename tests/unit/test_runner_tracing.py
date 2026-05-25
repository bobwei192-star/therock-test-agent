"""Runner tracing config tests."""

from unittest.mock import MagicMock

from src.agent.runner import build_runtime_config


def test_build_runtime_config_merges_langfuse_callbacks(monkeypatch):
    """运行入口应同时保留 checkpoint thread_id 和 Langfuse callbacks。"""
    mock_handler = MagicMock()

    def fake_build_langfuse_config(thread_id: str):
        return {
            "callbacks": [mock_handler],
            "metadata": {"langfuse_user_id": thread_id},
        }

    monkeypatch.setattr(
        "src.agent.runner.build_langfuse_config",
        fake_build_langfuse_config,
    )

    config = build_runtime_config(thread_id="trace-thread")

    assert config["configurable"]["thread_id"] == "trace-thread"
    assert config["callbacks"] == [mock_handler]
    assert config["metadata"]["langfuse_user_id"] == "trace-thread"


def test_cli_runner_uses_runtime_config(monkeypatch):
    """make gen_case 的 CLI 路径也应携带 Langfuse callbacks。"""
    from src.agent.cli import cli_runner

    mock_graph = MagicMock()
    mock_handler = MagicMock()

    monkeypatch.setattr(
        cli_runner,
        "build_runnable_graph",
        lambda **kwargs: mock_graph,
    )
    monkeypatch.setattr(
        cli_runner,
        "build_runtime_config",
        lambda thread_id: {
            "configurable": {"thread_id": thread_id},
            "callbacks": [mock_handler],
        },
    )

    runner = cli_runner.CLIRunner(thread_id="cli-thread", hitl=False)

    assert runner.config["configurable"]["thread_id"] == "cli-thread"
    assert runner.config["callbacks"] == [mock_handler]


def test_print_final_result_skips_output_save_on_sandbox_failure(monkeypatch):
    """沙盒最终失败时不应再把完整代码保存到 output/。"""
    from src.agent.cli import cli_runner

    save_mock = MagicMock()
    monkeypatch.setattr(cli_runner, "_save_code", save_mock)

    cli_runner.print_final_result(
        {
            "generated_code": "def test_ok():\n    assert True\n",
            "validation_result": {
                "status": "passed",
                "quality_gate": "real_pytest_code",
                "errors": [],
            },
            "execution_result": {
                "status": "failed",
                "stage": "dependency",
                "exit_code": 127,
                "error": "Failed to install pytest in sandbox.",
            },
        }
    )

    save_mock.assert_not_called()