# [Issue]: error output from rocminfo with AMD Radeon Pro W7900

- **Issue #:** 2682
- **State:** closed
- **Created:** 2023-11-29T15:01:16Z
- **Updated:** 2024-01-30T16:22:32Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/2682

### Problem Description

Run rocminfo

### Operating System

Ubun

### CPU

AMD Ryzen 7900

### GPU

AMD Radeon Pro W7900

### ROCm Version

5.7.1

### ROCm Component

_No response_

### Steps to Reproduce

1. run rocminfo

### Output of /opt/rocm/bin/rocminfo --support

amd@AIG-PM:~$ rocminfo
ROCk module is loaded
hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1204
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
