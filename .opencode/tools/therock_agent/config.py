from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any


SENSITIVE_ENV_NAMES = {"SUDO_PASSWORD", "THEROCK_SUDO_PASSWORD"}


def load_project_env(project_root: Path) -> None:
    """Load safe THEROCK_* settings from .env without accepting passwords."""
    env_path = project_root / ".env"
    if not env_path.is_file():
        return

    for raw_line in env_path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")

        if key in SENSITIVE_ENV_NAMES or ("SUDO" in key and "PASSWORD" in key):
            raise SystemExit(
                f"拒绝从 .env 读取敏感字段 {key}。请不要把 sudo 密码写入项目文件，"
                "需要 sudo 时先在终端手动执行 `sudo -v`。"
            )
        if key.startswith("THEROCK_") and key not in os.environ:
            os.environ[key] = value


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_optional_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def normalize_list(value: str | None) -> list[str]:
    if not value:
        return []
    items = [item.strip() for item in value.split(",") if item.strip()]
    if any(item.lower() in {"all", "*"} for item in items):
        return []
    return items


def load_component_entries(config_path: Path) -> list[dict[str, Any]]:
    data = read_json(config_path)
    entries = data.get("entries")
    if not isinstance(entries, list):
        raise SystemExit(f"组件排序文件缺少 entries: {config_path}")
    return sorted(entries, key=lambda item: int(item.get("sort_order", 0)))


def load_component_env_index(index_path: Path) -> dict[str, Any]:
    data = read_json(index_path)
    if not isinstance(data.get("env_profiles"), dict):
        raise SystemExit(f"组件运行索引缺少 env_profiles: {index_path}")
    if not isinstance(data.get("components"), dict):
        raise SystemExit(f"组件运行索引缺少 components: {index_path}")
    if not isinstance(data.get("defaults"), dict):
        raise SystemExit(f"组件运行索引缺少 defaults: {index_path}")
    return data


def load_official_exclude(exclude_path: Path) -> list[dict[str, Any]]:
    if not exclude_path.is_file() or not exclude_path.read_text(encoding="utf-8").strip():
        return []
    data = read_json(exclude_path)
    entries = data.get("entries", [])
    if not isinstance(entries, list):
        raise SystemExit(f"官方排除文件 entries 必须是列表: {exclude_path}")
    return [entry for entry in entries if isinstance(entry, dict)]


def list_matches(value: str, patterns: list[Any]) -> bool:
    if not patterns:
        return True
    return "*" in patterns or value in {str(pattern) for pattern in patterns}


def find_official_exclude(
    entries: list[dict[str, Any]],
    component: str,
    test_type: str,
    amdgpu_families: str,
) -> dict[str, Any] | None:
    for entry in entries:
        if str(entry.get("component", "")) != component:
            continue
        if not list_matches(test_type, entry.get("test_types", [])):
            continue
        if not list_matches(amdgpu_families, entry.get("amdgpu_families", [])):
            continue
        return entry
    return None


def deep_merge(base: dict[str, Any], override: dict[str, Any]) -> dict[str, Any]:
    merged = dict(base)
    for key, value in override.items():
        if isinstance(value, dict) and isinstance(merged.get(key), dict):
            merged[key] = deep_merge(merged[key], value)
        else:
            merged[key] = value
    return merged
