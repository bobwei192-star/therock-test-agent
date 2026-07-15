# Issue 7: WSL/WSL2 环境识别与报告标识缺失

## 问题描述

当前测试代理原先只按常规 Linux ROCm 设备模型理解 GPU 环境，未区分原生 Linux、WSL 和 WSL2。WSL2 ROCm 的典型设备模型不是 `/dev/kfd`、`/dev/dri`，而是通过 `/dev/dxg` 暴露 GPU。如果代理继续按原生 Linux 设备模型判断，容易把正常的 WSL2 环境误判为设备缺失，或者在报告中无法解释为什么没有 `/dev/kfd`、`/dev/dri`。

典型 WSL2 环境如下：

```bash
sut1@NucBoxEVO-X2:/mnt/c/Users/sut1$ uname -a
Linux NucBoxEVO-X2 6.18.35.2-microsoft-standard-WSL2 #1 SMP PREEMPT_DYNAMIC Wed Jun 17 23:14:00 UTC 2026 x86_64 x86_64 x86_64 GNU/Linux

sut1@NucBoxEVO-X2:/mnt/c/Users/sut1$ ls -l /dev/dxg
crw-rw-rw- 1 root root 10, 258 Jul 15 15:21 /dev/dxg

sut1@NucBoxEVO-X2:/mnt/c/Users/sut1$ ls -l /dev/dri
ls: cannot access '/dev/dri': No such file or directory

sut1@NucBoxEVO-X2:/mnt/c/Users/sut1$ ls -l /dev/kfd
ls: cannot access '/dev/kfd': No such file or directory
```

## 影响

- 报告无法直接看出本次运行是在 `linux`、`wsl` 还是 `wsl2` 下执行。
- WSL2 下 `/dev/kfd`、`/dev/dri` 缺失属于预期现象，但原先没有明确记录。
- 如果 WSL2 缺少 `/dev/dxg`，代理应在任务执行前给出清晰的 `missing_wsl_dxg` 阻断原因。
- 失败报告、汇总报告和事件日志缺少统一的运行环境标签，不利于后续归档和对比。

## 修复要求

- 新增运行环境检测，识别 `linux`、`linux-rocm`、`wsl`、`wsl2-dxg`、`wsl2-missing-dxg`。
- 在 `environment_summary.json` 中记录 `runtime_label`、kernel 信息和 `/dev/dxg`、`/dev/kfd`、`/dev/dri` 状态。
- 在 WSL2 下将 `/dev/dxg` 作为 ROCm GPU 访问的关键预检条件。
- 在 WSL2 报告中明确说明 `/dev/kfd`、`/dev/dri` 通常不存在，不应按原生 Linux 误判。
- 在 `summary.json`、`failures.json`、单项 failure JSON、`agent_activity.jsonl`、`tool_calls.jsonl` 中写入 `runtime_label`。
- 保持现有 task stdout/stderr 日志文件名兼容，不把运行环境拼进文件名，避免破坏已有脚本；通过 JSON 字段和事件日志体现 WSL/WSL2 环境。

## 当前处理

已增加 `therock_agent.runtime` 运行环境检测模块，并把检测结果接入状态创建、预检、汇总报告、失败报告、任务结果、活动日志和工具调用日志。

## 验收标准

- WSL2 且存在 `/dev/dxg` 时，`runtime_label` 应为 `wsl2-dxg`。
- WSL2 且缺少 `/dev/dxg` 时，任务应在执行前阻断，错误以 `missing_wsl_dxg:` 开头。
- `environment_summary.json`、`summary.json`、`failures.json`、单项 failure JSON、`agent_activity.jsonl`、`tool_calls.jsonl` 均能看到 `runtime_label`。
- 原有日志路径如 `logs/<task_id>.round<round>.stdout.log` 和 `logs/<task_id>.round<round>.stderr.log` 保持不变。