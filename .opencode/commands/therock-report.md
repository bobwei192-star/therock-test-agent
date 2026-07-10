---
description: Regenerate TheRock loop test reports for an existing run
agent: therock-loop
subtask: true
---

刷新指定 run 的 runner JSON 报告，并由 `therock-reporter` 生成 Markdown 总结。

请调用项目内工具：

```bash
.opencode/tools/therock_agent.sh report "<run_id>"
```

生成后读取并总结：

- `runs/<run_id>/summary.json`
- `runs/<run_id>/failures.json`
- `runs/<run_id>/failures/*_failure.json`
- `runs/<run_id>/tool_calls.jsonl`
- `runs/<run_id>/agent_activity.jsonl`
- `runs/<run_id>/wrapper_changes.jsonl`
- `runs/<run_id>/global_state.json`

Markdown 输出由 `therock-reporter` 从 JSON 生成：

- `runs/<run_id>/summary_report.md`
- `runs/<run_id>/failures/*_failure_report.md`

检查报告是否覆盖 `需求.md` 中的三类输出：

- 汇总测试报告：总任务数、pass/fail/skip/blocked/flaky、loop 失败集合变化、顽固失败任务、环境信息。
- 测试日志：每个任务 stdout / stderr / 执行命令 / 环境摘要。
- 单组件失败详细报告：组件、测试类型、失败命令、wrapper、失败日志、复现结果、根因分类、稳定性和处理建议。

额外检查这些字段是否在 JSON 中存在，Markdown 由 reporter 组织呈现。
