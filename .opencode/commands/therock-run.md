---
description: Run TheRock loop tests with the rough shell runner
agent: therock-loop
subtask: true
---

启动 TheRock 循环测试。

参数：

- `$1`: ARTIFACTS_PATH，必填绝对路径，例如 `/home/zs/TheRock/output-linux-portable/build` 或 `/output/build`
- `$2`: THEROCK_AMDGPU_FAMILIES / AMDGPU_FAMILIES，必填，例如 `gfx1151`
- `$3`: 组件列表，可选，逗号分隔，例如 `hiprand,sanity`
- `$4`: 测试类型，可选，逗号分隔，默认 `quick,standard,comprehensive,full`
- `$5`: GPU risk 策略，可选，默认 `skip`

请调用项目内工具启动测试：

```bash
.opencode/tools/therock_agent.sh run \
  --therock-repo "$(pwd)" \
  --artifacts "$1" \
  --amdgpu-families "$2" \
  --sudo-policy "${THEROCK_SUDO_POLICY:-none}"
```

如果用户提供了可选参数，再追加：

- `$3` 非空时追加 `--components "$3"`
- `$4` 非空时追加 `--test-types "$4"`
- `$5` 非空时追加 `--gpu-risk "$5"`，否则保持 runner 默认 `skip`

规则：

- 默认 `--gpu-risk skip`，跳过 `component_sort_order.json` 中 `gpu_hang_risk=true` 的任务。
- 如果用户明确要求执行高风险任务，才允许改为 `include` 或 `quarantine`。
- 不要读取或要求用户提供 sudo 密码；如果 `.env` 中 `THEROCK_SUDO_POLICY=cache`，先提示用户在同一用户终端执行 `sudo -v`。
- 执行完成后读取 `runs/<run_id>/summary_report.md`，向用户总结结果和输出路径。
