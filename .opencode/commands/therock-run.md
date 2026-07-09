---
description: Run TheRock loop tests with the rough shell runner
---

请调用项目内工具启动 TheRock 循环测试：

```bash
.opencode/tools/therock_agent.sh run \
  --therock-repo "<TheRock repo path>" \
  --artifacts "<output-linux-portable/build or output/build>" \
  --gpu "<gfx model, e.g. gfx1151>" \
  --components "<optional comma separated components>" \
  --test-types "<optional comma separated test types>" \
  --gpu-risk "skip" \
  --sudo-policy "${THEROCK_SUDO_POLICY:-none}"
```

规则：

- 默认 `--gpu-risk skip`，跳过 `component_sort_order.json` 中 `gpu_hang_risk=true` 的任务。
- 如果用户明确要求执行高风险任务，才允许改为 `include` 或 `quarantine`。
- 不要读取或要求用户提供 sudo 密码；如果 `.env` 中 `THEROCK_SUDO_POLICY=cache`，先提示用户在同一用户终端执行 `sudo -v`。
- 执行完成后读取 `runs/<run_id>/summary_report.md`，向用户总结结果和输出路径。
