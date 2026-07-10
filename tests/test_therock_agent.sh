#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
AGENT="${PROJECT_ROOT}/.opencode/tools/therock_agent.sh"

TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT

mkdir -p "${TMP_DIR}/output/build/dist/rocm/bin" "${TMP_DIR}/output/build/dist/rocm/lib"

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

echo "[test] run loop with risk skip"
"${AGENT}" run \
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
SUMMARY_FILE="${RUN_DIR}/summary_report.md"
FAILURE_FILE="${RUN_DIR}/failures/fail_component-quick_failure_report.md"
ACTIVITY_FILE="${RUN_DIR}/agent_activity.jsonl"
TOOL_CALLS_FILE="${RUN_DIR}/tool_calls.jsonl"
ENVIRONMENT_FILE="${RUN_DIR}/environment_summary.json"
GLOBAL_AUDIT_FILE="${TMP_DIR}/runs/_audit/agent_invocations.jsonl"

test -f "${STATE_FILE}"
test -f "${SUMMARY_FILE}"
test -f "${FAILURE_FILE}"
test -f "${ACTIVITY_FILE}"
test -f "${TOOL_CALLS_FILE}"
test -f "${ENVIRONMENT_FILE}"
test -f "${GLOBAL_AUDIT_FILE}"

python3 - "${STATE_FILE}" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
results = state["results"]["task_results"]

assert state["final_status"] == "failed", state["final_status"]
assert results["pass_component-quick"]["status"] == "pass"
assert results["fail_component-quick"]["status"] == "fail"
assert results["risk_component-quick"]["status"] == "skip"
assert results["exclude_component-quick"]["status"] == "skip"
assert state["loop"]["stable_failed_count"] == 1
assert state["schedule"]["failed_tasks"] == ["fail_component-quick"]
PY

grep -q "fail_component-quick" "${SUMMARY_FILE}"
grep -q "risk_component-quick" "${SUMMARY_FILE}"
grep -q "docs_this_project/汇总测试报告.md" "${SUMMARY_FILE}"
grep -q "模板字段覆盖" "${SUMMARY_FILE}"
grep -q "Runner 活动日志" "${SUMMARY_FILE}"
grep -q "docs_this_project/问题模板.md" "${FAILURE_FILE}"
grep -q "组件与测试信息" "${FAILURE_FILE}"
grep -q '"event": "task_start"' "${ACTIVITY_FILE}"
grep -q '"event": "task_end"' "${ACTIVITY_FILE}"
grep -q '"event": "report_generated"' "${ACTIVITY_FILE}"
grep -q '"tool": "shell"' "${TOOL_CALLS_FILE}"
grep -q '"event": "invocation_start"' "${GLOBAL_AUDIT_FILE}"
grep -q '"event": "invocation_end"' "${GLOBAL_AUDIT_FILE}"

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
"${AGENT}" status background_case \
  --output-root "${TMP_DIR}/background_runs" \
  --format brief >"${TMP_DIR}/background_status_brief.out"
"${AGENT}" status \
  --output-root "${TMP_DIR}/background_runs" >"${TMP_DIR}/background_status_list.out"

grep -q "status: passed" "${TMP_DIR}/background_status.out"
grep -q "progress: 1/1" "${TMP_DIR}/background_status.out"
grep -q "passed|1|1/1" "${TMP_DIR}/background_status_brief.out"
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

"${AGENT}" stop stop_case \
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

"${AGENT}" resume resume_case \
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

grep -q "official_exclude" "${OFFICIAL_EXCLUDE_RUN_DIR}/summary_report.md"
grep -q "TheRock/上游测试矩阵" "${OFFICIAL_EXCLUDE_RUN_DIR}/summary_report.md"

cat >"${TMP_DIR}/sudo_component_sort_order.json" <<'JSON'
{
  "version": "test",
  "entries": [
    {"test_type": "standard", "component": "amdsmi", "duration_ref": 1, "category": "lightweight", "status": "pass", "sort_order": 1, "gpu_hang_risk": false}
  ]
}
JSON

"${AGENT}" run \
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

grep -q "sudo_unavailable" "${SUDO_RUN_DIR}/failures/amdsmi-standard_failure_report.md"

FAKE_SUDO_FAIL_DIR="${TMP_DIR}/fake_sudo_fail"
mkdir -p "${FAKE_SUDO_FAIL_DIR}"
cat >"${FAKE_SUDO_FAIL_DIR}/sudo" <<SH
#!/usr/bin/env bash
printf '%s\n' "\$*" >> "${TMP_DIR}/fake_sudo_fail.log"
exit 1
SH
chmod +x "${FAKE_SUDO_FAIL_DIR}/sudo"

PATH="${FAKE_SUDO_FAIL_DIR}:${PATH}" "${AGENT}" run \
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
grep -q "Index 命中规则" "${NATIVE_RUN_DIR}/summary_report.md"
grep -q "Wrapper 变更日志" "${NATIVE_RUN_DIR}/summary_report.md"

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
grep -q "硬编码路径检测" "${PATH_HARDCODE_RUN_DIR}/summary_report.md"
grep -q "wrapper_changes.jsonl" "${PATH_HARDCODE_RUN_DIR}/failures/hipdnn-quick_failure_report.md"

echo "[test] all assertions passed"
