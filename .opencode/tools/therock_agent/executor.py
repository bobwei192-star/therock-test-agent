from __future__ import annotations

import os
import shlex
import subprocess
import time
from pathlib import Path
from typing import Any

from .artifacts import discover_therock_repo
from .audit import append_activity
from .audit import append_jsonl
from .audit import append_wrapper_audit
from .audit import ensure_dir
from .audit import now_iso
from .audit import safe_env_value
from .classifier import detect_failure_summary
from .classifier import detect_path_hardcode
from .classifier import extract_failure_evidence
from .config import SENSITIVE_ENV_NAMES
from .config import load_component_env_index
from .entrypoint import build_task_env
from .entrypoint import expand_template
from .entrypoint import resolve_entrypoint
from .entrypoint import task_context
from .preflight import check_task_preflight
from .state import save_state
from .venv import resolve_test_python_executable


ROCBLAS_QUICK_TIMEOUT_SECONDS = 3 * 60 * 60


def changed_env_values(env: dict[str, str]) -> dict[str, str]:
    changes: dict[str, str] = {}
    for key, value in sorted(env.items()):
        if key in SENSITIVE_ENV_NAMES or ("PASSWORD" in key.upper()) or ("TOKEN" in key.upper()):
            continue
        if os.environ.get(key) != value:
            changes[key] = value
    return changes


def rocblas_quick_timeout_seconds(task: dict[str, Any], entrypoint_metadata: dict[str, Any]) -> int | None:
    test_component = str(entrypoint_metadata.get("test_component") or task.get("component") or "")
    test_type = str(task.get("test_type") or "")
    if (
        entrypoint_metadata.get("entrypoint_type") == "test_runner"
        and test_component == "rocblas"
        and test_type == "quick"
    ):
        return ROCBLAS_QUICK_TIMEOUT_SECONDS
    return None


def write_rocblas_quick_timeout_launcher(launcher_path: Path) -> None:
    launcher_path.write_text(
        """#!/usr/bin/env python3
from __future__ import annotations

import importlib.util
import os
import re
import shutil
import sys
from pathlib import Path


def _quote_ctest_timeout(match: re.Match[str], timeout_seconds: int) -> str:
    return f"{match.group(1)}{match.group(2)}{timeout_seconds}{match.group(4)}"


def _build_timeout_overlay(test_dir: str, overlay_root: str, timeout_seconds: int) -> str:
    source_dir = Path(test_dir).resolve()
    ctest_file = source_dir / "CTestTestfile.cmake"
    if not ctest_file.is_file():
        print(
            f"# TheRock Test Agent: rocblas quick timeout override skipped; missing {ctest_file}",
            file=sys.stderr,
        )
        return str(source_dir)

    overlay_base = Path(overlay_root).resolve()
    if overlay_base.exists():
        shutil.rmtree(overlay_base)
    overlay_base.mkdir(parents=True, exist_ok=True)

    # Preserve the original parent/test-dir shape so CTest relative commands
    # like "../rocblas-test" still resolve from the patched CTestTestfile.
    overlay_dir = overlay_base / source_dir.name
    overlay_dir.mkdir(parents=True, exist_ok=True)

    for sibling in source_dir.parent.iterdir():
        if sibling.name == source_dir.name:
            continue
        target = overlay_base / sibling.name
        os.symlink(sibling, target, target_is_directory=sibling.is_dir())

    for child in source_dir.iterdir():
        if child.name == "CTestTestfile.cmake":
            continue
        target = overlay_dir / child.name
        os.symlink(child, target, target_is_directory=child.is_dir())

    text = ctest_file.read_text(encoding="utf-8")
    patched, replacements = re.subn(
        r"(\\bTIMEOUT\\s+)([\\\"']?)(\\d+)([\\\"']?)",
        lambda match: _quote_ctest_timeout(match, timeout_seconds),
        text,
    )
    (overlay_dir / "CTestTestfile.cmake").write_text(patched, encoding="utf-8")
    print(
        "# TheRock Test Agent: rocblas quick CTest TIMEOUT override "
        f"seconds={timeout_seconds} replacements={replacements} overlay={overlay_dir}"
    )
    return str(overlay_dir)


def main() -> int:
    try:
        timeout_seconds = int(sys.argv[1])
        overlay_root = sys.argv[2]
        separator_index = sys.argv.index("--")
    except (IndexError, ValueError) as exc:
        print(f"Invalid timeout launcher arguments: {sys.argv}: {exc}", file=sys.stderr)
        return 2

    command = sys.argv[separator_index + 1 :]
    if len(command) < 2:
        print(f"Invalid wrapped command: {command}", file=sys.stderr)
        return 2

    script_path = Path(command[1] if Path(command[0]).name.startswith("python") else command[0])
    script_args = command[2:] if Path(command[0]).name.startswith("python") else command[1:]
    sys.argv = [str(script_path), *script_args]

    spec = importlib.util.spec_from_file_location("_therock_test_runner", script_path)
    if spec is None or spec.loader is None:
        print(f"Unable to load test runner: {script_path}", file=sys.stderr)
        return 2

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    module.ctest_timeout_seconds = timeout_seconds
    if hasattr(module, "TEST_DIR"):
        module.TEST_DIR = _build_timeout_overlay(str(module.TEST_DIR), overlay_root, timeout_seconds)
    if not hasattr(module, "main"):
        print(f"test runner has no main(): {script_path}", file=sys.stderr)
        return 2
    return int(module.main())


if __name__ == "__main__":
    raise SystemExit(main())
""",
        encoding="utf-8",
    )
    launcher_path.chmod(0o755)


def write_execution_wrapper(
    state: dict[str, Any],
    task: dict[str, Any],
    round_no: int,
    command: list[str],
    cwd: str,
    env: dict[str, str],
    entrypoint_metadata: dict[str, Any],
) -> tuple[Path, dict[str, Any]]:
    wrappers_dir = Path(state["meta"]["output_dir"]) / "wrappers"
    ensure_dir(wrappers_dir)
    wrapper_path = wrappers_dir / f"{task['task_id']}.round{round_no}.sh"
    timeout_seconds = rocblas_quick_timeout_seconds(task, entrypoint_metadata)
    actual_command = command
    timeout_override: dict[str, Any] = {}
    if timeout_seconds is not None:
        launcher_path = wrappers_dir / f"{task['task_id']}.round{round_no}.timeout_launcher.py"
        overlay_root = wrappers_dir / f"{task['task_id']}.round{round_no}.ctest_timeout_overlay"
        write_rocblas_quick_timeout_launcher(launcher_path)
        env["THEROCK_AGENT_CTEST_TIMEOUT_SECONDS"] = str(timeout_seconds)
        actual_command = [
            "python3",
            str(launcher_path),
            str(timeout_seconds),
            str(overlay_root),
            "--",
            *command,
        ]
        timeout_override = {
            "enabled": True,
            "seconds": timeout_seconds,
            "strategy": "ctest_test_dir_overlay",
            "launcher_path": str(launcher_path),
            "overlay_root": str(overlay_root),
        }
    env_changes = changed_env_values(env)

    lines = [
        "#!/usr/bin/env bash",
        "set -euo pipefail",
        "",
        "# Generated by TheRock Test Agent. Do not edit artifacts or component sources.",
        f"# task_id={task['task_id']}",
        f"# entrypoint_type={entrypoint_metadata.get('entrypoint_type', '')}",
        f"# script={entrypoint_metadata.get('script', '')}",
        f"cd {shlex.quote(cwd)}",
        "",
    ]
    for key, value in env_changes.items():
        lines.append(f"export {key}={shlex.quote(value)}")
    lines.extend(["", "exec " + " ".join(shlex.quote(item) for item in actual_command)])

    wrapper_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    wrapper_path.chmod(0o755)

    details = {
        "wrapper_path": str(wrapper_path),
        "cwd": cwd,
        "command": " ".join(actual_command),
        "original_command": " ".join(command),
        "env_changes": {key: safe_env_value(key, value) for key, value in env_changes.items()},
        "entrypoint": entrypoint_metadata,
        "timeout_override": timeout_override,
        "policy": "wrapper_only_no_artifact_or_source_mutation",
    }
    return wrapper_path, details


def render_command(
    project_root: Path,
    state: dict[str, Any],
    task: dict[str, Any],
    round_no: int,
) -> list[str] | str:
    meta = state["meta"]
    mock_command = meta.get("mock_command")
    if mock_command:
        return mock_command.format(
            task_id=task["task_id"],
            component=task["component"],
            test_type=task["test_type"],
            round=round_no,
        )

    therock_repo = discover_therock_repo(project_root, str(meta.get("therock_repo_path") or ""))
    if not therock_repo:
        raise FileNotFoundError("缺少 TheRock 仓库路径，请传入 --therock-repo 或设置 THEROCK_REPO。")
    entrypoint = task.get("entrypoint") or resolve_entrypoint(
        load_component_env_index(Path(meta["component_env_index"])),
        task["component"],
        task["test_type"],
    )
    entrypoint_type = entrypoint.get("entrypoint_type", "test_runner")

    scripts_dir = therock_repo / "build_tools" / "github_actions" / "test_executable_scripts"
    if entrypoint_type == "test_runner":
        script_name = "test_runner.py"
    elif entrypoint_type == "dedicated_python":
        script_name = str(entrypoint.get("script") or "")
        if not script_name:
            raise FileNotFoundError(f"{task['component']} 缺少 dedicated_python script 配置。")
    else:
        raise FileNotFoundError(f"{task['component']} entrypoint_type={entrypoint_type} 不可执行。")

    script_path = scripts_dir / script_name
    if not script_path.is_file():
        raise FileNotFoundError(f"找不到 TheRock 测试脚本: {script_path}")

    context = task_context(state, task, entrypoint)
    python_executable = resolve_test_python_executable(state, therock_repo)
    command = [python_executable, str(script_path)]
    for arg in entrypoint.get("cli_args", []):
        command.append(expand_template(str(arg), context))
    return command


def run_task(project_root: Path, state: dict[str, Any], task: dict[str, Any], round_no: int) -> dict[str, Any]:
    output_dir = Path(state["meta"]["output_dir"])
    logs_dir = output_dir / "logs"
    runtime_label = state.get("meta", {}).get("runtime_label", "unknown")
    stdout_path = logs_dir / f"{task['task_id']}.round{round_no}.stdout.log"
    stderr_path = logs_dir / f"{task['task_id']}.round{round_no}.stderr.log"
    command_record: str
    original_command_record = ""
    wrapper_details: dict[str, Any] | None = None
    start = time.monotonic()
    entrypoint = task.get("entrypoint") or resolve_entrypoint(
        load_component_env_index(Path(state["meta"]["component_env_index"])),
        task["component"],
        task["test_type"],
    )
    env, entrypoint_metadata = build_task_env(state, task, entrypoint)

    # Evidence for OpenCode: distinguish "test python" vs "bootstrap venv python".
    # This is required to correctly classify python_interpreter_mismatch and to avoid
    # repairing packages into a venv that the test runner never imports.
    therock_repo_for_python = discover_therock_repo(project_root, str(state["meta"].get("therock_repo_path") or ""))
    bootstrap_venv_python = (((state.get("bootstrap") or {}).get("venv") or {}).get("python")) or ""
    test_python_executable = resolve_test_python_executable(state, therock_repo_for_python)
    python_context = {
        "test_python_executable": test_python_executable,
        "bootstrap_venv_python": bootstrap_venv_python,
        "test_python_kind": (
            "venv"
            if bootstrap_venv_python and str(test_python_executable) == str(bootstrap_venv_python)
            else ("system" if test_python_executable == "python3" else "unknown")
        ),
        "bootstrap_venv_python_exists": bool(bootstrap_venv_python) and Path(str(bootstrap_venv_python)).is_file(),
    }

    state["schedule"]["current_task"] = task["task_id"]
    save_state(state)
    append_activity(
        state,
        "task_start",
        {
            "task_id": task["task_id"],
            "round": round_no,
            "component": task["component"],
            "test_type": task["test_type"],
            "stdout_log": str(stdout_path),
            "stderr_log": str(stderr_path),
            "runtime_label": runtime_label,
            "entrypoint": entrypoint_metadata,
        },
    )

    try:
        preflight_error = check_task_preflight(state, task, env, entrypoint_metadata)
        if preflight_error:
            command_record = "blocked before execution"
            return_code = 125
            status = "blocked"
            failure_summary = preflight_error
            stdout_path.write_text("", encoding="utf-8")
            stderr_path.write_text(preflight_error + "\n", encoding="utf-8")
        else:
            command = render_command(project_root, state, task, round_no)
            command_record = command if isinstance(command, str) else " ".join(command)
            cwd = (
                state["meta"]["build_root"]
                if isinstance(command, str)
                else str(discover_therock_repo(project_root, str(state["meta"].get("therock_repo_path") or "")) or state["meta"]["build_root"])
            )
            if isinstance(command, str):
                executable_command: str | list[str] = command
            else:
                wrapper_path, wrapper_details = write_execution_wrapper(
                    state,
                    task,
                    round_no,
                    command,
                    cwd,
                    env,
                    entrypoint_metadata,
                )
                original_command_record = command_record
                command_record = str(wrapper_path)
                executable_command = [str(wrapper_path)]
                append_wrapper_audit(
                    state,
                    {
                        "time": now_iso(),
                        "event": "wrapper_generated",
                        "task_id": task["task_id"],
                        "round": round_no,
                        **wrapper_details,
                    },
                )
                append_activity(
                    state,
                    "wrapper_generated",
                    {
                        "task_id": task["task_id"],
                        "round": round_no,
                        "wrapper_path": str(wrapper_path),
                        "env_change_keys": sorted(wrapper_details["env_changes"].keys()),
                        "policy": wrapper_details["policy"],
                    },
                )
            with stdout_path.open("w", encoding="utf-8") as stdout_handle, stderr_path.open("w", encoding="utf-8") as stderr_handle:
                if isinstance(executable_command, str):
                    proc = subprocess.run(
                        executable_command,
                        shell=True,
                        cwd=cwd,
                        env=env,
                        stdout=stdout_handle,
                        stderr=stderr_handle,
                        text=True,
                    )
                else:
                    proc = subprocess.run(
                        executable_command,
                        cwd=cwd,
                        env=os.environ.copy(),
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

    path_hardcode_detection = detect_path_hardcode(stdout_path, stderr_path)
    failure_evidence = extract_failure_evidence(stdout_path, stderr_path) if status != "pass" else {}
    if status != "pass":
        # Attach deterministic python context for later OpenCode classification/repair.
        # Additionally, test whether the missing modules are importable under the bootstrap venv python
        # so python_interpreter_mismatch can be decided without guessing.
        missing_modules = failure_evidence.get("missing_python_modules") or []
        bootstrap_python = python_context.get("bootstrap_venv_python") or ""
        bootstrap_importable: dict[str, bool] = {}
        if missing_modules and bootstrap_python and python_context.get("bootstrap_venv_python_exists"):
            for module_name in missing_modules:
                try:
                    proc = subprocess.run(
                        [
                            bootstrap_python,
                            "-c",
                            "import importlib.util, sys; sys.exit(0 if importlib.util.find_spec(%r) is not None else 1)"
                            % module_name,
                        ],
                        stdout=subprocess.DEVNULL,
                        stderr=subprocess.DEVNULL,
                        text=True,
                        timeout=20,
                    )
                    bootstrap_importable[module_name] = proc.returncode == 0
                except Exception:
                    bootstrap_importable[module_name] = False

        python_context["bootstrap_importable_missing_modules"] = bootstrap_importable
        failure_evidence["python_context"] = python_context
    if path_hardcode_detection["detected"]:
        append_activity(
            state,
            "path_hardcode_detected",
            {
                "task_id": task["task_id"],
                "round": round_no,
                "categories": path_hardcode_detection["categories"],
                "matches": path_hardcode_detection["matches"],
                "policy": "detected_only_no_artifact_or_source_mutation",
            },
        )
        if status != "pass":
            first_match = path_hardcode_detection["matches"][0]
            failure_summary = f"{first_match['category']}: {first_match['line']}"

    duration = round(time.monotonic() - start, 3)
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
        "entrypoint_type": entrypoint_metadata.get("entrypoint_type"),
        "script": entrypoint_metadata.get("script"),
        "test_component": entrypoint_metadata.get("test_component"),
        "env_profiles": entrypoint_metadata.get("env_profiles", []),
        "known_issue_category": entrypoint_metadata.get("known_issue_category"),
        "retry_policy": entrypoint_metadata.get("retry_policy"),
        "timeout_hint_seconds": entrypoint_metadata.get("timeout_hint_seconds"),
        "preflight_python_modules": entrypoint_metadata.get("preflight_python_modules", []),
        "round": round_no,
        "command": command_record,
        "original_command": original_command_record,
        "wrapper_path": wrapper_details["wrapper_path"] if wrapper_details else "",
        "wrapper_env_change_keys": sorted(wrapper_details["env_changes"].keys()) if wrapper_details else [],
        "path_hardcode_detection": path_hardcode_detection,
        "failure_evidence": failure_evidence,
        "runtime_label": runtime_label,
        "runtime_summary": state.get("runtime_summary", {}),
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
            "original_command": original_command_record,
            "wrapper_path": wrapper_details["wrapper_path"] if wrapper_details else "",
            "wrapper_env_change_keys": sorted(wrapper_details["env_changes"].keys()) if wrapper_details else [],
            "path_hardcode_detection": path_hardcode_detection,
            "failure_evidence": failure_evidence,
            "return_code": return_code,
            "duration_seconds": duration,
            "status": status,
            "runtime_label": runtime_label,
            "entrypoint": entrypoint_metadata,
        },
    )
    append_activity(
        state,
        "task_end",
        {
            "task_id": task["task_id"],
            "round": round_no,
            "command": command_record,
            "return_code": return_code,
            "duration_seconds": duration,
            "status": status,
            "stdout_log": str(stdout_path),
            "stderr_log": str(stderr_path),
            "runtime_label": runtime_label,
            "wrapper_path": wrapper_details["wrapper_path"] if wrapper_details else "",
            "path_hardcode_detection": path_hardcode_detection,
        },
    )
    return result
