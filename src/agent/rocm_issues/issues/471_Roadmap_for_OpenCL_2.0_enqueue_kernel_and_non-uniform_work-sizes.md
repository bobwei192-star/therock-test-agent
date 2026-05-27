# Roadmap for OpenCL 2.0 enqueue_kernel and non-uniform work-sizes

> **Issue #471**
> **状态**: closed
> **创建时间**: 2018-07-26T12:57:10Z
> **更新时间**: 2019-02-08T14:52:43Z
> **关闭时间**: 2019-02-08T14:52:43Z
> **作者**: blueberry
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/471

## 描述

Any rough estimate on when various missing OpenCL 2.0 features will be available on Vega 64?

Specifically, I am interested in enqueue_kernel and non-uniform work-sizes, but sharing a features matrix that shows what works and what is missing in the OpenCL 2.0 support would be even better, and coupling that with (at least rough) estimates on when that could be expected would be awesome.

For reference, I'm on Arch Linux and have Vega 64 waiting to be installed (but currently I'll have to do with R9 290 because I need these OpenCL 2.0 features and they are supported in Catalyst)

For the time being, it does not even have to be open-source. Any hints about AMDGPU-PRO and any other combination would solve this issue form me temporarily until it is available in ROCm...

---

## 评论 (3 条)

### 评论 #1 — preda (2018-07-26T23:25:42Z)

I'm under the impression that non-uniform work sizes work right now in amdgpu-pro. (but that's not a big deal anyway IMO, as it can easily be worked around if not present with a simple conditional). 

OTOH I don't know about device-side enqueue plans.


---

### 评论 #2 — gstoner (2018-09-09T17:02:34Z)

We are looking to have full OpenCL 2.0 support with ROCm 2.0.   Note All the 2.0 features have been in for quite a while, except for kernel enqueue and Pipes are the last two feature we need to role out to formally turn on OpenCL 2.0.  

I will have the teamwork on Feature matrix for AMDGPUpro vs ROCm.   You find we even have some of the OpenCL 2.1 runtime features in ROCm OpenCL driver now.   RIght now we are focused on any new runtime and Kernel feature.

---

### 评论 #3 — jlgreathouse (2019-02-08T14:52:43Z)

Hi @blueberry 

As of ROCm 2.0, device enqueue should work on Vega10 GPUs (gfx900), so long as you have working PCIe atomics between your GPU and your CPU. We have supported non-uniform workgroup sizes for quite a while now. As such, this request is met.



---
