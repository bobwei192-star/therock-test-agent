# Disable P2P and large BAR support for mining machines

> **Issue #678**
> **状态**: closed
> **创建时间**: 2019-01-18T02:30:51Z
> **更新时间**: 2023-12-12T21:53:27Z
> **关闭时间**: 2023-12-12T21:53:27Z
> **作者**: nioroso-x3
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/678

## 描述

Hi, I'm having an issue with Intel consumer platform motherboards (Z270 and Z370), where the driver is unable to allocate large BARs for more than four rx vega 56/64.
This causes crashes and hangs when mining with ROCM using all GPUs, but no problems if using the PAL opencl libraries or when using ROCM selecting only the GPUS that had large BAR enabled.

Attachment is for dmesg output of a machine with 7 vega 64 cards.
[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/2771383/dmesg.txt)


---

## 评论 (2 条)

### 评论 #1 — tasso (2023-12-08T17:56:06Z)

Thanks for reaching out. Is this still an issue?  if not; can we please close it?

---

### 评论 #2 — tasso (2023-12-12T21:53:27Z)

Original ticket is more than a year old and the person that originally opened ticket  has not responded to the latest request.  If this is still an issue, please file a new ticket and we will be happy to investigate it.  Thanks!

---
