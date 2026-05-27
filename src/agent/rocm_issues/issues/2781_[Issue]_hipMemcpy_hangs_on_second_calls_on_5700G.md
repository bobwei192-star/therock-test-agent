# [Issue]: hipMemcpy hangs on second calls on 5700G

> **Issue #2781**
> **状态**: closed
> **创建时间**: 2024-01-07T12:53:00Z
> **更新时间**: 2024-04-21T13:18:34Z
> **关闭时间**: 2024-04-21T13:18:34Z
> **作者**: taweili
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2781

## 负责人

- benrichard-amd

## 描述

### Problem Description

```
OS:
NAME="Ubuntu"
VERSION="22.04.3 LTS (Jammy Jellyfish)"
CPU: 
model name	: AMD Ryzen 7 5700G with Radeon Graphics
GPU:
  Name:                    AMD Ryzen 7 5700G with Radeon Graphics
  Marketing Name:          AMD Ryzen 7 5700G with Radeon Graphics
  Name:                    gfx90c                             
  Marketing Name:          AMD Radeon Graphics                
      Name:                    amdgcn-amd-amdhsa--gfx90c:xnack-   
```
Compile the following program with hipcc and `HSA_OVERRIDE_GFX_VERSION=9.0.0`
```
OS:
NAME="Ubuntu"
VERSION="22.04.3 LTS (Jammy Jellyfish)"
CPU: 
model name	: AMD Ryzen 7 5700G with Radeon Graphics
GPU:
  Name:                    AMD Ryzen 7 5700G with Radeon Graphics
  Marketing Name:          AMD Ryzen 7 5700G with Radeon Graphics
  Name:                    gfx900                            
  Marketing Name:          AMD Radeon Graphics                
      Name:                    amdgcn-amd-amdhsa--gfx900:xnack-   
```
The allocations work and the first hipMemcpy works but hangs at second call to copy y. 
```c++
#include <hip/hip_runtime.h>
#include <stdio.h>

#define HIP_SAFECALL(x) { \
  hipError_t status = x; \
  if (status != hipSuccess) { \
    printf("HIP Error: %s\n", hipGetErrorString(status)); \
  } \
}

int main(void) {
    const int n = 10000;
    float x[n], y[n];
    float *x_, *y_;

    for (int i = 0; i < n; i++) {
        x[i] = y[i] = 1.0f;
    }

    HIP_SAFECALL(hipMalloc((void **)&x_, sizeof(float) * n));
    printf("x_ allocated\n");
    HIP_SAFECALL(hipMalloc((void **)&y_, sizeof(float) * n));
    printf("y_ allocated\n");
    HIP_SAFECALL(hipMemcpy(x_, x, sizeof(float) * n, hipMemcpyHostToDevice));
    printf("x_ copied\n");
    HIP_SAFECALL(hipMemcpy(y_, y, sizeof(float) * n, hipMemcpyHostToDevice));
    printf("y_ copied\n");

    return 0;
}
```

### Operating System

Ubuntu 22.04

### CPU

AMD Ryzen 7 5700G with Radeon Graphics

### GPU

Other

### Other

_No response_

### ROCm Version

ROCm 6.0.0

### ROCm Component

HIP

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_
