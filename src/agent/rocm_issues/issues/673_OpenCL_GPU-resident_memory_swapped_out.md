# OpenCL GPU-resident memory swapped out?

> **Issue #673**
> **状态**: closed
> **创建时间**: 2019-01-16T19:23:28Z
> **更新时间**: 2019-03-15T20:00:37Z
> **关闭时间**: 2019-03-12T18:36:55Z
> **作者**: preda
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/673

## 标签

- **Question** (颜色: #cc317c)

## 描述

ROCm 2.0 OpenCL, Vega64, Ubuntu 18.10 w linux 4.20.

In OpenCL I'm trying to allocate the maximum amount of GPU memory, by doing a repeated creation of a buffer of size 36MB. This buffer is allocated with CL_MEM_READ_WRITE | CL_MEM_HOST_NO_ACCESS to clCreateBuffer(). Just to make sure that the buffer is actually allocated, I also do a clEnqueueFillBuffer() for the full size of the newly created buffer with zeros and wait on it with clFinish().

My GPU has 8GB of physical GPU memory. I expect the buffers to reside on the GPU (because CL_MEM_HOST_NO_ACCESS). Yet somehow I can allocate without error (and write to as indicated above) 374 buffers (of 36MB each), for a total of about 13GB (after the 374 buffers I get CL_MEM_OBJECT_ALLOCATION_FAILURE on buffer creation).

How is this possible -- that I can allocate and write to 13GB of GPU resident buffers on a 8GB Vega64?

To investigate I started to query CL_DEVICE_GLOBAL_FREE_MEMORY_AMD after each allocation, and what I see is this: initially the free memory is decreasing at the expected rate of 36MB per allocation. But later on, the allocations continue to proceed successfully while the free memory remains constant at 53MB. Another observation, once the 53MB point is reached, the allocations become slower.

2019-01-17 06:01:15 vega0 GPU free mem 7937 MB
2019-01-17 06:01:15 vega0 GPU free mem 7901 MB
2019-01-17 06:01:15 vega0 GPU free mem 7865 MB
[...]
2019-01-17 06:01:16 vega0 GPU free mem 197 MB
2019-01-17 06:01:16 vega0 GPU free mem 161 MB
2019-01-17 06:01:16 vega0 GPU free mem 125 MB
2019-01-17 06:01:16 vega0 GPU free mem 89 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:16 vega0 GPU free mem 53 MB
2019-01-17 06:01:17 vega0 GPU free mem 53 MB
2019-01-17 06:01:17 vega0 GPU free mem 53 MB

What is happening? is GPU memory evicted to host memory? something else? can the behavior be controlled? (what I want to achieve is "fast GPU-resident memory" without any over-allocation)


---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2019-03-12T18:36:55Z)

Hi @preda,

ROCm does not swap data between the host and device at this time.

You are seeing the following:
 - When you perform your OpenCL memory allocations, the allocation request goes [into the OpenCL runtime](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blob/roc-2.1.0/runtime/device/rocm/rocmemory.cpp#L650). From there, [the OpenCL runtime](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blob/roc-2.1.0/runtime/device/rocm/rocdevice.cpp#L1527) thn calls [into ROCr](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/roc-2.1.0/src/core/common/hsa_table_interface.cpp#L943). [ROCr](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/roc-2.1.0/src/core/runtime/hsa_ext_amd.cpp#L627) [eventually](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/roc-2.1.0/src/core/runtime/runtime.cpp#L279) [calls](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/roc-2.1.0/src/core/runtime/amd_memory_region.cpp#L190) [into](https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/roc-2.1.0/src/core/runtime/amd_memory_region.cpp#L58) the Thunk. [The Thunk will call to the KFD](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/roc-2.0.0/src/memory.c#L107), which tries to allocate the region onto the device.
 - If the KFD cannot find enough space on the device for the allocation, it will fail to allocate the region. [This failure will propagate back up through all of those layers I just mentioned](https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/blob/roc-2.1.0/src/memory.c#L167).
 - The OpenCL runtime will see this failure, and fall back to [trying to allocate the data into system memory](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blob/roc-2.1.0/runtime/device/rocm/rocmemory.cpp#L741). This may run slower (accesses go over the PCIe bus, for instance) but it allows your program to make progress.

So it's not that old allocations are being evicted. It's that your new allocations are being placed into system memory rather than failing.

Note that `CL_MEM_HOST_NO_ACCESS` does not guarantee that the host *cannot* access the buffer. It is a hint that the programmer passes in that tells the runtime that the host *will not* access the buffer. The runtime can choose to use this information to make optimizations, but it does not need to ensure host accesses will fail.

---

### 评论 #2 — preda (2019-03-15T19:54:43Z)

@jlgreathouse thanks for the explanation. This behavior is worthy of being documented better. To me at least, it is surprising. Given that I use OpenCL for high-performance computing, I'm quite sensitive to memory that is an order of magnitude slower than what I expect given what I request to the API. The fact that I get the slower memory without any indication in the API or any control over it, makes this behavior bug-grade IMO. Not an API compliance bug, but a performance bug.

---
