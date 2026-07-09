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

echo "[test] all assertions passed"
