from __future__ import annotations

import argparse
import datetime as dt
import os
import sys
import uuid
from pathlib import Path
from typing import Any

from .artifacts import discover_therock_repo as _discover_therock_repo
from .artifacts import resolve_artifacts_path
from .audit import append_activity
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


def run_loop(state: dict[str, Any]) -> dict[str, Any]:
    lookup = task_lookup(state)
    failed_set = list(state["schedule"].get("next_tasks") or [])
    if not failed_set:
        state["final_status"] = "passed"
        state["end_time"] = now_iso()
        save_state(state)
        generate_reports(state)
        return state

    max_rounds = int(state["meta"].get("max_rounds", 10))
    stable_threshold = int(state["meta"].get("stable_threshold", 3))

    while state["schedule"]["current_loop"] < max_rounds:
        round_no = int(state["schedule"]["current_loop"]) + 1
        state["schedule"]["current_loop"] = round_no
        current_failed: list[str] = []
        print(f"[therock-agent] Round {round_no}: executing {len(failed_set)} task(s)")
        save_state(state)

        for index, task_id in enumerate(failed_set, start=1):
            task = lookup[task_id]
            print(f"[therock-agent] ({index}/{len(failed_set)}) {task_id}")
            result = run_task(state, task, round_no)
            if result["status"] != "pass":
                current_failed.append(task_id)
                write_failure_report(state, result)

        current_failed_sorted = sorted(current_failed)
        history = state["loop"]["failed_task_history"]
        history.append({"round": round_no, "failed_tasks": current_failed_sorted})

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
    return state


def cmd_init(args: argparse.Namespace) -> None:
    state = create_state(args)
    print(state["meta"]["output_dir"])


def cmd_run(args: argparse.Namespace) -> None:
    state = create_state(args)
    run_loop(state)
    print(f"[therock-agent] run_id={state['run_id']} status={state['final_status']}")
    print(f"[therock-agent] output={state['meta']['output_dir']}")


def cmd_resume(args: argparse.Namespace) -> None:
    state = load_state(args.output_root, args.run_id)
    sudo_policy = args.sudo_policy or state.get("meta", {}).get("sudo_policy", "none")
    if state.get("final_status") not in {"running", "interrupted", "stopped"}:
        print(f"[therock-agent] run 已结束，无需 resume: {state.get('final_status')}")
        return
    if state["schedule"].get("current_task"):
        interrupted = state["schedule"]["current_task"]
        state["schedule"]["interrupted_task"] = interrupted
        existing = state["schedule"].get("next_tasks") or []
        state["schedule"]["next_tasks"] = [interrupted] + [task for task in existing if task != interrupted]
        state["schedule"]["current_task"] = None
    state["resume_count"] = int(state.get("resume_count", 0)) + 1
    state["final_status"] = "running"
    if args.mock_command:
        state["meta"]["mock_command"] = args.mock_command
    state["meta"]["sudo_policy"] = sudo_policy
    if args.sudo_askpass:
        state["meta"]["sudo_askpass"] = args.sudo_askpass
    if args.sudo_agent_socket:
        state["meta"]["sudo_agent_socket"] = args.sudo_agent_socket
    save_state(state)
    run_loop(state)
    print(f"[therock-agent] resumed run_id={state['run_id']} status={state['final_status']}")


def cmd_report(args: argparse.Namespace) -> None:
    state = load_state(args.output_root, args.run_id)
    generate_reports(state)
    print(Path(state["meta"]["output_dir"]) / "summary_report.md")


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

    run_parser = subparsers.add_parser("run")
    add_common_run_options(run_parser)
    run_parser.set_defaults(func=cmd_run)

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
