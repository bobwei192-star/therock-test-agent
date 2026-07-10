from __future__ import annotations

import subprocess
import sys
from pathlib import Path
from typing import Any

from .artifacts import check_sudo_policy


def check_python_modules(modules: list[str]) -> list[str]:
    missing: list[str] = []
    for module in modules:
        result = subprocess.run(
            [sys.executable, "-c", f"import importlib.util; raise SystemExit(importlib.util.find_spec({module!r}) is None)"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            text=True,
        )
        if result.returncode != 0:
            missing.append(module)
    return missing


def check_task_preflight(
    state: dict[str, Any],
    task: dict[str, Any],
    env: dict[str, str],
    metadata: dict[str, Any],
) -> str | None:
    rocm_dist = Path(state["meta"]["rocm_dist"])
    if not (rocm_dist / "bin").is_dir():
        return f"missing_artifacts: {rocm_dist / 'bin'} 不存在"
    if not (rocm_dist / "lib").is_dir() and not (rocm_dist / "lib64").is_dir():
        return f"missing_artifacts: {rocm_dist}/lib 或 lib64 不存在"

    sudo_policy = state["meta"].get("sudo_policy")
    if metadata.get("requires_sudo_policy") and sudo_policy not in {"askpass", "cache"}:
        return (
            "sudo_unavailable: sudo_sensitive task requires THEROCK_SUDO_POLICY=cache "
            "with a valid `sudo -v` cache, or THEROCK_SUDO_POLICY=askpass "
            "with a running session-scoped sudo agent"
        )
    if metadata.get("requires_sudo_policy") and sudo_policy in {"askpass", "cache"}:
        try:
            check_sudo_policy(sudo_policy, env)
        except SystemExit as exc:
            return f"sudo_unavailable: {exc}"

    missing_env = [
        name
        for name in ("THEROCK_BIN_DIR", "OUTPUT_ARTIFACTS_DIR", "ROCM_PATH", "HIP_PATH")
        if not env.get(name)
    ]
    if missing_env:
        return "missing_env: " + ", ".join(missing_env)

    if metadata.get("entrypoint_type") == "test_runner" and not env.get("TEST_COMPONENT"):
        return "entrypoint_error: TEST_COMPONENT environment variable is required"

    missing_modules = check_python_modules(list(metadata.get("preflight_python_modules") or []))
    if missing_modules:
        return "missing_dependency: " + ", ".join(missing_modules)

    return None
