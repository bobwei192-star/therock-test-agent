---
description: Resume an interrupted TheRock loop test run
---

请调用项目内工具恢复指定 run：

```bash
.opencode/tools/therock_agent.sh resume "<run_id>"
```

恢复后检查：

- `runs/<run_id>/global_state.json`
- `runs/<run_id>/summary_report.md`
- `runs/<run_id>/logs/`

如果恢复失败或 GPU / ROCm 健康检查不通过，停止继续执行并向用户说明原因。
