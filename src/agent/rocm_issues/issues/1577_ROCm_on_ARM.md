# ROCm on ARM

> **Issue #1577**
> **状态**: closed
> **创建时间**: 2021-09-24T15:18:09Z
> **更新时间**: 2024-11-08T19:04:49Z
> **关闭时间**: 2021-09-27T10:48:47Z
> **作者**: Sturmflut
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1577

## 描述

We are extending our ARM testbed and will get some nodes with an Ampere Q80 ARM CPU and two MI100 GPUs to match the NVIDIA ARM HPC Development Kits (Ampere Q80 ARM CPU and A100 GPUs) we are also getting. We know ROCm isn't officially supported on ARM yet (although ARM support has been announced at least back in 2016 and 2017), but it's worth the try.

What is the current status on ARM? Are there source RPMs available for the packages offered at https://repo.radeon.com/rocm/yum/rpm/ ? That would make it easier to try to build all the software.

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-09-27T10:48:47Z)

Hi @Sturmflut 
Thanks for reaching out.
We are not supporting ROCm on ARM right now.
We are not creating src content for the packages available. I will discuss once again with BU team and share some update on this, if any. 

---

### 评论 #2 — Bigsmart408 (2024-06-26T10:49:26Z)

Is arm supported now?

---

### 评论 #3 — geerlingguy (2024-11-08T19:04:47Z)

@Bigsmart408 - No; see https://github.com/ROCm/ROCm/issues/3960

---
