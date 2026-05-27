# CU Masking access

> **Issue #1110**
> **状态**: closed
> **创建时间**: 2020-05-16T18:19:19Z
> **更新时间**: 2020-09-10T16:17:11Z
> **关闭时间**: 2020-09-10T16:17:00Z
> **作者**: trinayan
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/1110

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

What is the intended way to use the CU Masking feature available in ROCM. I can see both the driver, Thunk and runtime have code for CU Masking. Yet is not clear how to use it. The calls to both the APIs in Thunk and ROCR require some sort of queue to pass to it. Its not clear how this queue is created and how to use it from something like HIP . Any userspace example that demonstrates this will be really helpful.Thanks

---

## 评论 (4 条)

### 评论 #1 — Rmalavally (2020-05-16T20:12:55Z)

Thank you for your feedback. Have you looked on the documentation website at http://rocmdocs.amd.com? 

Please let us know if you are unable to find the information you need.

AMD ROCm Documentation Team

---

### 评论 #2 — trinayan (2020-05-16T21:47:18Z)

I have gone through the documentation. I cannot find how to do this in the current docs

---

### 评论 #3 — Rmalavally (2020-05-17T06:08:11Z)

Thank you for confirming. We have noted your feedback. 

Currently, this feature is not supported. Please check back as the documentation is updated on a continuous basis. 

AMD ROCm Documentation Team

---

### 评论 #4 — jlgreathouse (2020-09-10T16:17:00Z)

This feature is available in HIP as of ROCm 3.6 using the API `hipExtStreamCreateWithCUMask()`. See [this header](https://github.com/ROCm-Developer-Tools/HIP/blob/roc-3.6.x/include/hip/hcc_detail/hip_runtime_api.h#L852) for documentation. We do not plan on adding a similar feature to OpenCL at this time.

---
