# [Issue]: Wrong warpSize in host code on 9070XT

- **Issue #:** 5423
- **State:** closed
- **Created:** 2025-09-24T08:46:50Z
- **Updated:** 2025-09-29T19:09:10Z
- **Labels:** status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5423

### Problem Description

warpSize return 64 in my host code, but it return 32 in my device code, the warp mode is 32 by default on my 9070XT, so I think the warpSize shall be 32 in both host and device code.

This happens on both Windows ROCm 6.4.2 and Linux ROCm 7.0.0 rc1. 

### Operating System

Ubuntu 24.04.3 LTS (Noble Numbat) and Windows 11 10.0.26100

### CPU

AMD Ryzen 9 7900X3D 12-Core Processor

### GPU

AMD Radeon RX 9070 XT

### ROCm Version

ROCm 6.4.2 on Windows and ROCm 7.0.0 rc1 on Linux

### ROCm Component

HIP

### Steps to Reproduce

main.hip
```
#include <hip/hip_runtime.h>

__global__ void test() {
    if (threadIdx.x == 0) {
        printf("warpSize from device is %i.\n", warpSize);
    }
}

int main(int argc, char** argv) {
    printf("warpSize from host is %i.\n", warpSize);
    test <<< 1, warpSize >>> ();
    return 0;
}
```

build command
```
"%HIP_PATH%bin/clang++" --offload-arch=gfx1201 main.hip -o main.exe
```

output
```
warpSize from host is 64.
warpSize from device is 32.
```


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_