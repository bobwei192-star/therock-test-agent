---
description: Run TheRock loop tests through the OpenCode coordinator and deterministic runner
agent: therock-loop
subtask: true
---

启动 TheRock 循环测试。

参数：

- `$1`: ARTIFACTS_PATH，必填绝对路径，例如 `/home/zs/TheRock/output-linux-portable/build` 或 `/output/build`
- `$2`: THEROCK_AMDGPU_FAMILIES / AMDGPU_FAMILIES，必填，例如 `gfx1151`
- `$3`: 组件列表，可选，逗号分隔，例如 `hiprand,sanity`；传 `all` 表示全部组件
- `$4`: 测试类型，可选，逗号分隔，默认 `quick,standard,comprehensive,full`
- `$5`: GPU risk 策略，可选，默认 `skip`，可选 `include` / `quarantine`

项目默认配置：

- `docs_this_project/component_sort_order.json`
- `docs_this_project/component_env_script_index.json`
- `docs_this_project/official_exclude.json`

请调用项目内工具启动测试：

```bash
.opencode/tools/therock_agent.sh run \
  --therock-repo "$(pwd)" \
  --artifacts "$1" \
  --amdgpu-families "$2" \
  --component-config "docs_this_project/component_sort_order.json" \
  --component-env-index "docs_this_project/component_env_script_index.json" \
  --official-exclude "docs_this_project/official_exclude.json" \
  --sudo-policy "${THEROCK_SUDO_POLICY:-none}"
```

如果用户提供了可选参数，再追加：

- `$3` 非空时追加 `--components "$3"`；如果是 `all`，runner 会按 `component_sort_order.json` 执行全部组件
- `$4` 非空时追加 `--test-types "$4"`
- `$5` 非空时追加 `--gpu-risk "$5"`，否则保持 runner 默认 `skip`

规则：

- 默认 `--gpu-risk skip`，跳过 `gpu_hang_risk=true` 的任务。
- 如果用户明确要求执行高风险任务，才允许改为 `include` 或 `quarantine`。
- 组件入口由 `component_env_script_index.json` 决定，不要在 command 里猜脚本。
- 官方排除由 `official_exclude.json` 决定，命中后不要执行。
- 不要读取或要求用户提供 sudo 密码；如果 `.env` 中 `THEROCK_SUDO_POLICY=cache`，先提示用户在同一用户终端执行 `sudo -v`。
- `sudo_sensitive` 任务没有可用 sudo cache 时应 blocked。
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
