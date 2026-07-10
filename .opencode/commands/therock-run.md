---
description: Run TheRock loop tests through the OpenCode coordinator and deterministic runner
agent: therock-loop
subtask: true
---

启动 TheRock 循环测试。不要在 prompt 层手工拆解参数；必须把用户输入原文交给 runner 的 `run-kv` 子命令，由 Python 代码做确定性解析。

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

请调用项目内工具启动测试，必须使用这一条：

```bash
.opencode/tools/therock_agent.sh run-kv $ARGUMENTS
```

`run-kv` 会把 `artifacts=/real/output/build gpu=gfx1151 components=amdsmi test_types=standard sudo_policy=askpass max_rounds=1 stable_threshold=1` 解析为对应 runner flags。

规则：

- 默认 `--gpu-risk skip`，跳过 `gpu_hang_risk=true` 的任务。
- 如果用户明确要求执行高风险任务，才允许改为 `include` 或 `quarantine`。
- 组件入口由 `component_env_script_index.json` 决定，不要在 command 里猜脚本。
- 官方排除由 `official_exclude.json` 决定，命中后不要执行。
- 不要读取或要求用户提供 sudo 密码。
- 如果本次任务包含 `sudo_sensitive` 组件，`THEROCK_SUDO_POLICY=cache` 需要已有 sudo cache，`THEROCK_SUDO_POLICY=askpass` 建议通过 `./scripts/therock-sudo-agent run -- opencode` 启动 OpenCode。
- 非 sudo 组件不应因为 `THEROCK_SUDO_POLICY=cache` 但 sudo cache 失效而被启动前拦住。
- `sudo_sensitive` 任务没有可用 sudo cache 或 askpass agent 时应 blocked。
- 执行完成后读取 `runs/<run_id>/summary_report.md` 和 `global_state.json`，向用户总结结果和输出路径。

完成后必须检查并总结：

- `runs/<run_id>/summary_report.md`
- `runs/<run_id>/global_state.json`
- `runs/<run_id>/wrapper_changes.jsonl`
- `runs/<run_id>/agent_activity.jsonl`
- `runs/<run_id>/tool_calls.jsonl`
- `runs/<run_id>/failures/`

回复用户时必须包含：

- `run_id`
- 输出目录
- pass / fail / skip / blocked 数量
- official exclude 命中项
- sudo blocked 项
- GPU risk skipped / quarantined 项
- wrapper 目录和 wrapper 变更日志
