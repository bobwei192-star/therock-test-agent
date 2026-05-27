from src.agent.nodes import node_sandbox_executor
from src.agent.sandbox.base import CommandResult, SandboxHandle
from src.agent.sandbox import strategy as sandbox_strategy


def test_sandbox_executor_fails_without_generated_code():
    result = node_sandbox_executor.sandbox_executor(
        {
            "generated_code": "",
            "sandbox_retry_count": 0,
            "max_sandbox_retries": 3,
        }
    )

    assert result["execution_result"]["status"] == "failed"
    assert result["execution_result"]["stage"] == "missing_code"
    assert result["sandbox_retry_count"] == 1


def test_sandbox_executor_success(monkeypatch):
    monkeypatch.setattr(
        sandbox_strategy,
        "execute_with_strategy",
        lambda intent, artifact_path, state: {
            "status": "success",
            "stdout": "pytest stdout",
            "stderr": "",
            "returncode": 0,
        },
    )

    result = node_sandbox_executor.sandbox_executor(
        {
            "generated_code": "def test_ok():\n    assert True\n",
            "sandbox_config": {"provider": "local_docker"},
            "sandbox_retry_count": 0,
            "max_sandbox_retries": 3,
        }
    )

    assert result["execution_result"]["status"] == "success"
    assert result["feedback"] == ""


def test_sandbox_executor_uses_detected_python_for_dependency_and_pytest(monkeypatch):
    calls = []

    def fake_execute(intent, artifact_path, state):
        calls.append((intent, artifact_path))
        return {
            "status": "success",
            "stdout": "ok",
            "stderr": "",
            "returncode": 0,
        }

    monkeypatch.setattr(sandbox_strategy, "execute_with_strategy", fake_execute)

    node_sandbox_executor.sandbox_executor(
        {
            "generated_code": "def test_ok():\n    assert True\n",
            "sandbox_config": {"provider": "remote_ssh_docker"},
            "sandbox_retry_count": 0,
            "max_sandbox_retries": 3,
        }
    )

    assert len(calls) == 1
    assert calls[0][0] == "GENERATE"


def test_sandbox_executor_pytest_failure_increments_retry(monkeypatch):
    monkeypatch.setattr(
        sandbox_strategy,
        "execute_with_strategy",
        lambda intent, artifact_path, state: {
            "status": "failed",
            "stdout": "pytest stdout",
            "stderr": "pytest stderr",
            "returncode": 1,
            "errors": ["1 test failed"],
        },
    )

    result = node_sandbox_executor.sandbox_executor(
        {
            "generated_code": "def test_fail():\n    assert False\n",
            "sandbox_config": {"provider": "local_docker"},
            "sandbox_retry_count": 0,
            "max_sandbox_retries": 3,
        }
    )

    assert result["execution_result"]["status"] == "failed"
    assert result["execution_result"]["stage"] == "generate_execution"
    assert result["sandbox_retry_count"] == 1
    assert result["feedback"] != ""