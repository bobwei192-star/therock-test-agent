from __future__ import annotations

from pathlib import Path
from typing import Any


def therock_repo_from_state(state: dict[str, Any]) -> Path | None:
    raw = str(state.get("meta", {}).get("therock_repo_path") or "")
    if not raw:
        return None
    return Path(raw)


def venv_dir(therock_repo: Path) -> Path:
    return therock_repo / ".venv"


def venv_bin_dir(therock_repo: Path) -> Path:
    return venv_dir(therock_repo) / "bin"


def venv_python(therock_repo: Path) -> Path:
    return venv_bin_dir(therock_repo) / "python"


def resolve_test_python_executable(state: dict[str, Any], therock_repo: Path | None = None) -> str:
    """Prefer TheRock checkout .venv/bin/python for test scripts and preflight."""
    repo = therock_repo or therock_repo_from_state(state)
    if repo is not None:
        candidate = venv_python(repo)
        if candidate.is_file():
            return str(candidate)

    bootstrap_python = (state.get("bootstrap") or {}).get("venv", {}).get("python")
    if bootstrap_python and Path(str(bootstrap_python)).is_file():
        return str(bootstrap_python)

    return "python3"
