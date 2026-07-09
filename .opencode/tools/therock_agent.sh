#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "${SCRIPT_DIR}/../.." && pwd)"

python3 - "$PROJECT_ROOT" "$@" <<'PY'
from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import time
import uuid
from pathlib import Path
from typing import Any


PROJECT_ROOT = Path(sys.argv[1]).resolve()
DEFAULT_COMPONENT_CONFIG = PROJECT_ROOT / "docs_this_project" / "component_sort_order.json"
DEFAULT_FAILURE_TEMPLATE = PROJECT_ROOT / "docs_this_project" / "问题模板.md"
DEFAULT_SUMMARY_TEMPLATE = PROJECT_ROOT / "docs_this_project" / "汇总测试报告.md"
SENSITIVE_ENV_NAMES = {"SUDO_PASSWORD", "THEROCK_SUDO_PASSWORD"}


def load_project_env() -> None:
    """Load safe THEROCK_* settings from .env without accepting passwords."""
    env_path = PROJECT_ROOT / ".env"
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


load_project_env()


def now_iso() -> str:
    return dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def atomic_write_json(path: Path, data: dict[str, Any]) -> None:
    ensure_dir(path.parent)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(path)


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    ensure_dir(path.parent)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")


def read_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def read_optional_text(path: Path) -> str:
    return path.read_text(encoding="utf-8") if path.is_file() else ""


def normalize_list(value: str | None) -> list[str]:
    if not value:
        return []
    return [item.strip() for item in value.split(",") if item.strip()]


def check_sudo_policy(policy: str) -> None:
    """Validate sudo readiness without reading or prompting for passwords."""
    if policy in {"none", "ask"}:
        return
    if policy != "cache":
        raise SystemExit(f"未知 THEROCK_SUDO_POLICY: {policy}")

    sudo = shutil.which("sudo")
    if not sudo:
        raise SystemExit("THEROCK_SUDO_POLICY=cache 需要系统存在 sudo 命令。")

    result = subprocess.run(
        [sudo, "-n", "true"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        text=True,
    )
    if result.returncode != 0:
        raise SystemExit(
            "THEROCK_SUDO_POLICY=cache 但当前 sudo 缓存不可用。请先在同一用户终端执行 "
            "`sudo -v`，再启动 opencode 或重新执行 /therock-run。"
        )


def resolve_artifacts_path(raw_path: str) -> tuple[Path, Path]:
    """Resolve build root and dist/rocm path from accepted artifact path shapes."""
    path = Path(raw_path).expanduser().resolve()

    if (path / "dist" / "rocm").is_dir():
        return path, path / "dist" / "rocm"

    if path.name == "rocm" and path.parent.name == "dist":
        return path.parent.parent, path

    if (path / "bin").is_dir() and (path / "lib").is_dir():
        return path.parent.parent if path.parent.name == "dist" else path, path

    raise SystemExit(
        "无法识别 ROCm artifacts path。请传入 /output-linux-portable/build、"
        "/output/build，或 dist/rocm 目录。"
    )


def load_component_entries(config_path: Path) -> list[dict[str, Any]]:
    data = read_json(config_path)
    entries = data.get("entries")
    if not isinstance(entries, list):
        raise SystemExit(f"组件排序文件缺少 entries: {config_path}")
    return sorted(entries, key=lambda item: int(item.get("sort_order", 0)))


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
    component_config: Path,
    components: list[str],
    test_types: list[str],
    gpu_risk_policy: str,
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
        if task["task_id"] in seen:
            continue
        seen.add(task["task_id"])

        if task["source_status"] == "exclude":
            task["skip_reason"] = "component_sort_order.json status=exclude"
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

    tasks, skipped = build_task_plan(component_config, components, test_types, args.gpu_risk)
    ensure_dir(output_dir / "logs")
    ensure_dir(output_dir / "failures")
    ensure_dir(output_dir / "memory")

    state: dict[str, Any] = {
        "schema_version": "0.1",
        "run_id": run_id,
        "start_time": now_iso(),
        "end_time": None,
        "final_status": "running",
        "meta": {
            "therock_repo_path": str(Path(args.therock_repo).expanduser().resolve()) if args.therock_repo else "",
            "artifacts_path": str(Path(args.artifacts).expanduser().resolve()),
            "build_root": str(build_root),
            "rocm_dist": str(rocm_dist),
            "gpu_model": amdgpu_families,
            "amdgpu_families": amdgpu_families,
            "amdgpu_targets": args.amdgpu_targets or amdgpu_families,
            "output_dir": str(output_dir),
            "component_config": str(component_config),
            "components_filter": components,
            "test_types": test_types,
            "gpu_reset_risk_policy": args.gpu_risk,
            "sudo_policy": args.sudo_policy,
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
                    "status": "skip",
                    "skip_reason": task.get("skip_reason", "skipped"),
                    "gpu_hang_risk": task.get("gpu_hang_risk", False),
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
    save_state(state)
    return state


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


def render_command(state: dict[str, Any], task: dict[str, Any], round_no: int) -> list[str] | str:
    meta = state["meta"]
    mock_command = meta.get("mock_command")
    if mock_command:
        return mock_command.format(
            task_id=task["task_id"],
            component=task["component"],
            test_type=task["test_type"],
            round=round_no,
        )

    therock_repo = Path(meta.get("therock_repo_path") or os.environ.get("THEROCK_REPO", "")).expanduser()
    runner = therock_repo / "build_tools" / "github_actions" / "test_executable_scripts" / "test_runner.py"
    if not runner.is_file():
        raise FileNotFoundError(f"找不到 TheRock test_runner.py: {runner}")

    return [
        "python3",
        str(runner),
        "--component",
        task["component"],
        "--test-type",
        task["test_type"],
    ]


def run_task(state: dict[str, Any], task: dict[str, Any], round_no: int) -> dict[str, Any]:
    output_dir = Path(state["meta"]["output_dir"])
    logs_dir = output_dir / "logs"
    stdout_path = logs_dir / f"{task['task_id']}.round{round_no}.stdout.log"
    stderr_path = logs_dir / f"{task['task_id']}.round{round_no}.stderr.log"
    command_record: str
    start = time.time()
    env = os.environ.copy()
    rocm_dist = state["meta"]["rocm_dist"]
    env["AMDGPU_FAMILIES"] = state["meta"]["amdgpu_families"]
    env["THEROCK_AMDGPU_FAMILIES"] = state["meta"]["amdgpu_families"]
    env["THEROCK_AMDGPU_TARGETS"] = state["meta"].get("amdgpu_targets", state["meta"]["amdgpu_families"])
    env["ROCM_PATH"] = rocm_dist
    env["LD_LIBRARY_PATH"] = f"{rocm_dist}/lib:{env.get('LD_LIBRARY_PATH', '')}"

    state["schedule"]["current_task"] = task["task_id"]
    save_state(state)

    try:
        command = render_command(state, task, round_no)
        command_record = command if isinstance(command, str) else " ".join(command)
        with stdout_path.open("w", encoding="utf-8") as stdout_handle, stderr_path.open("w", encoding="utf-8") as stderr_handle:
            if isinstance(command, str):
                proc = subprocess.run(
                    command,
                    shell=True,
                    cwd=state["meta"]["build_root"],
                    env=env,
                    stdout=stdout_handle,
                    stderr=stderr_handle,
                    text=True,
                )
            else:
                proc = subprocess.run(
                    command,
                    cwd=state["meta"]["build_root"],
                    env=env,
                    stdout=stdout_handle,
                    stderr=stderr_handle,
                    text=True,
                )
        return_code = proc.returncode
        status = "pass" if return_code == 0 else "fail"
        failure_summary = "" if status == "pass" else detect_failure_summary(stdout_path, stderr_path)
    except FileNotFoundError as exc:
        command_record = str(exc)
        return_code = 127
        status = "blocked"
        failure_summary = str(exc)
        stdout_path.write_text("", encoding="utf-8")
        stderr_path.write_text(str(exc) + "\n", encoding="utf-8")

    duration = round(time.time() - start, 3)
    result = {
        "task_id": task["task_id"],
        "component": task["component"],
        "test_type": task["test_type"],
        "status": status,
        "return_code": return_code,
        "duration_seconds": duration,
        "stdout_log": str(stdout_path),
        "stderr_log": str(stderr_path),
        "failure_summary": failure_summary,
        "gpu_hang_risk": task.get("gpu_hang_risk", False),
        "round": round_no,
        "command": command_record,
        "finished_at": now_iso(),
    }

    state["results"]["task_results"][task["task_id"]] = result
    state["schedule"]["current_task"] = None
    save_state(state)

    append_jsonl(
        Path(state["meta"]["output_dir"]) / "tool_calls.jsonl",
        {
            "time": now_iso(),
            "tool": "shell",
            "task_id": task["task_id"],
            "command": command_record,
            "return_code": return_code,
            "duration_seconds": duration,
            "status": status,
        },
    )
    return result


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


def summarize_counts(state: dict[str, Any]) -> dict[str, int]:
    counts = {"pass": 0, "fail": 0, "skip": 0, "blocked": 0, "timeout": 0, "flaky": 0, "interrupted": 0}
    for result in state["results"]["task_results"].values():
        status = result.get("status", "blocked")
        counts[status] = counts.get(status, 0) + 1
    return counts


def generate_reports(state: dict[str, Any]) -> None:
    output_dir = Path(state["meta"]["output_dir"])
    counts = summarize_counts(state)
    history = state["loop"]["failed_task_history"]
    total_tasks = len(state["schedule"]["task_queue"]) + len(state["schedule"]["skipped_tasks"])
    final_failures = [
        result
        for result in state["results"]["task_results"].values()
        if result.get("status") in {"fail", "blocked", "timeout", "interrupted"}
    ]
    skipped_risk = [
        result["task_id"]
        for result in state["results"]["task_results"].values()
        if result.get("status") == "skip" and result.get("gpu_hang_risk")
    ]

    lines = [
        f"# TheRock Test Summary - {state['run_id']}",
        "",
        f"> 本报告按 `docs_this_project/汇总测试报告.md` 的汇总报告要求自动生成。",
        f"> 模板路径：`{DEFAULT_SUMMARY_TEMPLATE}`",
        "",
        "## 基本信息",
        "",
        f"- 状态：`{state['final_status']}`",
        f"- AMDGPU_FAMILIES：`{state['meta'].get('amdgpu_families', state['meta'].get('gpu_model', ''))}`",
        f"- THEROCK_AMDGPU_TARGETS：`{state['meta'].get('amdgpu_targets', '')}`",
        f"- artifacts：`{state['meta']['artifacts_path']}`",
        f"- build_root：`{state['meta']['build_root']}`",
        f"- rocm_dist：`{state['meta']['rocm_dist']}`",
        f"- sudo_policy：`{state['meta'].get('sudo_policy', 'none')}`",
        f"- 开始时间：`{state['start_time']}`",
        f"- 结束时间：`{state.get('end_time')}`",
        "",
        "## 模板字段覆盖",
        "",
        f"- 总任务数：`{total_tasks}`",
        f"- 通过数：`{counts.get('pass', 0)}`",
        f"- 失败数：`{counts.get('fail', 0)}`",
        f"- 跳过数：`{counts.get('skip', 0)}`",
        f"- blocked 数：`{counts.get('blocked', 0)}`",
        f"- flaky 数：`{counts.get('flaky', 0)}`",
        f"- loop 轮次：`{len(history)}`",
        f"- 最终顽固失败任务数：`{len(final_failures)}`",
        "",
        "## 结果统计",
        "",
        "| 状态 | 数量 |",
        "|------|:----:|",
    ]
    for key in ("pass", "fail", "skip", "blocked", "timeout", "flaky", "interrupted"):
        lines.append(f"| {key} | {counts.get(key, 0)} |")

    lines.extend(["", "## Loop 收敛记录", ""])
    for item in history:
        failed = ", ".join(item["failed_tasks"]) if item["failed_tasks"] else "无"
        lines.append(f"- Round {item['round']}: {failed}")

    lines.extend(["", "## GPU reset 高风险跳过任务", ""])
    if skipped_risk:
        lines.extend(f"- `{task_id}`" for task_id in skipped_risk)
    else:
        lines.append("- 无")

    lines.extend(["", "## 最终失败 / 阻塞任务", ""])
    if final_failures:
        for result in final_failures:
            lines.append(f"- `{result['task_id']}`: {result.get('failure_summary', '')}")
    else:
        lines.append("- 无")

    lines.extend(
        [
            "",
            "## 报告产物",
            "",
            f"- 状态文件：`{output_dir / 'global_state.json'}`",
            f"- 日志目录：`{output_dir / 'logs'}`",
            f"- 失败报告目录：`{output_dir / 'failures'}`",
            f"- 审计日志：`{output_dir / 'tool_calls.jsonl'}`",
        ]
    )

    (output_dir / "summary_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_failure_report(state: dict[str, Any], result: dict[str, Any]) -> None:
    output_dir = Path(state["meta"]["output_dir"])
    template = read_optional_text(DEFAULT_FAILURE_TEMPLATE)
    meta = state["meta"]
    content = [
        f"# {result['task_id']} 失败报告",
        "",
        f"> 本报告按 `docs_this_project/问题模板.md` 的单组件问题模板自动生成。",
        f"> 模板路径：`{DEFAULT_FAILURE_TEMPLATE}`",
        "",
        "## 问题标题",
        "",
        f"{result['component']} {result['test_type']} {result.get('failure_summary', '测试失败')}",
        "",
        "## 问题时间",
        "",
        result.get("finished_at", now_iso()),
        "",
        "## 组件与测试信息",
        "",
        "| 字段 | 内容 |",
        "|------|------|",
        f"| 组件 | `{result['component']}` |",
        f"| 测试类型 | `{result['test_type']}` |",
        "| 测试框架 | TheRock test script / CTest / pytest / GoogleTest |",
        f"| 测试脚本 | `{result.get('command', '')}` |",
        f"| 测试命令 | `{result.get('command', '')}` |",
        "| 单用例复现命令 | 暂未缩小到单用例 |",
        f"| 测试配置文件 | `{meta.get('component_config', '')}` |",
        "| 超时配置 | 使用 TheRock 测试脚本默认值 |",
        "| 并发配置 | 使用 TheRock 测试脚本默认值 |",
        f"| 返回码 / 信号 | `{result.get('return_code')}` |",
        f"| 执行耗时 | `{result.get('duration_seconds')}s` |",
        f"| 日志路径 | stdout: `{result.get('stdout_log')}`<br>stderr: `{result.get('stderr_log')}` |",
        "",
        "## 问题具体描述",
        "",
        result.get("failure_summary") or "任务返回非 0 或被标记为 blocked，需要结合日志继续分析。",
        "",
        "## 原始失败结果",
        "",
        "| 项目 | 内容 |",
        "|------|------|",
        f"| 原始测试结果 | `{result.get('status')}`, rc=`{result.get('return_code')}` |",
        "| 失败用例数量 | 暂未解析 |",
        "| 失败用例名称 | 暂未解析 |",
        "| 原始判断 | 自动分类待补充 |",
        f"| 来源位置 | `{result.get('stderr_log')}` |",
        "| 是否历史失败 | 不确定 |",
        "| 是否本次新增失败 | 不确定 |",
        "| 是否影响 CI 阻塞 | 是 |",
        "",
        "## 测试环境",
        "",
        "| 项目 | 值 |",
        "|------|----|",
        "| 测试执行人 | OpenCode / 手动触发 |",
        "| 问题发生主机 | 自动采集待补充 |",
        "| OS / Kernel | 自动采集待补充 |",
        f"| GPU / 架构 | `{meta.get('amdgpu_families', meta.get('gpu_model', ''))}` |",
        f"| ROCm 版本 | `{meta.get('rocm_dist', '')}` |",
        "| Python 版本 | 自动采集待补充 |",
        f"| `AMDGPU_FAMILIES` | `{meta.get('amdgpu_families', '')}` |",
        f"| 关键环境变量 | `ROCM_PATH={meta.get('rocm_dist', '')}` |",
        f"| 权限 | sudo_policy=`{meta.get('sudo_policy', 'none')}` |",
        "| 是否单 GPU | 不确定 |",
        "| 是否发生 GPU reset / ring timeout | 需检查 stderr / dmesg |",
        "",
        "## 代码与构建版本",
        "",
        "| 项目 | 值 |",
        "|------|----|",
        f"| TheRock 仓库路径 | `{meta.get('therock_repo_path', '')}` |",
        "| TheRock branch | 自动采集待补充 |",
        "| TheRock commit | 自动采集待补充 |",
        "| TheRock 工作区状态 | 自动采集待补充 |",
        f"| 构建目录 | `{meta.get('build_root', '')}` |",
        f"| 安装 / 分发目录 | `{meta.get('rocm_dist', '')}` |",
        f"| 构建目标架构 | `{meta.get('amdgpu_families', '')}` |",
        "",
        "## 复现 / 复测步骤",
        "",
        "1. 进入 TheRock 仓库目录。",
        f"2. 确认 artifacts 路径：`{meta.get('artifacts_path', '')}`。",
        f"3. 执行命令：`{result.get('command', '')}`。",
        f"4. 查看 stdout：`{result.get('stdout_log')}`。",
        f"5. 查看 stderr：`{result.get('stderr_log')}`。",
        "",
        "## 复测结果",
        "",
        "| 项目 | 结果 |",
        "|------|------|",
        "| 是否复现原问题 | 是 |",
        f"| 复测返回码 / 信号 | `{result.get('return_code')}` |",
        "| 复测用例结果 | 暂未解析 |",
        "| 与原结果对比 | 当前为自动复测结果 |",
        f"| 复测结论 | `{result.get('status')}` |",
        "| 复测次数 | 见 `global_state.json` loop 记录 |",
        "| 结果稳定性 | 需结合多轮 loop 判断 |",
        "",
        "## 问题关键 log",
        "",
        f"- stdout log：`{result.get('stdout_log')}`",
        f"- stderr log：`{result.get('stderr_log')}`",
        f"- 失败摘要：{result.get('failure_summary', '')}",
        "",
        "## 问题原因解释",
        "",
        "自动初步结论：待人工结合日志、GPU 状态和已知 gfx1151 / ROCm issue 继续分类。",
        "",
        "## CI 处理建议",
        "",
        "- 保留该任务的 stdout / stderr 日志。",
        "- 如果是环境或 artifacts 缺失，先标记 blocked，不归为组件失败。",
        "- 如果多轮稳定失败，纳入顽固失败集合并生成上游 issue / CI skip 建议。",
        "",
        "## 附件与证据",
        "",
        f"- `global_state.json`: `{output_dir / 'global_state.json'}`",
        f"- `summary_report.md`: `{output_dir / 'summary_report.md'}`",
        f"- stdout: `{result.get('stdout_log')}`",
        f"- stderr: `{result.get('stderr_log')}`",
        "",
        "## 原始模板参考",
        "",
        template or "未找到 docs_this_project/问题模板.md。",
    ]
    (output_dir / "failures" / f"{result['task_id']}_failure_report.md").write_text(
        "\n".join(content) + "\n",
        encoding="utf-8",
    )


def cmd_init(args: argparse.Namespace) -> None:
    state = create_state(args)
    print(state["meta"]["output_dir"])


def cmd_run(args: argparse.Namespace) -> None:
    check_sudo_policy(args.sudo_policy)
    state = create_state(args)
    run_loop(state)
    print(f"[therock-agent] run_id={state['run_id']} status={state['final_status']}")
    print(f"[therock-agent] output={state['meta']['output_dir']}")


def cmd_resume(args: argparse.Namespace) -> None:
    state = load_state(args.output_root, args.run_id)
    sudo_policy = args.sudo_policy or state.get("meta", {}).get("sudo_policy", "none")
    check_sudo_policy(sudo_policy)
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
        target.add_argument("--run-id", default="")
        target.add_argument("--stable-threshold", type=int, default=3)
        target.add_argument("--max-rounds", type=int, default=10)
        target.add_argument("--mock-command", default="")
        target.add_argument(
            "--sudo-policy",
            choices=["none", "cache", "ask"],
            default=os.environ.get("THEROCK_SUDO_POLICY", "none"),
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
    resume_parser.add_argument("--sudo-policy", choices=["none", "cache", "ask"], default="")
    resume_parser.set_defaults(func=cmd_resume)

    report_parser = subparsers.add_parser("report")
    report_parser.add_argument("run_id")
    report_parser.add_argument("--output-root", default=str(PROJECT_ROOT / "runs"))
    report_parser.set_defaults(func=cmd_report)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args(sys.argv[2:])
    args.func(args)


if __name__ == "__main__":
    main()
PY
