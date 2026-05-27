# [Issue]: Driver not initialized (amdgpu not found in modules)

> **Issue #2767**
> **状态**: closed
> **创建时间**: 2023-12-22T04:54:40Z
> **更新时间**: 2025-02-10T07:50:49Z
> **关闭时间**: 2024-04-05T14:52:10Z
> **作者**: PatchouliPatch
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/2767

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

### Problem Description

Previously, I was able to run ROCm 5.7.1 without any issues but as soon as I installed ROCm 6.0 it would not function properly.

Upon running rocm-smi after performing an install using `sudo amdgpu-install --usecase=rocm,hiplibsdk,graphics` and rebooting, I get the following error:

cat: /sys/module/amdgpu/initstate: No such file or directory
ERROR:root:Driver not initialized (amdgpu not found in modules)

### Operating System

22.04.3 LTS (Jammy Jellyfish)

### CPU

AMD Ryzen 7 7700X 8-Core Processor

### GPU

AMD Radeon RX 7900 XTX

### Other

_No response_

### ROCm Version

ROCm 6.0.0

### ROCm Component

ROCm

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

cannot use `rocminfo --support`, gives the error: `ROCk module is NOT loaded, possibly no GPU devices`


### Additional Information

[rocm-output.txt](https://github.com/ROCm/ROCm/files/13748456/rocm-output.txt)
Here is the terminal output when I attempted to uninstall then reinstall ROCm 6.0
