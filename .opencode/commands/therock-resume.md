---
description: Resume an interrupted TheRock loop test run
agent: therock-loop
subtask: true
---

请调用项目内工具恢复指定 run：

```bash
.opencode/tools/therock_agent.sh resume "<run_id>" \
  --sudo-policy "${THEROCK_SUDO_POLICY:-none}"
```

恢复后检查：

- `runs/<run_id>/global_state.json`
- `runs/<run_id>/summary.json`
- `runs/<run_id>/failures.json`
- `runs/<run_id>/logs/`
- `runs/<run_id>/wrappers/`
- `runs/<run_id>/wrapper_changes.jsonl`
- `runs/<run_id>/agent_activity.jsonl`
- `runs/<run_id>/tool_calls.jsonl`

如果恢复失败或 GPU / ROCm 健康检查不通过，停止继续执行并向用户说明原因。

恢复规则：

- 不从聊天上下文推断失败集，必须读取 `global_state.json`。
- 如果 `status=stale` 或上次中断时存在未完成 task，runner 会结合 `progress.jsonl` 和 `global_state.json` 找到 start 但没有 end 的 task，并放回当前轮 pending 队列。
- 已经 pass 且写入结果的 task 不应重复执行。
- 如果涉及 `sudo_sensitive`，仍然遵守 `THEROCK_SUDO_POLICY=cache` + 手动 `sudo -v`，或通过 `./scripts/therock-sudo-agent run -- opencode` 启动的 `THEROCK_SUDO_POLICY=askpass` 会话。
- GPU reset 后不要自动扩大测试范围。
