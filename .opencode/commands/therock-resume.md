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
- `runs/<run_id>/summary_report.md`
- `runs/<run_id>/logs/`
- `runs/<run_id>/wrappers/`
- `runs/<run_id>/wrapper_changes.jsonl`
- `runs/<run_id>/agent_activity.jsonl`
- `runs/<run_id>/tool_calls.jsonl`

如果恢复失败或 GPU / ROCm 健康检查不通过，停止继续执行并向用户说明原因。

恢复规则：

- 不从聊天上下文推断失败集，必须读取 `global_state.json`。
- 如果上次中断时 `current_task` 非空，runner 会把该 task 放回 `next_tasks`。
- 如果涉及 `sudo_sensitive`，仍然遵守 `THEROCK_SUDO_POLICY=cache` + 手动 `sudo -v`，或通过 `./scripts/therock-sudo-agent run -- opencode` 启动的 `THEROCK_SUDO_POLICY=askpass` 会话。
- GPU reset 后不要自动扩大测试范围。
