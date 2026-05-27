# ROCM memory management support on AMD APUs? 

> **Issue #72**
> **状态**: closed
> **创建时间**: 2017-01-09T04:34:23Z
> **更新时间**: 2017-02-24T20:51:24Z
> **关闭时间**: 2017-02-24T20:51:24Z
> **作者**: VishwasRao17
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/72

## 负责人

- hthangirala

## 描述

Is it possible to reserve few addresses of DRAM as config registers during boot up ? I need to access the same physical address on each boot up . These will be a device config registers for my application research.
Can we modify the MMU for this requirement in ROCM platform ? 

---

## 评论 (1 条)

### 评论 #1 — hthangirala (2017-02-24T20:51:24Z)

It is not possible since this will bypass important protections provided by ASLR. However, you are welcome to modify the ROCK-Kernel-Driver for local experimentation.

---
