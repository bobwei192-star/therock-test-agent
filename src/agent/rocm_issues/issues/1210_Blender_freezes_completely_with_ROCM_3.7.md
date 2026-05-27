# Blender freezes completely with ROCM 3.7 

> **Issue #1210**
> **状态**: closed
> **创建时间**: 2020-09-01T18:06:23Z
> **更新时间**: 2021-03-09T12:10:42Z
> **关闭时间**: 2021-03-01T08:15:33Z
> **作者**: xcom169
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1210

## 描述

Blender freezes completely my whole PC with ROCM 3.7 on Manjaro Linux.

My test file: 
https://cloud.blender.org/p/gallery/5dd6d7044441651fa3decb56

My GPU: 
Vega 56

blender: /mnt/8942b2b9/tmp/pamac-build/hsa-rocr/src/ROCR-Runtime-rocm-3.7.0/src/core/runtime/runtime.cpp:1214: static bool rocr::core::Runtime::VMFaultHandler(hsa_signal_value_t, void*): Assertion `false && "GPU memory access fault."' failed.
zsh: abort (core dumped)  blender --debug




---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2020-12-16T05:44:16Z)

Hi @xcom169 
Thanks for reaching out.
We are able to reproduce this issue with ROCm 3.10.
I will share more details soon.


---

### 评论 #2 — ROCmSupport (2020-12-16T05:44:59Z)

Hi @xcom169 
I came to know that developer is working on the fix and will update once fix is ready.
Please stay tuned
Thank you.

---

### 评论 #3 — ROCmSupport (2021-03-01T08:15:39Z)

Hi All,

As per the latest information and clarity provided in our Documentation that ROCm does not support GUI applications officially.


Docs also updated accordingly @ [https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url)

Hardware and Software Support
ROCm is focused on using AMD GPUs to accelerate computational tasks such as machine learning, engineering workloads, and scientific computing. In order to focus our development efforts on these domains of interest, ROCm supports a targeted set of hardware configurations which are detailed further in this section.
**Note: The AMD ROCm™ open software platform is a compute stack for headless system deployments. GUI-based software applications are currently not supported.**


---

### 评论 #4 — ROCmSupport (2021-03-09T12:10:41Z)

We are going to rephrase the text about GUI apps in our rocm documentation.
We have come up with some plans to handle GUI apps in a way.
But I am marking this as duplicate of #1106 and hence not reopening for now.
All progress can be seen at #1106 
Thank you.

---
