from __future__ import annotations

import re
from pathlib import Path
from typing import Any


EVIDENCE_NEEDLES = [
    "ModuleNotFoundError",
    "ImportError",
    "missing_dependency:",
    "Connection timed out",
    "Temporary failure in name resolution",
    "Could not resolve host",
    "Connection reset by peer",
    "CMake Error",
    "Could NOT find",
    "find_package",
    "CMAKE_PREFIX_PATH",
    "ninja: error",
    "cannot open shared object file",
    "LD_LIBRARY_PATH",
    "ROCM_PATH",
    "HIP_PATH",
    "sudo_unavailable",
    "Permission denied",
    "No space left on device",
    "Disk quota exceeded",
    "TimeoutExpired",
    "timed out",
    "GPU reset",
    "ring timeout",
    "HSA_STATUS_ERROR",
    "AssertionError",
    "Traceback",
    "ERROR",
    "FAILED",
    "CalledProcessError",
]


def evidence_signals(text: str) -> list[dict[str, str]]:
    signals: list[dict[str, str]] = []
    for line in text.splitlines():
        for needle in EVIDENCE_NEEDLES:
            if needle in line:
                signals.append({"needle": needle, "line": line.strip()[:500]})
                break
        if len(signals) >= 40:
            break
    return signals


def detect_path_hardcode(stdout_path: Path, stderr_path: Path) -> dict[str, Any]:
    patterns = {
        "path_hardcode": ["/therock/src/", "/therock/build/", "CTestTestfile.cmake"],
        "invalid_embedded_python_path": ["/opt/python/cp312-cp312/bin/python3.12", "/opt/python/"],
        "missing_runtime_library": ["libhipdnn_backend.so", "cannot open shared object file", "No such file or directory"],
    }
    text = ""
    for path in (stderr_path, stdout_path):
        if path.is_file():
            text += path.read_text(encoding="utf-8", errors="replace")[-12000:]

    matches: list[dict[str, str]] = []
    for line in text.splitlines():
        for category, needles in patterns.items():
            if any(needle in line for needle in needles):
                matches.append({"category": category, "line": line.strip()[:500]})
                break
        if len(matches) >= 20:
            break

    return {
        "detected": bool(matches),
        "categories": sorted({match["category"] for match in matches}),
        "matches": matches,
    }


def detect_failure_summary(stdout_path: Path, stderr_path: Path) -> str:
    text = ""
    for path in (stderr_path, stdout_path):
        if path.is_file():
            text += path.read_text(encoding="utf-8", errors="replace")[-12000:]

    missing_module = re.search(r"ModuleNotFoundError: No module named ['\"]([^'\"]+)['\"]", text)
    if missing_module:
        return f"evidence: missing python module {missing_module.group(1)}"

    import_error = re.search(r"ImportError: .*", text)
    if import_error:
        return import_error.group(0).strip()[:500]

    missing_dependency = re.search(r"missing_dependency:\s*([A-Za-z0-9_.-]+)", text)
    if missing_dependency:
        return f"evidence: missing dependency {missing_dependency.group(1)}"

    signals = evidence_signals(text)
    if signals:
        return "evidence: " + signals[0]["line"]
    return text.strip().splitlines()[-1][:500] if text.strip() else "任务返回非 0，但未捕获关键日志"


def extract_failure_evidence(stdout_path: Path, stderr_path: Path) -> dict[str, Any]:
    """Extract concise, report-ready failure evidence from task logs."""
    combined = ""
    sources: list[tuple[str, Path]] = [("stderr", stderr_path), ("stdout", stdout_path)]
    for _name, path in sources:
        if path.is_file():
            combined += path.read_text(encoding="utf-8", errors="replace")[-24000:] + "\n"

    missing_modules = sorted(set(re.findall(r"ModuleNotFoundError: No module named ['\"]([^'\"]+)['\"]", combined)))
    missing_deps = sorted(set(re.findall(r"missing_dependency:\s*([A-Za-z0-9_.-]+)", combined)))
    signals = evidence_signals(combined)
    if missing_modules:
        summary = "evidence: missing python module " + ", ".join(missing_modules)
    elif missing_deps:
        summary = "evidence: missing dependency " + ", ".join(missing_deps)
    elif signals:
        summary = "evidence: " + signals[0]["line"]
    else:
        summary = "evidence: no known signal extracted"

    excerpts: dict[str, list[str]] = {}
    for name, path in sources:
        if not path.is_file():
            continue
        lines = path.read_text(encoding="utf-8", errors="replace").splitlines()
        selected: list[str] = []
        for index, line in enumerate(lines):
            if any(needle in line for needle in EVIDENCE_NEEDLES):
                start = max(0, index - 2)
                end = min(len(lines), index + 4)
                selected.extend(lines[start:end])
                selected.append("...")
        if not selected and lines:
            selected = lines[-40:]
        excerpts[name] = selected[:120]

    return {
        "kind": "runner_evidence",
        "summary": summary,
        "missing_python_modules": missing_modules,
        "missing_dependencies": missing_deps,
        "signals": signals,
        "excerpts": excerpts,
        "classification_policy": "opencode_therock_debugger",
    }
