---
description: Regenerate TheRock loop test reports for an existing run
agent: therock-loop
subtask: true
---

按项目模板重新生成指定 run 的报告。

模板来源：

- 汇总报告模板：`docs_this_project/汇总测试报告.md`
- 单组件问题模板：`docs_this_project/问题模板.md`

请调用项目内工具：

```bash
.opencode/tools/therock_agent.sh report "<run_id>"
```

生成后读取并总结：

- `runs/<run_id>/summary_report.md`
- `runs/<run_id>/failures/*.md`
- `runs/<run_id>/tool_calls.jsonl`

检查报告是否覆盖 `需求.md` 中的三类输出：

- 汇总测试报告：总任务数、pass/fail/skip/blocked/flaky、loop 失败集合变化、顽固失败任务、环境信息。
- 测试日志：每个任务 stdout / stderr / 执行命令 / 环境摘要。
- 单组件失败详细报告：组件、测试类型、失败命令、失败日志、复现结果、根因分类、稳定性和处理建议。
