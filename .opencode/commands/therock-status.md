---
description: Show TheRock background test run status
agent: therock-loop
subtask: true
---

查看 TheRock 后台测试运行状态。

用户可能输入：

```text
$ARGUMENTS
```

用法：

```text
/therock-status run_id=<run_id>
```

如果用户没有提供 `run_id`，调用：

```bash
.opencode/tools/therock_agent.sh status
```

列出所有 run。

如果用户提供 `run_id`，调用：

```bash
.opencode/tools/therock_agent.sh status "<run_id>"
```

不要读取大量 stdout/stderr。默认使用 runner 的摘要输出即可。

输出解读：

- `status=running`：后台 runner 仍在运行。
- `status=waiting_for_opencode_debug`：runner 已完成当前失败轮次，正在等待 OpenCode 执行 `/therock-debug-round`、`/therock-repair-round apply=safe` 和 `/therock-resume` 编排。
- `status=stale`：`global_state.json` 仍是 running，但后台进程不存在，应提示用户 `/therock-resume run_id=<run_id>`。
- `status=passed/failed/interrupted/stopped`：run 已进入终态或被停止。
- `progress`：已完成 runnable task / runnable 总数。
- `counts`：pass/fail/skip/blocked/timeout 数量。
- `latest`：最近 task 事件摘要。

回复用户时必须包含：

- `run_id`
- status
- progress
- 当前 task
- elapsed
- pass/fail/skip/blocked 数量
- output 目录
