---
description: Regenerate TheRock loop test reports for an existing run
agent: therock-loop
subtask: true
---

按项目模板重新生成指定 run 的报告，并检查 runner 审计产物是否完整。

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
- `runs/<run_id>/agent_activity.jsonl`
- `runs/<run_id>/wrapper_changes.jsonl`
- `runs/<run_id>/global_state.json`

检查报告是否覆盖 `需求.md` 中的三类输出：

- 汇总测试报告：总任务数、pass/fail/skip/blocked/flaky、loop 失败集合变化、顽固失败任务、环境信息。
- 测试日志：每个任务 stdout / stderr / 执行命令 / 环境摘要。
- 单组件失败详细报告：组件、测试类型、失败命令、wrapper、失败日志、复现结果、根因分类、稳定性和处理建议。

额外检查：

- `Index 命中规则` 是否列出 entrypoint、script、env profiles、known issue。
- `Official exclude` 是否列出官方排除原因。
- `硬编码路径检测` 是否列出 `path_hardcode_detection`。
- `wrapper_changes.jsonl` 是否存在并能对应到 wrapper 文件。
- blocked 是否区分 `missing_artifacts`、`missing_dependency`、`sudo_unavailable`、`missing_env`。
