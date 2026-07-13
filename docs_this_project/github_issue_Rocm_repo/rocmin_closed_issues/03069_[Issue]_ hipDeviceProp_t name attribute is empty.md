# [Issue]: hipDeviceProp_t name attribute is empty 

- **Issue #:** 3069
- **State:** closed
- **Created:** 2024-04-25T21:24:35Z
- **Updated:** 2024-06-21T19:27:27Z
- **Labels:** AMD Instinct MI250X, ROCm 6.0.0, AMD Instinct MI100, AMD Instinct MI250
- **URL:** https://github.com/ROCm/ROCm/issues/3069

### Problem Description

Reopening since the attribute name for the device string is empty with rocm-6.0.0 on MI250, MI100, MI250x. Tagging @nartmada 
```bash
HIP version: 6.0.32830-d62f6a171
AMD clang version 17.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-6.0.0 23483 7208e8d15fbf218deb74483ea8c549c67ca4985e)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /soft/compilers/rocm/rocm-6.0.0/llvm/bin
Configuration file: /soft/compilers/rocm/rocm-6.0.0/lib/llvm/bin/clang++.cfg
```


### Operating System

openSUSE Leap 15.4

### CPU

AMD EPYC 7543 32-Core Processor

### GPU

AMD Instinct MI250X, AMD Instinct MI250, AMD Instinct MI100

### ROCm Version

ROCm 6.0.0

### ROCm Component

HIP

### Steps to Reproduce

```c++
#include<iostream>
#include <hip/hip_runtime.h>
int main(){
  hipDeviceProp_t deviceProp;
  hipGetDeviceProperties(&deviceProp, 0);
  std::cout << deviceProp.name << std::endl;
}
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

Mentioned in these issues: https://github.com/ROCm/ROCm/issues/1625, https://github.com/ROCm/ROCm/issues/1778