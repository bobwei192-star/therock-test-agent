"""Local Docker sandbox provider."""

from __future__ import annotations

import io
import tarfile
import time
from pathlib import PurePosixPath

from .base import CommandResult, SandboxClient, SandboxConfig, SandboxHandle


class LocalDockerSandboxClient(SandboxClient):
    """Run generated tests in an isolated local Docker container."""

    def create(
        self,
        config: SandboxConfig,
        sandbox_id: str | None = None,
    ) -> SandboxHandle:
        """Create a detached Python container or reuse an existing one."""
        docker = self._docker_module()
        client = docker.from_env()

        if sandbox_id:
            try:
                container = client.containers.get(sandbox_id)
                container.reload()
                if container.status == "running":
                    return SandboxHandle(
                        sandbox_id=container.id,
                        provider=config.provider,
                    )
            except docker.errors.NotFound:
                pass

        network_mode = "none" if config.block_network else None
        container = client.containers.run(
            config.image,
            command=["sleep", "infinity"],
            detach=True,
            environment=config.env_vars,
            network_mode=network_mode,
            working_dir="/tmp/testcase_agent",
        )
        return SandboxHandle(sandbox_id=container.id, provider=config.provider)

    def upload_text(
        self,
        handle: SandboxHandle,
        content: str,
        remote_path: str,
    ) -> None:
        """Upload text by writing a small tar archive into the container."""
        docker = self._docker_module()
        client = docker.from_env()
        container = client.containers.get(handle.sandbox_id)

        target = PurePosixPath(remote_path)
        data = content.encode("utf-8")
        archive = io.BytesIO()
        with tarfile.open(fileobj=archive, mode="w") as tar:
            info = tarfile.TarInfo(name=target.name)
            info.size = len(data)
            info.mtime = int(time.time())
            tar.addfile(info, io.BytesIO(data))
        archive.seek(0)

        self.exec(
            handle,
            f"mkdir -p {self._quote_posix(str(target.parent))}",
            timeout=30,
        )
        container.put_archive(str(target.parent), archive.getvalue())

    def exec(
        self,
        handle: SandboxHandle,
        command: str,
        timeout: int,
    ) -> CommandResult:
        """Execute a shell command inside the container."""
        docker = self._docker_module()
        client = docker.from_env()
        container = client.containers.get(handle.sandbox_id)

        timeout_seconds = max(1, int(timeout))
        wrapped_command = (
            f"timeout {timeout_seconds}s sh -lc {self._quote_posix(command)}"
        )
        started = time.monotonic()
        result = container.exec_run(
            ["sh", "-lc", wrapped_command],
            stdout=True,
            stderr=True,
            demux=True,
            workdir="/tmp/testcase_agent",
        )
        duration = time.monotonic() - started
        stdout_bytes, stderr_bytes = result.output or (b"", b"")
        stdout = (stdout_bytes or b"").decode("utf-8", errors="replace")
        stderr = (stderr_bytes or b"").decode("utf-8", errors="replace")

        if result.exit_code == 124 or duration > timeout_seconds:
            return CommandResult(
                exit_code=124,
                stdout=stdout,
                stderr=(
                    f"{stderr}\nCommand timed out after {timeout_seconds}s".strip()
                ),
                duration_seconds=duration,
            )
        return CommandResult(
            exit_code=result.exit_code,
            stdout=stdout,
            stderr=stderr,
            duration_seconds=duration,
        )

    def destroy(self, handle: SandboxHandle) -> None:
        """Stop and remove a local Docker container."""
        docker = self._docker_module()
        client = docker.from_env()
        try:
            container = client.containers.get(handle.sandbox_id)
        except docker.errors.NotFound:
            return
        container.remove(force=True)

    @staticmethod
    def _docker_module():
        """Import Docker lazily so normal graph imports do not require Docker."""
        try:
            import docker
        except ImportError as exc:
            raise RuntimeError(
                "Docker SDK is required for local_docker sandbox. "
                "Install it with: pip install docker"
            ) from exc
        return docker

    @staticmethod
    def _quote_posix(value: str) -> str:
        return "'" + value.replace("'", "'\\''") + "'"
