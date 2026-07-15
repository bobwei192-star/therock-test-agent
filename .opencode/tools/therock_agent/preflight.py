from __future__ import annotations

import os
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


def check_runtime_gpu_access(state: dict[str, Any]) -> str | None:
    if state["meta"].get("mock_command"):
        return None
    if os.environ.get("THEROCK_ALLOW_MISSING_WSL_DXG") == "1":
        return None

    runtime = state.get("runtime_summary") or {}
    rocm_runtime = runtime.get("rocm_runtime") or {}
    if not rocm_runtime.get("is_wsl2"):
        return None

    dxg = rocm_runtime.get("gpu_devices", {}).get("/dev/dxg", {})
    if dxg.get("exists"):
        if os.environ.get("THEROCK_ALLOW_MISSING_ROCDXG") == "1":
            return None
        integrity = rocm_runtime.get("rocm_library_integrity") or {}
        rocdxg = integrity.get("librocdxg") or {}
        if rocdxg.get("found"):
            return None
        return (
            "missing_wsl_rocdxg: runtime=wsl2-dxg; /dev/dxg exists but librocdxg.so "
            "was not found in ROCm artifact libs, LD_LIBRARY_PATH, or /opt/rocm. "
            "Install ROCm on WSL/librocdxg, or add its library directory to "
            "THEROCK_ROCDXG_SEARCH_PATHS or LD_LIBRARY_PATH."
        )

    runtime_label = rocm_runtime.get("runtime_label", "wsl2-missing-dxg")
    return (
        f"missing_wsl_dxg: runtime={runtime_label}; WSL2 ROCm requires /dev/dxg. "
        "/dev/kfd and /dev/dri are normally absent under WSL2."
    )


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

    runtime_error = check_runtime_gpu_access(state)
    if runtime_error:
        return runtime_error

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
