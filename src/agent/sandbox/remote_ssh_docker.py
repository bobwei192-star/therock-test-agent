"""Remote SSH Docker sandbox provider for ROCm-capable hosts."""

from __future__ import annotations

import os
import shlex
import shutil
import subprocess
import tempfile
import time
import uuid
from pathlib import PurePosixPath

from .base import CommandResult, SandboxClient, SandboxConfig, SandboxHandle


class RemoteSshDockerSandboxClient(SandboxClient):
    """Run generated tests in Docker on a remote AMD/ROCm host over SSH."""

    def __init__(self) -> None:
        self._configs: dict[str, SandboxConfig] = {}

    def create(
        self,
        config: SandboxConfig,
        sandbox_id: str | None = None,
    ) -> SandboxHandle:
        """Create a detached remote Docker container or reuse an existing one."""
        if sandbox_id and self._is_container_running(config, sandbox_id):
            self._configs[sandbox_id] = config
            return SandboxHandle(sandbox_id=sandbox_id, provider=config.provider)

        container_name = f"testcase-agent-{uuid.uuid4().hex[:12]}"
        device_args = self._build_device_args(config.device_name)
        env_args = self._build_env_args(config)
        network_arg = "--network none" if config.block_network else ""
        command = " ".join(
            part
            for part in (
                f"mkdir -p {shlex.quote(config.remote_work_dir)} &&",
                "docker run -d",
                f"--name {shlex.quote(container_name)}",
                "-w /tmp/testcase_agent",
                network_arg,
                device_args,
                env_args,
                shlex.quote(config.image),
                "sleep infinity",
            )
            if part
        )
        result = self._run_remote(config, command, timeout=config.timeout)
        if result.exit_code != 0:
            raise RuntimeError(
                "Failed to create remote Docker sandbox: "
                f"{result.stderr or result.stdout}"
            )

        container_id = result.stdout.strip().splitlines()[-1]
        self._configs[container_id] = config
        return SandboxHandle(sandbox_id=container_id, provider=config.provider)

    def upload_text(
        self,
        handle: SandboxHandle,
        content: str,
        remote_path: str,
    ) -> None:
        """Copy text to the remote host, then into the remote container."""
        config = self._get_config(handle)
        target = PurePosixPath(remote_path)
        remote_stage_dir = f"{config.remote_work_dir}/{handle.sandbox_id}"
        remote_stage_file = f"{remote_stage_dir}/{target.name}"

        mkdir_result = self._run_remote(
            config,
            f"mkdir -p {shlex.quote(remote_stage_dir)}",
            timeout=30,
        )
        if mkdir_result.exit_code != 0:
            raise RuntimeError(
                "Failed to create remote staging directory: "
                f"{mkdir_result.stderr or mkdir_result.stdout}"
            )

        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False) as tmp:
            tmp.write(content)
            tmp_path = tmp.name
        try:
            self._copy_to_remote(config, tmp_path, remote_stage_file)
        finally:
            os.unlink(tmp_path)

        copy_result = self._run_remote(
            config,
            " ".join(
                (
                    f"docker exec {shlex.quote(handle.sandbox_id)}",
                    f"mkdir -p {shlex.quote(str(target.parent))} &&",
                    "docker cp",
                    shlex.quote(remote_stage_file),
                    f"{shlex.quote(handle.sandbox_id)}:{shlex.quote(str(target))}",
                )
            ),
            timeout=30,
        )
        if copy_result.exit_code != 0:
            raise RuntimeError(
                "Failed to copy generated code into remote container: "
                f"{copy_result.stderr or copy_result.stdout}"
            )

    def exec(
        self,
        handle: SandboxHandle,
        command: str,
        timeout: int,
    ) -> CommandResult:
        """Execute a shell command inside the remote Docker container."""
        config = self._get_config(handle)
        timeout_seconds = max(1, int(timeout))
        wrapped_command = f"timeout {timeout_seconds}s sh -lc {shlex.quote(command)}"
        remote_command = (
            f"docker exec -w /tmp/testcase_agent {shlex.quote(handle.sandbox_id)} "
            f"sh -lc {shlex.quote(wrapped_command)}"
        )
        result = self._run_remote(
            config,
            remote_command,
            timeout=timeout_seconds + 10,
        )
        if result.exit_code == 124 or result.duration_seconds > timeout_seconds:
            return CommandResult(
                exit_code=124,
                stdout=result.stdout,
                stderr=(
                    f"{result.stderr}\nCommand timed out after "
                    f"{timeout_seconds}s"
                ).strip(),
                duration_seconds=result.duration_seconds,
            )
        return result

    def destroy(self, handle: SandboxHandle) -> None:
        """Remove the remote Docker container and staged files."""
        config = self._get_config(handle)
        self._run_remote(
            config,
            (
                f"docker rm -f {shlex.quote(handle.sandbox_id)} >/dev/null 2>&1 || true; "
                f"rm -rf {shlex.quote(config.remote_work_dir + '/' + handle.sandbox_id)}"
            ),
            timeout=30,
        )

    def _get_config(self, handle: SandboxHandle) -> SandboxConfig:
        return self._configs.get(handle.sandbox_id, SandboxConfig(provider=handle.provider))

    def _is_container_running(self, config: SandboxConfig, sandbox_id: str) -> bool:
        result = self._run_remote(
            config,
            f"docker inspect -f '{{{{.State.Running}}}}' {shlex.quote(sandbox_id)}",
            timeout=30,
        )
        return result.exit_code == 0 and result.stdout.strip() == "true"

    def _run_remote(
        self,
        config: SandboxConfig,
        command: str,
        timeout: int,
    ) -> CommandResult:
        ssh_cmd = self._ssh_command(config) + [
            self._target(config),
            f"sh -lc {shlex.quote(command)}",
        ]
        started = time.monotonic()
        try:
            completed = subprocess.run(
                ssh_cmd,
                text=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                check=False,
                timeout=max(1, int(timeout)),
                env=self._command_env(config),
            )
        except subprocess.TimeoutExpired as exc:
            duration = time.monotonic() - started
            return CommandResult(
                exit_code=124,
                stdout=exc.stdout or "",
                stderr=(exc.stderr or "") + f"\nSSH command timed out after {timeout}s",
                duration_seconds=duration,
            )
        duration = time.monotonic() - started
        return CommandResult(
            exit_code=completed.returncode,
            stdout=completed.stdout or "",
            stderr=completed.stderr or "",
            duration_seconds=duration,
        )

    def _copy_to_remote(
        self,
        config: SandboxConfig,
        local_path: str,
        remote_path: str,
    ) -> None:
        scp_cmd = self._scp_command(config) + [
            local_path,
            f"{self._target(config)}:{remote_path}",
        ]
        completed = subprocess.run(
            scp_cmd,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
            timeout=60,
            env=self._command_env(config),
        )
        if completed.returncode != 0:
            raise RuntimeError(
                "Failed to push generated code to remote host: "
                f"{completed.stderr or completed.stdout}"
            )

    def _ssh_command(self, config: SandboxConfig) -> list[str]:
        return self._auth_prefix(config) + [
            "ssh",
            "-o",
            "StrictHostKeyChecking=no",
            "-o",
            "UserKnownHostsFile=/dev/null",
        ]

    def _scp_command(self, config: SandboxConfig) -> list[str]:
        return self._auth_prefix(config) + [
            "scp",
            "-o",
            "StrictHostKeyChecking=no",
            "-o",
            "UserKnownHostsFile=/dev/null",
        ]

    def _auth_prefix(self, config: SandboxConfig) -> list[str]:
        if not config.remote_password:
            return []
        if shutil.which("sshpass") is None:
            raise RuntimeError(
                "sshpass is required when TEST_CASE_AGENT_REMOTE_PASSWORD is set. "
                "Install sshpass or configure SSH key authentication and clear "
                "remote_password."
            )
        return ["sshpass", "-e"]

    def _command_env(self, config: SandboxConfig) -> dict[str, str]:
        env = os.environ.copy()
        if config.remote_password:
            env["SSHPASS"] = config.remote_password
        return env

    @staticmethod
    def _target(config: SandboxConfig) -> str:
        return f"{config.remote_user}@{config.remote_host}"

    @staticmethod
    def _build_device_args(device_name: str) -> str:
        devices = [item.strip() for item in device_name.split(",") if item.strip()]
        return " ".join(f"--device {shlex.quote(device)}" for device in devices)

    @staticmethod
    def _build_env_args(config: SandboxConfig) -> str:
        env_vars = {"DEVICE_NAME": config.device_name, **config.env_vars}
        return " ".join(
            f"-e {shlex.quote(key)}={shlex.quote(value)}"
            for key, value in env_vars.items()
        )
