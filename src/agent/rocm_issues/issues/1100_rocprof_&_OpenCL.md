# rocprof & OpenCL

> **Issue #1100**
> **状态**: closed
> **创建时间**: 2020-05-07T21:35:47Z
> **更新时间**: 2021-02-09T09:47:55Z
> **关闭时间**: 2021-02-09T09:47:55Z
> **作者**: 3D-360
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1100

## 描述

We have ported a large project from CUDA to OpenCL, but CUDA is currently about 4x faster on equivalent hardware.  We want to tune the code for OpenCL.  
We used to tune with rcprof on ROCm 2.x, 
but we do not have an OpenCL profiling tool for ROCm 3.3.0.

rcprof used to report OCCUPANCY & register usage for OpenCL.
rocprof has replaced rcprof, and while it can profile ROCm, HIP, HSA, it does NOT profile OpenCL.

The problem is that there is no documentation about configuring rocprof to profile OpenCL.
We can get some diagnostics from rocprof on our code, but nothing on OpenCL. Here is our input.text file with several rocprof profiling features enabled:
```
# Perf counters group 1
pmc : Wavefronts 
# Perf counters group 2
pmc : VALUInsts SALUInsts SFetchInsts FlatVMemInsts LDSInsts
# Perf counters group 3
pmc : GDSInsts VALUUtilization FetchSize
# Perf counters group 4
pmc : WriteSize L2CacheHit
# supported range formats: "3:9", "3:", "3"
range: 1
gpu: 0 
kernel: MedianFilterKernel
```
What flags do we need to profile OpenCL with rocprof in ROCm 3.3.0?
Specifically, we want to monitor occupancy, shared memory & register usage.



---

## 评论 (5 条)

### 评论 #1 — vvsteg (2020-05-13T10:42:53Z)

From our experience (https://link.springer.com/chapter/10.1007/978-3-030-43229-4_28) if you use AMD GPUs then porting from CUDA to HIP is much more performance efficient than porting to OpenCL. It might be that porting to HIP would be a lesser and more productive effort that tuning the OpenCL version.

---

### 评论 #2 — 3D-360 (2020-05-14T00:45:15Z)

Thanks for the suggestion, but we have already ported to OpenCL.  

We have given up on rcprof, and we are now evaluating Radeon GPU Profiler.  It can be found at gpuopen.com

---

### 评论 #3 — eshcherb (2020-06-27T06:39:02Z)

rocprof doesn't support OpenCL which should have internal profiler.
You can use '--hsa-trace' with OpenCL.

---

### 评论 #4 — EvgeniyPeshkov (2020-08-25T17:49:09Z)

Hello @3D-360! Maybe I'm late to the party, but I would like to suggest [CLtracer](https://www.cltracer.com/). It supports any GPU on both Linux and Windows

---

### 评论 #5 — ROCmSupport (2021-02-09T09:47:55Z)

Thanks @3D-360 
Hope you got answers from above.
Am closing this.
Request you to open a new ticket, if you find any.

---
