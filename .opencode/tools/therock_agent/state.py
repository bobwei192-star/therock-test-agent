from __future__ import annotations

from pathlib import Path
from typing import Any

from .audit import atomic_write_json
from .audit import now_iso
from .config import read_json


def state_path(state: dict[str, Any]) -> Path:
    return Path(state["meta"]["output_dir"]) / "global_state.json"


def save_state(state: dict[str, Any]) -> None:
    state["last_checkpoint_time"] = now_iso()
    atomic_write_json(state_path(state), state)


def load_state(output_root: str, run_id: str) -> dict[str, Any]:
    path = Path(output_root).expanduser().resolve() / run_id / "global_state.json"
    if not path.is_file():
        raise SystemExit(f"找不到 global_state.json: {path}")
    return read_json(path)


def task_lookup(state: dict[str, Any]) -> dict[str, dict[str, Any]]:
    return {task["task_id"]: task for task in state["schedule"]["task_queue"]}
