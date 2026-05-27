# What is limit on the maximum number of VGPR (vector registers) for one work-item in MI100?

> **Issue #1784**
> **状态**: closed
> **创建时间**: 2022-08-13T09:24:55Z
> **更新时间**: 2022-08-15T13:22:52Z
> **关闭时间**: 2022-08-15T13:22:52Z
> **作者**: vasslavich
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1784

## 描述

Hello, does anyone know if there is some kind of limit on the maximum number of VGPR for a single work-item in MI100?
Thanks!

---

## 评论 (2 条)

### 评论 #1 — b-sumner (2022-08-13T16:08:52Z)

The ISA can't encode more than 256.  And since there is a physical limit, the number a wave/warp can get depends on the size of the work-group.  For example, with a work group size of 1024, you can have at most 64 registers per work-item.

---

### 评论 #2 — vasslavich (2022-08-15T13:22:52Z)

@b-sumner , thank you very much!

---
