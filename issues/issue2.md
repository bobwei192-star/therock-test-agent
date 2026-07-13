# Issue 2: Resume 命令参数错误与状态分析

## 问题描述

尝试使用 `therock_agent.sh resume` 命令恢复测试运行时，使用了错误的参数 `--therock-repo`，导致命令执行失败。

## 关键发现

1. **resume 命令不支持 `--therock-repo` 参数**
2. **resume 命令需要 `--output-root` 参数**指定状态文件所在目录
3. **状态文件中已保存所有必要配置**，无需重复传入

## Resume 命令正确用法

```bash
# 基本用法
.opencode/tools/therock_agent.sh resume <run_id> --output-root <状态文件目录>

# 示例
.opencode/tools/therock_agent.sh resume 20260710_190554_105b10f6 \
  --output-root "/home/zs/TheRock/runs" \
  --sudo-policy "cache"
```

## Resume 命令参数说明

| 参数 | 说明 | 必填 |
|------|------|------|
| `<run_id>` | 运行 ID（位置参数） | 是 |
| `--output-root` | 状态文件所在目录 | 是（状态文件不在默认位置时） |
| `--sudo-policy` | sudo 策略：none/cache/askpass | 否 |

## 运行状态分析（Run ID: 20260710_190554_105b10f6）

### 运行概览

| 项目 | 值 |
|------|-----|
| 运行ID | 20260710_190554_105b10f6 |
| 开始时间 | 2026-07-10T19:05:54+08:00 |
| 结束时间 | 未设置（进程被中断） |
| 最终状态 | running（但进程已死） |
| 当前轮数 | 1（只运行了 Round 1） |
| GPU 型号 | gfx1151 |
| 中断信号 | signal:15 (SIGTERM) |

### 任务统计

```
总任务数: 112
已完成:   83
阻塞:     12
待执行:   17 (实际)
```

### 阻塞任务

| 任务 | 缺少依赖 |
|------|----------|
| libhipcxx_hiprtc-quick/standard/comprehensive/full | `lit` |
| libhipcxx_hipcc-quick/standard/comprehensive/full | `lit` |
| tensilelite-quick/standard/comprehensive/full | `joblib`, `pytest`, `pytest-xdist` |

### 中断原因

**SIGTERM (signal:15)** - 进程收到了终止信号，可能原因：

| 可能原因 | 说明 |
|---------|------|
| OpenCode 超时 | OpenCode 对长时间运行的进程设置了超时限制（运行了约 10 小时） |
| 用户手动 stop | 执行了 `.opencode/tools/therock_agent.sh stop` 命令 |
| 系统重启 | 系统关机或重启时发送 SIGTERM |

> **不是 OOM Killer**（OOM 发送的是 SIGKILL signal:9）

## 恢复步骤

```bash
# 1. 安装缺失依赖
pip install lit joblib pytest pytest-xdist prettytable

# 2. 恢复运行
.opencode/tools/therock_agent.sh resume 20260710_190554_105b10f6 \
  --output-root "/home/zs/TheRock/runs" \
  --sudo-policy "cache"
```

## 运行配置

```json
{
  "therock_repo_path": "/home/zs/TheRock",
  "artifacts_path": "/home/zs/TheRock/output-linux-portable/build",
  "gpu_model": "gfx1151",
  "sudo_policy": "askpass",
  "max_rounds": 10,
  "stable_threshold": 3
}
```
