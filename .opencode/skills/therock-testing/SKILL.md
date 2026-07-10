---
name: therock-testing
description: Use when executing TheRock component tests, analyzing ROCm artifacts, planning retest loops, handling GPU reset risk, or generating per-component failure reports.
---

# TheRock Testing Skill

Use this skill when the user asks to run, resume, analyze, or report TheRock ROCm component tests.

## Core Design

TheRock testing follows a configuration-driven, layered orchestration model:

- GitHub Actions and Python wrapper scripts decide what to test, where to run it, and how to shard it.
- CTest, GoogleTest, pytest, and component-specific executables perform the actual test execution.
- TheRock's Python scripts are orchestration glue; they do not implement the test assertions themselves.
- Test machines reuse build artifacts instead of rebuilding ROCm locally.
- OpenCode agents decide intent, permissions, risk policy, and result interpretation.
- `.opencode/tools/therock_agent.sh` remains the deterministic executor and state machine.

Reference document:

- `docs_this_project/ROCm_TheRock—测试test流程与设计`

## Test Execution Chain

The high-level CI chain is:

1. `multi_arch_ci.yml`
2. `multi_arch_ci_linux.yml`
3. `test_artifacts.yml`
4. `test_component.yml`
5. `build_tools/github_actions/test_executable_scripts/<test_script>`

Within `test_component.yml`, the normal order is:

1. Clean stale GPU processes with `cleanup_processes.sh`.
2. Create the Python environment and install ROCm artifacts.
3. Run GPU health checks such as `health_status.py` and `print_driver_gpu_info.py`.
4. Execute the component `test_script`.
5. On failure, run or inspect `reproduce_test_failure.py` output.
6. Clean up again after the test.

## Test Script Types

Do not guess component entrypoints from memory. The runner must read:

- `docs_this_project/component_env_script_index.json`

This file maps each component to:

- `entrypoint_type`: `test_runner`, `dedicated_python`, or `none`
- `script`: dedicated `test_<component>.py` when needed
- `test_component`: value for `TEST_COMPONENT` when using `test_runner.py`
- `env_profiles`
- `requires`
- `known_issue_category`
- `retry_policy`
- `gpu_hang_risk`
- `timeout_hint_seconds`

Most CTest-label components use:

- `build_tools/github_actions/test_executable_scripts/test_runner.py`

Special components may use dedicated scripts, for example:

- `test_sanity.py`
- `test_hiptests.py`
- `test_rccl.py`
- `test_tensilelite.py`
- `test_hipblaslt.py`
- `test_rocfft.py`
- `test_amdsmi.py`
- `test_hipdnn_integration_tests.py`
- `test_rocgdb.py`
- `test_rocr-debug-agent.py`
- `test_rocsparse.py`
- `test_hipsparse.py`
- `test_rocprofiler_sdk.py`

When `entrypoint_type=none`, skip or block according to config instead of guessing.

Important `test_runner.py` rule:

- Do not pass `--component` or `--test-type`.
- Set `TEST_COMPONENT` and `TEST_TYPE` in the environment.

## Test Type Order

Use this increasing scope order:

1. `quick`
2. `standard`
3. `comprehensive`
4. `full`

`quick` is suitable for PR-style smoke validation. `full` is suitable for broader nightly or release-style validation.

## Component Order

Read component order from:

- `docs_this_project/component_sort_order.json`

The file is authoritative for:

- `test_type`
- `component`
- `duration_ref`
- `status`
- `sort_order`
- `gpu_hang_risk`

Do not invent a different order unless the user explicitly asks for an experiment.

## Official Exclude Rules

Read official skip/block rules from:

- `docs_this_project/official_exclude.json`

This file has higher priority than `component_sort_order.json` and the entrypoint index. If a task matches official exclude:

- Do not execute it.
- Do not guess a fallback script.
- Record `official_exclude` in `global_state.json` and summary output.
- Report it as `skip` or `blocked` according to the rule.

Current expected examples include:

- `hipsparselt` on `gfx1151`
- `rocroller` on `gfx1151`
- `rocprofiler_compute` with no independent entrypoint

## Artifact Paths

The rough runner should support these artifact path shapes:

- `/output-linux-portable/build`
- `/output/build`
- a direct `dist/rocm` path

Normalize them into:

- `build_root`
- `rocm_dist = <build_root>/dist/rocm`

Set runtime environment consistently:

- `ROCM_PATH=<rocm_dist>`
- `HIP_PATH=<rocm_dist>`
- `THEROCK_BIN_DIR=<rocm_dist>/bin`
- `OUTPUT_ARTIFACTS_DIR=<rocm_dist>`
- `PATH=<rocm_dist>/bin:$PATH`
- `LD_LIBRARY_PATH=<rocm_dist>/lib:<rocm_dist>/lib64:$LD_LIBRARY_PATH`
- `AMDGPU_FAMILIES=<gfx family, e.g. gfx1151>`
- `THEROCK_AMDGPU_FAMILIES=<same gfx family>`
- `THEROCK_AMDGPU_TARGETS=<same gfx value unless a narrower target list is explicitly provided>`

## CTest Selection Model

The common `test_runner.py` path uses CTest labels:

- Discover labels with `ctest --print-labels` or `ctest -N`.
- Select the test category using the test type: `quick`, `standard`, `comprehensive`, or `full`.
- Combine category labels with GPU architecture labels such as `gpu_gfxXXXX`.
- Exclude category-specific or architecture-specific exclusion labels.
- Use sharding when available through `GTEST_SHARD_INDEX` and `GTEST_TOTAL_SHARDS`.

The important mental model is:

`test_runner.py` filters by test type and GPU architecture, then delegates real execution to CTest / GoogleTest / pytest / component executables.

## Loop Rules

The deterministic state machine belongs in `.opencode/tools/therock_agent.sh`, not in chat memory.

Loop behavior:

1. First round runs all allowed tasks.
2. Later rounds rerun only the previous round's failures.
3. Stop when the failure set is empty.
4. Stop when the failure set is unchanged for the configured stable threshold.
5. Persist every state transition to `runs/<run_id>/global_state.json`.

OpenCode agents should call the runner and interpret results. They should not independently maintain failure sets.

## Execution Wrapper And Audit

Real task execution should go through generated wrappers under:

- `runs/<run_id>/wrappers/<task_id>.round<N>.sh`

The wrapper records:

- target working directory
- exported environment variables
- final Python test script command

The wrapper must not mutate:

- component source
- ROCm submodule source
- `dist/rocm/bin`
- `dist/rocm/lib`

Audit and report files include:

- `runs/<run_id>/wrapper_changes.jsonl`
- `runs/<run_id>/agent_activity.jsonl`
- `runs/<run_id>/tool_calls.jsonl`
- `runs/<run_id>/global_state.json`
- `runs/<run_id>/summary.json`
- `runs/<run_id>/failures.json`
- `runs/<run_id>/failures/*_failure.json`
- `runs/<run_id>/round_analysis/round<N>_inputs.json`
- `runs/<run_id>/debug/round<N>_failure_index.json`
- OpenCode-generated `runs/<run_id>/round_analysis/round<N>.json`
- OpenCode-generated `runs/<run_id>/round_analysis/round<N>.md`
- OpenCode-generated `runs/<run_id>/debug/round<N>_log_excerpt.md`

If logs contain hardcoded path indicators such as `/therock/src/`, `/opt/python/cp312-cp312/bin/python3.12`, or missing `libhipdnn_backend.so`, classify them under `path_hardcode_detection`. Do not patch installed ROCm artifacts automatically.

## Debug / Repair Loop Artifacts

Every failed round should be debuggable from files, not chat memory:

- `round_analysis/round<N>_inputs.json`: structured input for that round, including failed/blocked tasks and log paths.
- `debug/round<N>_failure_index.json`: compact failure index with task IDs, status, logs, and reports.
- `round_analysis/round<N>.json`: OpenCode-generated machine-readable classification, `next_action`, `repair_policy`, and repairability.
- `round_analysis/round<N>.md`: OpenCode-generated human-readable round analysis.
- `debug/round<N>_log_excerpt.md`: OpenCode-generated curated stdout/stderr excerpts.

Use these before reading raw full logs. Read full stdout/stderr only when excerpts are insufficient.

## Failure Classifications

OpenCode, not the runner, owns final root cause and repair policy. Use runner evidence plus these categories consistently in debug reports and repair plans:

| Classification | Typical Signals | next_action | repair_policy |
|----------------|-----------------|-------------|---------------|
| `missing_python_dependency` | `ModuleNotFoundError: No module named X` | `repair_then_retry` | `safe_auto` |
| `missing_dependency` | `missing_dependency: X` | `repair_then_retry` or `inspect_dependency_then_retry` | `safe_auto` only for confirmed Python packages |
| `network_transient` | DNS failures, connection reset, timeout, HTTP 5xx, TLS temporary failure | `retry_transient` | `safe_auto` |
| `cmake_configuration_error` | `CMake Error`, `Could NOT find`, `find_package`, `CMAKE_PREFIX_PATH`, `ninja: error` | `plan_wrapper_or_build_tools_repair` | `safe_plan_only` |
| `missing_runtime_library` | `cannot open shared object file`, missing `.so` | `inspect_runtime_path_then_retry` | `safe_plan_only` |
| `runtime_path_error` | `LD_LIBRARY_PATH`, `ROCM_PATH`, `HIP_PATH`, artifact path mismatch | `inspect_runtime_path_then_retry` | `safe_plan_only` |
| `permission_or_sudo` | `sudo_unavailable`, `Permission denied`, `Operation not permitted` | `check_sudo_policy_then_retry` | `manual_required` |
| `disk_space_error` | `No space left on device`, `Disk quota exceeded`, `ENOSPC` | `needs_environment_cleanup` | `manual_required` |
| `timeout` | `TimeoutExpired`, `timed out`, `SIGTERM` | `retry_or_timeout_review` | `manual_required` |
| `gpu_runtime_error` | `HSA_STATUS_ERROR`, `PERMISSION_FAULT`, ROCr/HIP runtime errors | `quarantine_or_manual` | `manual_required` |
| `gpu_hang_risk` | ring timeout, GPU reset, MES failure | `quarantine_or_manual` | `manual_required` |
| `test_assertion_failure` | `AssertionError`, pytest/gtest failure lines | `retry_until_stable` | `manual_required` |

## Repair Policy Rules

Repair planning must be conservative:

- `safe_auto`: only Python dependency installation, clearly transient retry, and writing run-directory audit outputs.
- `safe_plan_only`: generate a plan and evidence. Do not mutate files automatically.
- `safe_patch_limited`: only patch TheRock `build_tools/**` or this overlay's wrapper-generation logic, and always record diff and reason.
- `manual_required`: do not execute repair; report the blocker and required manual decision.

Never modify:

- TheRock component source.
- ROCm submodule source.
- `dist/rocm/bin`.
- `dist/rocm/lib`.
- Build artifacts or installed ROCm payload.

Repair execution is an OpenCode responsibility:

- The deterministic runner generates failed-round inputs and logs.
- `/therock-debug-round run_id=<run_id> round=<N>` invokes `therock-debugger` to generate analysis.
- `/therock-repair-round run_id=<run_id> round=<N> apply=safe` invokes `therock-repairer`.
- `therock-repairer` may execute only `safe_auto` actions and must write `repairs/**` audit files.
- The runner must not silently execute repair commands in the background without OpenCode-visible permissions and records.

## GPU Reset Risk

Default behavior:

- Skip tasks where `gpu_hang_risk` is `true`.

Only run high-risk tasks when the user explicitly requests one of:

- `--gpu-risk include`
- `--gpu-risk quarantine`

Prefer `quarantine` for real machines: run normal tasks first, then run GPU reset risk tasks in a separate stage.

If logs contain GPU timeout indicators such as `ring gfx`, `GPU reset`, `MES failed`, `PERMISSION_FAULT`, or `HSA_STATUS_ERROR`, preserve the logs and avoid automatic aggressive retries.

## Sudo Policy

Never ask for or store sudo passwords.

Valid policies:

- `THEROCK_SUDO_POLICY=none`
- `THEROCK_SUDO_POLICY=cache`
- `THEROCK_SUDO_POLICY=askpass`

For non-interactive loop execution, `sudo_sensitive` tasks should only proceed with one of:

- `THEROCK_SUDO_POLICY=cache`
- a valid `sudo -v` cache verified by `sudo -n true`
- `THEROCK_SUDO_POLICY=askpass`
- a running `therock-sudo-agent` session verified by `sudo -A true`; prefer launching OpenCode via `./scripts/therock-sudo-agent run -- opencode` so cleanup is automatic

Do not perform a global sudo cache check for every run. Only check sudo during task preflight when the resolved entrypoint profile requires sudo.

If sudo is unavailable, mark the task `blocked`, not failed.

## Reports

Runner produces structured data:

- `runs/<run_id>/global_state.json`
- `runs/<run_id>/summary.json`
- `runs/<run_id>/failures.json`
- `runs/<run_id>/logs/*.stdout.log`
- `runs/<run_id>/logs/*.stderr.log`
- `runs/<run_id>/wrappers/*.sh`
- `runs/<run_id>/wrapper_changes.jsonl`
- `runs/<run_id>/failures/*_failure.json`

`therock-reporter` generates Markdown from JSON when needed:

- `runs/<run_id>/summary_report.md`
- `runs/<run_id>/failures/*_failure_report.md`

At minimum, include:

- Problem title.
- Component and test type.
- Code and artifact version when available.
- Hardware and runtime environment.
- Raw command and return code.
- Key stdout/stderr excerpts.
- Failure classification.
- Reproduce or retest steps.
- CI recommendation.
- Evidence paths.
- Index hit details.
- Official exclude reason when applicable.
- Wrapper path and environment changes.
- Hardcoded path detection results.

## Safety Boundaries

Keep test execution deterministic and auditable:

- Never store sudo passwords in `.env`, prompts, logs, or state files.
- If sudo is required for the selected task, use `THEROCK_SUDO_POLICY=cache` plus a manual `sudo -v`, or launch OpenCode with `./scripts/therock-sudo-agent run -- opencode` for `THEROCK_SUDO_POLICY=askpass`.
- The runner may check `sudo -n true` or `sudo -A true` only for `sudo_sensitive` tasks, but it must not read or store the password.
- Do not modify ROCm installed artifacts under `dist/rocm/bin` or `dist/rocm/lib`.
- Do not modify TheRock component source directories by default.
- If modifications are needed, prefer TheRock `build_tools/**` test wrapper scripts and record the reason, diff, and round.
- Use OpenCode permissions to restrict what agents can edit or execute, but keep runner-side checks for operations that happen inside an allowed shell command.

## Recommended OpenCode Role Split

Use agents as thin roles around the runner:

- `therock-loop`: main coordinator, accepts user intent and summarizes state.
- `therock-executor`: restricted executor, validates command arguments and calls the shell runner.
- `therock-reporter`: reads logs/state, summarizes results, and checks report completeness.

Do not move the core loop state machine out of `therock_agent.sh`.
