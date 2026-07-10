from __future__ import annotations

import datetime as dt
import json
import os
from pathlib import Path
from typing import Any

from .config import SENSITIVE_ENV_NAMES


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    ensure_dir(path.parent)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with tmp.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
        handle.flush()
        os.fsync(handle.fileno())
    tmp.replace(path)
    try:
        dir_fd = os.open(path.parent, os.O_DIRECTORY)
    except OSError:
        return
    try:
        os.fsync(dir_fd)
    finally:
        os.close(dir_fd)


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    ensure_dir(path.parent)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def safe_argv(argv: list[str]) -> list[str]:
    safe: list[str] = []
    mask_next = False
    for item in argv:
        if mask_next:
            safe.append("***")
            mask_next = False
            continue
        if "password" in item.lower():
            safe.append("***")
            if item.startswith("--"):
                mask_next = True
            continue
        safe.append(item)
    return safe


def safe_env_value(key: str, value: str) -> str:
    if key in SENSITIVE_ENV_NAMES or ("PASSWORD" in key.upper()) or ("TOKEN" in key.upper()):
        return "***"
    return value


def env_summary() -> dict[str, str]:
    keys = [
        "THEROCK_SUDO_POLICY",
        "THEROCK_AMDGPU_FAMILIES",
        "THEROCK_AMDGPU_TARGETS",
        "THEROCK_REPO",
        "ROCM_PATH",
        "AMDGPU_FAMILIES",
        "TEST_TYPE",
    ]
    return {key: os.environ.get(key, "") for key in keys if os.environ.get(key)}


def global_audit_path(project_root: Path, argv: list[str]) -> Path:
    if "--output-root" in argv:
        index = argv.index("--output-root")
        if index + 1 < len(argv):
            return Path(argv[index + 1]).expanduser().resolve() / "_audit" / "agent_invocations.jsonl"
    return project_root / "runs" / "_audit" / "agent_invocations.jsonl"


def write_global_audit(
    project_root: Path,
    argv: list[str],
    event: str,
    status: str,
    *,
    command: str | None = None,
    run_id: str | None = None,
    output_dir: str | None = None,
    error: str | None = None,
) -> None:
    append_jsonl(
        global_audit_path(project_root, argv),
        {
            "time": now_iso(),
            "event": event,
            "status": status,
            "cwd": str(Path.cwd()),
            "project_root": str(project_root),
            "command": command,
            "argv": safe_argv(argv),
            "run_id": run_id,
            "output_dir": output_dir,
            "error": error,
            "env_summary": env_summary(),
        },
    )


def append_activity(state: dict[str, Any], event: str, details: dict[str, Any] | None = None) -> None:
    append_jsonl(
        Path(state["meta"]["output_dir"]) / "agent_activity.jsonl",
        {
            "time": now_iso(),
            "event": event,
            "run_id": state["run_id"],
            "details": details or {},
        },
    )


def append_wrapper_audit(state: dict[str, Any], record: dict[str, Any]) -> None:
    append_jsonl(Path(state["meta"]["output_dir"]) / "wrapper_changes.jsonl", record)
