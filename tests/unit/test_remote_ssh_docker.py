from pathlib import PurePosixPath

from src.agent.sandbox.base import CommandResult, SandboxConfig, SandboxHandle
from src.agent.sandbox.remote_ssh_docker import RemoteSshDockerSandboxClient


class RecordingRemoteClient(RemoteSshDockerSandboxClient):
    def __init__(self):
        super().__init__()
        self.commands: list[str] = []
        self.copies: list[tuple[str, str]] = []

    def _run_remote(self, config, command, timeout):
        self.commands.append(command)
        if "docker run" in command:
            return CommandResult(exit_code=0, stdout="container-123\n", stderr="")
        return CommandResult(exit_code=0, stdout="", stderr="")

    def _copy_to_remote(self, config, local_path, remote_path):
        assert PurePosixPath(local_path).name
        self.copies.append((local_path, remote_path))


def test_remote_create_passes_amd_devices_and_device_name():
    client = RecordingRemoteClient()
    config = SandboxConfig(
        provider="remote_ssh_docker",
        image="rocm/dev-ubuntu-22.04:6.0",
        device_name="/dev/kfd,/dev/dri",
    )

    handle = client.create(config)

    assert handle.sandbox_id == "container-123"
    docker_run = next(command for command in client.commands if "docker run" in command)
    assert "--device /dev/kfd" in docker_run
    assert "--device /dev/dri" in docker_run
    assert "-e DEVICE_NAME=/dev/kfd,/dev/dri" in docker_run
    assert "rocm/dev-ubuntu-22.04:6.0" in docker_run


def test_remote_upload_pushes_to_host_then_copies_into_container():
    client = RecordingRemoteClient()
    config = SandboxConfig(provider="remote_ssh_docker")
    handle = SandboxHandle(sandbox_id="container-123", provider="remote_ssh_docker")
    client._configs[handle.sandbox_id] = config

    client.upload_text(handle, "def test_ok():\n    assert True\n", "/tmp/testcase_agent/test_generated.py")

    assert client.copies
    assert client.copies[0][1] == "/tmp/testcase_agent/container-123/test_generated.py"
    assert any("docker cp" in command for command in client.commands)