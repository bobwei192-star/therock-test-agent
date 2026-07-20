#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENT="${PROJECT_ROOT}/.opencode/tools/therock_agent.sh"
RUN_BOOTSTRAP_OFF=(--bootstrap-env off)

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT

mkdir -p "${TMP_DIR}/output/build/dist/rocm/bin" "${TMP_DIR}/output/build/dist/rocm/lib"
touch "${TMP_DIR}/output/build/dist/rocm/lib/librocdxg.so"

cat >"${TMP_DIR}/component_sort_order.json" <<'JSON'
{
  "version": "test",
  "entries": [
    {"test_type": "quick", "component": "pass_component", "duration_ref": 1, "category": "lightweight", "status": "pass", "sort_order": 1, "gpu_hang_risk": false},
    {"test_type": "quick", "component": "fail_component", "duration_ref": 1, "category": "lightweight", "status": "fail", "sort_order": 2, "gpu_hang_risk": false},
    {"test_type": "quick", "component": "risk_component", "duration_ref": 1, "category": "heavy", "status": "pass", "sort_order": 3, "gpu_hang_risk": true},
    {"test_type": "quick", "component": "exclude_component", "duration_ref": 1, "category": "medium", "status": "exclude", "sort_order": 4, "gpu_hang_risk": false}
  ]
}
JSON

cat >"${TMP_DIR}/mock_runner.sh" <<'SH'
#!/usr/bin/env bash
set -euo pipefail
case "$1" in
  pass_component-quick)
    echo "mock pass"
    exit 0
    ;;
  fail_component-quick)
    echo "ModuleNotFoundError: No module named 'prettytable'"
    echo "[  FAILED  ] mock stable failure" >&2
    exit 8
    ;;
  *)
    echo "unexpected task: $1" >&2
    exit 99
    ;;
esac
SH
chmod +x "${TMP_DIR}/mock_runner.sh"

python3 - "${PROJECT_ROOT}" <<'PY'
import sys
from pathlib import Path

project_root = Path(sys.argv[1])
sys.path.insert(0, str(project_root / ".opencode" / "tools"))

from therock_agent.cli import kv_to_runner_argv

start_argv = kv_to_runner_argv("start", ["artifacts=/tmp/build", "gpu=gfx1151"])
assert start_argv[-2:] == ["--debug-repair", "opencode"], start_argv

off_argv = kv_to_runner_argv("start", ["artifacts=/tmp/build", "gpu=gfx1151", "debug_repair=off"])
assert off_argv.count("--debug-repair") == 1, off_argv
assert off_argv[-2:] == ["--debug-repair", "off"], off_argv

flag_off_argv = kv_to_runner_argv("start", ["artifacts=/tmp/build", "gpu=gfx1151", "--debug-repair=off"])
assert "--debug-repair=off" in flag_off_argv, flag_off_argv
assert flag_off_argv[-1] != "opencode", flag_off_argv

bootstrap_argv = kv_to_runner_argv("start", ["artifacts=/tmp/build", "gpu=gfx1151", "bootstrap_env=off"])
assert bootstrap_argv[-2:] == ["--debug-repair", "opencode"], bootstrap_argv
assert "--bootstrap-env" in bootstrap_argv, bootstrap_argv
assert "off" in bootstrap_argv, bootstrap_argv
PY

python3 - "${PROJECT_ROOT}" "${TMP_DIR}" <<'PY'
import json
import os
import sys
from pathlib import Path

project_root = Path(sys.argv[1])
tmp_dir = Path(sys.argv[2])
sys.path.insert(0, str(project_root / ".opencode" / "tools"))

from therock_agent.preflight import check_task_preflight
from therock_agent.runtime import detect_rocm_runtime

rocm_dist = tmp_dir / "runtime_preflight" / "dist" / "rocm"
(rocm_dist / "bin").mkdir(parents=True)
(rocm_dist / "lib").mkdir(parents=True)
device_root = tmp_dir / "runtime_devices"
(device_root / "dev").mkdir(parents=True)

os.environ["THEROCK_RUNTIME_KIND"] = "wsl2"
os.environ["THEROCK_RUNTIME_DEVICE_ROOT"] = str(device_root)
os.environ.pop("THEROCK_ALLOW_MISSING_WSL_DXG", None)

runtime = detect_rocm_runtime()
state = {
    "meta": {
        "rocm_dist": str(rocm_dist),
        "mock_command": "",
        "sudo_policy": "",
    },
    "runtime_summary": {
        "runtime_label": runtime["runtime_label"],
        "rocm_runtime": runtime,
    },
}
env = {
    "THEROCK_BIN_DIR": str(rocm_dist / "bin"),
    "OUTPUT_ARTIFACTS_DIR": str(rocm_dist),
    "ROCM_PATH": str(rocm_dist),
    "HIP_PATH": str(rocm_dist),
}

assert runtime["runtime_label"] == "wsl2-missing-dxg", json.dumps(runtime, indent=2)
blocked = check_task_preflight(state, {}, env, {})
assert blocked and blocked.startswith("missing_wsl_dxg:"), blocked

(device_root / "dev" / "dxg").touch()
runtime = detect_rocm_runtime()
state["runtime_summary"] = {
    "runtime_label": runtime["runtime_label"],
    "rocm_runtime": runtime,
}
assert runtime["runtime_label"] == "wsl2-dxg", json.dumps(runtime, indent=2)
blocked = check_task_preflight(state, {}, env, {})
assert blocked and blocked.startswith("missing_wsl_rocdxg:"), blocked

(rocm_dist / "lib" / "librocdxg.so").touch()
runtime = detect_rocm_runtime(rocm_dist)
state["runtime_summary"] = {
    "runtime_label": runtime["runtime_label"],
    "rocm_runtime": runtime,
}
assert runtime["rocm_library_integrity"]["librocdxg"]["found"]
assert check_task_preflight(state, {}, env, {}) is None
PY

echo "[test] auto bootstrap prepares host dependencies"
FAKE_BOOTSTRAP_BIN="${TMP_DIR}/fake_bootstrap_bin"
FAKE_BOOTSTRAP_REPO="${TMP_DIR}/fake_bootstrap_therock"
FAKE_BOOTSTRAP_LOG="${TMP_DIR}/fake_bootstrap_commands.log"
mkdir -p \
  "${FAKE_BOOTSTRAP_BIN}" \
  "${FAKE_BOOTSTRAP_REPO}/build_tools/github_actions/test_executable_scripts" \
  "${TMP_DIR}/bootstrap_artifacts/dist/rocm/bin" \
  "${TMP_DIR}/bootstrap_artifacts/dist/rocm/lib"
touch "${TMP_DIR}/bootstrap_artifacts/dist/rocm/lib/librocdxg.so"
touch "${FAKE_BOOTSTRAP_REPO}/requirements.txt"
touch "${FAKE_BOOTSTRAP_REPO}/requirements-test.txt"

cat >"${FAKE_BOOTSTRAP_BIN}/sudo" <<'SH'
#!/usr/bin/env bash
set -euo pipefail
echo "sudo $*" >> "${THEROCK_FAKE_BOOTSTRAP_LOG}"
if [ "${1:-}" = "-n" ] || [ "${1:-}" = "-A" ]; then
  shift
fi
if [ "${1:-}" = "true" ]; then
  exit 0
fi
exec "$@"
SH
chmod +x "${FAKE_BOOTSTRAP_BIN}/sudo"

cat >"${FAKE_BOOTSTRAP_BIN}/apt" <<'SH'
#!/usr/bin/env bash
set -euo pipefail
echo "apt $*" >> "${THEROCK_FAKE_BOOTSTRAP_LOG}"
exit 0
SH
chmod +x "${FAKE_BOOTSTRAP_BIN}/apt"

for command_name in cmake ctest ninja g++ pkg-config; do
  cat >"${FAKE_BOOTSTRAP_BIN}/${command_name}" <<'SH'
#!/usr/bin/env bash
exit 0
SH
  chmod +x "${FAKE_BOOTSTRAP_BIN}/${command_name}"
done

cat >"${FAKE_BOOTSTRAP_BIN}/bootstrap-python3" <<'SH'
#!/usr/bin/env bash
set -euo pipefail
echo "bootstrap-python3 $*" >> "${THEROCK_FAKE_BOOTSTRAP_LOG}"
if [ "${1:-}" = "-m" ] && [ "${2:-}" = "venv" ]; then
  venv_dir="${3:?missing venv dir}"
  mkdir -p "${venv_dir}/bin"
  cat >"${venv_dir}/bin/python" <<'PYSH'
#!/usr/bin/env bash
set -euo pipefail
echo "venv-python $*" >> "${THEROCK_FAKE_BOOTSTRAP_LOG}"
if [ "${1:-}" = "-m" ] && [ "${2:-}" = "pip" ]; then
  exit 0
fi
if [ "${1:-}" = "-c" ]; then
  echo "boto3 ok"
  exit 0
fi
exit 0
PYSH
  chmod +x "${venv_dir}/bin/python"
  exit 0
fi
exit 0
SH
chmod +x "${FAKE_BOOTSTRAP_BIN}/bootstrap-python3"

cat >"${FAKE_BOOTSTRAP_REPO}/build_tools/github_actions/test_executable_scripts/test_runner.py" <<'PY'
import os

assert os.environ["TEST_COMPONENT"] == "hiprand"
assert os.environ["TEST_TYPE"] == "quick"
print("bootstrap test runner ok")
PY

cat >"${TMP_DIR}/bootstrap_component_sort_order.json" <<'JSON'
{
  "version": "bootstrap-test",
  "entries": [
    {"test_type": "quick", "component": "hiprand", "duration_ref": 1, "category": "medium", "status": "pass", "sort_order": 1, "gpu_hang_risk": false}
  ]
}
JSON

PATH="${FAKE_BOOTSTRAP_BIN}:${PATH}" \
THEROCK_FAKE_BOOTSTRAP_LOG="${FAKE_BOOTSTRAP_LOG}" \
THEROCK_BOOTSTRAP_PYTHON="${FAKE_BOOTSTRAP_BIN}/bootstrap-python3" \
"${AGENT}" run \
  --therock-repo "${FAKE_BOOTSTRAP_REPO}" \
  --artifacts "${TMP_DIR}/bootstrap_artifacts" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/bootstrap_component_sort_order.json" \
  --components hiprand \
  --test-types quick \
  --output-root "${TMP_DIR}/bootstrap_runs" \
  --sudo-policy cache \
  --bootstrap-env auto \
  --stable-threshold 1 \
  --max-rounds 1

BOOTSTRAP_RUN_DIRS=("${TMP_DIR}"/bootstrap_runs/*)
BOOTSTRAP_RUN_DIR="${BOOTSTRAP_RUN_DIRS[0]}"
python3 - "${BOOTSTRAP_RUN_DIR}" "${FAKE_BOOTSTRAP_LOG}" <<'PY'
import json
from pathlib import Path
import sys

run_dir = Path(sys.argv[1])
fake_log = Path(sys.argv[2]).read_text(encoding="utf-8")
state = json.load(open(run_dir / "global_state.json", encoding="utf-8"))
summary = json.load(open(run_dir / "summary.json", encoding="utf-8"))
bootstrap = json.load(open(run_dir / "bootstrap" / "bootstrap_env.json", encoding="utf-8"))
bootstrap_log = (run_dir / "bootstrap" / "bootstrap_env.log").read_text(encoding="utf-8")

assert state["final_status"] == "passed", state["final_status"]
assert state["bootstrap"]["status"] == "completed", state["bootstrap"]
assert summary["bootstrap"]["status"] == "completed", summary["bootstrap"]
assert bootstrap["status"] == "completed", bootstrap
assert bootstrap["venv"]["requirements_installed"] is True, bootstrap
assert bootstrap["venv"]["boto3_import"] is True, bootstrap
assert "apt update" in fake_log, fake_log
assert "apt install -y" in fake_log, fake_log
assert "bootstrap-python3 -m venv" in fake_log, fake_log
assert "pip install -r requirements.txt" in bootstrap_log, bootstrap_log
assert "pip install -r requirements.txt -r requirements-test.txt" in bootstrap_log, bootstrap_log
assert bootstrap["venv"]["requirements_test_installed"] is True, bootstrap
assert "boto3 ok" in bootstrap_log, bootstrap_log
assert summary["artifacts"]["bootstrap_summary"].endswith("bootstrap/bootstrap_env.json")
PY

echo "[test] WSL2 missing /dev/dxg blocks before execution"
cat >"${TMP_DIR}/missing_dxg_component_sort_order.json" <<'JSON'
{
  "version": "missing-dxg-test",
  "entries": [
    {"test_type": "standard", "component": "amdsmi", "duration_ref": 1, "category": "medium", "status": "pass", "sort_order": 1, "gpu_hang_risk": false}
  ]
}
JSON
mkdir -p "${TMP_DIR}/missing_dxg_devices/dev"

THEROCK_RUNTIME_KIND=wsl2 \
THEROCK_RUNTIME_DEVICE_ROOT="${TMP_DIR}/missing_dxg_devices" \
THEROCK_ALLOW_MISSING_WSL_DXG= \
"${AGENT}" run \
  "${RUN_BOOTSTRAP_OFF[@]}" \
  --artifacts "${TMP_DIR}/output/build" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/missing_dxg_component_sort_order.json" \
  --components amdsmi \
  --test-types standard \
  --output-root "${TMP_DIR}/missing_dxg_runs" \
  --stable-threshold 1 \
  --max-rounds 1 >"${TMP_DIR}/missing_dxg_agent.out"

MISSING_DXG_RUN_DIRS=("${TMP_DIR}"/missing_dxg_runs/*)
MISSING_DXG_RUN_DIR="${MISSING_DXG_RUN_DIRS[0]}"
python3 - "${MISSING_DXG_RUN_DIR}" "${TMP_DIR}/missing_dxg_agent.out" <<'PY'
import json
from pathlib import Path
import sys

run_dir = Path(sys.argv[1])
agent_out = Path(sys.argv[2]).read_text(encoding="utf-8")
state = json.load(open(run_dir / "global_state.json", encoding="utf-8"))
summary = json.load(open(run_dir / "summary.json", encoding="utf-8"))
failures = json.load(open(run_dir / "failures.json", encoding="utf-8"))
failure = json.load(open(run_dir / "failures" / "amdsmi-standard_failure.json", encoding="utf-8"))
environment = json.load(open(run_dir / "environment_summary.json", encoding="utf-8"))
progress = (run_dir / "progress.jsonl").read_text(encoding="utf-8")
activity = (run_dir / "agent_activity.jsonl").read_text(encoding="utf-8")
tool_calls = (run_dir / "tool_calls.jsonl").read_text(encoding="utf-8")
stderr_log = (run_dir / "logs" / "amdsmi-standard.round1.stderr.log").read_text(encoding="utf-8")

result = state["results"]["task_results"]["amdsmi-standard"]
assert state["final_status"] == "failed", state["final_status"]
assert result["status"] == "blocked", result
assert result["return_code"] == 125, result
assert result["failure_summary"].startswith("missing_wsl_dxg:"), result["failure_summary"]
assert "missing_wsl_dxg:" in stderr_log, stderr_log
assert summary["runtime_label"] == "wsl2-missing-dxg", summary["runtime_label"]
assert failures["runtime_label"] == "wsl2-missing-dxg", failures["runtime_label"]
assert failure["runtime_label"] == "wsl2-missing-dxg", failure["runtime_label"]
assert failure["task"]["runtime_label"] == "wsl2-missing-dxg", failure["task"]
assert environment["runtime_label"] == "wsl2-missing-dxg", environment["runtime_label"]
assert environment["runtime_summary"]["rocm_runtime"]["gpu_devices"]["/dev/dxg"]["exists"] is False
assert '"runtime_label": "wsl2-missing-dxg"' in progress, progress
assert '"runtime_label": "wsl2-missing-dxg"' in activity, activity
assert '"runtime_label": "wsl2-missing-dxg"' in tool_calls, tool_calls
assert "runtime=wsl2-missing-dxg" in agent_out, agent_out
PY

echo "[test] WSL2 missing librocdxg blocks before execution"
cat >"${TMP_DIR}/missing_rocdxg_component_sort_order.json" <<'JSON'
{
  "version": "missing-rocdxg-test",
  "entries": [
    {"test_type": "standard", "component": "amdsmi", "duration_ref": 1, "category": "medium", "status": "pass", "sort_order": 1, "gpu_hang_risk": false}
  ]
}
JSON
mkdir -p \
  "${TMP_DIR}/missing_rocdxg_devices/dev" \
  "${TMP_DIR}/missing_rocdxg_artifacts/dist/rocm/bin" \
  "${TMP_DIR}/missing_rocdxg_artifacts/dist/rocm/lib"
touch "${TMP_DIR}/missing_rocdxg_devices/dev/dxg"

THEROCK_RUNTIME_KIND=wsl2 \
THEROCK_RUNTIME_DEVICE_ROOT="${TMP_DIR}/missing_rocdxg_devices" \
THEROCK_ROCDXG_SEARCH_PATHS="${TMP_DIR}/missing_rocdxg_artifacts/dist/rocm/lib" \
THEROCK_ROCDXG_SEARCH_PATHS_ONLY=1 \
"${AGENT}" run \
  "${RUN_BOOTSTRAP_OFF[@]}" \
  --artifacts "${TMP_DIR}/missing_rocdxg_artifacts" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/missing_rocdxg_component_sort_order.json" \
  --components amdsmi \
  --test-types standard \
  --output-root "${TMP_DIR}/missing_rocdxg_runs" \
  --stable-threshold 1 \
  --max-rounds 1 >"${TMP_DIR}/missing_rocdxg_agent.out"

MISSING_ROCDXG_RUN_DIRS=("${TMP_DIR}"/missing_rocdxg_runs/*)
MISSING_ROCDXG_RUN_DIR="${MISSING_ROCDXG_RUN_DIRS[0]}"
python3 - "${MISSING_ROCDXG_RUN_DIR}" "${TMP_DIR}/missing_rocdxg_agent.out" <<'PY'
import json
from pathlib import Path
import sys

run_dir = Path(sys.argv[1])
agent_out = Path(sys.argv[2]).read_text(encoding="utf-8")
state = json.load(open(run_dir / "global_state.json", encoding="utf-8"))
summary = json.load(open(run_dir / "summary.json", encoding="utf-8"))
failure = json.load(open(run_dir / "failures" / "amdsmi-standard_failure.json", encoding="utf-8"))
environment = json.load(open(run_dir / "environment_summary.json", encoding="utf-8"))
stderr_log = (run_dir / "logs" / "amdsmi-standard.round1.stderr.log").read_text(encoding="utf-8")

result = state["results"]["task_results"]["amdsmi-standard"]
integrity = environment["runtime_summary"]["rocm_runtime"]["rocm_library_integrity"]

assert state["final_status"] == "failed", state["final_status"]
assert result["status"] == "blocked", result
assert result["failure_summary"].startswith("missing_wsl_rocdxg:"), result["failure_summary"]
assert "missing_wsl_rocdxg:" in stderr_log, stderr_log
assert summary["runtime_label"] == "wsl2-dxg", summary["runtime_label"]
assert failure["task"]["runtime_label"] == "wsl2-dxg", failure["task"]
assert integrity["status"] == "incomplete", integrity
assert "librocdxg.so" in integrity["missing"], integrity
assert not integrity["librocdxg"]["found"], integrity
assert "runtime=wsl2-dxg" in agent_out, agent_out
PY

echo "[test] run loop with risk skip"
"${AGENT}" run \
  "${RUN_BOOTSTRAP_OFF[@]}" \
  --artifacts "${TMP_DIR}/output/build" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/component_sort_order.json" \
  --test-types quick \
  --output-root "${TMP_DIR}/runs" \
  --mock-command "bash ${TMP_DIR}/mock_runner.sh {task_id}" \
  --stable-threshold 1 \
  --max-rounds 3

RUN_DIR="$(find "${TMP_DIR}/runs" -mindepth 1 -maxdepth 1 -type d | sort | head -n 1)"
STATE_FILE="${RUN_DIR}/global_state.json"
SUMMARY_FILE="${RUN_DIR}/summary.json"
FAILURES_FILE="${RUN_DIR}/failures.json"
FAILURE_FILE="${RUN_DIR}/failures/fail_component-quick_failure.json"
ACTIVITY_FILE="${RUN_DIR}/agent_activity.jsonl"
TOOL_CALLS_FILE="${RUN_DIR}/tool_calls.jsonl"
ENVIRONMENT_FILE="${RUN_DIR}/environment_summary.json"
GLOBAL_AUDIT_FILE="${TMP_DIR}/runs/_audit/agent_invocations.jsonl"
ROUND1_INPUTS_FILE="${RUN_DIR}/round_analysis/round1_inputs.json"
ROUND1_FAILURE_INDEX_FILE="${RUN_DIR}/debug/round1_failure_index.json"
ROUND2_INPUTS_FILE="${RUN_DIR}/round_analysis/round2_inputs.json"
ROUND2_FAILURE_INDEX_FILE="${RUN_DIR}/debug/round2_failure_index.json"

test -f "${STATE_FILE}"
test -f "${SUMMARY_FILE}"
test -f "${FAILURES_FILE}"
test -f "${FAILURE_FILE}"
test -f "${ACTIVITY_FILE}"
test -f "${TOOL_CALLS_FILE}"
test -f "${ENVIRONMENT_FILE}"
test -f "${GLOBAL_AUDIT_FILE}"
test -f "${ROUND1_INPUTS_FILE}"
test -f "${ROUND1_FAILURE_INDEX_FILE}"
test -f "${ROUND2_INPUTS_FILE}"
test -f "${ROUND2_FAILURE_INDEX_FILE}"
test ! -f "${RUN_DIR}/round_analysis/round1.json"
test ! -f "${RUN_DIR}/round_analysis/round1.md"
test ! -f "${RUN_DIR}/debug/round1_log_excerpt.md"

python3 - "${STATE_FILE}" "${RUN_DIR}" <<'PY'
import json
from pathlib import Path
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
run_dir = Path(sys.argv[2])
results = state["results"]["task_results"]
summary = json.load(open(run_dir / "summary.json", encoding="utf-8"))
failures = json.load(open(run_dir / "failures.json", encoding="utf-8"))
failure = json.load(open(run_dir / "failures" / "fail_component-quick_failure.json", encoding="utf-8"))
environment = json.load(open(run_dir / "environment_summary.json", encoding="utf-8"))
round1_inputs = json.load(open(run_dir / "round_analysis" / "round1_inputs.json", encoding="utf-8"))
round1_index = json.load(open(run_dir / "debug" / "round1_failure_index.json", encoding="utf-8"))
round2_inputs = json.load(open(run_dir / "round_analysis" / "round2_inputs.json", encoding="utf-8"))
round2_index = json.load(open(run_dir / "debug" / "round2_failure_index.json", encoding="utf-8"))

assert state["final_status"] == "failed", state["final_status"]
assert results["pass_component-quick"]["status"] == "pass"
assert results["fail_component-quick"]["status"] == "fail"
assert results["risk_component-quick"]["status"] == "skip"
assert results["exclude_component-quick"]["status"] == "skip"
assert summary["status"] == "failed"
assert summary["counts"]["pass"] == 1
assert summary["counts"]["fail"] == 1
assert summary["artifacts"]["summary_json"].endswith("summary.json")
assert summary["runtime_label"]
assert summary["runtime_summary"]["rocm_runtime"]["gpu_devices"]["/dev/dxg"]["expected_on_wsl2"] is True
assert summary["reporter_note"].startswith("Markdown summaries are generated")
assert failures["runtime_label"] == summary["runtime_label"]
assert failures["failures"][0]["task_id"] == "fail_component-quick"
assert failure["runtime_label"] == summary["runtime_label"]
assert failure["runtime_summary"]["runtime_label"] == summary["runtime_label"]
assert failure["task"]["failure_evidence"]["kind"] == "runner_evidence"
assert failure["task"]["failure_evidence"]["missing_python_modules"] == ["prettytable"]
assert environment["runtime_label"] == summary["runtime_label"]
assert state["meta"]["runtime_label"] == summary["runtime_label"]
assert results["fail_component-quick"]["runtime_label"] == summary["runtime_label"]
assert state["loop"]["stable_failed_count"] == 1
assert state["schedule"]["failed_tasks"] == ["fail_component-quick"]
assert state["schedule"]["failed_tasks_this_round"] == ["fail_component-quick"]
assert state["schedule"]["blocked_tasks_this_round"] == []
assert state["schedule"]["round_failed_tasks"] == ["fail_component-quick"]
assert round1_inputs["round"] == 1
assert round1_inputs["failed_tasks"][0]["task_id"] == "fail_component-quick"
assert round1_inputs["failed_tasks"][0]["stdout_log"] == "logs/fail_component-quick.round1.stdout.log"
assert round1_inputs["blocked_tasks"] == []
assert round1_index["round_failed_task_ids"] == ["fail_component-quick"]
assert round2_inputs["round"] == 2
assert round2_inputs["failed_tasks"][0]["stdout_log"] == "logs/fail_component-quick.round2.stdout.log"
assert round2_index["failed_task_ids"] == ["fail_component-quick"]
PY

grep -q '"event": "task_start"' "${ACTIVITY_FILE}"
grep -q '"event": "task_end"' "${ACTIVITY_FILE}"
grep -q '"event": "report_generated"' "${ACTIVITY_FILE}"
grep -q '"runtime_label":' "${ACTIVITY_FILE}"
grep -q '"tool": "shell"' "${TOOL_CALLS_FILE}"
grep -q '"runtime_label":' "${TOOL_CALLS_FILE}"
grep -q '"event": "invocation_start"' "${GLOBAL_AUDIT_FILE}"
grep -q '"event": "invocation_end"' "${GLOBAL_AUDIT_FILE}"
grep -q '"event": "round_failure_index_written"' "${RUN_DIR}/progress.jsonl"
grep -q '"runtime_label":' "${RUN_DIR}/progress.jsonl"
! grep -q '"event": "auto_debug_start"' "${RUN_DIR}/progress.jsonl"
! grep -q '"event": "auto_debug_end"' "${RUN_DIR}/progress.jsonl"

echo "[test] opencode debug handoff"
"${AGENT}" run \
  "${RUN_BOOTSTRAP_OFF[@]}" \
  --artifacts "${TMP_DIR}/output/build" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/component_sort_order.json" \
  --components fail_component \
  --test-types quick \
  --output-root "${TMP_DIR}/opencode_handoff_runs" \
  --mock-command "bash ${TMP_DIR}/mock_runner.sh {task_id}" \
  --stable-threshold 1 \
  --max-rounds 3 \
  --debug-repair opencode

OPENCODE_HANDOFF_RUN_DIR="$(find "${TMP_DIR}/opencode_handoff_runs" -mindepth 1 -maxdepth 1 -type d | sort | head -n 1)"
python3 - "${OPENCODE_HANDOFF_RUN_DIR}/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))

assert state["final_status"] == "waiting_for_opencode_debug", state["final_status"]
assert state["schedule"]["current_loop"] == 1
assert state["schedule"]["next_tasks"] == ["fail_component-quick"]
assert state["debug_repair"]["mode"] == "opencode"
assert state["debug_repair"]["last_failed_round"] == 1
assert state["debug_repair"]["last_inputs"] == "round_analysis/round1_inputs.json"
assert state["debug_repair"]["last_failure_index"] == "debug/round1_failure_index.json"
PY
test -f "${OPENCODE_HANDOFF_RUN_DIR}/round_analysis/round1_inputs.json"
test -f "${OPENCODE_HANDOFF_RUN_DIR}/debug/round1_failure_index.json"
test ! -f "${OPENCODE_HANDOFF_RUN_DIR}/round_analysis/round1.json"
test ! -f "${OPENCODE_HANDOFF_RUN_DIR}/debug/round1_log_excerpt.md"
grep -q '"event": "waiting_for_opencode_debug"' "${OPENCODE_HANDOFF_RUN_DIR}/progress.jsonl"

echo "[test] background start/status"
"${AGENT}" start-kv \
  "run_id=background_case" \
  "artifacts=${TMP_DIR}/output/build" \
  "gpu=gfx1151" \
  "component_config=${TMP_DIR}/component_sort_order.json" \
  "components=pass_component" \
  "test_types=quick" \
  "output_root=${TMP_DIR}/background_runs" \
  "mock_command=bash ${TMP_DIR}/mock_runner.sh {task_id}" \
  "stable_threshold=1" \
  "max_rounds=1" >"${TMP_DIR}/background_start.out"

grep -q "run_id=background_case" "${TMP_DIR}/background_start.out"
test -f "${TMP_DIR}/background_runs/background_case/runner.pid.json"
test -f "${TMP_DIR}/background_runs/background_case/progress.jsonl"

for _ in 1 2 3 4 5 6 7 8 9 10; do
  if python3 - "${TMP_DIR}/background_runs/background_case/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
raise SystemExit(0 if state["final_status"] != "running" else 1)
PY
  then
    break
  fi
  sleep 0.2
done

"${AGENT}" status background_case \
  --output-root "${TMP_DIR}/background_runs" >"${TMP_DIR}/background_status.out"
"${AGENT}" status run_id=background_case \
  --output-root "${TMP_DIR}/background_runs" >"${TMP_DIR}/background_status_kv.out"
"${AGENT}" status background_case \
  --output-root "${TMP_DIR}/background_runs" \
  --format brief >"${TMP_DIR}/background_status_brief.out"
"${AGENT}" report run_id=background_case \
  --output-root "${TMP_DIR}/background_runs" >"${TMP_DIR}/background_report_kv.out"
"${AGENT}" status \
  --output-root "${TMP_DIR}/background_runs" >"${TMP_DIR}/background_status_list.out"

grep -q "status: passed" "${TMP_DIR}/background_status.out"
grep -q "status: passed" "${TMP_DIR}/background_status_kv.out"
grep -q "progress: 1/1" "${TMP_DIR}/background_status.out"
grep -q "passed|1|1/1" "${TMP_DIR}/background_status_brief.out"
grep -q "summary.json" "${TMP_DIR}/background_report_kv.out"
grep -q "background_case" "${TMP_DIR}/background_status_list.out"
grep -q '"event": "background_started"' "${TMP_DIR}/background_runs/background_case/progress.jsonl"
grep -q '"event": "task_end"' "${TMP_DIR}/background_runs/background_case/progress.jsonl"

echo "[test] background stop"
"${AGENT}" start-kv \
  "run_id=stop_case" \
  "artifacts=${TMP_DIR}/output/build" \
  "gpu=gfx1151" \
  "component_config=${TMP_DIR}/component_sort_order.json" \
  "components=pass_component" \
  "test_types=quick" \
  "output_root=${TMP_DIR}/stop_runs" \
  "mock_command=python3 -c 'import time; time.sleep(30)'" \
  "stable_threshold=1" \
  "max_rounds=1" >"${TMP_DIR}/stop_start.out"

for _ in 1 2 3 4 5 6 7 8 9 10; do
  if grep -q '"event": "task_start"' "${TMP_DIR}/stop_runs/stop_case/progress.jsonl"; then
    break
  fi
  sleep 0.2
done

"${AGENT}" stop run_id=stop_case \
  --output-root "${TMP_DIR}/stop_runs" \
  --timeout 2 >"${TMP_DIR}/stop.out"

grep -q "stopped run_id=stop_case" "${TMP_DIR}/stop.out"
python3 - "${TMP_DIR}/stop_runs/stop_case/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
assert state["final_status"] == "interrupted", state["final_status"]
assert state["runtime"]["interrupt_reason"] in {"stop_requested", "signal:15"}
PY

echo "[test] sudo cache policy does not block non-sudo tasks"
"${AGENT}" run \
  "${RUN_BOOTSTRAP_OFF[@]}" \
  --artifacts "${TMP_DIR}/output/build" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/component_sort_order.json" \
  --components pass_component \
  --test-types quick \
  --output-root "${TMP_DIR}/sudo_cache_non_sudo_runs" \
  --mock-command "bash ${TMP_DIR}/mock_runner.sh {task_id}" \
  --sudo-policy cache \
  --stable-threshold 1 \
  --max-rounds 1

SUDO_CACHE_NON_SUDO_RUN_DIR="$(find "${TMP_DIR}/sudo_cache_non_sudo_runs" -mindepth 1 -maxdepth 1 -type d | sort | head -n 1)"
python3 - "${SUDO_CACHE_NON_SUDO_RUN_DIR}/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
result = state["results"]["task_results"]["pass_component-quick"]

assert state["final_status"] == "passed", state["final_status"]
assert result["status"] == "pass"
assert state["meta"]["sudo_policy"] == "cache"
PY

echo "[test] init and resume"
"${AGENT}" init \
  --run-id resume_case \
  --artifacts "${TMP_DIR}/output/build" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/component_sort_order.json" \
  --components pass_component \
  --test-types quick \
  --output-root "${TMP_DIR}/resume_runs" \
  --mock-command "bash ${TMP_DIR}/mock_runner.sh {task_id}"

"${AGENT}" resume run_id=resume_case \
  --output-root "${TMP_DIR}/resume_runs" \
  --mock-command "bash ${TMP_DIR}/mock_runner.sh {task_id}"

python3 - "${TMP_DIR}/resume_runs/resume_case/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
assert state["resume_count"] == 1
assert state["final_status"] == "passed"
assert state["results"]["task_results"]["pass_component-quick"]["status"] == "pass"
PY

echo "[test] official exclude and sudo preflight"
cat >"${TMP_DIR}/official_exclude_component_sort_order.json" <<'JSON'
{
  "version": "test",
  "entries": [
    {"test_type": "quick", "component": "hipsparselt", "duration_ref": 1, "category": "lightweight", "status": "pass", "sort_order": 1, "gpu_hang_risk": false},
    {"test_type": "quick", "component": "rocprofiler_compute", "duration_ref": 1, "category": "lightweight", "status": "pass", "sort_order": 2, "gpu_hang_risk": false}
  ]
}
JSON

"${AGENT}" run \
  "${RUN_BOOTSTRAP_OFF[@]}" \
  --artifacts "${TMP_DIR}/output/build" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/official_exclude_component_sort_order.json" \
  --components hipsparselt,rocprofiler_compute \
  --test-types quick \
  --output-root "${TMP_DIR}/official_exclude_runs" \
  --mock-command "echo should-not-run-{task_id}" \
  --stable-threshold 1 \
  --max-rounds 1

OFFICIAL_EXCLUDE_RUN_DIR="$(find "${TMP_DIR}/official_exclude_runs" -mindepth 1 -maxdepth 1 -type d | sort | head -n 1)"
python3 - "${OFFICIAL_EXCLUDE_RUN_DIR}/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
results = state["results"]["task_results"]

assert state["final_status"] == "passed", state["final_status"]
assert results["hipsparselt-quick"]["status"] == "skip"
assert results["hipsparselt-quick"]["official_exclude"]["known_issue_category"] == "gfx1151_exclude_family"
assert results["rocprofiler_compute-quick"]["status"] == "skip"
assert results["rocprofiler_compute-quick"]["official_exclude"]["known_issue_category"] == "no_independent_entrypoint"
PY

python3 - "${OFFICIAL_EXCLUDE_RUN_DIR}/summary.json" <<'PY'
import json
import sys

summary = json.load(open(sys.argv[1], encoding="utf-8"))
tasks = {task["task_id"]: task for task in summary["tasks"]}

assert tasks["hipsparselt-quick"]["official_exclude"]["known_issue_category"] == "gfx1151_exclude_family"
assert tasks["rocprofiler_compute-quick"]["official_exclude"]["known_issue_category"] == "no_independent_entrypoint"
PY

cat >"${TMP_DIR}/sudo_component_sort_order.json" <<'JSON'
{
  "version": "test",
  "entries": [
    {"test_type": "standard", "component": "amdsmi", "duration_ref": 1, "category": "lightweight", "status": "pass", "sort_order": 1, "gpu_hang_risk": false}
  ]
}
JSON

"${AGENT}" run \
  "${RUN_BOOTSTRAP_OFF[@]}" \
  --artifacts "${TMP_DIR}/output/build" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/sudo_component_sort_order.json" \
  --components amdsmi \
  --test-types standard \
  --output-root "${TMP_DIR}/sudo_runs" \
  --mock-command "echo should-not-run-{task_id}" \
  --sudo-policy none \
  --stable-threshold 1 \
  --max-rounds 2

SUDO_RUN_DIR="$(find "${TMP_DIR}/sudo_runs" -mindepth 1 -maxdepth 1 -type d | sort | head -n 1)"
python3 - "${SUDO_RUN_DIR}/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
result = state["results"]["task_results"]["amdsmi-standard"]

assert state["final_status"] == "failed", state["final_status"]
assert result["status"] == "blocked"
assert "sudo_unavailable" in result["failure_summary"]
assert result["entrypoint_type"] == "dedicated_python"
PY

grep -q "sudo_unavailable" "${SUDO_RUN_DIR}/failures/amdsmi-standard_failure.json"

FAKE_SUDO_FAIL_DIR="${TMP_DIR}/fake_sudo_fail"
mkdir -p "${FAKE_SUDO_FAIL_DIR}"
cat >"${FAKE_SUDO_FAIL_DIR}/sudo" <<SH
#!/usr/bin/env bash
printf '%s\n' "\$*" >> "${TMP_DIR}/fake_sudo_fail.log"
exit 1
SH
chmod +x "${FAKE_SUDO_FAIL_DIR}/sudo"

PATH="${FAKE_SUDO_FAIL_DIR}:${PATH}" "${AGENT}" run \
  "${RUN_BOOTSTRAP_OFF[@]}" \
  --artifacts "${TMP_DIR}/output/build" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/sudo_component_sort_order.json" \
  --components amdsmi \
  --test-types standard \
  --output-root "${TMP_DIR}/sudo_cache_fail_runs" \
  --mock-command "echo should-not-run-{task_id}" \
  --sudo-policy cache \
  --stable-threshold 1 \
  --max-rounds 2

SUDO_CACHE_FAIL_RUN_DIR="$(find "${TMP_DIR}/sudo_cache_fail_runs" -mindepth 1 -maxdepth 1 -type d | sort | head -n 1)"
python3 - "${SUDO_CACHE_FAIL_RUN_DIR}/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
result = state["results"]["task_results"]["amdsmi-standard"]

assert state["final_status"] == "failed", state["final_status"]
assert result["status"] == "blocked"
assert "sudo_unavailable" in result["failure_summary"]
assert result["command"] == "blocked before execution"
PY
grep -q -- "-n true" "${TMP_DIR}/fake_sudo_fail.log"

FAKE_SUDO_OK_DIR="${TMP_DIR}/fake_sudo_ok"
mkdir -p "${FAKE_SUDO_OK_DIR}"
cat >"${FAKE_SUDO_OK_DIR}/sudo" <<SH
#!/usr/bin/env bash
printf '%s\n' "\$*" >> "${TMP_DIR}/fake_sudo_ok.log"
exit 0
SH
chmod +x "${FAKE_SUDO_OK_DIR}/sudo"

PATH="${FAKE_SUDO_OK_DIR}:${PATH}" "${AGENT}" run \
  "${RUN_BOOTSTRAP_OFF[@]}" \
  --artifacts "${TMP_DIR}/output/build" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/sudo_component_sort_order.json" \
  --components amdsmi \
  --test-types standard \
  --output-root "${TMP_DIR}/sudo_cache_ok_runs" \
  --mock-command "echo sudo-sensitive-ran-{task_id}" \
  --sudo-policy cache \
  --stable-threshold 1 \
  --max-rounds 1

SUDO_CACHE_OK_RUN_DIR="$(find "${TMP_DIR}/sudo_cache_ok_runs" -mindepth 1 -maxdepth 1 -type d | sort | head -n 1)"
python3 - "${SUDO_CACHE_OK_RUN_DIR}/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
result = state["results"]["task_results"]["amdsmi-standard"]

assert state["final_status"] == "passed", state["final_status"]
assert result["status"] == "pass"
assert result["command"].startswith("echo sudo-sensitive-ran-")
PY
grep -q -- "-n true" "${TMP_DIR}/fake_sudo_ok.log"
grep -q "sudo-sensitive-ran-amdsmi-standard" "${SUDO_CACHE_OK_RUN_DIR}/logs/amdsmi-standard.round1.stdout.log"

FAKE_ASKPASS="${TMP_DIR}/fake_askpass.sh"
cat >"${FAKE_ASKPASS}" <<SH
#!/usr/bin/env bash
printf '%s\n' "askpass-called" >> "${TMP_DIR}/fake_askpass.log"
printf '%s\n' "fake-password"
SH
chmod +x "${FAKE_ASKPASS}"

FAKE_SUDO_ASKPASS_DIR="${TMP_DIR}/fake_sudo_askpass"
mkdir -p "${FAKE_SUDO_ASKPASS_DIR}"
cat >"${FAKE_SUDO_ASKPASS_DIR}/sudo" <<SH
#!/usr/bin/env bash
printf '%s\n' "\$*" >> "${TMP_DIR}/fake_sudo_askpass.log"
if [ -n "\${SUDO_ASKPASS:-}" ]; then
  "\${SUDO_ASKPASS}" >/dev/null
fi
if [ "\${1:-}" = "-A" ]; then
  shift
fi
if [ "\${1:-}" = "true" ]; then
  exit 0
fi
exec "\$@"
SH
chmod +x "${FAKE_SUDO_ASKPASS_DIR}/sudo"

PATH="${FAKE_SUDO_ASKPASS_DIR}:${PATH}" \
THEROCK_SUDO_ASKPASS="${FAKE_ASKPASS}" \
"${AGENT}" run \
  "${RUN_BOOTSTRAP_OFF[@]}" \
  --artifacts "${TMP_DIR}/output/build" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/sudo_component_sort_order.json" \
  --components amdsmi \
  --test-types standard \
  --output-root "${TMP_DIR}/sudo_askpass_runs" \
  --mock-command "sudo echo sudo-askpass-ran-{task_id}" \
  --sudo-policy askpass \
  --stable-threshold 1 \
  --max-rounds 1

SUDO_ASKPASS_RUN_DIR="$(find "${TMP_DIR}/sudo_askpass_runs" -mindepth 1 -maxdepth 1 -type d | sort | head -n 1)"
python3 - "${SUDO_ASKPASS_RUN_DIR}/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
result = state["results"]["task_results"]["amdsmi-standard"]

assert state["final_status"] == "passed", state["final_status"]
assert result["status"] == "pass"
assert result["command"].startswith("sudo echo sudo-askpass-ran-")
PY
grep -q -- "-A true" "${TMP_DIR}/fake_sudo_askpass.log"
grep -q -- "-A echo sudo-askpass-ran-amdsmi-standard" "${TMP_DIR}/fake_sudo_askpass.log"
grep -q "askpass-called" "${TMP_DIR}/fake_askpass.log"
grep -q "sudo-askpass-ran-amdsmi-standard" "${SUDO_ASKPASS_RUN_DIR}/logs/amdsmi-standard.round1.stdout.log"

echo "[test] native index-driven execution"
FAKE_THEROCK="${TMP_DIR}/TheRock"
FAKE_SCRIPTS="${FAKE_THEROCK}/build_tools/github_actions/test_executable_scripts"
mkdir -p "${FAKE_SCRIPTS}"

cat >"${TMP_DIR}/native_component_sort_order.json" <<'JSON'
{
  "version": "test",
  "entries": [
    {"test_type": "quick", "component": "hiprand", "duration_ref": 1, "category": "lightweight", "status": "pass", "sort_order": 1, "gpu_hang_risk": false},
    {"test_type": "quick", "component": "sanity", "duration_ref": 1, "category": "lightweight", "status": "pass", "sort_order": 2, "gpu_hang_risk": false}
  ]
}
JSON

cat >"${FAKE_SCRIPTS}/test_runner.py" <<'PY'
import os
import sys

assert len(sys.argv) == 1, sys.argv
assert os.environ["TEST_COMPONENT"] == "hiprand"
assert os.environ["TEST_TYPE"] == "quick"
assert os.environ["AMDGPU_FAMILIES"] == "gfx1151"
assert os.environ["THEROCK_AMDGPU_FAMILIES"] == "gfx1151"
assert os.environ["THEROCK_AMDGPU_TARGETS"] == "gfx1151"
assert os.environ["THEROCK_BIN_DIR"].endswith("/dist/rocm/bin")
assert os.environ["OUTPUT_ARTIFACTS_DIR"].endswith("/dist/rocm")
assert os.environ["ROCM_PATH"].endswith("/dist/rocm")
assert os.environ["HIP_PATH"].endswith("/dist/rocm")
print(f"test_runner component={os.environ['TEST_COMPONENT']} type={os.environ['TEST_TYPE']}")
PY

cat >"${FAKE_SCRIPTS}/test_sanity.py" <<'PY'
import os
import sys

assert len(sys.argv) == 1, sys.argv
assert os.environ["TEST_TYPE"] == "quick"
assert os.environ["THEROCK_BIN_DIR"].endswith("/dist/rocm/bin")
assert os.environ["OUTPUT_ARTIFACTS_DIR"].endswith("/dist/rocm")
assert os.environ["ROCM_PATH"].endswith("/dist/rocm")
assert os.environ["HIP_PATH"].endswith("/dist/rocm")
print(f"sanity output={os.environ['OUTPUT_ARTIFACTS_DIR']}")
PY

"${AGENT}" run \
  "${RUN_BOOTSTRAP_OFF[@]}" \
  --therock-repo "${FAKE_THEROCK}" \
  --artifacts "${TMP_DIR}/output/build" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/native_component_sort_order.json" \
  --components hiprand,sanity \
  --test-types quick \
  --output-root "${TMP_DIR}/native_runs" \
  --stable-threshold 1 \
  --max-rounds 1

NATIVE_RUN_DIR="$(find "${TMP_DIR}/native_runs" -mindepth 1 -maxdepth 1 -type d | sort | head -n 1)"
python3 - "${NATIVE_RUN_DIR}/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
results = state["results"]["task_results"]

assert state["final_status"] == "passed", state["final_status"]
assert results["hiprand-quick"]["status"] == "pass"
assert results["hiprand-quick"]["entrypoint_type"] == "test_runner"
assert results["hiprand-quick"]["test_component"] == "hiprand"
assert "--component" not in results["hiprand-quick"]["command"]
assert "--test-type" not in results["hiprand-quick"]["command"]
assert "--component" not in results["hiprand-quick"]["original_command"]
assert "--test-type" not in results["hiprand-quick"]["original_command"]
assert results["hiprand-quick"]["wrapper_path"].endswith("hiprand-quick.round1.sh")
assert "OUTPUT_ARTIFACTS_DIR" in results["hiprand-quick"]["wrapper_env_change_keys"]
assert results["sanity-quick"]["status"] == "pass"
assert results["sanity-quick"]["entrypoint_type"] == "dedicated_python"
assert results["sanity-quick"]["script"] == "test_sanity.py"
PY

grep -q "test_runner component=hiprand" "${NATIVE_RUN_DIR}/logs/hiprand-quick.round1.stdout.log"
grep -q "sanity output=" "${NATIVE_RUN_DIR}/logs/sanity-quick.round1.stdout.log"
test -x "${NATIVE_RUN_DIR}/wrappers/hiprand-quick.round1.sh"
test -x "${NATIVE_RUN_DIR}/wrappers/sanity-quick.round1.sh"
test -f "${NATIVE_RUN_DIR}/wrapper_changes.jsonl"
grep -q "export TEST_COMPONENT=hiprand" "${NATIVE_RUN_DIR}/wrappers/hiprand-quick.round1.sh"
grep -q "export OUTPUT_ARTIFACTS_DIR=" "${NATIVE_RUN_DIR}/wrappers/sanity-quick.round1.sh"
grep -q '"event": "wrapper_generated"' "${NATIVE_RUN_DIR}/wrapper_changes.jsonl"
grep -q '"event": "wrapper_generated"' "${NATIVE_RUN_DIR}/agent_activity.jsonl"
python3 - "${NATIVE_RUN_DIR}/summary.json" <<'PY'
import json
import sys

summary = json.load(open(sys.argv[1], encoding="utf-8"))
tasks = {task["task_id"]: task for task in summary["tasks"]}

assert tasks["hiprand-quick"]["entrypoint_type"] == "test_runner"
assert "OUTPUT_ARTIFACTS_DIR" in tasks["hiprand-quick"]["wrapper_env_change_keys"]
PY

echo "[test] rocblas quick timeout override"
cat >"${TMP_DIR}/rocblas_quick_component_sort_order.json" <<'JSON'
{
  "version": "test",
  "entries": [
    {"test_type": "quick", "component": "rocblas", "duration_ref": 1, "category": "heavy", "status": "pass", "sort_order": 1, "gpu_hang_risk": false}
  ]
}
JSON

mkdir -p "${TMP_DIR}/output/build/dist/rocm/bin/rocblas"
touch "${TMP_DIR}/output/build/dist/rocm/bin/rocblas-test"
cat >"${TMP_DIR}/output/build/dist/rocm/bin/rocblas/CTestTestfile.cmake" <<'CMAKE'
add_test(rocblas-test_quick_suite "../rocblas-test" "--gtest_filter=*quick*")
set_tests_properties(rocblas-test_quick_suite PROPERTIES LABELS "quick" TIMEOUT "1800")
CMAKE

cat >"${FAKE_SCRIPTS}/test_runner.py" <<'PY'
import os
import sys
from pathlib import Path

ctest_timeout_seconds = 7200
TEST_DIR = os.environ["THEROCK_BIN_DIR"] + "/rocblas"


def main():
    assert len(sys.argv) == 1, sys.argv
    assert os.environ["TEST_COMPONENT"] == "rocblas"
    assert os.environ["TEST_TYPE"] == "quick"
    assert os.environ["THEROCK_AGENT_CTEST_TIMEOUT_SECONDS"] == "10800"
    assert ctest_timeout_seconds == 10800

    patched_test_dir = Path(TEST_DIR)
    patched_text = (patched_test_dir / "CTestTestfile.cmake").read_text(encoding="utf-8")
    original_test_dir = Path(os.environ["THEROCK_BIN_DIR"]) / "rocblas"
    original_text = (original_test_dir / "CTestTestfile.cmake").read_text(encoding="utf-8")

    assert patched_test_dir != original_test_dir.resolve()
    assert patched_test_dir.name == "rocblas"
    assert (patched_test_dir.parent / "rocblas-test").exists()
    assert 'TIMEOUT "10800"' in patched_text
    assert 'TIMEOUT "1800"' in original_text
    assert '../rocblas-test' in patched_text
    print(f"rocblas timeout={ctest_timeout_seconds} overlay={patched_test_dir}")
    return 0
PY

"${AGENT}" run \
  "${RUN_BOOTSTRAP_OFF[@]}" \
  --therock-repo "${FAKE_THEROCK}" \
  --artifacts "${TMP_DIR}/output/build" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/rocblas_quick_component_sort_order.json" \
  --components rocblas \
  --test-types quick \
  --output-root "${TMP_DIR}/rocblas_quick_runs" \
  --stable-threshold 1 \
  --max-rounds 1

ROCBLAS_QUICK_RUN_DIR="$(find "${TMP_DIR}/rocblas_quick_runs" -mindepth 1 -maxdepth 1 -type d | sort | head -n 1)"
python3 - "${ROCBLAS_QUICK_RUN_DIR}/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
result = state["results"]["task_results"]["rocblas-quick"]
assert state["final_status"] == "passed", state["final_status"]
assert result["status"] == "pass"
assert result["timeout_hint_seconds"] == 10800
assert result["wrapper_path"].endswith("rocblas-quick.round1.sh")
assert "THEROCK_AGENT_CTEST_TIMEOUT_SECONDS" in result["wrapper_env_change_keys"]
PY

grep -q "rocblas quick CTest TIMEOUT override seconds=10800" "${ROCBLAS_QUICK_RUN_DIR}/logs/rocblas-quick.round1.stdout.log"
grep -q "rocblas timeout=10800" "${ROCBLAS_QUICK_RUN_DIR}/logs/rocblas-quick.round1.stdout.log"
grep -q "timeout_launcher.py" "${ROCBLAS_QUICK_RUN_DIR}/wrappers/rocblas-quick.round1.sh"
grep -q "10800" "${ROCBLAS_QUICK_RUN_DIR}/wrappers/rocblas-quick.round1.sh"

echo "[test] path hardcode detection"
cat >"${TMP_DIR}/path_hardcode_component_sort_order.json" <<'JSON'
{
  "version": "test",
  "entries": [
    {"test_type": "quick", "component": "hipdnn", "duration_ref": 1, "category": "medium", "status": "fail", "sort_order": 1, "gpu_hang_risk": false}
  ]
}
JSON

cat >"${FAKE_SCRIPTS}/test_hipdnn.py" <<'PY'
import sys

print("CTestTestfile.cmake references /therock/src/hipdnn/tests", file=sys.stderr)
print("/opt/python/cp312-cp312/bin/python3.12 not found", file=sys.stderr)
print("libhipdnn_backend.so: cannot open shared object file", file=sys.stderr)
raise SystemExit(5)
PY

"${AGENT}" run \
  "${RUN_BOOTSTRAP_OFF[@]}" \
  --therock-repo "${FAKE_THEROCK}" \
  --artifacts "${TMP_DIR}/output/build" \
  --gpu gfx1151 \
  --component-config "${TMP_DIR}/path_hardcode_component_sort_order.json" \
  --components hipdnn \
  --test-types quick \
  --output-root "${TMP_DIR}/path_hardcode_runs" \
  --stable-threshold 1 \
  --max-rounds 2

PATH_HARDCODE_RUN_DIR="$(find "${TMP_DIR}/path_hardcode_runs" -mindepth 1 -maxdepth 1 -type d | sort | head -n 1)"
python3 - "${PATH_HARDCODE_RUN_DIR}/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
result = state["results"]["task_results"]["hipdnn-quick"]

assert result["status"] == "fail"
assert result["path_hardcode_detection"]["detected"]
assert "path_hardcode" in result["path_hardcode_detection"]["categories"]
assert "invalid_embedded_python_path" in result["path_hardcode_detection"]["categories"]
assert "missing_runtime_library" in result["path_hardcode_detection"]["categories"]
assert result["wrapper_path"].endswith("hipdnn-quick.round2.sh")
PY

grep -q "path_hardcode_detected" "${PATH_HARDCODE_RUN_DIR}/agent_activity.jsonl"
python3 - "${PATH_HARDCODE_RUN_DIR}/summary.json" "${PATH_HARDCODE_RUN_DIR}/failures/hipdnn-quick_failure.json" <<'PY'
import json
import sys

summary = json.load(open(sys.argv[1], encoding="utf-8"))
failure = json.load(open(sys.argv[2], encoding="utf-8"))

assert summary["path_hardcode_task_ids"] == ["hipdnn-quick"]
assert failure["task"]["path_hardcode_detection"]["detected"]
PY

echo "[test] all assertions passed"
