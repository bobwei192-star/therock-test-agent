# Changing number of available CUs

> **Issue #1012**
> **状态**: closed
> **创建时间**: 2020-02-13T01:28:23Z
> **更新时间**: 2024-08-01T14:31:38Z
> **关闭时间**: 2024-08-01T14:31:38Z
> **作者**: pfotouhi
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1012

## 标签

- **Documentation** (颜色: #5319e7)

## 描述

I'm studying scaling of a variety of compute workloads, and I was wondering if there is a way to adjust the number of CUs?

I came across a [similar discussion](https://github.com/RadeonOpenCompute/ROC-smi/issues/5) where use of "hsa_amd_queue_cu_set_mask()" was suggested. Since this requires changing the applications source code, are there any other alternative approaches that can achieve the same without modifying the source code?

---

## 评论 (8 条)

### 评论 #1 — pfotouhi (2020-02-16T03:18:13Z)

More on this one, can "hsa_amd_queue_cu_set_mask()" used somewhere inside rocprof to disbale CUs while profiling?

---

### 评论 #2 — ROCmSupport (2021-04-19T12:56:55Z)

Thanks @pfotouhi for reaching out.
Request you to share an update like whether you are still looking for the same query.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-04-20T07:30:14Z)

Hi @pfotouhi 
Feel free to close this issue, if you do not have any open query.
Thank you.

---

### 评论 #4 — jlgreathouse (2023-08-05T16:35:26Z)

I'm sorry for the long delay in responding to this. As of ROCm 4.5, we have a mechanism that should help you do what you want. The environment variable HSA_CU_MASK (with syntax described [here](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/rocm-5.6.0/src/core/util/flag.cpp#L105)) will allow you to set the CU mask on all queues created within a process without needing to modify any code.

Please note that not all CU masks are legal on all devices. For instance, on gfx10+ devices where two CUs can be combined together into a WGP (for kernels running in WGP mode), [it is not legal to disable only a single CU in a WGP](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/rocm-5.6.0/src/core/runtime/amd_aql_queue.cpp#L1130). You may want to [read this paper](https://www.cs.unc.edu/~otternes/papers/rtsj2022.pdf) where a research group explores how setting some CU masks (such as enabling one CU on an SE and all CUs on another SE) can lead to corner-case situations that do not perform as you would expect.

I'm relatively confident (though I haven't tested it at this time) that setting this environment variable will also cause the CU mask to be set on queues being profiled, because this sets the mask on the lowest-level of our queue creation, the ROCr runtime. This is different than the [ROC_GLOBAL_CU_MASK environment variable](https://github.com/ROCm-Developer-Tools/ROCclr/blob/rocm-5.6.0/utils/flags.hpp#L258), which will only set the CU mask on queues created by the HIP and OpenCL language runtimes.

All of these environment variables are for ROCm software only, and will not work for graphics workloads (such as Mesa). There is a driver-level mechanism to disable CUs ([the amdgpu modparm disable_cu](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c#L517)), but this will apply to all GPUs in your system. In addition, setting this incorrectly (e.g., disabling all CUs in an SE, which is legal for CU masking but not for this modparm) can lead to a non-working GPU. This modparm is not recommended for production usage.

---

### 评论 #5 — keryell (2023-08-12T05:11:51Z)

There is quite a lot of interesting information here!
@saadrahim it would be nice to have this described in a synthetic way in the official documentation.

---

### 评论 #6 — saadrahim (2023-08-15T18:20:37Z)

@jlgreathouse unless you object by closing this, I am reopening this until the content is included directly in the repository.

---

### 评论 #7 — nartmada (2024-04-05T21:29:39Z)

Internal ticket has been created to track of the progress of this task.

---

### 评论 #8 — neon60 (2024-06-12T20:40:42Z)

We can close this issue, because the page is added:

https://github.com/ROCm/ROCm/blob/develop/docs/how-to/setting-cus.rst

@saadrahim I will close this tomorrow, if I do not get any comments.

---
