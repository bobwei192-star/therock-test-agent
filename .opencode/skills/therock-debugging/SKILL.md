---
name: therock-debugging
description: Use when analyzing TheRock failed rounds, reviewing round_analysis/debug artifacts, planning safe repairs, or deciding retry/manual actions after a test loop failure.
---

# TheRock Debugging Skill

Use this skill for the `测试 -> 分析 -> 修复计划 -> 验证` loop after TheRock test rounds fail.

This skill does not replace the deterministic runner. The runner owns task execution, state transitions, checkpointing, logs, and failed-round input indexes. OpenCode agents use this skill to generate debug analysis, plan safe follow-up actions, and execute `safe_auto` repairs when explicitly invoked through the repair command.

Repair execution belongs to OpenCode:

- The runner generates `round_analysis/round<N>_inputs.json`, `debug/round<N>_failure_index.json`, and logs.
- `therock-debugger` generates `round_analysis/round<N>.json`, `round_analysis/round<N>.md`, and `debug/round<N>_log_excerpt.md`.
- `therock-repairer` reads the OpenCode-generated analysis files.
- `/therock-repair-round ... apply=safe` may execute `safe_auto` actions using OpenCode permissions.
- All repair actions must be recorded under `repairs/**`.

## Required Inputs

Start from the run directory:

- `global_state.json`
- `progress.jsonl`
- `round_analysis/round<N>_inputs.json`
- `round_analysis/round<N>.json`
- `round_analysis/round<N>.md`
- `debug/round<N>_failure_index.json`
- `debug/round<N>_log_excerpt.md`
- `failures/*_failure.json`
- `logs/*.round<N>.stdout.log`
- `logs/*.round<N>.stderr.log`

Read in this order:

1. `global_state.json` for current status, output directory, loop round, and failed tasks.
2. `debug/round<N>_failure_index.json` and `round_analysis/round<N>_inputs.json` to verify the task list.
3. Failure reports and full stdout/stderr logs for evidence.
4. Existing `round_analysis/round<N>.json` only if the user is asking to review or update previous OpenCode analysis.

## Classification Rules

Use `therock-testing` as the single source of truth for classification names, `next_action`, and `repair_policy`. The runner only provides evidence signals; final root cause and repair policy are OpenCode judgments.

### Hard classification rules
- If `failure_evidence.missing_python_modules` is non-empty AND
  `failure_evidence.python_context.bootstrap_importable_missing_modules[<module>] == true`
  （表示 bootstrap venv python 可以 import 该 module；而 runner 已观察到 test python 无法 import），则：
  - `classification = python_interpreter_mismatch`
  - `repair_policy = safe_patch_limited`
  - `next_action = repair_then_retry`
  - The fix must target the test execution environment (wrapper/env), not just installing into the venv.
- If logs include `FileNotFoundError` and the missing path contains `share/amdsmitst` (or the missing binary is `amdsmitst`), then:
  - `classification = runtime_path_error`
  - `repair_policy = safe_plan_only` (or `safe_patch_limited` if it can be fixed by wrapper/env/OUTPUT_ARTIFACTS_DIR)

## Safe Repair Boundaries

Do not duplicate safety rules here. Enforce them through:

- agent `permission` blocks;
- runner policies for sudo, GPU risk, and artifact mutation;
- the `therock-testing` Safety Boundaries section.

## Debugger Agent Output

When acting as debugger, produce:

- Failed task list with classification.
- Evidence paths and key log excerpts.
- Root cause confidence.
- `next_action` for each task.
- Whether the generated analysis is complete.
- Gaps that require reading full logs or manual input.

Do not apply repairs in debugger mode.

## Repairer Agent Output

When acting as repairer, produce a plan first:

- Task ID.
- Classification.
- Proposed action.
- `repair_policy`.
- Commands or files involved.
- Risk level.
- Audit files to write.

Only proceed with actions allowed by the policy and current OpenCode permissions. If the action is `manual_required`, stop at the plan and report the blocker.

When `apply=safe`, write:

- `repairs/round<N>_repair_plan.json`
- `repairs/round<N>_repair_plan.md`
- `repairs/round<N>_actions.jsonl`
- `repairs/round<N>_tool_calls.jsonl`
- `repairs/round<N>_environment_changes.md`

Allowed `safe_auto` execution:

- Use the *test python* executable for pip installs:
  - Prefer `$VENV_PYTHON -m pip install <package>` where `$VENV_PYTHON` is sourced from `global_state.bootstrap.venv.python` or `failure_evidence.python_context.test_python_executable`.
  - Do not assume `python3` / system python3 is the interpreter used by the test wrapper.
- Retry/resume recommendation for clear `network_transient`.

For `missing_python_dependency`, the debug analysis must include concrete `repair_items`. If the debugger omitted them, the repairer should fall back to `failure_evidence.missing_python_modules` in `failures/*_failure.json` before stopping.

Do not execute CMake, runtime path, sudo, disk cleanup, timeout expansion, GPU-risk, component-source, or artifact mutations automatically.
