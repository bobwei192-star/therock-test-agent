# [Issue]: <hip/device_functions.h> header automatially padded to <hip/hip/device_function.h> when building rocm for torch extension

- **Issue #:** 3937
- **State:** closed
- **Created:** 2024-10-23T08:11:09Z
- **Updated:** 2025-04-22T19:06:27Z
- **Labels:** Under Investigation, ROCm 6.2.3, mi300
- **URL:** https://github.com/ROCm/ROCm/issues/3937

### Problem Description

as  `device_functions.h` is located at `/opt/rocm/include/hip` , so expecting to use it as: 

```c++
#include <hip/hip_runtime.h>
#include <hip/hip_runtime_api.h>
// Buggy: somehow setuptool will add prefix to <hip/hip/device_functions.h>
// #include <hip/device_functions.h>  // for amd_warp_sync_functions
#include <device_functions.h>
```

while it's auto padded to  <hip/hip/device_functions.h>,  and to make it work, had to modify as `#include<device_functions.h>`

is this expected behavior ?

Thanks
David 

### Operating System

Ubuntu 22.04

### CPU

Ryzen 

### GPU

mi300

### ROCm Version

ROCm 6.2.3

### ROCm Component

hipBLAS

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_