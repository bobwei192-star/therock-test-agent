# [Issue]: clang: error: cannot find HIP runtime

- **Issue #:** 2903
- **State:** closed
- **Created:** 2024-02-17T16:34:33Z
- **Updated:** 2024-07-01T11:33:02Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon RX 7900 XT
- **URL:** https://github.com/ROCm/ROCm/issues/2903

### Problem Description

Just installed ROCM and it doesn't work:

```
user@host :~/gpu/snippets/asm1$ /opt/rocm/bin/hipcc --save-temps -o test1 test1.cpp
clang: error: cannot find HIP runtime; provide its path via '--rocm-path', or pass '-nogpuinc' to build without HIP runtime
clang: error: cannot find HIP runtime; provide its path via '--rocm-path', or pass '-nogpuinc' to build without HIP runtime
user@host :~/gpu/snippets/asm1$ 
```


another attempt:

```
user@host :~/gpu/snippets/asm1$ /opt/rocm/bin/hipcc --rocm-path=/opt/rocm -o test1 test1.cpp
clang: error: cannot find HIP runtime; provide its path via '--rocm-path', or pass '-nogpuinc' to build without HIP runtime
clang: error: cannot find HIP runtime; provide its path via '--rocm-path', or pass '-nogpuinc' to build without HIP runtime
user@host :~/gpu/snippets/asm1$ 
```

I just downloaded amdgpu install and ran:
` amdgpu-install --usecase=graphics,rocm`
 
 didn't do anything extraordinary
 
```
 user@host :~/gpu/snippets/asm1$ /opt/rocm/bin/hipcc --version
HIP version: 5.7.0-0
AMD clang version 17.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-6.0.2 24012 af27734ed982b52a9f1be0f035ac91726fc697e4)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/llvm/bin
Configuration file: /opt/rocm-6.0.2/lib/llvm/bin/clang++.cfg

```

### Operating System

Ubuntu 22.04.4 LTS

### CPU

 Ryzen 7 3700X

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.0.0

### ROCm Component

HIP

### Steps to Reproduce

Follow official installation guide

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_