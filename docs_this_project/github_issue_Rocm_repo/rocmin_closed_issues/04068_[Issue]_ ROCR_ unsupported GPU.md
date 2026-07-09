# [Issue]: ROCR: unsupported GPU

- **Issue #:** 4068
- **State:** closed
- **Created:** 2024-11-30T04:03:33Z
- **Updated:** 2025-01-28T07:49:23Z
- **Labels:** ROCm 6.1.0, AMD Radeon 7800XT
- **URL:** https://github.com/ROCm/ROCm/issues/4068

### Problem Description

ROCR: unsupported GPU
hsa api call failure at: ./sources/wsl/tools/rocminfo/rocminfo.cc:1087
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.



### Operating System

Linux DESKTOP-0O8UKKK 5.15.167.4-microsoft-standard-WSL2 #1 SMP Tue Nov 5 00:21:55 UTC 2024 x86_64 x86_64 x86_64 GNU/Linux

### CPU

AMD Ryzen 7500F

### GPU

AMD Radeon 7800XT

### ROCm Version

ROCm 6.1.0

### ROCm Component

ROCm

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_