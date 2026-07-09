# [Issue]: amdgpu-dkms fails with Ubuntu kernel 6.8.0-44

- **Issue #:** 3701
- **State:** closed
- **Created:** 2024-09-11T08:12:13Z
- **Updated:** 2025-11-06T09:36:56Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX, AMD Radeon VII, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3701

### Problem Description

Looks like another problem with `amdgpu-dkms` and new kernels. I was running ROCm 6.2 just fine with kernel 6.8.0-41 - Ubuntu just pushed kernel 6.8.0-44, however, `amdgpu-dkms` fails with that kernel. Rolling back to kernel 6.8.0-41 restored ROCm for me.

### Operating System

Ubuntu 24.04.1

### CPU

Zen 2 and Zen 3

### GPU

AMD Radeon RX 7900 XTX, AMD Radeon VII

### ROCm Version

ROCm 6.2.0

### ROCm Component

ROCm

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_