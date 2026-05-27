# Command to disable the L2 cache or command to invalidate / flush the cache operation on AMD APUs ? 

> **Issue #71**
> **状态**: closed
> **创建时间**: 2017-01-09T04:32:25Z
> **更新时间**: 2017-07-02T17:19:50Z
> **关闭时间**: 2017-07-02T17:19:50Z
> **作者**: VishwasRao17
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/71

## 描述

I would like to know, when a memory is reserved in the GPU RAM, then when GPU tries to modify it, the data will be put into L2 , L1 cache before going to ALU. My question is can I flush the cache before a third party other than GPU tries to access that memory region? Is there an ISA for the same . I am trying to use AMD GPU for some research. Since ROCM is open source I want to make use of it. OpenCL also runs on top of Rocm, so will make use of the same. 

---

## 评论 (3 条)

### 评论 #1 — gstoner (2017-01-09T15:39:33Z)

Can you put your request into Descriptions,  Your put this in the title.    When you make your request 

"Is there a command to disable the L2 cache or command to invalidate/flush the cache operation on AMD APUs. Kaveri APU Sea islands based architecture #71"   

Question "Are you doing this on ROCm and what Language"

---

### 评论 #2 — VishwasRao17 (2017-01-10T03:27:04Z)

@gstoner I have updated the description. I am looking into a explicit command which will flush the cache L2 during external device read and invalidate the cache contents during external writes into same memory locations. 

---

### 评论 #3 — jedwards-AMD (2017-02-22T17:15:34Z)

Invalidating L2 cache is done using AQL packet commands, using the various hsa_fence_scope_t values in the packet. Refer to the HSA Runtime specification for a description of AQL and controlling memory synchronization.

---
