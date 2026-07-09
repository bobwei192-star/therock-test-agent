# [Issue]: WSL2 Environment detected

- **Issue #:** 3677
- **State:** closed
- **Created:** 2024-09-04T19:16:35Z
- **Updated:** 2024-09-10T16:18:33Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XT, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3677

### Problem Description

When i run rocminfo i get the error

WSL environment detected.
hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1306
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

Also when I try to run 

 echo "GPU:" && /opt/rocm/bin/rocminfo | grep -E "^\s*(Name|Marketing Name)"

There is nothing listed. I have tried different versions of the AMD adrenalin software that shows support for wsl2.

### Operating System

WSL2 Ubuntu 24.04

### CPU

Ryzen 9 3900x

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.2.0

### ROCm Component

rocminfo

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

WSL environment detected.
hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1306
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

### Additional Information

_No response_