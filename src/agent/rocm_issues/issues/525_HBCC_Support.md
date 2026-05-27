# HBCC Support

> **Issue #525**
> **状态**: closed
> **创建时间**: 2018-09-09T03:10:07Z
> **更新时间**: 2018-09-11T17:36:22Z
> **关闭时间**: 2018-09-11T17:36:22Z
> **作者**: monik3r
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/525

## 标签

- **Question** (颜色: #cc317c)

## 描述

Hi,

I was wondering what the current status of HBCC in the ROCM stack. I would like to enable my kernels to use >16GB memory.

Thanks! 

---

## 评论 (4 条)

### 评论 #1 — gstoner (2018-09-09T16:48:16Z)

For ROCm we plan on properly supporting Page Migration, in conjunction with SVM, this gives access to the full system memory from the GPU,  HBCC was a solution really for graphics and not for computing. 

Note the Core Hardware support GFX9 hardware supports paging 




---

### 评论 #2 — monik3r (2018-09-09T17:52:21Z)

Thanks for the clarification. Is there a time frame when this feature might be available?

---

### 评论 #3 — ekondis (2018-09-11T17:05:51Z)

> For ROCm we plan on properly supporting Page Migration, in conjunction with SVM, this gives access to the full system memory from the GPU, HBCC was a solution really for graphics and not for computing. Note the Core Hardware support GFX9 hardware supports paging

Wouldn't that be essentially the same for compute (HBCC functionality in ROCm)?

---

### 评论 #4 — gstoner (2018-09-11T17:36:22Z)

No.. 

---
