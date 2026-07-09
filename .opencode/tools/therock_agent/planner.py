from __future__ import annotations

from typing import Any, Callable

from .config import find_official_exclude
from .config import load_component_entries


ResolveEntrypoint = Callable[[dict[str, Any], str, str], dict[str, Any]]


def make_task(entry: dict[str, Any]) -> dict[str, Any]:
    test_type = str(entry["test_type"])
    component = str(entry["component"])
    task_id = f"{component}-{test_type}"
    return {
        "task_id": task_id,
        "component": component,
        "test_type": test_type,
        "duration_ref": entry.get("duration_ref"),
        "category": entry.get("category"),
        "source_status": entry.get("status"),
        "gpu_hang_risk": bool(entry.get("gpu_hang_risk", False)),
        "sort_order": entry.get("sort_order"),
    }


def build_task_plan(
    component_config,
    component_env_index: dict[str, Any],
    official_excludes: list[dict[str, Any]],
    components: list[str],
    test_types: list[str],
    gpu_risk_policy: str,
    amdgpu_families: str,
    resolve_entrypoint: ResolveEntrypoint,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    entries = load_component_entries(component_config)
    component_filter = set(components)
    test_type_filter = set(test_types)
    normal_tasks: list[dict[str, Any]] = []
    risk_tasks: list[dict[str, Any]] = []
    skipped_tasks: list[dict[str, Any]] = []
    seen: set[str] = set()

    for entry in entries:
        if component_filter and entry.get("component") not in component_filter:
            continue
        if test_type_filter and entry.get("test_type") not in test_type_filter:
            continue

        task = make_task(entry)
        entrypoint = resolve_entrypoint(component_env_index, task["component"], task["test_type"])
        task["entrypoint"] = entrypoint
        task["entrypoint_type"] = entrypoint.get("entrypoint_type", "test_runner")
        task["script"] = entrypoint.get("script") or "test_runner.py"
        task["test_component"] = entrypoint.get("test_component")
        task["env_profiles"] = entrypoint.get("env_profiles", [])
        task["known_issue_category"] = entrypoint.get("known_issue_category")
        task["retry_policy"] = entrypoint.get("retry_policy")
        task["timeout_hint_seconds"] = entrypoint.get("timeout_hint_seconds")
        task["gpu_hang_risk"] = bool(task.get("gpu_hang_risk") or entrypoint.get("gpu_hang_risk", False))
        if task["task_id"] in seen:
            continue
        seen.add(task["task_id"])

        official_exclude = find_official_exclude(
            official_excludes,
            task["component"],
            task["test_type"],
            amdgpu_families,
        )
        if official_exclude:
            task["skip_reason"] = f"official_exclude.json: {official_exclude.get('reason', 'official exclude')}"
            task["skip_status"] = str(official_exclude.get("status", "skip"))
            task["official_exclude"] = official_exclude
            task["known_issue_category"] = official_exclude.get(
                "known_issue_category",
                task.get("known_issue_category"),
            )
            skipped_tasks.append(task)
            continue

        if task["source_status"] == "exclude":
            task["skip_reason"] = "component_sort_order.json status=exclude"
            skipped_tasks.append(task)
            continue

        default_status = entrypoint.get("default_status")
        if entrypoint.get("entrypoint_type") == "none" or default_status in {"skip", "blocked"}:
            task["skip_reason"] = (
                f"component_env_script_index.json entrypoint_type={entrypoint.get('entrypoint_type')} "
                f"default_status={default_status or 'skip'}"
            )
            task["skip_status"] = default_status or "skip"
            skipped_tasks.append(task)
            continue

        if task["gpu_hang_risk"] and gpu_risk_policy == "skip":
            task["skip_reason"] = "gpu_hang_risk=true and policy=skip"
            skipped_tasks.append(task)
            continue

        if task["gpu_hang_risk"] and gpu_risk_policy == "quarantine":
            risk_tasks.append(task)
        else:
            normal_tasks.append(task)

    return normal_tasks + risk_tasks, skipped_tasks
