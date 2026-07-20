from __future__ import annotations

import os
import shutil
import subprocess
from pathlib import Path
from typing import Any

from .artifacts import check_sudo_policy
from .audit import append_activity
from .audit import atomic_write_json
from .audit import ensure_dir
from .audit import now_iso


APT_PACKAGES = [
    "gfortran",
    "git",
    "ninja-build",
    "cmake",
    "g++",
    "pkg-config",
    "xxd",
    "automake",
    "libtool",
    "python3-venv",
    "python3-full",
    "python3-dev",
    "libegl1-mesa-dev",
    "texinfo",
    "bison",
    "flex",
    "curl",
    "make",
]

REQUIRED_COMMANDS = ["cmake", "ctest", "ninja", "g++", "pkg-config", "python3"]


class BootstrapError(RuntimeError):
    """Raised when host bootstrap cannot prepare the test machine."""


def command_path(command: str) -> str:
    return shutil.which(command) or ""


def run_command(
    command: list[str],
    *,
    cwd: Path,
    log_path: Path,
    env: dict[str, str] | None = None,
) -> None:
    with log_path.open("a", encoding="utf-8") as log:
        log.write(f"++ [{cwd}]$ {' '.join(command)}\n")
        log.flush()
        result = subprocess.run(
            command,
            cwd=str(cwd),
            env=env,
            stdout=log,
            stderr=subprocess.STDOUT,
            text=True,
        )
        log.write(f"++ exit={result.returncode}\n")
    if result.returncode != 0:
        raise BootstrapError(f"bootstrap command failed: {' '.join(command)}")


def bootstrap_dir(state: dict[str, Any]) -> Path:
    return Path(state["meta"]["output_dir"]) / "bootstrap"


def bootstrap_paths(state: dict[str, Any]) -> tuple[Path, Path]:
    directory = bootstrap_dir(state)
    ensure_dir(directory)
    return directory / "bootstrap_env.json", directory / "bootstrap_env.log"


def should_skip_bootstrap(state: dict[str, Any], therock_repo: Path | None) -> str:
    if state["meta"].get("bootstrap_env") == "off":
        return "disabled"
    if state["meta"].get("mock_command"):
        return "mock_command"
    if not therock_repo:
        return "missing_therock_repo"
    if not (therock_repo / "requirements.txt").is_file():
        return "missing_requirements_txt"
    return ""


def install_apt_packages(state: dict[str, Any], therock_repo: Path, log_path: Path) -> None:
    sudo_policy = str(state["meta"].get("sudo_policy") or "none")
    if sudo_policy not in {"cache", "askpass"}:
        raise BootstrapError(
            "bootstrap_env=auto requires --sudo-policy cache or askpass to install system packages"
        )

    env = os.environ.copy()
    if state["meta"].get("sudo_askpass"):
        env["SUDO_ASKPASS"] = str(state["meta"]["sudo_askpass"])
    if state["meta"].get("sudo_agent_socket"):
        env["THEROCK_SUDO_AGENT_SOCKET"] = str(state["meta"]["sudo_agent_socket"])

    check_sudo_policy(sudo_policy, env)
    sudo_prefix = ["sudo", "-A"] if sudo_policy == "askpass" else ["sudo", "-n"]
    run_command(sudo_prefix + ["apt", "update"], cwd=therock_repo, log_path=log_path, env=env)
    run_command(
        sudo_prefix + ["apt", "install", "-y", *APT_PACKAGES],
        cwd=therock_repo,
        log_path=log_path,
        env=env,
    )


def ensure_venv(therock_repo: Path, log_path: Path) -> Path:
    venv_dir = therock_repo / ".venv"
    python_bin = venv_dir / "bin" / "python"
    if not python_bin.is_file():
        run_command([bootstrap_python(), "-m", "venv", str(venv_dir)], cwd=therock_repo, log_path=log_path)
    run_command([str(python_bin), "-m", "pip", "install", "--upgrade", "pip"], cwd=therock_repo, log_path=log_path)
    pip_requirements = ["-r", "requirements.txt"]
    if (therock_repo / "requirements-test.txt").is_file():
        pip_requirements.extend(["-r", "requirements-test.txt"])
    run_command(
        [str(python_bin), "-m", "pip", "install", *pip_requirements],
        cwd=therock_repo,
        log_path=log_path,
    )
    if (therock_repo / "pyproject.toml").is_file() or (therock_repo / "setup.py").is_file():
        run_command([str(python_bin), "-m", "pip", "install", "-e", "."], cwd=therock_repo, log_path=log_path)
    run_command([str(python_bin), "-c", "import boto3; print('boto3 ok')"], cwd=therock_repo, log_path=log_path)
    return python_bin


def collect_command_status() -> dict[str, str]:
    return {command: command_path(command) for command in REQUIRED_COMMANDS}


def bootstrap_python() -> str:
    return os.environ.get("THEROCK_BOOTSTRAP_PYTHON", "python3")


def run_host_bootstrap(state: dict[str, Any]) -> dict[str, Any]:
    """Prepare host dependencies before the first test round."""

    mode = str(state["meta"].get("bootstrap_env") or "auto")
    if state.get("bootstrap", {}).get("status") in {"completed", "skipped"}:
        return state["bootstrap"]

    output_json, log_path = bootstrap_paths(state)
    therock_repo_raw = str(state["meta"].get("therock_repo_path") or "")
    therock_repo = Path(therock_repo_raw) if therock_repo_raw else None
    skip_reason = should_skip_bootstrap(state, therock_repo)
    record: dict[str, Any] = {
        "schema_version": "0.1",
        "mode": mode,
        "started_at": now_iso(),
        "ended_at": None,
        "status": "running",
        "therock_repo": str(therock_repo) if therock_repo else "",
        "apt_packages": APT_PACKAGES,
        "commands_before": collect_command_status(),
        "commands_after": {},
        "venv": {},
        "log": str(log_path),
    }
    append_activity(state, "bootstrap_start", {"mode": mode, "skip_reason": skip_reason})

    try:
        if mode == "off" or skip_reason:
            record["status"] = "skipped"
            record["skip_reason"] = skip_reason or "disabled"
            return record
        if mode != "auto":
            raise BootstrapError(f"unsupported bootstrap_env mode: {mode}")
        assert therock_repo is not None
        install_apt_packages(state, therock_repo, log_path)
        python_bin = ensure_venv(therock_repo, log_path)
        record["venv"] = {
            "path": str(therock_repo / ".venv"),
            "python": str(python_bin),
            "requirements_installed": True,
            "requirements_test_installed": (therock_repo / "requirements-test.txt").is_file(),
            "boto3_import": True,
            "editable_install": (therock_repo / "pyproject.toml").is_file() or (therock_repo / "setup.py").is_file(),
        }
        record["status"] = "completed"
    except Exception as exc:
        record["status"] = "failed"
        record["error"] = str(exc)
        raise
    finally:
        record["ended_at"] = now_iso()
        record["commands_after"] = collect_command_status()
        state["bootstrap"] = record
        atomic_write_json(output_json, record)
        append_activity(state, f"bootstrap_{record['status']}", record)

    return record
