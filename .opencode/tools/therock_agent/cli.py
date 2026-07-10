from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import signal
import subprocess
import sys
import time
import uuid
from pathlib import Path
from typing import Any

from .artifacts import discover_therock_repo as _discover_therock_repo
from .artifacts import resolve_artifacts_path
from .audit import append_activity
from .audit import append_jsonl
from .audit import atomic_write_json
from .audit import ensure_dir
from .audit import env_summary
from .audit import now_iso
from .audit import safe_argv
from .audit import write_global_audit as _write_global_audit
from .config import load_component_env_index
from .config import load_official_exclude
from .config import load_project_env as _load_project_env
from .config import normalize_list
from .entrypoint import resolve_entrypoint
from .executor import run_task as _run_task
from .planner import build_task_plan
from .reports import generate_reports as _generate_reports
from .reports import write_failure_report as _write_failure_report
from .state import load_state
from .state import save_state
from .state import task_lookup


PROJECT_ROOT: Path
DEFAULT_COMPONENT_CONFIG: Path
DEFAULT_COMPONENT_ENV_INDEX: Path
DEFAULT_OFFICIAL_EXCLUDE: Path
DEFAULT_FAILURE_TEMPLATE: Path
DEFAULT_SUMMARY_TEMPLATE: Path


def configure(project_root: Path) -> None:
    global PROJECT_ROOT
    global DEFAULT_COMPONENT_CONFIG
    global DEFAULT_COMPONENT_ENV_INDEX
    global DEFAULT_OFFICIAL_EXCLUDE
    global DEFAULT_FAILURE_TEMPLATE
    global DEFAULT_SUMMARY_TEMPLATE

    PROJECT_ROOT = project_root
    DEFAULT_COMPONENT_CONFIG = PROJECT_ROOT / "docs_this_project" / "component_sort_order.json"
    DEFAULT_COMPONENT_ENV_INDEX = PROJECT_ROOT / "docs_this_project" / "component_env_script_index.json"
    DEFAULT_OFFICIAL_EXCLUDE = PROJECT_ROOT / "docs_this_project" / "official_exclude.json"
    DEFAULT_FAILURE_TEMPLATE = PROJECT_ROOT / "docs_this_project" / "问题模板.md"
    DEFAULT_SUMMARY_TEMPLATE = PROJECT_ROOT / "docs_this_project" / "汇总测试报告.md"


def load_project_env() -> None:
    _load_project_env(PROJECT_ROOT)


def write_global_audit(
    argv: list[str],
    event: str,
    status: str,
    *,
    command: str | None = None,
    run_id: str | None = None,
    output_dir: str | None = None,
    error: str | None = None,
) -> None:
    _write_global_audit(
        PROJECT_ROOT,
        argv,
        event,
        status,
        command=command,
        run_id=run_id,
        output_dir=output_dir,
        error=error,
    )


def discover_therock_repo(raw_path: str = "") -> Path | None:
    return _discover_therock_repo(PROJECT_ROOT, raw_path)


def create_state(args: argparse.Namespace) -> dict[str, Any]:
    build_root, rocm_dist = resolve_artifacts_path(args.artifacts)
    amdgpu_families = args.amdgpu_families or args.amdgpu_targets or args.gpu
    if not amdgpu_families:
        raise SystemExit("缺少 AMD GPU 架构参数，请传入 --amdgpu-families gfx1151 或 --gpu gfx1151。")
    component_config = Path(args.component_config).expanduser().resolve()
    components = normalize_list(args.components)
    test_types = normalize_list(args.test_types) or ["quick", "standard", "comprehensive", "full"]
    run_id = args.run_id or dt.datetime.now().strftime("%Y%m%d_%H%M%S") + "_" + uuid.uuid4().hex[:8]
    output_root = Path(args.output_root).expanduser().resolve()
    output_dir = output_root / run_id
    therock_repo = discover_therock_repo(args.therock_repo)

    component_env_index_path = Path(args.component_env_index).expanduser().resolve()
    component_env_index = load_component_env_index(component_env_index_path)
    official_exclude_path = Path(args.official_exclude).expanduser().resolve()
    official_excludes = load_official_exclude(official_exclude_path)
    tasks, skipped = build_task_plan(
        component_config,
        component_env_index,
        official_excludes,
        components,
        test_types,
        args.gpu_risk,
        amdgpu_families,
        resolve_entrypoint,
    )
    ensure_dir(output_dir / "logs")
    ensure_dir(output_dir / "failures")
    ensure_dir(output_dir / "memory")
    ensure_dir(output_dir / "wrappers")

    state: dict[str, Any] = {
        "schema_version": "0.1",
        "run_id": run_id,
        "start_time": now_iso(),
        "end_time": None,
        "final_status": "running",
        "meta": {
            "therock_repo_path": str(therock_repo) if therock_repo else "",
            "artifacts_path": str(Path(args.artifacts).expanduser().resolve()),
            "build_root": str(build_root),
            "rocm_dist": str(rocm_dist),
            "gpu_model": amdgpu_families,
            "amdgpu_families": amdgpu_families,
            "amdgpu_targets": args.amdgpu_targets or amdgpu_families,
            "output_dir": str(output_dir),
            "component_config": str(component_config),
            "component_env_index": str(component_env_index_path),
            "official_exclude": str(official_exclude_path),
            "components_filter": components,
            "test_types": test_types,
            "gpu_reset_risk_policy": args.gpu_risk,
            "sudo_policy": args.sudo_policy,
            "sudo_askpass": args.sudo_askpass,
            "sudo_agent_socket": args.sudo_agent_socket,
            "stable_threshold": args.stable_threshold,
            "max_rounds": args.max_rounds,
            "mock_command": args.mock_command or "",
        },
        "schedule": {
            "task_queue": tasks,
            "skipped_tasks": skipped,
            "current_loop": 0,
            "current_task": None,
            "next_tasks": [task["task_id"] for task in tasks],
            "round_pending_tasks": [],
            "round_failed_tasks": [],
            "completed_tasks": [],
            "failed_tasks": [],
            "blocked_tasks": [],
            "interrupted_task": None,
        },
        "results": {
            "task_results": {
                task["task_id"]: {
                    "task_id": task["task_id"],
                    "component": task["component"],
                    "test_type": task["test_type"],
                    "status": task.get("skip_status", "skip"),
                    "skip_reason": task.get("skip_reason", "skipped"),
                    "gpu_hang_risk": task.get("gpu_hang_risk", False),
                    "entrypoint_type": task.get("entrypoint_type"),
                    "script": task.get("script"),
                    "test_component": task.get("test_component"),
                    "env_profiles": task.get("env_profiles", []),
                    "known_issue_category": task.get("known_issue_category"),
                    "retry_policy": task.get("retry_policy"),
                    "timeout_hint_seconds": task.get("timeout_hint_seconds"),
                    "official_exclude": task.get("official_exclude"),
                }
                for task in skipped
            }
        },
        "loop": {
            "failed_task_history": [],
            "stable_failed_count": 0,
            "last_failed_set": None,
        },
        "resume_count": 0,
        "last_checkpoint_time": now_iso(),
    }
    state["_component_env_index"] = component_env_index
    save_state(state)
    state.pop("_component_env_index", None)
    atomic_write_json(
        output_dir / "environment_summary.json",
        {
            "time": now_iso(),
            "project_root": str(PROJECT_ROOT),
            "cwd": str(Path.cwd()),
            "env_summary": env_summary(),
            "meta": state["meta"],
        },
    )
    append_activity(
        state,
        "state_created",
        {
            "task_count": len(tasks),
            "skipped_count": len(skipped),
            "next_tasks": state["schedule"]["next_tasks"],
            "skipped_tasks": [task["task_id"] for task in skipped],
        },
    )
    return state


def run_task(state: dict[str, Any], task: dict[str, Any], round_no: int) -> dict[str, Any]:
    return _run_task(PROJECT_ROOT, state, task, round_no)


def generate_reports(state: dict[str, Any]) -> None:
    _generate_reports(state, PROJECT_ROOT, DEFAULT_SUMMARY_TEMPLATE)


def write_failure_report(state: dict[str, Any], result: dict[str, Any]) -> None:
    _write_failure_report(state, result, DEFAULT_FAILURE_TEMPLATE)


def progress_path(state: dict[str, Any]) -> Path:
    return Path(state["meta"]["output_dir"]) / "progress.jsonl"


def append_progress(state: dict[str, Any], event: str, details: dict[str, Any] | None = None) -> None:
    append_jsonl(
        progress_path(state),
        {
            "time": now_iso(),
            "event": event,
            "run_id": state["run_id"],
            **(details or {}),
        },
    )


def pid_metadata_path(state: dict[str, Any]) -> Path:
    return Path(state["meta"]["output_dir"]) / "runner.pid.json"


def output_root_from_state(state: dict[str, Any]) -> Path:
    return Path(state["meta"]["output_dir"]).parent


def read_pid_metadata(state: dict[str, Any]) -> dict[str, Any]:
    path = pid_metadata_path(state)
    if not path.is_file():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def process_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        return True
    return True


def process_cmdline(pid: int) -> str:
    path = Path("/proc") / str(pid) / "cmdline"
    try:
        return path.read_bytes().replace(b"\x00", b" ").decode("utf-8", errors="replace")
    except OSError:
        return ""


def runner_alive(state: dict[str, Any]) -> bool:
    metadata = read_pid_metadata(state)
    pid = int(metadata.get("pid") or 0)
    if pid <= 0 or not process_alive(pid):
        return False
    cmdline = process_cmdline(pid)
    if cmdline and state["run_id"] not in cmdline:
        return False
    return True


def task_status_counts(state: dict[str, Any]) -> dict[str, int]:
    counts = {"pass": 0, "fail": 0, "skip": 0, "blocked": 0, "timeout": 0, "flaky": 0, "interrupted": 0}
    for result in state["results"]["task_results"].values():
        status = result.get("status", "blocked")
        counts[status] = counts.get(status, 0) + 1
    return counts


def runnable_total(state: dict[str, Any]) -> int:
    return len(state["schedule"].get("task_queue") or [])


def completed_runnable_count(state: dict[str, Any]) -> int:
    runnable = {task["task_id"] for task in state["schedule"].get("task_queue") or []}
    return sum(
        1
        for task_id, result in state["results"]["task_results"].items()
        if task_id in runnable and result.get("status") in {"pass", "fail", "blocked", "timeout", "flaky", "interrupted"}
    )


def latest_progress_events(state: dict[str, Any], limit: int = 5) -> list[dict[str, Any]]:
    path = progress_path(state)
    if not path.is_file():
        return []
    events: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            events.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return events[-limit:]


def effective_status(state: dict[str, Any]) -> str:
    status = str(state.get("final_status") or "running")
    if status == "running" and not runner_alive(state):
        return "stale"
    return status


def write_run_index(state: dict[str, Any], event: str) -> None:
    append_jsonl(
        output_root_from_state(state) / "_index.jsonl",
        {
            "time": now_iso(),
            "event": event,
            "run_id": state["run_id"],
            "output_dir": state["meta"]["output_dir"],
            "status": state.get("final_status"),
        },
    )


def find_interrupted_task_from_progress(state: dict[str, Any]) -> str:
    last_start = ""
    path = progress_path(state)
    if not path.is_file():
        return str(state["schedule"].get("current_task") or "")
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        if event.get("event") == "task_start":
            last_start = str(event.get("task_id") or "")
        elif event.get("event") == "task_end" and event.get("task_id") == last_start:
            last_start = ""
    return last_start or str(state["schedule"].get("current_task") or "")


def run_loop(state: dict[str, Any]) -> dict[str, Any]:
    lookup = task_lookup(state)
    failed_set = list(state["schedule"].get("next_tasks") or [])
    if not failed_set:
        state["final_status"] = "passed"
        state["end_time"] = now_iso()
        save_state(state)
        generate_reports(state)
        append_progress(state, "run_end", {"status": state["final_status"]})
        return state

    max_rounds = int(state["meta"].get("max_rounds", 10))
    stable_threshold = int(state["meta"].get("stable_threshold", 3))
    append_progress(
        state,
        "run_start",
        {
            "runnable_total": runnable_total(state),
            "skipped": len(state["schedule"].get("skipped_tasks") or []),
            "max_rounds": max_rounds,
            "stable_threshold": stable_threshold,
        },
    )

    while state["schedule"]["current_loop"] < max_rounds:
        pending_tasks = list(state["schedule"].get("round_pending_tasks") or [])
        if pending_tasks:
            round_no = int(state["schedule"].get("current_loop") or 1)
            current_failed = list(state["schedule"].get("round_failed_tasks") or [])
        else:
            round_no = int(state["schedule"]["current_loop"]) + 1
            state["schedule"]["current_loop"] = round_no
            pending_tasks = list(failed_set)
            current_failed = []
            state["schedule"]["round_pending_tasks"] = pending_tasks
            state["schedule"]["round_failed_tasks"] = current_failed
            append_progress(state, "round_start", {"round": round_no, "task_count": len(pending_tasks)})

        print(f"[therock-agent] Round {round_no}: executing {len(pending_tasks)} task(s)", flush=True)
        save_state(state)

        round_total = len(state["schedule"].get("round_pending_tasks") or [])
        while state["schedule"].get("round_pending_tasks"):
            task_id = state["schedule"]["round_pending_tasks"][0]
            existing_result = state["results"]["task_results"].get(task_id, {})
            if existing_result.get("status") == "pass":
                state["schedule"]["round_pending_tasks"] = [
                    item for item in state["schedule"].get("round_pending_tasks", []) if item != task_id
                ]
                completed = list(state["schedule"].get("completed_tasks") or [])
                if task_id not in completed:
                    completed.append(task_id)
                state["schedule"]["completed_tasks"] = completed
                append_progress(state, "task_checkpoint_skip", {"round": round_no, "task_id": task_id, "status": "pass"})
                save_state(state)
                continue
            task = lookup[task_id]
            round_index = round_total - len(state["schedule"].get("round_pending_tasks") or []) + 1
            print(
                f"[therock-agent] task_start round={round_no} index={round_index}/{round_total} task={task_id}",
                flush=True,
            )
            append_progress(
                state,
                "task_start",
                {
                    "round": round_no,
                    "task_id": task_id,
                    "round_index": round_index,
                    "round_total": round_total,
                    "completed": completed_runnable_count(state),
                    "total": runnable_total(state),
                },
            )
            result = run_task(state, task, round_no)
            pending = [item for item in state["schedule"].get("round_pending_tasks", []) if item != task_id]
            state["schedule"]["round_pending_tasks"] = pending
            if result["status"] != "pass":
                current_failed.append(task_id)
                state["schedule"]["round_failed_tasks"] = sorted(set(current_failed))
                if result["status"] == "blocked":
                    blocked = list(state["schedule"].get("blocked_tasks") or [])
                    if task_id not in blocked:
                        blocked.append(task_id)
                    state["schedule"]["blocked_tasks"] = blocked
                write_failure_report(state, result)
            else:
                completed = list(state["schedule"].get("completed_tasks") or [])
                if task_id not in completed:
                    completed.append(task_id)
                state["schedule"]["completed_tasks"] = completed
            counts = task_status_counts(state)
            append_progress(
                state,
                "task_end",
                {
                    "round": round_no,
                    "task_id": task_id,
                    "status": result["status"],
                    "return_code": result["return_code"],
                    "duration_seconds": result["duration_seconds"],
                    "pass": counts.get("pass", 0),
                    "fail": counts.get("fail", 0),
                    "skip": counts.get("skip", 0),
                    "blocked": counts.get("blocked", 0),
                },
            )
            print(
                "[therock-agent] task_end "
                f"task={task_id} status={result['status']} rc={result['return_code']} "
                f"duration={result['duration_seconds']}s pass={counts.get('pass', 0)} "
                f"fail={counts.get('fail', 0)} blocked={counts.get('blocked', 0)}",
                flush=True,
            )
            save_state(state)

        current_failed_sorted = sorted(set(current_failed))
        history = state["loop"]["failed_task_history"]
        history.append({"round": round_no, "failed_tasks": current_failed_sorted})
        state["schedule"]["round_pending_tasks"] = []
        state["schedule"]["round_failed_tasks"] = []
        append_progress(state, "round_end", {"round": round_no, "failed_tasks": current_failed_sorted})

        if not current_failed_sorted:
            state["final_status"] = "passed"
            state["schedule"]["next_tasks"] = []
            break

        last_failed = state["loop"].get("last_failed_set")
        if current_failed_sorted == last_failed:
            state["loop"]["stable_failed_count"] += 1
        else:
            state["loop"]["stable_failed_count"] = 0

        state["loop"]["last_failed_set"] = current_failed_sorted
        state["schedule"]["next_tasks"] = current_failed_sorted
        state["schedule"]["failed_tasks"] = current_failed_sorted
        save_state(state)

        if int(state["loop"]["stable_failed_count"]) >= stable_threshold:
            state["final_status"] = "failed"
            break

        failed_set = current_failed_sorted

    if state["final_status"] == "running":
        state["final_status"] = "stopped"
    state["end_time"] = now_iso()
    save_state(state)
    generate_reports(state)
    append_progress(state, "run_end", {"status": state["final_status"]})
    write_run_index(state, "run_end")
    return state


def cmd_init(args: argparse.Namespace) -> None:
    state = create_state(args)
    print(state["meta"]["output_dir"])


def cmd_run(args: argparse.Namespace) -> None:
    state = create_state(args)
    run_loop(state)
    print(f"[therock-agent] run_id={state['run_id']} status={state['final_status']}", flush=True)
    print(f"[therock-agent] output={state['meta']['output_dir']}", flush=True)


def start_background_runner(state: dict[str, Any]) -> None:
    output_dir = Path(state["meta"]["output_dir"])
    stdout_path = output_dir / "runner.stdout.log"
    stderr_path = output_dir / "runner.stderr.log"
    script_path = PROJECT_ROOT / ".opencode" / "tools" / "therock_agent.sh"
    command = [str(script_path), "_run-existing", state["run_id"], "--output-root", str(output_root_from_state(state))]
    env = os.environ.copy()
    env["PYTHONUNBUFFERED"] = "1"
    with stdout_path.open("a", encoding="utf-8") as stdout_handle, stderr_path.open("a", encoding="utf-8") as stderr_handle:
        proc = subprocess.Popen(
            command,
            cwd=PROJECT_ROOT,
            env=env,
            stdout=stdout_handle,
            stderr=stderr_handle,
            start_new_session=True,
            text=True,
        )
    metadata = {
        "backend": "pid",
        "pid": proc.pid,
        "pgid": os.getpgid(proc.pid),
        "run_id": state["run_id"],
        "started_at": now_iso(),
        "command": command,
        "stdout": str(stdout_path),
        "stderr": str(stderr_path),
    }
    atomic_write_json(pid_metadata_path(state), metadata)
    state.setdefault("runtime", {})
    state["runtime"].update({"runner_backend": "pid", "runner_pid": proc.pid, "runner_alive": True})
    save_state(state)
    append_progress(state, "background_started", {"backend": "pid", "pid": proc.pid})
    write_run_index(state, "run_start")


def cmd_start(args: argparse.Namespace) -> None:
    state = create_state(args)
    start_background_runner(state)
    runnable = runnable_total(state)
    skipped = len(state["schedule"].get("skipped_tasks") or [])
    print("[therock-agent] started", flush=True)
    print(f"run_id={state['run_id']}", flush=True)
    print(f"output={state['meta']['output_dir']}", flush=True)
    print("backend=pid", flush=True)
    print(f"runnable={runnable}", flush=True)
    print(f"skipped={skipped}", flush=True)
    print(f"gpu_risk={state['meta']['gpu_reset_risk_policy']}", flush=True)
    print(f"sudo_policy={state['meta']['sudo_policy']}", flush=True)
    print(f"status=.opencode/tools/therock_agent.sh status {state['run_id']}", flush=True)
    print(f"report=.opencode/tools/therock_agent.sh report {state['run_id']}", flush=True)


def mark_interrupted(state: dict[str, Any], reason: str) -> None:
    state["final_status"] = "interrupted"
    state["end_time"] = now_iso()
    state.setdefault("runtime", {})
    state["runtime"]["interrupt_reason"] = reason
    save_state(state)
    append_progress(state, "run_interrupted", {"reason": reason})
    write_run_index(state, "run_interrupted")


def cmd_run_existing(args: argparse.Namespace) -> None:
    state = load_state(args.output_root, args.run_id)

    def handle_signal(signum: int, _frame: Any) -> None:
        mark_interrupted(state, f"signal:{signum}")
        raise SystemExit(128 + signum)

    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)
    run_loop(state)
    print(f"[therock-agent] run_id={state['run_id']} status={state['final_status']}", flush=True)


def cmd_resume(args: argparse.Namespace) -> None:
    state = load_state(args.output_root, args.run_id)
    sudo_policy = args.sudo_policy or state.get("meta", {}).get("sudo_policy", "none")
    if state.get("final_status") == "running" and runner_alive(state):
        print(f"[therock-agent] run 仍在执行中，无需 resume: {state['run_id']}", flush=True)
        return
    if state.get("final_status") not in {"running", "interrupted", "stopped"}:
        print(f"[therock-agent] run 已结束，无需 resume: {state.get('final_status')}", flush=True)
        return
    interrupted = find_interrupted_task_from_progress(state)
    if interrupted:
        state["schedule"]["interrupted_task"] = interrupted
        existing = state["schedule"].get("round_pending_tasks") or state["schedule"].get("next_tasks") or []
        state["schedule"]["round_pending_tasks"] = [interrupted] + [task for task in existing if task != interrupted]
        state["schedule"]["current_task"] = None
    state["resume_count"] = int(state.get("resume_count", 0)) + 1
    state["final_status"] = "running"
    state["end_time"] = None
    if args.mock_command:
        state["meta"]["mock_command"] = args.mock_command
    state["meta"]["sudo_policy"] = sudo_policy
    if args.sudo_askpass:
        state["meta"]["sudo_askpass"] = args.sudo_askpass
    if args.sudo_agent_socket:
        state["meta"]["sudo_agent_socket"] = args.sudo_agent_socket
    save_state(state)
    append_progress(state, "resume_start", {"interrupted_task": interrupted})
    run_loop(state)
    print(f"[therock-agent] resumed run_id={state['run_id']} status={state['final_status']}", flush=True)


def cmd_report(args: argparse.Namespace) -> None:
    state = load_state(args.output_root, args.run_id)
    generate_reports(state)
    print(Path(state["meta"]["output_dir"]) / "summary_report.md")


def iter_run_states(output_root: str) -> list[dict[str, Any]]:
    root = Path(output_root).expanduser().resolve()
    if not root.is_dir():
        return []
    states: list[dict[str, Any]] = []
    for child in sorted(root.iterdir(), key=lambda item: item.name):
        if not child.is_dir() or child.name.startswith("_"):
            continue
        state_file = child / "global_state.json"
        if not state_file.is_file():
            continue
        try:
            states.append(json.loads(state_file.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            continue
    return states


def format_elapsed(state: dict[str, Any]) -> str:
    start_raw = str(state.get("start_time") or "")
    if not start_raw:
        return "unknown"
    try:
        start = dt.datetime.fromisoformat(start_raw)
    except ValueError:
        return "unknown"
    end_raw = state.get("end_time")
    if end_raw:
        try:
            end = dt.datetime.fromisoformat(str(end_raw))
        except ValueError:
            end = dt.datetime.now().astimezone()
    else:
        end = dt.datetime.now().astimezone()
    seconds = max(0, int((end - start).total_seconds()))
    hours, rem = divmod(seconds, 3600)
    minutes, secs = divmod(rem, 60)
    return f"{hours:02d}:{minutes:02d}:{secs:02d}"


def print_state_summary(state: dict[str, Any], output_format: str) -> None:
    counts = task_status_counts(state)
    completed = completed_runnable_count(state)
    total = runnable_total(state)
    status = effective_status(state)
    current = state["schedule"].get("current_task") or ""
    if not current and state["schedule"].get("round_pending_tasks"):
        current = state["schedule"]["round_pending_tasks"][0]
    if output_format == "json":
        payload = {
            "run_id": state["run_id"],
            "status": status,
            "round": state["schedule"].get("current_loop"),
            "progress": {"completed": completed, "total": total},
            "current_task": current,
            "elapsed": format_elapsed(state),
            "counts": counts,
            "output_dir": state["meta"]["output_dir"],
            "latest": latest_progress_events(state),
        }
        print(json.dumps(payload, ensure_ascii=False, indent=2), flush=True)
        return
    if output_format == "brief":
        print(
            "|".join(
                [
                    status,
                    str(state["schedule"].get("current_loop") or 0),
                    f"{completed}/{total}",
                    current,
                    format_elapsed(state),
                    str(counts.get("pass", 0)),
                    str(counts.get("fail", 0)),
                    str(counts.get("skip", 0)),
                    str(counts.get("blocked", 0)),
                ]
            ),
            flush=True,
        )
        return

    print(f"run_id: {state['run_id']}", flush=True)
    print(f"status: {status}", flush=True)
    print(f"round: {state['schedule'].get('current_loop')}", flush=True)
    print(f"progress: {completed}/{total}", flush=True)
    print(f"current: {current or 'none'}", flush=True)
    print(f"elapsed: {format_elapsed(state)}", flush=True)
    print(
        "counts: "
        f"pass={counts.get('pass', 0)} fail={counts.get('fail', 0)} "
        f"skip={counts.get('skip', 0)} blocked={counts.get('blocked', 0)} "
        f"timeout={counts.get('timeout', 0)}",
        flush=True,
    )
    print(f"output: {state['meta']['output_dir']}", flush=True)
    latest = [event for event in latest_progress_events(state, 8) if event.get("event") in {"task_end", "task_start"}]
    if latest:
        print("latest:", flush=True)
        for event in latest[-5:]:
            if event.get("event") == "task_end":
                print(
                    f"- {event.get('task_id')} {event.get('status')} {event.get('duration_seconds')}s",
                    flush=True,
                )
            else:
                print(f"- {event.get('task_id')} started", flush=True)
    if status == "stale":
        print(f"suggestion: .opencode/tools/therock_agent.sh resume {state['run_id']}", flush=True)


def cmd_status(args: argparse.Namespace) -> None:
    if not args.run_id:
        states = iter_run_states(args.output_root)
        if args.format == "json":
            payload = [
                {
                    "run_id": state["run_id"],
                    "status": effective_status(state),
                    "progress": f"{completed_runnable_count(state)}/{runnable_total(state)}",
                    "elapsed": format_elapsed(state),
                    "output_dir": state["meta"]["output_dir"],
                }
                for state in states
            ]
            print(json.dumps(payload, ensure_ascii=False, indent=2), flush=True)
            return
        print("run_id status progress elapsed output", flush=True)
        for state in states:
            print(
                f"{state['run_id']} {effective_status(state)} "
                f"{completed_runnable_count(state)}/{runnable_total(state)} "
                f"{format_elapsed(state)} {state['meta']['output_dir']}",
                flush=True,
            )
        return
    state = load_state(args.output_root, args.run_id)
    print_state_summary(state, args.format)


def cmd_stop(args: argparse.Namespace) -> None:
    state = load_state(args.output_root, args.run_id)
    if state.get("final_status") not in {"running", "interrupted", "stopped"}:
        print(f"[therock-agent] run already ended run_id={state['run_id']} status={state.get('final_status')}", flush=True)
        return
    metadata = read_pid_metadata(state)
    pid = int(metadata.get("pid") or 0)
    pgid = int(metadata.get("pgid") or 0)
    if pid <= 0:
        raise SystemExit(f"找不到后台 runner pid: {pid_metadata_path(state)}")
    if not runner_alive(state):
        mark_interrupted(state, "runner_not_alive")
        print(f"[therock-agent] runner already stopped run_id={state['run_id']}", flush=True)
        return
    target = -pgid if pgid > 0 else pid
    os.kill(target, signal.SIGTERM)
    deadline = time.time() + float(args.timeout)
    while time.time() < deadline:
        if not process_alive(pid):
            break
        time.sleep(0.2)
    if process_alive(pid):
        os.kill(target, signal.SIGKILL)
    mark_interrupted(state, "stop_requested")
    print(f"[therock-agent] stopped run_id={state['run_id']}", flush=True)


def kv_to_runner_argv(command: str, raw_args: list[str]) -> list[str]:
    """Convert /therock-run key=value tokens into canonical runner flags."""
    key_map = {
        "artifacts": "--artifacts",
        "artifact": "--artifacts",
        "gpu": "--amdgpu-families",
        "amdgpu_families": "--amdgpu-families",
        "amdgpu-families": "--amdgpu-families",
        "amdgpu_targets": "--amdgpu-targets",
        "amdgpu-targets": "--amdgpu-targets",
        "components": "--components",
        "component": "--components",
        "test_types": "--test-types",
        "test-types": "--test-types",
        "gpu_risk": "--gpu-risk",
        "gpu-risk": "--gpu-risk",
        "sudo_policy": "--sudo-policy",
        "sudo-policy": "--sudo-policy",
        "max_rounds": "--max-rounds",
        "max-rounds": "--max-rounds",
        "stable_threshold": "--stable-threshold",
        "stable-threshold": "--stable-threshold",
        "therock_repo": "--therock-repo",
        "therock-repo": "--therock-repo",
        "output_root": "--output-root",
        "output-root": "--output-root",
        "run_id": "--run-id",
        "run-id": "--run-id",
        "component_config": "--component-config",
        "component-config": "--component-config",
        "component_env_index": "--component-env-index",
        "component-env-index": "--component-env-index",
        "official_exclude": "--official-exclude",
        "official-exclude": "--official-exclude",
        "mock_command": "--mock-command",
        "mock-command": "--mock-command",
        "sudo_askpass": "--sudo-askpass",
        "sudo-askpass": "--sudo-askpass",
        "sudo_agent_socket": "--sudo-agent-socket",
        "sudo-agent-socket": "--sudo-agent-socket",
    }
    positionals = ["--artifacts", "--amdgpu-families", "--components", "--test-types", "--gpu-risk"]
    argv: list[str] = [command]
    positional_index = 0

    for token in raw_args:
        if not token:
            continue
        if token == "--":
            continue
        if "=" in token and not token.startswith("--"):
            key, value = token.split("=", 1)
            key = key.strip().lower()
            value = value.strip()
            flag = key_map.get(key)
            if not flag:
                raise SystemExit(f"未知 /therock-run 参数: {key}")
            if not value or value in {"<你的真实build路径>", "<path>"}:
                raise SystemExit(f"{key} 参数缺少有效值")
            argv.extend([flag, value])
            continue
        if token.startswith("--"):
            argv.append(token)
            continue
        if positional_index >= len(positionals):
            raise SystemExit(f"无法解析多余位置参数: {token}")
        argv.extend([positionals[positional_index], token])
        positional_index += 1
    return argv


def cmd_run_kv(args: argparse.Namespace) -> None:
    parser = build_parser()
    parsed = parser.parse_args(kv_to_runner_argv("run", args.raw_args))
    parsed.func(parsed)


def cmd_start_kv(args: argparse.Namespace) -> None:
    parser = build_parser()
    parsed = parser.parse_args(kv_to_runner_argv("start", args.raw_args))
    parsed.func(parsed)


def cmd_init_kv(args: argparse.Namespace) -> None:
    parser = build_parser()
    parsed = parser.parse_args(kv_to_runner_argv("init", args.raw_args))
    parsed.func(parsed)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="TheRock rough loop test agent")
    subparsers = parser.add_subparsers(dest="command", required=True)

    def add_common_run_options(target: argparse.ArgumentParser) -> None:
        target.add_argument("--therock-repo", default=os.environ.get("THEROCK_REPO", ""))
        target.add_argument("--artifacts", required=True)
        target.add_argument("--gpu", default="", help="Backward-compatible alias for --amdgpu-families")
        target.add_argument("--amdgpu-families", default=os.environ.get("THEROCK_AMDGPU_FAMILIES", ""))
        target.add_argument("--amdgpu-targets", default=os.environ.get("THEROCK_AMDGPU_TARGETS", ""))
        target.add_argument("--components", default="")
        target.add_argument("--test-types", default="quick,standard,comprehensive,full")
        target.add_argument("--gpu-risk", choices=["skip", "include", "quarantine"], default="skip")
        target.add_argument("--output-root", default=str(PROJECT_ROOT / "runs"))
        target.add_argument("--component-config", default=str(DEFAULT_COMPONENT_CONFIG))
        target.add_argument("--component-env-index", default=str(DEFAULT_COMPONENT_ENV_INDEX))
        target.add_argument("--official-exclude", default=str(DEFAULT_OFFICIAL_EXCLUDE))
        target.add_argument("--run-id", default="")
        target.add_argument("--stable-threshold", type=int, default=3)
        target.add_argument("--max-rounds", type=int, default=10)
        target.add_argument("--mock-command", default="")
        target.add_argument(
            "--sudo-policy",
            choices=["none", "cache", "askpass"],
            default=os.environ.get("THEROCK_SUDO_POLICY", "none"),
        )
        target.add_argument(
            "--sudo-askpass",
            default=os.environ.get("THEROCK_SUDO_ASKPASS", ""),
        )
        target.add_argument(
            "--sudo-agent-socket",
            default=os.environ.get("THEROCK_SUDO_AGENT_SOCKET", ""),
        )

    init_parser = subparsers.add_parser("init")
    add_common_run_options(init_parser)
    init_parser.set_defaults(func=cmd_init)

    init_kv_parser = subparsers.add_parser("init-kv")
    init_kv_parser.add_argument("raw_args", nargs=argparse.REMAINDER)
    init_kv_parser.set_defaults(func=cmd_init_kv)

    run_parser = subparsers.add_parser("run")
    add_common_run_options(run_parser)
    run_parser.set_defaults(func=cmd_run)

    run_kv_parser = subparsers.add_parser("run-kv")
    run_kv_parser.add_argument("raw_args", nargs=argparse.REMAINDER)
    run_kv_parser.set_defaults(func=cmd_run_kv)

    start_parser = subparsers.add_parser("start")
    add_common_run_options(start_parser)
    start_parser.set_defaults(func=cmd_start)

    start_kv_parser = subparsers.add_parser("start-kv")
    start_kv_parser.add_argument("raw_args", nargs=argparse.REMAINDER)
    start_kv_parser.set_defaults(func=cmd_start_kv)

    run_existing_parser = subparsers.add_parser("_run-existing")
    run_existing_parser.add_argument("run_id")
    run_existing_parser.add_argument("--output-root", default=str(PROJECT_ROOT / "runs"))
    run_existing_parser.set_defaults(func=cmd_run_existing)

    resume_parser = subparsers.add_parser("resume")
    resume_parser.add_argument("run_id")
    resume_parser.add_argument("--output-root", default=str(PROJECT_ROOT / "runs"))
    resume_parser.add_argument("--mock-command", default="")
    resume_parser.add_argument("--sudo-policy", choices=["none", "cache", "askpass"], default="")
    resume_parser.add_argument("--sudo-askpass", default=os.environ.get("THEROCK_SUDO_ASKPASS", ""))
    resume_parser.add_argument("--sudo-agent-socket", default=os.environ.get("THEROCK_SUDO_AGENT_SOCKET", ""))
    resume_parser.set_defaults(func=cmd_resume)

    report_parser = subparsers.add_parser("report")
    report_parser.add_argument("run_id")
    report_parser.add_argument("--output-root", default=str(PROJECT_ROOT / "runs"))
    report_parser.set_defaults(func=cmd_report)

    status_parser = subparsers.add_parser("status")
    status_parser.add_argument("run_id", nargs="?")
    status_parser.add_argument("--output-root", default=str(PROJECT_ROOT / "runs"))
    status_parser.add_argument("--format", choices=["text", "brief", "json"], default="text")
    status_parser.set_defaults(func=cmd_status)

    stop_parser = subparsers.add_parser("stop")
    stop_parser.add_argument("run_id")
    stop_parser.add_argument("--output-root", default=str(PROJECT_ROOT / "runs"))
    stop_parser.add_argument("--timeout", type=int, default=5)
    stop_parser.set_defaults(func=cmd_stop)
    return parser


def main(project_root: str, argv: list[str]) -> None:
    configure(Path(project_root).resolve())
    write_global_audit(argv, "invocation_start", "running", command=" ".join(safe_argv(argv)))
    try:
        load_project_env()
        parser = build_parser()
        args = parser.parse_args(argv)
        args.func(args)
        write_global_audit(argv, "invocation_end", "success", command=" ".join(safe_argv(argv)))
    except SystemExit as exc:
        status = "success" if exc.code in (0, None) else "failed"
        write_global_audit(
            argv,
            "invocation_failed" if status == "failed" else "invocation_end",
            status,
            command=" ".join(safe_argv(argv)),
            error=str(exc.code) if exc.code not in (0, None) else None,
        )
        raise
    except Exception as exc:
        write_global_audit(
            argv,
            "invocation_failed",
            "failed",
            command=" ".join(safe_argv(argv)),
            error=f"{type(exc).__name__}: {exc}",
        )
        raise


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("usage: python -m therock_agent.cli <project_root> <command> [args...]")
    main(sys.argv[1], sys.argv[2:])
