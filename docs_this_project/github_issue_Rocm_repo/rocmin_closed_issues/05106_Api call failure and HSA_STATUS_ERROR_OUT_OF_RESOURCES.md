# Api call failure and HSA_STATUS_ERROR_OUT_OF_RESOURCES

- **Issue #:** 5106
- **State:** closed
- **Created:** 2025-07-27T17:56:38Z
- **Updated:** 2025-08-13T18:05:51Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5106

### Problem Description

Whenever I run rocminfo it prints out following:

WSL environment detected.
hsa api call failure at: /longer_pathname_so_that_rpms_can_support_packaging_the_debug_info_for_all_os_profiles/src/rocminfo/rocminfo.cc:1306
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

### Operating System

WSL 2 Ubuntu Jammy 22.04.5 LTS

### CPU

AMD Ryzen 7 7800X3D

### GPU

rx 7800 xt 

### ROCm Version

6.4.2

### ROCm Component

ROCm

### Steps to Reproduce

I upgraded from 6.4.1 to 6.4.2 since I had torch, torchvision and etc for 6.4.2 and when I did sudo reboot and shutdown, this happened.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

Now while rx 7800 xt is in the supported category, I find this very frustrating, since I cannot run my gpu for AI development.