# hip-samples provides *.hipref.* files without explaining them

> **Issue #1138**
> **状态**: closed
> **创建时间**: 2020-06-06T19:19:50Z
> **更新时间**: 2021-02-15T10:28:14Z
> **关闭时间**: 2021-02-15T10:28:14Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1138

## 描述

I believe `/opt/rocm-3.5.0/hip/samples/0_Intro/square/square.hipref.cpp` is not actually used for anything. And shipping it is confusing. Please remove it.

Even better, make the `0_Intro/square`, be separated into two projects. First one, not using CUDA, but native manually written HIP code and just uses `hipcc`, a second one, that uses CUDA and `hipify+hcc`, and `nvcc`.


---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2021-01-12T09:26:05Z)

Hi @baryluk for reaching out.
square.hipref.cpp is just a reference file and it does nothing.
However I will check with HIP team and get back to you on this.
Thank you.


---

### 评论 #2 — ROCmSupport (2021-02-15T10:28:14Z)

Hi @baryluk 
Got an update on this:
We can not remove it, as the file is for comparing to show that after you hipify you would get code similar to the hipref.cpp.

---
