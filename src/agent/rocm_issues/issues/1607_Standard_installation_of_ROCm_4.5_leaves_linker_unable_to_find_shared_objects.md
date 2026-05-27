# Standard installation of ROCm 4.5 leaves linker unable to find shared objects

> **Issue #1607**
> **状态**: closed
> **创建时间**: 2021-11-02T09:09:20Z
> **更新时间**: 2021-11-21T22:21:54Z
> **关闭时间**: 2021-11-17T10:51:31Z
> **作者**: Malexandra-de
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1607

## 描述

Following the installation guide [https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html](https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html) using the `amdgpu-install --usecase=hiplibsdk,rocm` method leaves the system unable to run Tensorflow-rocm. This is due to several necessary libraries being missing from locations in the LD_LIBRARY_PATH. Prepending a manually extended LD_LIBRARY_PATH fixes this and enables training on the GPU:
`$ LD_LIBRARY_PATH="/opt/rocm/rocblas/lib/:/opt/rocm/rccl/lib/:/opt/rocm/hsa/lib/:/opt/rocm/hip/lib/:/opt/rocm/miopen/lib/:/opt/rocm/hipfft/lib/:/opt/rocm/rocrand/lib/::$LD_LIBRARY_PATH" python3 mlp\ classifier.py`

OpenCL is unaffected by this.

OS: Ubuntu 20.4.3
CPU: Ryzen9 5900X
GPU: AMD Radeon RX6800

---

## 评论 (6 条)

### 评论 #1 — xuhuisheng (2021-11-02T10:11:52Z)

`export LD_LIBRARY_PATH=/opt/rocm/lib` should satisfied.
The reason is tensorflow-rocm build with `/opt/rocm-4.3.1`, the current version ROCm is `/opt/rocm-4.5.0`

---

### 评论 #2 — Malexandra-de (2021-11-02T10:16:52Z)

It works, but this should probably be added to the documentation.

---

### 评论 #3 — ROCmSupport (2021-11-03T13:02:34Z)

Hi @PMunkes 
Thanks for reaching out.
Good to know that exporting library path solves the issue.
I will work with Documentation team on these changes.
Thank you.

---

### 评论 #4 — ROCmSupport (2021-11-17T10:51:31Z)

Docs updated with this information now.
[https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#post-install-actions](url)

---

### 评论 #5 — Rmalavally (2021-11-17T14:32:49Z)

Minor correction. 

The URL to access the documentation on post-install actions is:

https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation_new.html#post-install-actions-and-verification-process

AMD ROCm Documentation

---

### 评论 #6 — Malexandra-de (2021-11-21T22:21:54Z)

Thanks.

---
