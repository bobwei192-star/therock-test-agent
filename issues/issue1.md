# Issue 1: GitHub Push 失败 - 大文件限制

## 问题描述

尝试将测试运行日志 `20260710_190554_105b10f6` push 到 GitHub 时失败，原因是日志文件超过 GitHub 的大小限制（100MB）。
cat /home/zs/therock-test-agent/20260710_190554_105b10f6.tar.gz.part_* > /home/zs/therock-test-agent/20260710_190554_105b10f6.tar.gz

## 错误信息

```
remote: error: File 20260710_190554_105b10f6/logs/rocwmma-standard.round1.stdout.log is 370.25 MB
remote: error: File 20260710_190554_105b10f6/logs/rocwmma-full.round1.stdout.log is 1268.35 MB
remote: error: File 20260710_190554_105b10f6/logs/rocwmma-comprehensive.round1.stdout.log is 370.23 MB
remote: error: GH001: Large files detected. You may want to try Git Large File Storage.
```

## 大文件列表

| 文件 | 大小 |
|------|------|
| `rocwmma-full.round1.stdout.log` | 1.2 GB |
| `rocwmma-standard.round1.stdout.log` | 370 MB |
| `rocwmma-comprehensive.round1.stdout.log` | 370 MB |

## 解决方案

### 方案 1：文件切割（临时方案）

```bash
# 切割文件，每块 36MB
split -b 36M 20260710_190554_105b10f6.tar.gz 20260710_190554_105b10f6.tar.gz.part_

# 合并文件（还原）
cat 20260710_190554_105b10f6.tar.gz.part_* > 20260710_190554_105b10f6.tar.gz
```

### 方案 2：添加 .gitignore（推荐）

在项目根目录添加 `.gitignore` 文件，排除大日志文件：

```gitignore
# 排除测试运行日志
*.tar.gz
runs/
*.log
```

### 方案 3：使用 Git LFS

```bash
# 安装 Git LFS
sudo apt install git-lfs
git lfs install

# 追踪大文件
git lfs track "*.log"
git lfs track "*.tar.gz"
```

## 阻塞任务记录

| 任务 | 缺少依赖 |
|------|----------|
| libhipcxx_hiprtc-quick/standard/comprehensive/full | `lit` |
| libhipcxx_hipcc-quick/standard/comprehensive/full | `lit` |
| tensilelite-quick/standard/comprehensive/full | `joblib`, `pytest`, `pytest-xdist` |
