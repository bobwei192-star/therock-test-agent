# Instruction for coherency between CPU and GPU on HUMA based Kaveri APU. 

> **Issue #80**
> **状态**: closed
> **创建时间**: 2017-01-18T06:04:26Z
> **更新时间**: 2017-02-22T15:57:50Z
> **关闭时间**: 2017-02-22T15:57:50Z
> **作者**: VishwasRao17
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/80

## 描述

I was going through the HUMA architecture for Kavei APU, they say there are instructions such as acquire and release for maintaining synchronization between CPU and GPU caches, as they share common memory space. Are these instructions supported in ROCM ?
Thank you

---

## 评论 (2 条)

### 评论 #1 — jedwards-AMD (2017-01-18T14:25:56Z)

They are for memory allocated from a memory region with the flag HSA_REGION_GLOBAL_FINE_GRAINED. Any GPU that supports a fine grained region will support the atomic instructions exposed in the host API and in the kernel language, on that region. The way this region is exposed through a higher level API, such as HIP or PSTL, will depend on the semantics of that API.

Support at the HSA runtime level for these types of memories is documented in the API descriptions in the has.h and hsa_ext_amd.h header files. You can also consult the various HSA specification documentation for the region based API description: http://www.hsafoundation.com/standards/


---

### 评论 #2 — nhaustov (2017-01-18T15:13:05Z)

For information on how HSA memory model maps to low level ISA, see
https://github.com/RadeonOpenCompute/ROCm-ComputeABI-Doc/blob/master/AMDGPU-ABI.md#memory-model

---
