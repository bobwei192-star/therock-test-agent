# Cache instructions available on AMD APUs under ROCM platform ? 

> **Issue #70**
> **状态**: closed
> **创建时间**: 2017-01-05T09:03:00Z
> **更新时间**: 2017-07-02T17:19:39Z
> **关闭时间**: 2017-07-02T17:19:39Z
> **作者**: VishwasRao17
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/70

## 描述

Is there any instruction to flush the cache and invalidate the cache L2 in specific ? The reason for asking is to achieve coherency between CPU and GPU accessing the DRAM in APUs there should be cache flushing action? How is it done , what is the instruction for the same ? 

---

## 评论 (5 条)

### 评论 #1 — nevion (2017-01-06T01:06:54Z)

@VishwasRao17 don't write a paragraph in the ticket title. If I had the answer, such a move would make me hesitate to answer you.

---

### 评论 #2 — VishwasRao17 (2017-01-09T04:24:41Z)

Ok, I wont . Is there a pointer for my question please. 

---

### 评论 #3 — gstoner (2017-01-10T03:33:05Z)

best place to start on ROCm rocm.github.io documentation Also you can look at HSA Foundation spec for background on the runtime and system architecture for ROCm 

---

### 评论 #4 — VishwasRao17 (2017-01-10T10:34:17Z)

@gstoner I was going through the ISA sea islands , this is because AMD Kaveri GPU follows Sea Islands Architecture. There they quote in introduction, page no 1-2 (" invalidate and flush caches on the Sea Islands GPU, and ") . But it was not mentioned in the ISA as a command as such . The statements says when the host tries to offload work to GPU , it should copy the contents to device memory and invalidate the L2 cache . So this must be done in ROCM too while offlading the kernel to device memory.  So I am curious how it is done ? I need to apply something similar in my application.

---

### 评论 #5 — jedwards-AMD (2017-02-22T16:05:04Z)

Invalidating L2 cache is done using AQL packet commands, using the various hsa_fence_scope_t values in the packet. Refer to the [HSA Runtime specification]( http://www.hsafoundation.com/standards/) for a description of AQL and controlling memory synchronization.

---
