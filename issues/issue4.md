# Issue 4: TheRock Agent 执行模型分析

## 问题描述

用户观察到测试运行时显示 "Round 1: executing 5 task(s)"，误以为是并发执行。实际分析后确认是串行执行模型。

## 执行模型：串行执行

### 代码证据

通过分析 `.opencode/tools/therock_agent/cli.py` 和 `.opencode/tools/therock_agent/executor.py`：

```python
# cli.py:543-575 - run_loop 函数
while state["schedule"].get("round_pending_tasks"):
    task_id = state["schedule"]["round_pending_tasks"][0]  # 一次取一个任务
    result = run_task(state, task, round_no)  # 同步执行，阻塞等待完成
```

```python
# executor.py:217-234 - run_task 函数使用 subprocess.run()
proc = subprocess.run(
    executable_command,
    cwd=cwd,
    env=os.environ.copy(),
    stdout=stdout_handle,
    stderr=stderr_handle,
    text=True,
)
```

### 关键证据

1. `run_task()` 使用 `subprocess.run()`，**阻塞等待**任务完成
2. 没有使用多线程、多进程或异步执行
3. 每次只执行一个任务，完成后才执行下一个

### 进程状态验证

```bash
$ ps aux | grep -E "(ctest|test_runner|therock)" | grep -v grep
zs       1243723  0.0  0.0  18824  3864 ?        Ss   10:04   0:00 bash /home/zs/TheRock/.opencode/tools/therock_agent.sh resume ...
zs       1243727  0.0  0.0  42952 22376 ?        S    10:04   0:00 python3 -m therock_agent.cli ...
```

只有 2 个进程：1 个 bash 包装进程 + 1 个 Python 主进程，**没有并发执行的测试进程**。

## "Round 1: executing 5 task(s)" 的含义

显示 "executing 5 task(s)" 指的是**这一轮还有 5 个任务待执行**，**不是同时执行 5 个**。

从 `agent_activity.jsonl` 可以看到任务是逐个开始的：

```
2026-07-13T09:47:34 → rocprim-full task_start
2026-07-13T10:04:56 → rocprim-full task_start (resume后)
```

## 设计原因

| 设计考虑 | 说明 |
|---------|------|
| GPU 资源 | 单张 GPU，并发会导致资源竞争 |
| 内存限制 | 测试任务内存占用大，并发容易 OOM |
| 日志清晰 | 串行执行日志顺序清晰，便于排查问题 |
| 状态管理 | 简单的状态机，无需处理并发冲突 |

## 执行流程

```
┌─────────────────────────────────────────────────────────────────┐
│                      Run Loop (Round 1)                        │
├─────────────────────────────────────────────────────────────────┤
│  round_pending_tasks = [task1, task2, task3, ...]              │
│                                                                 │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐      │
│  │ task1 开始   │───▶│ task1 结束   │───▶│ task2 开始   │───▶   │
│  │ subprocess   │    │ (同步等待)   │    │ subprocess   │      │
│  │ run()        │    │              │    │ run()        │      │
│  └──────────────┘    └──────────────┘    └──────────────┘      │
│         ↓                  ↓                  ↓                 │
│    记录状态           记录状态           记录状态                │
│                                                                 │
│  失败任务进入下一轮重试，成功任务标记为 completed                 │
└─────────────────────────────────────────────────────────────────┘
```

## 结论

**TheRock agent 是串行执行模型，不是并发执行。** 每次只运行一个测试任务，完成后再执行下一个。这是设计上的选择，主要考虑 GPU 资源和内存限制。

## 并发执行方案

如果需要并发执行，可以考虑：

1. **配置多张 GPU**：每个 GPU 执行不同的测试任务
2. **修改 executor.py**：使用 `subprocess.Popen` 异步执行
3. **使用 concurrent.futures**：线程池/进程池并发执行
