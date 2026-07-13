# [Issue]: WSL environment detected. ROCR: unsupported GPU hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1306 Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

- **Issue #:** 4215
- **State:** closed
- **Created:** 2025-01-02T02:33:10Z
- **Updated:** 2025-08-09T16:31:17Z
- **Labels:** Under Investigation, ROCm 6.2.3, AMD Radeon RX 7700XT
- **URL:** https://github.com/ROCm/ROCm/issues/4215

### Problem Description

Im trying to install ComfyUI in WSL2 im following this [Tutorial](https://www.youtube.com/watch?v=p1jKqV9IV8I) and https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/wsl/install-radeon.html 
when i try to do post-install verification by "rocminfo" im getting this error. 
GPU drivers are 24.12.1 and windows 11OS
im not sure what else to add in here. if this info is not enough please let me know, i will try to provide it. 

### Operating System

Ubuntu 22.04.5

### CPU

AMD Ryzen 5 7600X

### GPU

AMD Radeon RX 7700XT

### ROCm Version

ROCm 6.2.3

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_