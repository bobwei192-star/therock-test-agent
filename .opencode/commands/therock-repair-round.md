---
description: Plan or run safe TheRock repairs for a failed round
agent: therock-repairer
subtask: true
---

为某个 TheRock 失败轮次生成受限修复计划，并在 `apply=safe` 时由 OpenCode 执行 `safe_auto` 修复。

注意：自动修复执行不由后台 runner 完成。runner 只生成失败输入索引和日志；`/therock-debug-round` 先由 OpenCode 生成 `round_analysis`；本命令通过 `therock-repairer` 使用 OpenCode 原生读写和 shell 权限执行安全动作并写审计。

用户参数：

```text
$ARGUMENTS
```

支持：

- `run_id=<run_id>`：必填，目标 run。
- `round=<N>`：可选，指定轮次；缺省时使用最近失败轮次。
- `output_root=<path>`：可选，run 根目录；缺省使用 `runs`。
- `apply=<safe|off>`：可选，默认 `off`。`safe` 只允许 `safe_auto` 动作并遵守 OpenCode 权限。

## 必须使用的 skill

使用：

- `therock-debugging`
- 必要时参考 `therock-testing`

## 行为

1. 读取 `global_state.json` 和 `round_analysis/round<N>.json`。
2. 如果 analysis 缺失，先要求用户运行 `/therock-debug-round run_id=<run_id> round=<N>` 或说明缺失文件。
3. 对每个 task 读取：
   - `classification`
   - `next_action`
   - `repair_policy`
   - `repair_items`
   - `evidence`
4. 生成 repair plan：
   - `safe_auto`：Python dependency 或 transient retry。
   - `safe_plan_only`：CMake/runtime path 只生成计划。
   - `safe_patch_limited`：只允许 `build_tools/**` 或 overlay wrapper/env 逻辑，必须记录 diff。
   - `manual_required`：停止并说明原因。
5. 写 repair plan：
   - `repairs/round<N>_repair_plan.json`
   - `repairs/round<N>_repair_plan.md`
6. 如果用户传 `apply=safe`，只执行 `safe_auto` 且当前权限允许的动作。
7. 执行动作后写审计：
   - `repairs/round<N>_actions.jsonl`
   - `repairs/round<N>_tool_calls.jsonl`
   - `repairs/round<N>_environment_changes.md`
8. 修复完成后提示用户运行 `/therock-resume run_id=<run_id>` 或重新启动验证轮。

## safe_auto 执行规则

允许执行：

- `missing_python_dependency` 且 `repair_items` 明确时：

```bash
python3 -m pip install <package>
```

- `network_transient`：不 patch 文件，只建议有限 retry 或 resume。

`apply=safe` 的禁止范围不要在命令里重复维护；以 `therock-repairer` 的 permission、runner policy 和 `therock-testing` Safety Boundaries 为准。

## 输出必须包含

- run_id。
- round。
- 每个 task 的 repair policy。
- 将执行或建议执行的动作。
- 不执行的动作及原因。
- 需要写入的审计文件。
- 下一轮建议重跑任务。
- 如果执行了动作，提供命令、返回码、环境变化和 diff/patch 路径。
