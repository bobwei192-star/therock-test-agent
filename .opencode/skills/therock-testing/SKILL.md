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

Most components use:

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

When the rough runner cannot locate or confidently map the correct test entrypoint, mark the task as `blocked` instead of guessing.

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
- `LD_LIBRARY_PATH=<rocm_dist>/lib:$LD_LIBRARY_PATH`
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

## GPU Reset Risk

Default behavior:

- Skip tasks where `gpu_hang_risk` is `true`.

Only run high-risk tasks when the user explicitly requests one of:

- `--gpu-risk include`
- `--gpu-risk quarantine`

Prefer `quarantine` for real machines: run normal tasks first, then run GPU reset risk tasks in a separate stage.

If logs contain GPU timeout indicators such as `ring gfx`, `GPU reset`, `MES failed`, `PERMISSION_FAULT`, or `HSA_STATUS_ERROR`, preserve the logs and avoid automatic aggressive retries.

## Reports

Each run should produce:

- `runs/<run_id>/global_state.json`
- `runs/<run_id>/summary_report.md`
- `runs/<run_id>/logs/*.stdout.log`
- `runs/<run_id>/logs/*.stderr.log`
- `runs/<run_id>/failures/*_failure_report.md`

Failure reports should follow the project problem template:

- `../1问题描述格式.md`

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

## Safety Boundaries

Keep test execution deterministic and auditable:

- Never store sudo passwords in `.env`, prompts, logs, or state files.
- If sudo is required, use `THEROCK_SUDO_POLICY=cache` plus a manual `sudo -v` before launching OpenCode.
- The runner may check `sudo -n true` to verify the cache, but it must not prompt for or read the password.
- Do not modify ROCm installed artifacts under `dist/rocm/bin` or `dist/rocm/lib`.
- Do not modify TheRock component source directories by default.
- If modifications are needed, prefer TheRock `build_tools/**` test wrapper scripts and record the reason, diff, and round.
- Use OpenCode permissions to restrict what agents can edit or execute, but keep runner-side checks for operations that happen inside an allowed shell command.

## Recommended OpenCode Role Split

Use agents as thin roles around the runner:

- `therock-loop`: main coordinator, accepts user intent and summarizes state.
- `therock-executor`: restricted executor, calls the shell runner.
- `therock-reporter`: reads logs/state and improves reports.

Do not move the core loop state machine out of `therock_agent.sh`.
