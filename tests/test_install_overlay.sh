#!/usr/bin/env bash
set -euo pipefail

PROJECT_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
TMP_DIR="$(mktemp -d)"
trap 'rm -rf "${TMP_DIR}"' EXIT

TARGET_DIR="${TMP_DIR}/TheRock"
ARTIFACT_DIR="${TMP_DIR}/output/build"

mkdir -p "${TARGET_DIR}" "${ARTIFACT_DIR}/dist/rocm/bin" "${ARTIFACT_DIR}/dist/rocm/lib"

"${PROJECT_ROOT}/install.sh" "${TARGET_DIR}"

test -f "${TARGET_DIR}/.opencode/agents/therock-loop.md"
test -f "${TARGET_DIR}/.opencode/commands/therock-run.md"
test -f "${TARGET_DIR}/.opencode/skills/therock-testing/SKILL.md"
test -x "${TARGET_DIR}/.opencode/tools/therock_agent.sh"
test -f "${TARGET_DIR}/.opencode/tools/therock_agent/__init__.py"
test -f "${TARGET_DIR}/.opencode/tools/therock_agent/cli.py"
test -f "${TARGET_DIR}/.opencode/tools/therock_agent/executor.py"
test -f "${TARGET_DIR}/.opencode/tools/therock_agent/reports.py"
test -f "${TARGET_DIR}/docs_this_project/component_sort_order.json"
test -f "${TARGET_DIR}/docs_this_project/component_env_script_index.json"
test -f "${TARGET_DIR}/docs_this_project/official_exclude.json"
test -f "${TARGET_DIR}/docs_this_project/问题模板.md"
test -f "${TARGET_DIR}/docs_this_project/汇总测试报告.md"
test -f "${TARGET_DIR}/.env"
test -f "${TARGET_DIR}/.env_example"
! grep -q "SUDO_PASSWORD=" "${TARGET_DIR}/.env"

SETUP_TARGET_DIR="${TMP_DIR}/TheRockWithSudoAgent"
TEST_HOME="${TMP_DIR}/home"
mkdir -p "${SETUP_TARGET_DIR}" "${TEST_HOME}"
HOME="${TEST_HOME}" "${PROJECT_ROOT}/install.sh" --setup-sudo-agent "${SETUP_TARGET_DIR}"
test -x "${SETUP_TARGET_DIR}/scripts/therock-sudo-agent"
test -x "${TEST_HOME}/.therock/sudo-askpass.sh"
grep -q "THEROCK_SUDO_POLICY=askpass" "${SETUP_TARGET_DIR}/.env"
grep -q "THEROCK_SUDO_ASKPASS=${TEST_HOME}/.therock/sudo-askpass.sh" "${SETUP_TARGET_DIR}/.env"
grep -q "THEROCK_SUDO_AGENT_SOCKET=${TEST_HOME}/.therock/sudo-agent.sock" "${SETUP_TARGET_DIR}/.env"
! grep -q "SUDO_PASSWORD=" "${SETUP_TARGET_DIR}/.env"

ASKPASS_TEST_SOCKET="${TMP_DIR}/askpass-test.sock"
ASKPASS_TEST_PID="${TMP_DIR}/askpass-test.pid"
printf '%s\n' "prompt-secret" | "${SETUP_TARGET_DIR}/scripts/therock-sudo-agent" daemon \
  --socket "${ASKPASS_TEST_SOCKET}" \
  --pid-file "${ASKPASS_TEST_PID}" &
ASKPASS_DAEMON_PID="$!"
for _ in 1 2 3 4 5 6 7 8 9 10; do
  if "${SETUP_TARGET_DIR}/scripts/therock-sudo-agent" status \
    --socket "${ASKPASS_TEST_SOCKET}" \
    --pid-file "${ASKPASS_TEST_PID}" >/dev/null 2>&1; then
    break
  fi
  sleep 0.1
done
ASKPASS_OUTPUT="$("${SETUP_TARGET_DIR}/scripts/therock-sudo-agent" askpass \
  --socket "${ASKPASS_TEST_SOCKET}" \
  --pid-file "${ASKPASS_TEST_PID}" \
  "[sudo] password for zx:")"
test "${ASKPASS_OUTPUT}" = "prompt-secret"
"${SETUP_TARGET_DIR}/scripts/therock-sudo-agent" stop \
  --socket "${ASKPASS_TEST_SOCKET}" \
  --pid-file "${ASKPASS_TEST_PID}" >/dev/null
wait "${ASKPASS_DAEMON_PID}" 2>/dev/null || true

if "${TARGET_DIR}/.opencode/tools/therock_agent.sh" init \
  --run-id should_reject_legacy_ask \
  --artifacts "${ARTIFACT_DIR}" \
  --amdgpu-families gfx1151 \
  --components hiprand \
  --test-types quick \
  --sudo-policy ask \
  --output-root "${TMP_DIR}/legacy_ask_runs" 2>"${TMP_DIR}/legacy_ask.log"; then
  echo "runner accepted legacy sudo_policy=ask unexpectedly" >&2
  exit 1
fi
grep -q "invalid choice" "${TMP_DIR}/legacy_ask.log"

"${TARGET_DIR}/.opencode/tools/therock_agent.sh" init \
  --run-id install_smoke \
  --artifacts "${ARTIFACT_DIR}" \
  --amdgpu-families gfx1151 \
  --components hiprand \
  --test-types quick \
  --output-root "${TMP_DIR}/runs"

python3 - "${TMP_DIR}/runs/install_smoke/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
assert state["meta"]["component_config"].endswith("docs_this_project/component_sort_order.json")
assert state["meta"]["component_env_index"].endswith("docs_this_project/component_env_script_index.json")
assert state["meta"]["official_exclude"].endswith("docs_this_project/official_exclude.json")
assert state["schedule"]["task_queue"][0]["task_id"] == "hiprand-quick"
assert state["final_status"] == "running"
assert state["meta"]["amdgpu_families"] == "gfx1151"
PY

"${TARGET_DIR}/.opencode/tools/therock_agent.sh" init \
  --run-id all_components_smoke \
  --artifacts "${ARTIFACT_DIR}" \
  --amdgpu-families gfx1151 \
  --components all \
  --test-types quick \
  --output-root "${TMP_DIR}/all_runs"

python3 - "${TMP_DIR}/all_runs/all_components_smoke/global_state.json" <<'PY'
import json
import sys

state = json.load(open(sys.argv[1], encoding="utf-8"))
task_ids = [task["task_id"] for task in state["schedule"]["task_queue"]]
assert "hiprand-quick" in task_ids
assert all("all-" not in task_id for task_id in task_ids)
assert len(task_ids) > 1
PY

if "${TARGET_DIR}/.opencode/tools/therock_agent.sh" init \
  --run-id invalid_artifacts \
  --artifacts "${TMP_DIR}/missing/build" \
  --amdgpu-families gfx1151 \
  --components hiprand \
  --test-types quick \
  --output-root "${TMP_DIR}/invalid_runs" 2>"${TMP_DIR}/invalid.log"; then
  echo "runner accepted invalid artifacts unexpectedly" >&2
  exit 1
fi
test -f "${TMP_DIR}/invalid_runs/_audit/agent_invocations.jsonl"
grep -q '"event": "invocation_failed"' "${TMP_DIR}/invalid_runs/_audit/agent_invocations.jsonl"

echo "THEROCK_SUDO_PASSWORD=secret" >> "${TARGET_DIR}/.env"
if "${TARGET_DIR}/.opencode/tools/therock_agent.sh" init \
  --run-id should_reject_sudo_password \
  --artifacts "${ARTIFACT_DIR}" \
  --amdgpu-families gfx1151 \
  --components hiprand \
  --test-types quick \
  --output-root "${TMP_DIR}/reject_runs" 2>"${TMP_DIR}/reject.log"; then
  echo "runner accepted THEROCK_SUDO_PASSWORD unexpectedly" >&2
  exit 1
fi
grep -q "拒绝从 .env 读取敏感字段" "${TMP_DIR}/reject.log"

echo "[test] install overlay assertions passed"
