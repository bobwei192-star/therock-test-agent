# Scratch space used when VGPRs are available (50% speed hit)

> **Issue #709**
> **状态**: closed
> **创建时间**: 2019-02-16T18:14:28Z
> **更新时间**: 2019-04-02T19:16:18Z
> **关闭时间**: 2019-03-16T00:41:21Z
> **作者**: lwoog
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/709

## 描述

I have a proprietary kernel to provide for testing (I cannot post it). This only happens in rocm and not with the amdgpu drivers.

---

## 评论 (4 条)

### 评论 #1 — lwoog (2019-02-16T18:15:56Z)

       enable_sgpr_flat_scratch_init = 1
       workitem_private_segment_byte_size = 136
       workitem_vgpr_count = 82

  Platform ID:					 0x7f97dbd2ab30
  Name:						 gfx900
  Vendor:					 Advanced Micro Devices, Inc.
  Device OpenCL C version:			 OpenCL C 2.0 
  Driver version:				 2814.0 (HSA1.1,LC)
 

---

### 评论 #2 — lwoog (2019-02-17T17:24:13Z)

I found a way around the problem by combining two equally sized float buffers into a single float2 buffer. Unlike the rocm driver, the amdgpu driver maximum memory alloc was 4GB, so I assumed it was the increased use of SGPR that caused VGPRs to be cached.  Result is:

enable_sgpr_flat_scratch_init = 0
workitem_private_segment_byte_size = 0
workitem_vgpr_count = 100

Speed is back to what I expected (2x faster)

PS: Anyone knows what is the maximum size of a pinned memory buffer before I post another problem?

---

### 评论 #3 — jlgreathouse (2019-03-16T00:41:21Z)

Hi @lwoog 

Going all the way up to the maximum number of VGPRs (256), while possible, is not necessarily a good thing. More registers result in lower occupancy in the CUs. Especially after 64 VGPRs, the more registers you add, the smaller your resulting workgroups can be.

Lower occupancy results in lower latency hiding ability. This and smaller workgroups can reduce performance, so the compiler needs to make optimization decisions about how many registers to allocate and how much scratch to use.

AMD's open source Lightning Compiler chose to use scratch for your kernel, while the closed source compiler case may not have. If you would like to nudge this one way or another, you can try the `amdgpu_waves_per_eu` [kernel attribute](http://clang.llvm.org/docs/AttributeReference.html#amd-gpu-attributes). Put this as part of your kernel function definition, and it will inform the compiler of your desired occupancy and potentially free it up to use more VGPRs.

---

### 评论 #4 — lwoog (2019-04-02T19:01:42Z)

Thank you jl for that kernel attribute. I did try many ways of structuring the problem, but more occupancy did not give me more speed. The current code with it low occupancy is already at 97% ALU utilization. 

---
