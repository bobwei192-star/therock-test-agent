---
description: Stop a TheRock background test run safely
agent: therock-loop
subtask: true
---

安全停止 TheRock 后台测试 run。

用户原始参数：

```text
$ARGUMENTS
```

必须要求用户提供明确的 `run_id`。不要在没有 `run_id` 的情况下停止任何 run。

调用：

```bash
.opencode/tools/therock_agent.sh stop "<run_id>"
```

停止规则：

- 只停止由 runner `start-kv` 写入 `runner.pid.json` 的后台进程。
- 停止前 runner 会校验 pid 与 `run_id`。
- 停止后状态写为 `interrupted`。
- 不读取或处理 sudo 密码。
- 不扩大 GPU risk 测试范围。

停止后再调用：

```bash
.opencode/tools/therock_agent.sh status "<run_id>"
```

回复用户时包含：

- `run_id`
- 是否成功停止
- 当前 status
- output 目录
- resume 建议
