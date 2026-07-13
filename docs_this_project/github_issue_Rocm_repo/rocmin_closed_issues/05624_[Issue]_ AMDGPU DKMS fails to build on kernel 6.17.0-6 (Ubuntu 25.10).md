# [Issue]: AMDGPU DKMS fails to build on kernel 6.17.0-6 (Ubuntu 25.10)

- **Issue #:** 5624
- **State:** closed
- **Created:** 2025-11-04T20:13:23Z
- **Updated:** 2026-03-02T16:57:22Z
- **Labels:** status: assessed
- **Assignees:** lucbruni-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5624

### Problem Description

## Similar, past issue
https://github.com/ROCm/ROCm/issues/5111

## Problem description

Per the title - after upgrading to Ubuntu 25.10 from Ubuntu 25.04, the amdgpu-dkms no longer compiles via DKMS. The compilation worked perfectly for the 6.14 kernel. 

Is the lack of support expected? If so, is there any timeline as to when will the 6.17 kernel supported (if at all)?


### Operating System

NAME="Ubuntu" VERSION="25.10 (Questing Quokka)"

### CPU

AMD Ryzen 7 5800X 8-Core Processor

### GPU

AMD Radeon RX 9070 XT (radeonsi, gfx1201, ACO, DRM 3.64, 6.17.0-6-generic)

### ROCm Version

ROCm 6.4.4.60404-129~24.04

### ROCm Component

_No response_

### Steps to Reproduce

```bash
sudo amdgpu-install --usecase=graphics,opencl,hip,rocm
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

For more detail, the beginning of the make log:
```
DKMS (dkms-3.2.0) make.log for amdgpu/6.12.12-2202139.24.04 for kernel 6.17.0-6-generic (x86_64)
Tue Nov  4 11:45:31 CET 2025
```

I do have the full output, along a full suite of logs (per the recommendations in the `amdgpu-install` documentation), which I can provide if needed.

### Other info

Thanks for all the hard work you do :) 