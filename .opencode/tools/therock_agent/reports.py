from __future__ import annotations

import json
from pathlib import Path
from typing import Any

from .audit import append_activity
from .audit import atomic_write_json
from .audit import now_iso


def load_runtime_summary(output_dir: Path) -> dict[str, Any]:
    path = output_dir / "environment_summary.json"
    if not path.is_file():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {}
    return data.get("runtime_summary") or {}


def runtime_label_from_summary(runtime_summary: dict[str, Any]) -> str:
    if runtime_summary.get("runtime_label"):
        return str(runtime_summary["runtime_label"])
    rocm_runtime = runtime_summary.get("rocm_runtime") or {}
    return str(rocm_runtime.get("runtime_label") or "unknown")


def summarize_counts(state: dict[str, Any]) -> dict[str, int]:
    counts = {"pass": 0, "fail": 0, "skip": 0, "blocked": 0, "timeout": 0, "flaky": 0, "interrupted": 0}
    for result in state["results"]["task_results"].values():
        status = result.get("status", "blocked")
        counts[status] = counts.get(status, 0) + 1
    return counts


def report_paths(output_dir: Path) -> dict[str, str]:
    return {
        "global_state": str(output_dir / "global_state.json"),
        "summary_json": str(output_dir / "summary.json"),
        "failures_json": str(output_dir / "failures.json"),
        "agent_activity": str(output_dir / "agent_activity.jsonl"),
        "tool_calls": str(output_dir / "tool_calls.jsonl"),
        "wrapper_changes": str(output_dir / "wrapper_changes.jsonl"),
        "environment_summary": str(output_dir / "environment_summary.json"),
        "logs": str(output_dir / "logs"),
        "wrappers": str(output_dir / "wrappers"),
        "failures_dir": str(output_dir / "failures"),
        "round_analysis": str(output_dir / "round_analysis"),
        "debug": str(output_dir / "debug"),
    }


def compact_task_result(result: dict[str, Any]) -> dict[str, Any]:
    return {
        "task_id": result.get("task_id", ""),
        "component": result.get("component", ""),
        "test_type": result.get("test_type", ""),
        "status": result.get("status", ""),
        "return_code": result.get("return_code"),
        "duration_seconds": result.get("duration_seconds"),
        "stdout_log": result.get("stdout_log", ""),
        "stderr_log": result.get("stderr_log", ""),
        "failure_summary": result.get("failure_summary", ""),
        "gpu_hang_risk": result.get("gpu_hang_risk", False),
        "entrypoint_type": result.get("entrypoint_type", ""),
        "script": result.get("script", ""),
        "test_component": result.get("test_component", ""),
        "env_profiles": result.get("env_profiles", []),
        "known_issue_category": result.get("known_issue_category"),
        "official_exclude": result.get("official_exclude"),
        "wrapper_path": result.get("wrapper_path", ""),
        "wrapper_env_change_keys": result.get("wrapper_env_change_keys", []),
        "path_hardcode_detection": result.get("path_hardcode_detection", {}),
        "failure_evidence": result.get("failure_evidence", {}),
        "runtime_label": result.get("runtime_label", ""),
        "finished_at": result.get("finished_at", ""),
    }


def failure_records(state: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        compact_task_result(result)
        for result in sorted(state["results"]["task_results"].values(), key=lambda item: item["task_id"])
        if result.get("status") in {"fail", "blocked", "timeout", "interrupted"}
    ]


def generate_reports(state: dict[str, Any], project_root: Path, summary_template: Path) -> None:
    output_dir = Path(state["meta"]["output_dir"])
    counts = summarize_counts(state)
    runtime_summary = state.get("runtime_summary") or load_runtime_summary(output_dir)
    runtime_label = runtime_label_from_summary(runtime_summary)
    history = state["loop"]["failed_task_history"]
    total_tasks = len(state["schedule"]["task_queue"]) + len(state["schedule"]["skipped_tasks"])
    final_failures = failure_records(state)
    skipped_risk = [
        result["task_id"]
        for result in state["results"]["task_results"].values()
        if result.get("status") == "skip" and result.get("gpu_hang_risk")
    ]
    path_hardcode_results = [result for result in final_failures if result.get("path_hardcode_detection", {}).get("detected")]
    summary = {
        "schema_version": "0.2",
        "generated_at": now_iso(),
        "run_id": state["run_id"],
        "status": state["final_status"],
        "start_time": state.get("start_time"),
        "end_time": state.get("end_time"),
        "meta": state["meta"],
        "runtime_label": runtime_label,
        "runtime_summary": runtime_summary,
        "counts": counts,
        "total_tasks": total_tasks,
        "loop": {
            "rounds": len(history),
            "failed_task_history": history,
            "stable_failed_count": state["loop"].get("stable_failed_count", 0),
            "last_failed_set": state["loop"].get("last_failed_set"),
        },
        "tasks": [compact_task_result(result) for result in sorted(state["results"]["task_results"].values(), key=lambda item: item["task_id"])],
        "final_failure_task_ids": [result["task_id"] for result in final_failures],
        "gpu_risk_skipped_task_ids": skipped_risk,
        "path_hardcode_task_ids": [result["task_id"] for result in path_hardcode_results],
        "artifacts": report_paths(output_dir),
        "templates": {
            "summary_template": str(summary_template),
        },
        "global_audit": str(project_root / "runs" / "_audit" / "agent_invocations.jsonl"),
        "reporter_note": "Markdown summaries are generated by the OpenCode therock-reporter agent from this JSON.",
    }
    failures = {
        "schema_version": "0.2",
        "generated_at": summary["generated_at"],
        "run_id": state["run_id"],
        "runtime_label": runtime_label,
        "runtime_summary": runtime_summary,
        "failures": final_failures,
        "reporter_note": "Per-failure Markdown is generated by the OpenCode therock-reporter agent from this JSON.",
    }

    atomic_write_json(output_dir / "summary.json", summary)
    atomic_write_json(output_dir / "failures.json", failures)
    append_activity(
        state,
        "report_generated",
        {
            "summary_json": str(output_dir / "summary.json"),
            "failures_json": str(output_dir / "failures.json"),
            "failure_count": len(final_failures),
            "runtime_label": runtime_label,
            "markdown_policy": "opencode_therock_reporter",
        },
    )


def write_failure_report(state: dict[str, Any], result: dict[str, Any], failure_template: Path) -> None:
    output_dir = Path(state["meta"]["output_dir"])
    runtime_summary = state.get("runtime_summary") or load_runtime_summary(output_dir)
    failure_record = {
        "schema_version": "0.2",
        "generated_at": now_iso(),
        "run_id": state["run_id"],
        "task": compact_task_result(result),
        "runtime_label": runtime_label_from_summary(runtime_summary),
        "runtime_summary": runtime_summary,
        "failure_template": str(failure_template),
        "markdown_policy": "opencode_therock_reporter",
    }
    atomic_write_json(output_dir / "failures" / f"{result['task_id']}_failure.json", failure_record)
