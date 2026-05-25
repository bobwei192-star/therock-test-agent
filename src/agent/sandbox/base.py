"""Sandbox client abstractions used by the execution node."""

import os

from abc import ABC, abstractmethod
from dataclasses import dataclass, field


@dataclass(frozen=True)
class SandboxConfig:
    """Configuration for creating or reusing an isolated sandbox."""

    provider: str = "remote_ssh_docker"
    image: str = "rocm/dev-ubuntu-22.04:6.0"
    timeout: int = 120
    block_network: bool = False
    env_vars: dict[str, str] = field(default_factory=dict)
    remote_host: str = os.environ.get("TEST_CASE_AGENT_REMOTE_HOST", "10.67.69.34")
    remote_user: str = os.environ.get("TEST_CASE_AGENT_REMOTE_USER", "jenkins")
    remote_password: str = os.environ.get("TEST_CASE_AGENT_REMOTE_PASSWORD", "0")
    remote_work_dir: str = "/tmp/testcase_agent"
    device_name: str = "/dev/kfd,/dev/dri"


@dataclass(frozen=True)
class SandboxHandle:
    """Reference to a sandbox instance owned by a provider."""

    sandbox_id: str
    provider: str


@dataclass(frozen=True)
class CommandResult:
    """Result returned by a command executed inside a sandbox."""

    exit_code: int
    stdout: str
    stderr: str
    duration_seconds: float = 0.0


class SandboxClient(ABC):
    """Provider-neutral interface for sandbox operations."""

    @abstractmethod
    def create(
        self,
        config: SandboxConfig,
        sandbox_id: str | None = None,
    ) -> SandboxHandle:
        """Create or reuse a sandbox instance."""

    @abstractmethod
    def upload_text(
        self,
        handle: SandboxHandle,
        content: str,
        remote_path: str,
    ) -> None:
        """Upload text content to a path inside the sandbox."""

    @abstractmethod
    def exec(
        self,
        handle: SandboxHandle,
        command: str,
        timeout: int,
    ) -> CommandResult:
        """Execute a command inside the sandbox."""

    @abstractmethod
    def destroy(self, handle: SandboxHandle) -> None:
        """Destroy the sandbox instance."""
