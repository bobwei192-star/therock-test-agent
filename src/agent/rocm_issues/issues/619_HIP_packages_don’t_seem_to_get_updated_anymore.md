# HIP packages don’t seem to get updated anymore

> **Issue #619**
> **状态**: closed
> **创建时间**: 2018-11-19T16:20:34Z
> **更新时间**: 2018-11-19T16:44:12Z
> **关闭时间**: 2018-11-19T16:44:12Z
> **作者**: 949f45ac
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/619

## 描述

Hey there, don’t know whether I’m being totally stupid or the hip packages (mainly `hip_base`) are quite out of date in the Ubuntu Xenial repository. As per link in the README of this repo, I’d expect HIP to be in the state of its roc-1.9.x branch: https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP/tree/roc-1.9.x

Yet when I locally inspect the installed `/opt/rocm/hip/include/hip/hcc_detail/device_functions.hpp` for example, they are out of date compared to the file in the github branch. Timestamp says September 5.

Hope we can figure this out!
Cheers!

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2018-11-19T16:44:08Z)

The HIP packages are released on ROCm point release (e.g. 1.9.0, 1.9.1, the upcoming 1.9.2). However, the HIP 1.9.x branch is where all up-to-date development is done (at this point in time). Upon a ROCm point release, we [tag](https://github.com/ROCm-Developer-Tools/HIP/tags) the commit that is packaged.

Basically, you're comparing a _release version_ that is installed on your system with a _development version_ that exists in our code repository.

---
