# Why does `flang` predefine `__PGLLVM__`?

> **Issue #1811**
> **状态**: closed
> **创建时间**: 2022-09-21T14:34:45Z
> **更新时间**: 2024-05-09T16:18:32Z
> **关闭时间**: 2024-05-09T16:18:32Z
> **作者**: bertwesarg
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1811

## 描述

This was pre-defined for the "classic" flang implementation. The new `flang` (based on `f18`, i.e., upstream) does not define it anymore.

---

## 评论 (2 条)

### 评论 #1 — bertwesarg (2022-09-21T15:18:09Z)

https://github.com/RadeonOpenCompute/llvm-project/blob/57b3d44fd613446a5ec0a535794715872057b4dc/clang/lib/Driver/ToolChains/AMDFlang.cpp#L711

---

### 评论 #2 — nartmada (2023-12-18T19:25:37Z)

Hi @bertwesarg, please check latest ROCm Documentation and ROCm 6.0.0 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---
