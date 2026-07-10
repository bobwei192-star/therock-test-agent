---
description: Run TheRock loop tests through the OpenCode coordinator and deterministic runner
agent: therock-loop
subtask: true
---

启动 TheRock 循环测试。

参数：

优先支持 key=value 格式：

- `artifacts=<path>`：ARTIFACTS_PATH，必填绝对路径，例如 `/home/zs/TheRock/output-linux-portable/build` 或 `/output/build`
- `gpu=<gfx>`：THEROCK_AMDGPU_FAMILIES / AMDGPU_FAMILIES，必填，例如 `gfx1151`
- `components=<list>`：组件列表，可选，逗号分隔，例如 `hiprand,sanity`；传 `all` 表示全部组件
- `test_types=<list>`：测试类型，可选，逗号分隔，默认 `quick,standard,comprehensive,full`
- `gpu_risk=<skip|include|quarantine>`：GPU risk 策略，可选，默认 `skip`
- `sudo_policy=<none|cache|askpass>`：sudo 策略，可选，默认 `${THEROCK_SUDO_POLICY:-none}`
- `max_rounds=<n>`：最大 loop 轮数，可选，默认 runner 内置值
- `stable_threshold=<n>`：失败集稳定阈值，可选，默认 runner 内置值

也兼容旧位置参数：

- `$1`: ARTIFACTS_PATH
- `$2`: GPU family
- `$3`: components
- `$4`: test_types
- `$5`: gpu_risk

解析规则：

- key=value 输入时必须去掉 key 前缀，只把 value 传给 runner，例如 `components=amdsmi` 传 `--components "amdsmi"`，不要传 `--components "components=amdsmi"`。
- `sudo_policy`、`max_rounds`、`stable_threshold` 是独立参数，绝不能合并到 `--gpu-risk`。
- `--gpu-risk` 只允许 `skip`、`include`、`quarantine`。
- 如果 `artifacts` 是 `<你的真实build路径>`、空值或不存在，先向用户索要真实路径，不要启动 runner。

项目默认配置：

- `docs_this_project/component_sort_order.json`
- `docs_this_project/component_env_script_index.json`
- `docs_this_project/official_exclude.json`

请调用项目内工具启动测试：

```bash
.opencode/tools/therock_agent.sh run \
  --therock-repo "$(pwd)" \
  --artifacts "<artifacts_value>" \
  --amdgpu-families "<gpu_value>" \
  --component-config "docs_this_project/component_sort_order.json" \
  --component-env-index "docs_this_project/component_env_script_index.json" \
  --official-exclude "docs_this_project/official_exclude.json" \
  --sudo-policy "<sudo_policy_or_env_default>"
```

如果用户提供了可选参数，再追加：

- `components` 非空时追加 `--components "<components_value>"`；如果是 `all`，runner 会按 `component_sort_order.json` 执行全部组件
- `test_types` 非空时追加 `--test-types "<test_types_value>"`
- `gpu_risk` 非空时追加 `--gpu-risk "<gpu_risk_value>"`，否则保持 runner 默认 `skip`
- `max_rounds` 非空时追加 `--max-rounds "<max_rounds_value>"`
- `stable_threshold` 非空时追加 `--stable-threshold "<stable_threshold_value>"`

示例：

```bash
.opencode/tools/therock_agent.sh run \
  --therock-repo "$(pwd)" \
  --artifacts "/real/output/build" \
  --amdgpu-families "gfx1151" \
  --components "amdsmi" \
  --test-types "standard" \
  --gpu-risk "skip" \
  --sudo-policy "askpass" \
  --max-rounds 1 \
  --stable-threshold 1
```

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
