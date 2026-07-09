---
description: Regenerate TheRock loop test reports for an existing run
---

请调用项目内工具重新生成指定 run 的报告：

```bash
.opencode/tools/therock_agent.sh report "<run_id>"
```

生成后读取并总结：

- `runs/<run_id>/summary_report.md`
- `runs/<run_id>/failures/*.md`
- `runs/<run_id>/tool_calls.jsonl`
