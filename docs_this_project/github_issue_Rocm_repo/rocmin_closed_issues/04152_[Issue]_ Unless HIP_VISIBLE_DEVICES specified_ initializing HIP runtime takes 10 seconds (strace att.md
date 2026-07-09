# [Issue]: Unless HIP_VISIBLE_DEVICES specified, initializing HIP runtime takes 10 seconds (strace attached).

- **Issue #:** 4152
- **State:** closed
- **Created:** 2024-12-12T20:35:45Z
- **Updated:** 2024-12-16T21:52:13Z
- **Labels:** Under Investigation, ROCm 6.2.0, 8x  MI300X in CPX mode (total 64 logical devices).
- **URL:** https://github.com/ROCm/ROCm/issues/4152

### Problem Description

This simple test program doing just a 1-byte `hipMalloc` takes 10 seconds to run:
```c++
#include <hip/hip_runtime.h>

int main() {
  char* p;
  (void)hipMalloc(&p, 1);
}
```

But if I specify `HIP_VISIBLE_DEVICES=63` to pin to one specific GPU, then it runs in under 1 second.

I `strace`'d it and a difference that stood out was the `AMDKFD_IOC_MAP_MEMORY_TO_GPU` `ioctl`'s. These often have latency over 60ms.

By default (when the program takes 10 seconds), there are 260 such `ioctl`'s.
With `HIP_VISIBLE_DEVICES=63`, there are 135 such `ioctl's`.

Why is the number of `AMDKFD_IOC_MAP_MEMORY_TO_GPU` `ioctl`'s 2x higher when not pinned to a GPU? I thought that once a device has been picked, `HIP_VISIBLE_DEVICES` shouldn't make a difference anymore.

### Operating System

Ubuntu 22.04

### CPU

2x AMD EPYC 9454 48-Core Processor

### GPU

8x  MI300X in CPX mode (total 64 logical devices).

### ROCm Version

ROCm 6.2.0

### ROCm Component

HIP

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_