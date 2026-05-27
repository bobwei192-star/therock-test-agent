# Different results of CUDA/HIP kernels on Nvidia/AMD GPUs

> **Issue #1380**
> **状态**: closed
> **创建时间**: 2021-02-13T18:49:44Z
> **更新时间**: 2022-03-19T18:26:53Z
> **关闭时间**: 2021-04-06T06:29:59Z
> **作者**: DTolm
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1380

## 描述

Hello,

I have a kernel, that uploads 4096 float2 numbers with 512 threads (each stores 8 numbers) and does some reordering using 32KB of statically allocated shared memory. CUDA version run on Nvidia 1660Ti GPU produces the correct result. HIP version (obtained with hipify) run on AMD MI100 and Radeon VII produces a different result. I attach both kernels and outputs. What can be the issue behind this behavior? Thank you.

[test.zip](https://github.com/RadeonOpenCompute/ROCm/files/5976267/test.zip)

Best regards,
Dmitrii Tolmachev

---

## 评论 (8 条)

### 评论 #1 — seesturm (2021-02-14T12:48:49Z)

Looks like this is a compiler bug. When compiled without optimization "-O0" outputs appear to be correct.

---

### 评论 #2 — ROCmSupport (2021-02-15T06:00:23Z)

Thanks @DTolm for reaching us.
Most likely its a compiler bug and so reached compiler team for resolution.
Will share an update very soon.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-02-25T05:38:45Z)

Hi @DTolm 
Got an update for you.
This issue is ready-with-the-fix and it is part of 4.1 code.
ROCm 4.1 is very nearby and request you to check there.
Thank you.

---

### 评论 #4 — DTolm (2021-04-05T17:08:34Z)

@ROCmSupport 
Thanks! I have checked ROCm 4.1 and it works. I also understood the issue myself - it was related to the fact that hipDeviceAttributeMaxThreadsPerBlock was reporting 1024 even when the ROCm was configured with 256 max threads. It seems that you have increased that value to 1024 in the last update, but this reduced the number of registers a thread can use before spilling to global memory. Some of my kernels at VkFFT experience a drop in performance from this, so I wanted to ask if it is possible to provide the exact value of registers per thread I need at compile-time to avoid the spilling? __launch_bounds__ doesn't seem to have any impact.
Thank you!
Best regards,
Dmitrii

---

### 评论 #5 — ROCmSupport (2021-04-06T06:29:59Z)

Thanks @DTolm for the update.
I am closing this as the issue is fixed as per your confirmation too.
Thank you.

---

### 评论 #6 — DTolm (2021-04-06T09:38:03Z)

@ROCmSupport can you please comment on the other part of my response? Thank you!

---

### 评论 #7 — ROCmSupport (2021-04-06T09:59:31Z)

Hi @DTolm 
I recommend to open a new issue to discuss on that separately.
Thank you.

---

### 评论 #8 — robosina (2022-03-19T18:24:12Z)

> Looks like this is a compiler bug. When compiled without optimization "-O0" outputs appear to be correct.

I have the same issue in my codes(the codebase is very large), it's working without optimization (`rocm` version is : `5.0.2`)

---
