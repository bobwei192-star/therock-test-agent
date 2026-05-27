# OpenCL 3.0 Released

> **Issue #1092**
> **状态**: closed
> **创建时间**: 2020-04-27T17:08:27Z
> **更新时间**: 2020-12-23T14:36:51Z
> **关闭时间**: 2020-04-28T01:35:56Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1092

## 描述

https://www.khronos.org/news/press/khronos-group-releases-opencl-3.0



---

## 评论 (2 条)

### 评论 #1 — Degerz (2020-04-27T19:29:45Z)

Huge step backwards compared to OpenCL 2.0, I'll call it for what it really is which is just a rehash of OpenCL 1.2 ... 

No point in AMD even trying anymore to implement OpenCL when they have their HIP API which is so much better ... 

---

### 评论 #2 — informatorius (2020-12-23T14:36:51Z)

I want to see OpenCL 3.0 too. e.g. For OpenCL, since OpenCL 2.2, the cl_khr_throttle_hints extension is defined and allows to specify the throttling that's needed.
It allows to create a command queue with CL_QUEUE_THROTTLE_KHR set to CL_QUEUE_THROTTLE_LOW_KHR (4). That tells the runtime it may run in a way that's optimized, with lowest energy consumption.

---
