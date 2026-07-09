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
test -f "${TARGET_DIR}/docs_this_project/component_sort_order.json"
test -f "${TARGET_DIR}/docs_this_project/问题模板.md"
test -f "${TARGET_DIR}/docs_this_project/汇总测试报告.md"
test -f "${TARGET_DIR}/.env"
test -f "${TARGET_DIR}/.env_example"
! grep -q "SUDO_PASSWORD=" "${TARGET_DIR}/.env"

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
assert state["schedule"]["task_queue"][0]["task_id"] == "hiprand-quick"
assert state["final_status"] == "running"
assert state["meta"]["amdgpu_families"] == "gfx1151"
PY

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
