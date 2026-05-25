import pytest

from src.agent.sandbox.factory import build_sandbox_client
from src.agent.sandbox.local_docker import LocalDockerSandboxClient
from src.agent.sandbox.remote_ssh_docker import RemoteSshDockerSandboxClient


def test_build_local_docker_client():
    client = build_sandbox_client("local_docker")

    assert isinstance(client, LocalDockerSandboxClient)


def test_build_remote_ssh_docker_client():
    client = build_sandbox_client("remote_ssh_docker")

    assert isinstance(client, RemoteSshDockerSandboxClient)


def test_build_unknown_provider_fails():
    with pytest.raises(ValueError, match="Unsupported sandbox provider"):
        build_sandbox_client("unknown")