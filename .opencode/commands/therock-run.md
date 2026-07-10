---
description: Start TheRock loop tests in the background through the deterministic runner
agent: therock-loop
subtask: true
---

启动 TheRock 全自动循环测试。不要在 prompt 层手工拆解参数；必须把用户输入原文交给 runner 的 `start-kv` 子命令，由 Python 代码做确定性解析。

重要：测试执行仍由后台 runner 完成，问题分析、debug 建议和 safe repair 由 OpenCode 原生 agent 完成。本命令默认执行全自动编排，不只是启动后台任务。

用户原始参数：

```text
$ARGUMENTS
```

支持 key=value 格式：

- `artifacts=<path>`：ARTIFACTS_PATH，必填绝对路径，例如 `/home/zs/TheRock/output-linux-portable/build` 或 `/output/build`
- `gpu=<gfx>`：THEROCK_AMDGPU_FAMILIES / AMDGPU_FAMILIES，必填，例如 `gfx1151`
- `components=<list>`：组件列表，可选，逗号分隔，例如 `hiprand,sanity`；传 `all` 表示全部组件
- `test_types=<list>`：测试类型，可选，逗号分隔，默认 `quick,standard,comprehensive,full`
- `gpu_risk=<skip|include|quarantine>`：GPU risk 策略，可选，默认 `skip`
- `sudo_policy=<none|cache|askpass>`：sudo 策略，可选，默认 `${THEROCK_SUDO_POLICY:-none}`
- `max_rounds=<n>`：最大 loop 轮数，可选，默认 runner 内置值
- `stable_threshold=<n>`：失败集稳定阈值，可选，默认 runner 内置值
- `debug_repair=<opencode|off>`：debug/repair 编排模式，可选，默认 `opencode`

解析规则：

- 不要自己去掉 key 前缀，不要自己拼 `--components` / `--gpu-risk` 等 flags。
- 不要把 `artifacts=...`、`gpu=...` 等原始 token 当作 runner flag value。
- `sudo_policy`、`max_rounds`、`stable_threshold` 是独立参数，绝不能合并到 `--gpu-risk`。
- `--gpu-risk` 只允许 `skip`、`include`、`quarantine`。
- 如果 runner 返回 artifacts 缺失或路径不存在，再向用户索要真实路径。

项目默认配置：

- `docs_this_project/component_sort_order.json`
- `docs_this_project/component_env_script_index.json`
- `docs_this_project/official_exclude.json`

请调用项目内工具后台启动测试，必须使用这一条：

```bash
.opencode/tools/therock_agent.sh start-kv $ARGUMENTS debug_repair=opencode
```

如果用户显式传了 `debug_repair=off`，尊重用户输入，不再追加 `debug_repair=opencode`。

`start-kv` 会把 `artifacts=/real/output/build gpu=gfx1151 components=amdsmi test_types=standard sudo_policy=askpass max_rounds=1 stable_threshold=1 debug_repair=opencode` 解析为对应 runner flags，创建 `runs/<run_id>/global_state.json`，然后在后台执行内部入口 `_run-existing <run_id>`。

## 全自动 OpenCode 编排

启动后不要只返回 `run_id` 就结束。默认继续执行：

1. 调用 `/therock-status run_id=<run_id>` 或 runner `status` 观察状态。
2. 如果状态为 `running`，继续等待或提示用户可随时查询。
3. 如果状态为 `waiting_for_opencode_debug`：
   - 调用 `/therock-debug-round run_id=<run_id> round=<current_loop>`，由 OpenCode 生成 `round_analysis/round<N>.json/.md` 和 `debug/round<N>_log_excerpt.md`。
   - 调用 `/therock-repair-round run_id=<run_id> round=<current_loop> apply=safe`，由 OpenCode 执行 `safe_auto` 修复并写 `repairs/**`。
   - 调用 `/therock-resume run_id=<run_id>` 进入下一轮验证。
4. 重复上述过程，直到状态为 `passed`、`failed`、`interrupted` 或需要人工确认。

规则：

- 默认 `--gpu-risk skip`，跳过 `gpu_hang_risk=true` 的任务。
- 如果用户明确要求执行高风险任务，才允许改为 `include` 或 `quarantine`。
- 组件入口由 `component_env_script_index.json` 决定，不要在 command 里猜脚本。
- 官方排除由 `official_exclude.json` 决定，命中后不要执行。
- 不要读取或要求用户提供 sudo 密码。
- 如果本次任务包含 `sudo_sensitive` 组件，`THEROCK_SUDO_POLICY=cache` 需要已有 sudo cache，`THEROCK_SUDO_POLICY=askpass` 建议通过 `./scripts/therock-sudo-agent run -- opencode` 启动 OpenCode。
- 非 sudo 组件不应因为 `THEROCK_SUDO_POLICY=cache` 但 sudo cache 失效而被启动前拦住。
- `sudo_sensitive` 任务没有可用 sudo cache 或 askpass agent 时应 blocked。
- 启动后向用户返回 `run_id`、输出目录、runnable/skipped 数量，以及当前自动编排阶段。
- 不要假装测试已经完成；每次推进前都以 `global_state.json` / `status` 为准。

启动后必须检查并总结：

- `runs/<run_id>/global_state.json`
- `runs/<run_id>/agent_activity.jsonl`
- `runs/<run_id>/runner.pid.json`
- `runs/<run_id>/progress.jsonl`

回复用户时必须包含：

- `run_id`
- 输出目录
- 后台 backend
- runnable / skipped 数量
- status 查询命令
- report 命令
