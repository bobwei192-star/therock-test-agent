from src.agent.nodes import node_sandbox_executor
from src.agent.sandbox.base import CommandResult, SandboxHandle


class FakeSandboxClient:
    def __init__(self, pytest_exit_code: int = 0):
        self.pytest_exit_code = pytest_exit_code
        self.commands = []

    def create(self, config, sandbox_id=None):
        return SandboxHandle(sandbox_id=sandbox_id or "fake-sandbox", provider=config.provider)

    def upload_text(self, handle, content, remote_path):
        self.uploaded = (handle, content, remote_path)

    def exec(self, handle, command, timeout):
        self.commands.append(command)
        if "pip install" in command or "pytest --version" in command:
            return CommandResult(exit_code=0, stdout="", stderr="")
        return CommandResult(
            exit_code=self.pytest_exit_code,
            stdout="pytest stdout",
            stderr="pytest stderr" if self.pytest_exit_code else "",
        )

    def destroy(self, handle):
        pass


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
    fake_client = FakeSandboxClient(pytest_exit_code=0)
    monkeypatch.setattr(
        node_sandbox_executor,
        "build_sandbox_client",
        lambda provider: fake_client,
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
    assert "command -v python3 || command -v python" in fake_client.commands[0]
    assert "$PYTHON_BIN -m pytest test_generated.py -v" in fake_client.commands[1]


def test_sandbox_executor_uses_detected_python_for_dependency_and_pytest(monkeypatch):
    fake_client = FakeSandboxClient(pytest_exit_code=0)
    monkeypatch.setattr(
        node_sandbox_executor,
        "build_sandbox_client",
        lambda provider: fake_client,
    )

    node_sandbox_executor.sandbox_executor(
        {
            "generated_code": "def test_ok():\n    assert True\n",
            "sandbox_config": {"provider": "remote_ssh_docker"},
            "sandbox_retry_count": 0,
            "max_sandbox_retries": 3,
        }
    )

    assert len(fake_client.commands) == 2
    assert "PYTHON_BIN=$(command -v python3 || command -v python)" in fake_client.commands[0]
    assert "$PYTHON_BIN -m pip install pytest -q" in fake_client.commands[0]
    assert "PYTHON_BIN=$(command -v python3 || command -v python)" in fake_client.commands[1]
    assert "$PYTHON_BIN -m pytest test_generated.py -v" in fake_client.commands[1]


def test_sandbox_executor_pytest_failure_increments_retry(monkeypatch):
    monkeypatch.setattr(
        node_sandbox_executor,
        "build_sandbox_client",
        lambda provider: FakeSandboxClient(pytest_exit_code=1),
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
    assert result["execution_result"]["stage"] == "pytest"
    assert result["sandbox_retry_count"] == 1
    assert "完整新计划" in result["feedback"]