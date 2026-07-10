---
description: Generate TheRock debug analysis for a failed round with OpenCode
agent: therock-debugger
subtask: true
---

为某个 TheRock run 的失败轮次生成 debug analysis。这个命令使用 OpenCode 原生读取、推理和写文件能力，不由 runner 做问题分析，也不执行修复。

用户参数：

```text
$ARGUMENTS
```

支持：

- `run_id=<run_id>`：必填，目标 run。
- `round=<N>`：可选，指定轮次；缺省时分析最近失败轮次。
- `output_root=<path>`：可选，run 根目录；缺省使用 `runs`。

## 必须使用的 skill

使用：

- `therock-debugging`
- 必要时参考 `therock-testing`

## 行为

1. 定位 run 目录和 `global_state.json`。
2. 如需要，调用：

```bash
.opencode/tools/therock_agent.sh status "<run_id>"
```

3. 读取：
   - `round_analysis/round<N>_inputs.json`
   - `debug/round<N>_failure_index.json`
   - 必要时读取对应 `failures/*_failure.json`
   - 必要时读取对应 `logs/*.round<N>.stdout.log` / `.stderr.log`
4. 由 OpenCode 分析每个 task 的：
   - `classification`
   - `root_cause`
   - `next_action`
   - `repair_policy`
   - `repairable`
5. 写入：
   - `round_analysis/round<N>.json`
   - `round_analysis/round<N>.md`
   - `debug/round<N>_log_excerpt.md`
6. 写完后必须验证这 3 个文件真实存在且 `round_analysis/round<N>.json` 是合法 JSON。
7. 向 `progress.jsonl` 追加 `opencode_debug_written` 事件。
8. 输出 debug 结论。

## 成功判定

只有当以下文件都存在时，才允许回复“debug analysis 已完成”：

- `round_analysis/round<N>.json`
- `round_analysis/round<N>.md`
- `debug/round<N>_log_excerpt.md`

如果任一文件创建失败，必须停止并报告缺失路径；不要继续进入 repair。

## 权限与边界

本命令只生成 debug analysis。执行边界以 `therock-debugger` permission、runner policy 和 `therock-testing` Safety Boundaries 为准。

## 回复必须包含

- run_id。
- round。
- 失败任务数。
- 每个失败 task 的分类和 `next_action`。
- 关键证据路径。
- 是否建议继续 `/therock-repair-round`。
- 如果 runner 输入文件缺失，说明缺哪些文件。
