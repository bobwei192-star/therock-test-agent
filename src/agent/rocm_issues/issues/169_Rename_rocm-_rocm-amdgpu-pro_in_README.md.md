# Rename rocm-> rocm-amdgpu-pro in README.md

> **Issue #169**
> **状态**: closed
> **创建时间**: 2017-07-20T16:14:37Z
> **更新时间**: 2017-07-20T20:30:36Z
> **关闭时间**: 2017-07-20T20:30:36Z
> **作者**: jh2li
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/169

## 描述

There is no package named rocm anymore. Please update README.md.
sudo apt-get install rocm rocm-opencl-dev
To
sudo apt-get install rocm-amdgpu-pro rocm-amdgpu-pro-opencl-dev


---

## 评论 (1 条)

### 评论 #1 — gstoner (2017-07-20T20:30:34Z)

This is not CORRECT,   ROCm is the correct driver package to install from ROCm repo at the instructions 

ROCm driver is driver for the server market.   The AMDGPUpro recently added rocm functionality for only OpenCL support based on there packages.  The current ROCm packages are at https://rocm.github.io/ROCmLinuxpackages.html  should be run on the ROCm driver using these instructions  https://rocm.github.io/ROCmInstall.html



---
