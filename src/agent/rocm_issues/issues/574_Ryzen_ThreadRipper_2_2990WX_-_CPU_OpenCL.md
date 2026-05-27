# Ryzen ThreadRipper 2 2990WX - CPU OpenCL

> **Issue #574**
> **状态**: closed
> **创建时间**: 2018-10-05T00:35:57Z
> **更新时间**: 2018-10-05T02:15:23Z
> **关闭时间**: 2018-10-05T02:15:23Z
> **作者**: farhan333
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/574

## 描述

I'm working with Ryzen ThreadRipper 2 2990WX and the GPU I'm using is an NVIDIA GPU. I need to run OpenCL Kernels on the CPU. Would it be possible with ROCM or is it not possible to run OpenCL on this CPU?

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2018-10-05T02:15:13Z)

Hi @farhan333 

The current AMD OpenCL runtimes that are a part of ROCm do not support CPU targets. You may want to look into other runtimes, such as [pocl](http://portablecl.org/).

---
