# Drop Python 2 Dependencies

> **Issue #1767**
> **状态**: closed
> **创建时间**: 2022-07-08T10:21:59Z
> **更新时间**: 2024-07-29T20:59:04Z
> **关闭时间**: 2024-07-29T20:59:04Z
> **作者**: Bengt
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/1767

## 标签

- **Under Investigation** (颜色: #0052cc)

## 负责人

- saadrahim

## 描述

Currently, various components of ROCm rely on Python 2 as a dependency. This is problematic, because Python 2 is discontinued and Linux distributions tend to no longer include it in the repositories of their current OS releases. ROCm should therefore work towards dropping Python 2 dependencies in all its components.

---

## 评论 (5 条)

### 评论 #1 — Bengt (2022-07-08T10:22:59Z)

Idea for this issue: https://github.com/RadeonOpenCompute/ROCm/issues/1761#issuecomment-1178804147

---

### 评论 #2 — saadrahim (2022-07-08T16:59:44Z)

Is there a list of ROCm components that use python2? That will be helpful but is not required for me to raise this issue internally. 


---

### 评论 #3 — Bengt (2022-07-09T16:18:16Z)

Hi, @saadrahim! Finding a full list of implicit and explicit dependencies on Python is difficult. One approach would be to change all [Shebangs](https://de.wikipedia.org/wiki/Shebang) to Python 3 and hope that the software breaks in obvious ways. There are quite a few (115 at the time of writing) instances of shebangs that do not specify the Python version explicitly in this organization:

<https://github.com/search?q=org%3ARadeonOpenCompute+%21%2Fusr%2Fbin%2Fenv+python&type=code>

Based on that search, the affected projects are at least:

-   [RadeonOpenCompute/hcc-clang-upgrade](https://github.com/RadeonOpenCompute/hcc-clang-upgrade)
-   [RadeonOpenCompute/ROCK-Kernel-Driver](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver)
-   [RadeonOpenCompute/rdc](https://github.com/RadeonOpenCompute/rdc)
-   [RadeonOpenCompute/rocm_smi_lib](https://github.com/RadeonOpenCompute/rocm_smi_lib)

It may also be worth considering, if other affected AMD components need upgrading. A search for those:

<https://github.com/search?q=org%3Aamd+%21%2Fusr%2Fbin%2Fenv+python&type=code>

These seem to be:

-   [amd/OpenCL-caffe](https://github.com/amd/OpenCL-caffe)
-   [amd/rest3d](https://github.com/amd/rest3d)
-   [amd/Chromium-WebCL](https://github.com/amd/Chromium-WebCL)
-   [amd/UIF](https://github.com/amd/UIF)

GPUOpen-Drivers is also affected:

<https://github.com/search?q=org%3AGPUOpen-Drivers+%21%2Fusr%2Fbin%2Fenv+python&type=code>

Specifically these projects:

-   [GPUOpen-Drivers/llpc](https://github.com/GPUOpen-Drivers/llpc)
-   [GPUOpen-Drivers/spvgen](https://github.com/GPUOpen-Drivers/spvgen)
-   [GPUOpen-Drivers/xgl](https://github.com/GPUOpen-Drivers/xgl)

---

### 评论 #4 — ppanchad-amd (2024-07-29T15:14:24Z)

Internal ticket is created to fix this issue. Thanks!

---

### 评论 #5 — jamesxu2 (2024-07-29T20:59:04Z)

Hi there, as of ROCm 6.1.2, I don't see that ROCm uses Python2 as a dependency. I'm able to install ROCm using the [amdgpu-installer](https://rocm.docs.amd.com/projects/install-on-linux/en/develop/install/amdgpu-install.html#ubuntu) on Ubuntu 22.04, and compile and run HIP applications without having python2 installed (check using ``` apt list --installed | grep python2```). 

Also, there is internal awareness about the discontinuation of Python 2 and an ongoing effort to purge it. Thanks for highlighting this issue.

---
