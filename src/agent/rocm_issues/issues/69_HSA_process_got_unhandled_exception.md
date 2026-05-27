# HSA process got unhandled exception

> **Issue #69**
> **状态**: closed
> **创建时间**: 2017-01-04T02:31:59Z
> **更新时间**: 2017-07-02T17:17:58Z
> **关闭时间**: 2017-07-02T17:17:58Z
> **作者**: iotamudelta
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/69

## 描述

I have here a supermicro workstation with 2x R9 Nano and 2x S9150 installed running Ubuntu 16.04. This setup worked well with amdgpu-pro 16.40 previously.

I removed amdgpu-pro and installed ROCm 1.4 following instructions. However, the basic HSA sample (vector_copy) segfaults in libhsa-runtime64. dmesg shows a GPU fault detected, VM_CONTEXT1_PROTECTION_FAULT and VM fault.

Running any (previously working) OpenCL code or even just running clinfo causes "kfd: HSA Process (PID $$$$) got unhandled exception". After this, the executable hangs and after killing it dmesg contains kfd: cp queue preemption time out and amdkfd: Resetting wave fronts on dev.

What do I need to do to get this setup to work?

---

## 评论 (3 条)

### 评论 #1 — gstoner (2017-01-04T03:10:07Z)

Can we start simple,  start with 1 GPU in the system and let get Vector copy working.   Also which Supermicro system is it.  

---

### 评论 #2 — iotamudelta (2017-01-04T17:34:54Z)

Dear Greg,

thanks for your response! A single S9150 causes the same issue as described above. A single R9 Fury works, however at a seemingly 2-3x reduced performance compared to amdgpu-pro 16.40 for our in-house OpenCL code (both for single and double precision kernels and for both tests using clFFT calls and those that don't). Is the later expected?

The Supermicro system is a SYS-7048GR-TR. It has 2 Intel Xeon E5-2620 V4 alongside 64 GB DDR4 installed.

Let me know if I can provide more information.

---

### 评论 #3 — gstoner (2017-01-04T18:00:53Z)

Not expecting 2x drop in performance. The compiler is still early in development. With this release we were really looking functionality testing not performance.  Wonder if it has to do with how clFFT works since it does search space optimization using the JIT.  It why we working on rocBLAS which is even more Optimized for ROCm stack.  Really we need to profile it.


We use the same 7048GR-TR for Development, so we could do performance test in house, if you like. We can follow up up my AMD email address,  my firstname.lastname@amd.com<http://amd.com>   greg stoner.  The S9150 should not be a issue in the system, we run them as well.

Greg

On Jan 4, 2017, at 11:34 AM, iotamudelta <notifications@github.com<mailto:notifications@github.com>> wrote:


Dear Greg,

thanks for your response! A single S9150 causes the same issue as described above. A single R9 Fury works, however at a seemingly 2-3x reduced performance compared to amdgpu-pro 16.40 for our in-house OpenCL code (both for single and double precision kernels and for both tests using clFFT calls and those that don't). Is the later expected?

The Supermicro system is a SYS-7048GR-TR. It has 2 Intel Xeon E5-2620 V4 alongside 64 GB DDR4 installed.

Let me know if I can provide more information.

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/69#issuecomment-270433267>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuTuJ7vzBlNcL2VvjTDCObX8RjZUqks5rO9g_gaJpZM4LaPAI>.



---
