from __future__ import annotations

import os
import platform
from pathlib import Path
from typing import Any


def _read_text(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _runtime_kind(kernel_text: str) -> tuple[bool, bool]:
    override = os.environ.get("THEROCK_RUNTIME_KIND", "").strip().lower()
    if override:
        return override in {"wsl", "wsl2"}, override == "wsl2"

    lowered = kernel_text.lower()
    is_wsl = "microsoft" in lowered or "wsl" in lowered
    is_wsl2 = "wsl2" in lowered or "microsoft-standard-wsl2" in lowered
    return is_wsl, is_wsl2


def _device_root() -> Path:
    return Path(os.environ.get("THEROCK_RUNTIME_DEVICE_ROOT", "/")).expanduser()


def _device_exists(device_root: Path, device: str) -> bool:
    relative = device.lstrip("/")
    return (device_root / relative).exists()


def _runtime_label(is_wsl: bool, is_wsl2: bool, devices: dict[str, dict[str, Any]]) -> str:
    if is_wsl2:
        return "wsl2-dxg" if devices["/dev/dxg"]["exists"] else "wsl2-missing-dxg"
    if is_wsl:
        return "wsl"
    if devices["/dev/kfd"]["exists"] or devices["/dev/dri"]["exists"]:
        return "linux-rocm"
    return "linux"


def detect_rocm_runtime() -> dict[str, Any]:
    """Detect host runtime details relevant to ROCm on Linux and WSL2.

    WSL2 ROCm exposes `/dev/dxg`; `/dev/kfd` and `/dev/dri` are normally absent.
    The optional THEROCK_RUNTIME_* environment variables are test hooks.
    """

    release = platform.release()
    version = platform.version()
    proc_version = _read_text(Path("/proc/version"))
    kernel_text = " ".join([release, version, proc_version])
    is_wsl, is_wsl2 = _runtime_kind(kernel_text)
    device_root = _device_root()
    devices = {
        device: {
            "exists": _device_exists(device_root, device),
            "expected_on_wsl2": device == "/dev/dxg",
        }
        for device in ("/dev/dxg", "/dev/kfd", "/dev/dri")
    }
    label = _runtime_label(is_wsl, is_wsl2, devices)

    return {
        "runtime_label": label,
        "is_wsl": is_wsl,
        "is_wsl2": is_wsl2,
        "kernel_release": release,
        "kernel_version": version,
        "device_root": str(device_root),
        "gpu_device_model": "dxg" if is_wsl2 else "kfd_dri",
        "gpu_devices": devices,
        "wsl2_note": (
            "ROCm on WSL2 uses /dev/dxg; /dev/kfd and /dev/dri are expected to be absent."
            if is_wsl2
            else ""
        ),
    }
