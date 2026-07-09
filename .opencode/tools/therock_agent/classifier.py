from __future__ import annotations

from pathlib import Path
from typing import Any


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
            text += path.read_text(encoding="utf-8", errors="replace")[-4000:]

    patterns = [
        "ring gfx",
        "GPU reset",
        "MES failed",
        "PERMISSION_FAULT",
        "HSA_STATUS_ERROR",
        "SIGKILL",
        "Subprocess aborted",
        "FAILED",
        "ERROR",
        "Traceback",
    ]
    for line in text.splitlines():
        if any(pattern in line for pattern in patterns):
            return line.strip()[:500]
    return text.strip().splitlines()[-1][:500] if text.strip() else "任务返回非 0，但未捕获关键日志"
