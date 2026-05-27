# Q: OpenCL: perf impact of SVM vs. cl_mem buffers

> **Issue #655**
> **状态**: closed
> **创建时间**: 2019-01-02T01:28:33Z
> **更新时间**: 2021-05-09T20:07:31Z
> **关闭时间**: 2021-05-09T20:07:31Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/655

## 描述

I would like to ask: what is the expected performance impact of using SVM (clSVMAlloc) memory vs. "classic" OpenCL buffers (clCreateBuffer).

In particular in this scenario: two GPUs, accessing (read+write) disjoint regions of the same SVM buffer.

In the "high performance" scenario, I'd expect a memory page (4KB?) to be migrated locally to the GPU that's accessing it, and provide high local speed.

In the "low performance" scenario, I imagine the physical memory residing in one place (host or one GPU), and the access being done through PCIe, and that'd be slow.

So, do SVM buffers offer the same performance as "classic" buffers, or should I expect SVM to be slower?
thanks

---

## 评论 (3 条)

### 评论 #1 — Marc408 (2019-01-06T02:47:07Z)

I have yet to find a specific description of the SVM functionality in any OpenCL documentation. In the OpenCL Spec 2.0 it says the SVM resides in Host Memory "OpenCL extends the global memory region into the host memory region through a shared virtual memory (SVM) mechanism.".

According to this presentation https://youtu.be/H8tCCa9qV4U?t=656 you can expect SVM-implementations to show improved performance. Though I would expect it to be highly dependant on use case. 

If you find anything, please let me know!

---

### 评论 #2 — preda (2019-01-06T04:23:11Z)

I did a simple test: I replaced a cl_mem buffer that I was using in a kernel with clSVMAlloc()  memory, and the performance was abysmal. My interpretation: the cl_mem buffer was residing in GPU memory, while the SVM buffer was residing in host memory and accessed through PCIe, thus very slow. As such, SVM buffers can't be used as a general replacement for cl_mem buffers.

---

### 评论 #3 — preda (2021-05-09T20:07:31Z)

Closing as old. Better information/documentation on SVM in ROCm OpenCL would be nice though.

---
