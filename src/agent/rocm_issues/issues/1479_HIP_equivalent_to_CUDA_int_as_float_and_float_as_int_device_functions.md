# HIP equivalent to CUDA int_as_float and float_as_int device functions.

> **Issue #1479**
> **状态**: closed
> **创建时间**: 2021-05-23T01:11:23Z
> **更新时间**: 2021-05-24T19:21:23Z
> **关闭时间**: 2021-05-24T19:21:23Z
> **作者**: ctaylor389
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1479

## 描述

Hello, I am working on porting my CUDA code to HIP and ran into an issue with porting over two device functions: int_as_float and float_as_int. The Hipify tools state that they are unsupported. If this is the case, is there any way to implement these functions?

Specifically, they are used in a trick to implement floating point atomicMax using atomicCAS.

Any help is appreciated and thank you.

---

## 评论 (1 条)

### 评论 #1 — Rmalavally (2021-05-23T18:08:22Z)

Thank you for reaching out. Have you referred to our latest version of the CUDA to HIP Reference Guide? You can access it at:

https://github.com/RadeonOpenCompute/ROCm/blob/master/HIP_Supported_CUDA_API_Reference_Guide_v4.2.pdf

Please let us know if you are unable to find the information you need.

AMD ROCm Documentation


---
