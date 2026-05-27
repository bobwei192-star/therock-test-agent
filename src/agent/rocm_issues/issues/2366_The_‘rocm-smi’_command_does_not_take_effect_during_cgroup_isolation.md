# The ‘rocm-smi’ command does not take effect during cgroup isolation

> **Issue #2366**
> **状态**: closed
> **创建时间**: 2023-08-04T02:33:30Z
> **更新时间**: 2024-03-02T03:41:00Z
> **关闭时间**: 2024-03-02T03:40:59Z
> **作者**: wjp-cn
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2366

## 描述

Hello, may I ask for your advice? I have encountered a problem. I have two GPUs with AMD. When I use the ‘rocm-smi’ command in a container that has applied for cgroup isolation of one GPU, it still displays two GPUs. Is this because the ‘rocm-smi’  command does not support cgroup isolation at the bottom level
