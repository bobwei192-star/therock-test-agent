from __future__ import annotations

import os
import platform
import shutil
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


def _path_entries(value: str) -> list[Path]:
    return [Path(item).expanduser() for item in value.split(os.pathsep) if item]


def _existing_dirs(paths: list[Path]) -> list[Path]:
    seen: set[str] = set()
    existing: list[Path] = []
    for path in paths:
        try:
            resolved = path.resolve()
        except OSError:
            resolved = path
        key = str(resolved)
        if key in seen or not resolved.is_dir():
            continue
        seen.add(key)
        existing.append(resolved)
    return existing


def _library_search_dirs(rocm_dist: Path | None) -> list[Path]:
    explicit = _path_entries(os.environ.get("THEROCK_ROCDXG_SEARCH_PATHS", ""))
    paths: list[Path] = list(explicit)

    if os.environ.get("THEROCK_ROCDXG_SEARCH_PATHS_ONLY") != "1":
        if rocm_dist:
            paths.extend([rocm_dist / "lib", rocm_dist / "lib64"])
        paths.extend(_path_entries(os.environ.get("LD_LIBRARY_PATH", "")))
        paths.extend([Path("/opt/rocm/lib"), Path("/opt/rocm/lib64")])
        paths.extend(Path("/opt").glob("rocm-*/lib"))
        paths.extend(Path("/opt").glob("rocm-*/lib64"))

    return _existing_dirs(paths)


def _find_libraries(search_dirs: list[Path], pattern: str) -> list[str]:
    matches: list[str] = []
    for directory in search_dirs:
        matches.extend(str(path) for path in sorted(directory.glob(pattern)) if path.is_file())
    return matches[:20]


def _find_tool(command: str, rocm_dist: Path | None) -> str:
    candidates: list[Path] = []
    if rocm_dist:
        candidates.append(rocm_dist / "bin" / command)
    candidates.append(Path("/opt/rocm/bin") / command)
    candidates.extend(Path("/opt").glob(f"rocm-*/bin/{command}"))

    for candidate in candidates:
        if candidate.is_file() and os.access(candidate, os.X_OK):
            return str(candidate)
    return shutil.which(command) or ""


def _rocm_library_integrity(is_wsl2: bool, rocm_dist: Path | None) -> dict[str, Any]:
    search_dirs = _library_search_dirs(rocm_dist)
    rocdxg_libraries = _find_libraries(search_dirs, "librocdxg*.so*")
    rocminfo = _find_tool("rocminfo", rocm_dist)
    agent_enumerator = _find_tool("rocm_agent_enumerator", rocm_dist)

    missing: list[str] = []
    if is_wsl2 and not rocdxg_libraries:
        missing.append("librocdxg.so")
    if not rocminfo:
        missing.append("rocminfo")
    if not agent_enumerator:
        missing.append("rocm_agent_enumerator")

    status = "complete" if not missing else "incomplete"
    if not is_wsl2:
        status = "not_applicable" if not missing else "diagnostic_incomplete"

    return {
        "status": status,
        "required_for_wsl2": ["librocdxg.so"],
        "missing": missing,
        "search_dirs": [str(path) for path in search_dirs],
        "librocdxg": {
            "found": bool(rocdxg_libraries),
            "paths": rocdxg_libraries,
        },
        "tools": {
            "rocminfo": rocminfo,
            "rocm_agent_enumerator": agent_enumerator,
        },
        "environment": {
            "LD_LIBRARY_PATH": os.environ.get("LD_LIBRARY_PATH", ""),
            "HSA_ENABLE_DXG_DETECTION": os.environ.get("HSA_ENABLE_DXG_DETECTION", ""),
            "THEROCK_ROCDXG_SEARCH_PATHS": os.environ.get("THEROCK_ROCDXG_SEARCH_PATHS", ""),
        },
        "wsl2_fix_hint": (
            "Install ROCm on WSL and the librocdxg package, or add the directory "
            "containing librocdxg.so to LD_LIBRARY_PATH/THEROCK_ROCDXG_SEARCH_PATHS."
            if is_wsl2 and not rocdxg_libraries
            else ""
        ),
    }


def _runtime_label(is_wsl: bool, is_wsl2: bool, devices: dict[str, dict[str, Any]]) -> str:
    if is_wsl2:
        return "wsl2-dxg" if devices["/dev/dxg"]["exists"] else "wsl2-missing-dxg"
    if is_wsl:
        return "wsl"
    if devices["/dev/kfd"]["exists"] or devices["/dev/dri"]["exists"]:
        return "linux-rocm"
    return "linux"


def detect_rocm_runtime(rocm_dist: Path | None = None) -> dict[str, Any]:
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
    library_integrity = _rocm_library_integrity(is_wsl2, rocm_dist)

    return {
        "runtime_label": label,
        "is_wsl": is_wsl,
        "is_wsl2": is_wsl2,
        "kernel_release": release,
        "kernel_version": version,
        "device_root": str(device_root),
        "gpu_device_model": "dxg" if is_wsl2 else "kfd_dri",
        "gpu_devices": devices,
        "rocm_library_integrity": library_integrity,
        "wsl2_note": (
            "ROCm on WSL2 uses /dev/dxg; /dev/kfd and /dev/dri are expected to be absent."
            if is_wsl2
            else ""
        ),
    }
