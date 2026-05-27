# about "Limits GPU's usage of system memory to 3/8 of system memory" for upstream kernel driver

> **Issue #708**
> **状态**: closed
> **创建时间**: 2019-02-16T10:43:55Z
> **更新时间**: 2019-03-21T08:15:47Z
> **关闭时间**: 2019-03-21T08:15:47Z
> **作者**: jinmingjian
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/708

## 标签

- **Question** (颜色: #cc317c)

## 描述

I am planning somethings on rocm. I guess I'd like to embrace latest kernel always. Then I am a little nervous with this con in [Readme](https://github.com/RadeonOpenCompute/ROCm#rocm-support-in-upstream-linux-kernels) and interesting in the details about why we have this limitation for upstream kernel.

Intuitively, GPU does not often use system memory because it's large on-board memory? so, "GPU's usage of system memory" means the ROCm software side memory usage?

thanks first,

---

## 评论 (2 条)

### 评论 #1 — kentrussell (2019-03-20T19:32:11Z)

The GPU usage of system memory is defined upstream as a maximum of 3/8 of the total system memory (see https://github.com/torvalds/linux/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd_gpuvm.c#L95). This is the maximum amount of system memory that the GPU can use via TTM (Translation Table Maps, a generic memory manager for GPUs). For some buffers, it’s beneficial to be kept in system memory rather than in VRAM, so in our ROCm releases we increase this amount to 29/32 of system memory (https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-2.2.x/drivers/gpu/drm/amd/amdgpu/amdgpu_amdkfd_gpuvm.c#L94). This can allow for the use of larger buffers, not having to move tons of data from System RAM to VRAM continually, and also allow for the use of more memory than is available solely through VRAM, all of which can increase performance on certain applications. 

Note that this is dynamically allocated so it’s not like your system is limited to 3/32 of its system memory all the time, this is just a maximum amount allowable by the kernel for that specific memory pool. The lower amount makes sense for general kernel usage, to ensure that system memory isn’t completely stolen by the GPU, but this is less of a concern for ROCm and the high-performance applications that run on it.

---

### 评论 #2 — jinmingjian (2019-03-21T08:15:47Z)

@kentrussell  very appreciated for your answer. Great detailed reading for me as a newcomer for ROCm. 
We have strong open source community! I can't wait to go deeper and more! :tada: 

---
