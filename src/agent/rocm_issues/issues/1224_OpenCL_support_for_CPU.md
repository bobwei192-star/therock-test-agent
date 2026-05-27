# OpenCL support for CPU?

> **Issue #1224**
> **状态**: closed
> **创建时间**: 2020-09-18T20:38:47Z
> **更新时间**: 2020-12-16T05:46:44Z
> **关闭时间**: 2020-12-16T05:46:44Z
> **作者**: BA8F0D39
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1224

## 描述

https://rocmdocs.amd.com/en/latest/Programming_Guides/Opencl-optimization.html?highlight=CPU#using-the-cpu

ROCm says it has OpenCL support for CPU but when I run clinfo on my Ryzen 7 1700X machine there isn't any devices.

So how do I get OpenCL to work on CPU?

---

## 评论 (5 条)

### 评论 #1 — Rmalavally (2020-09-18T21:28:54Z)

Thank you for reaching out to us.

We will  investigate the issue and get back to you once we hear from our development team.

AMD ROCm Documentation Team


---

### 评论 #2 — boxerab (2020-09-24T12:16:04Z)

CPU support means that the library will support Ryzen CPU + AMD GPU. There is no OpenCL runtime for the CPU, so if you don't have a GPU, you will not see any devices. 

---

### 评论 #3 — BA8F0D39 (2020-09-24T21:41:38Z)

@boxerab besides OpenCL, what other frameworks does ROCm support on the CPU only? Like does it support OpenMP or HIP? The documentation is very vague on what ROCm exactly provides.

---

### 评论 #4 — boxerab (2020-09-25T00:05:28Z)

It certainly supports HIP. That is quite well documented. For OpenMP, I am not sure, but I found this:

https://github.com/ROCm-Developer-Tools/aomp

---

### 评论 #5 — ROCmSupport (2020-12-16T05:46:44Z)

Hi @BA8F0D39 
I am closing this issue as the relevant info for OpenCL support for ROCm is shared.
Recommed to open a new ticket, for any new issues.
Thank you.

---
