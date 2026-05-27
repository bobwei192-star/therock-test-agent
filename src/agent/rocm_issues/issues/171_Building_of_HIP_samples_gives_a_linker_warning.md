# Building of HIP samples gives a linker warning

> **Issue #171**
> **状态**: closed
> **创建时间**: 2017-07-27T08:53:04Z
> **更新时间**: 2018-06-03T14:55:24Z
> **关闭时间**: 2018-06-03T14:55:24Z
> **作者**: ekondis
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/171

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 负责人

- bensander
- scchan

## 描述

Compiling HIP sample programs gives a linker warning (ROCm 1.6.1). For instance, compiling hipDispatchLatency gives:

/opt/rocm/hip/bin/hipcc -O3 hipDispatchLatency.cpp ResultDatabase.cpp -o hipDispatchLatency
WARNING: Linking two modules of different data layouts: '/tmp/tmp.3MJGOayIJI/hipDispatchLatency-c45406.kernel.bc' is '' whereas 'llvm-link' is 'e-p:64:64-p1:64:64-p2:64:64-p3:32:32-p4:32:32-p5:32:32-i64:64-v16:16-v24:32-v32:32-v48:64-v96:128-v192:256-v256:256-v512:512-v1024:1024-v2048:2048-n32:64-A5'

The compiled executable runs fine, though.


---

## 评论 (1 条)

### 评论 #1 — scchan (2017-08-03T20:24:04Z)

The warning is benign and we've developed a fix for it in hcc
https://github.com/RadeonOpenCompute/hcc/pull/413

---
