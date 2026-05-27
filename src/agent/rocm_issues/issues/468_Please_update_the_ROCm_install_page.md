# Please update the ROCm install page

> **Issue #468**
> **状态**: closed
> **创建时间**: 2018-07-26T04:52:09Z
> **更新时间**: 2018-09-14T13:41:41Z
> **关闭时间**: 2018-09-14T13:41:41Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/468

## 描述

This page https://rocm.github.io/install.html
(which comes up on search for "rocm install") says:

Native Linux Distribution Support in ROCm 1.7:
Distribution | Kernel | GCC | GLIBC
Ubuntu 16.04 | 4.11 | 5.40 | 2.23

So, is that accurate -- ROCm 1.7, Ubuntu 16.04 with kernel 4.11, GCC 5.40 ?!


---

## 评论 (2 条)

### 评论 #1 — JMadgwick (2018-07-29T11:11:00Z)

Seems those pages are out of date. The readme: [README.md](https://github.com/RadeonOpenCompute/ROCm/blob/master/README.md) is up to date.
The GPUOpen [page](https://gpuopen.com/compute-product/rocm/) also links to those same outdated pages. I imagine different people are responsible for these various pages.

---

### 评论 #2 — kentrussell (2018-09-14T13:41:41Z)

@JMadgwick you're right. We're working internally to get to get documentation updated for each component, and to expand on the rocm.github.io documentation as well. We just need to establish who is doing what, and what we need to include.
@preda Stick to that README.md file that JMadgwick linked for now while we get things sorted out. And check the Pull Request in ROCm, our packaging guy has an update regarding support and installation steps that should be referred to (though it should get merged today)

---
