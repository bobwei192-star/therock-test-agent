# What is the functionality of si58_mc.bin

> **Issue #179**
> **状态**: closed
> **创建时间**: 2017-08-10T08:50:22Z
> **更新时间**: 2018-06-03T14:56:29Z
> **关闭时间**: 2018-06-03T14:56:29Z
> **作者**: FalconBsp
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/179

## 描述

With Git hub pre-build OCL bins , Luxmark  works with out si58_mc.bin from /lib/amdgpu/firmware.

I tried to build libOenCL.so and libamdocl64.so  from  open source.  But Luxmark failed to run and gave IOMMU fault. When i copy si58_mc.bin to amdgpu firmware and ran initramfs , Luxmark runs without any issue.

Can you explain how this firmware bin fixing the issue?



---

## 评论 (4 条)

### 评论 #1 — gstoner (2017-08-24T17:56:23Z)

What GPU are you using?...  This firmware should only be loaded for GFX6 hardware.

---

### 评论 #2 — gstoner (2017-08-24T18:41:30Z)

This firmware is only used for Tahiti, Pitcarin, Cape Verde, Oland, and Hainan It should never be used with ROCm. since these device are not supported by ROCm 

---

### 评论 #3 — rdemaria (2017-10-21T18:01:39Z)

Will ROCm ever support Tahiti hardware, like the AMD 280X?

---

### 评论 #4 — simonlui (2017-12-21T17:22:10Z)

+1 to GFX6 hardware support. Is there any technical hardware limitations for Southern Islands support, considering it is under amdgpu Linux driver but in limited support right now? I suppose we'll have to see more upstreaming before that happens, right?

---
