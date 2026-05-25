"""Factory for sandbox clients."""

from .base import SandboxClient
from .local_docker import LocalDockerSandboxClient
from .remote_ssh_docker import RemoteSshDockerSandboxClient


def build_sandbox_client(provider: str) -> SandboxClient:
    """Build a sandbox client for the requested provider."""
    if provider == "local_docker":
        return LocalDockerSandboxClient()
    if provider == "remote_ssh_docker":
        return RemoteSshDockerSandboxClient()
    raise ValueError(f"Unsupported sandbox provider: {provider}")
