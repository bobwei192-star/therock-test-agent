# ROCm Support for Radeon Pro 5600M

> **Issue #1172**
> **状态**: closed
> **创建时间**: 2020-07-02T07:02:09Z
> **更新时间**: 2023-08-30T17:00:33Z
> **关闭时间**: 2020-12-17T04:19:04Z
> **作者**: strategist922
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1172

## 描述

I check the document and repo of ROCm (http://repo.radeon.com/rocm/apt/3.5/pool/main/m/)
It seems only support architecture gfx900 and gfx906 at this moment.

I check the hardware spec. and LLVM doc on https://llvm.org/docs/AMDGPUUsage.html, it shows 
the new Radeon Pro 5600M's architecture should be gfx1011 with 40 CU.

May I know when will ROCm officially support new Radeon Pro 5600M?

Thanks and best regards,
  

---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2020-12-17T04:19:04Z)

Hi @strategist922 
Thanks for reaching out.
Currently we are not supporting Radeon 5000 series with ROCm.
We will update the docs with the supported config in future, once we have plans.
Thank you.

---

### 评论 #2 — unexploredtest (2020-12-17T05:25:10Z)

@ROCmSupport wait, there are no plans for Radeon 5000 series, just 6000?

---

### 评论 #3 — ROCmSupport (2020-12-17T05:31:49Z)

Hi @aliPMPAINT 
Am not commenting about Radeon 5000 future plans because I do not have handy information.
We will definitely share the information in future if any.

---

### 评论 #4 — Umang-Kumar (2023-08-30T17:00:33Z)

Hey @ROCmSupport do we have that functionality now, cause I've got a Radeon RX5600M GPU and was wondering if I can use ROCM on that..??

---
