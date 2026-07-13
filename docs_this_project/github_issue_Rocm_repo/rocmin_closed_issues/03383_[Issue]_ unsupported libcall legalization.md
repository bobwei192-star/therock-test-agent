# [Issue]: unsupported libcall legalization

- **Issue #:** 3383
- **State:** closed
- **Created:** 2024-07-02T15:58:37Z
- **Updated:** 2024-08-08T15:37:11Z
- **Labels:** AMD Radeon RX 7900 XTX, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3383

### Problem Description

I am getting a unsupported libcall legalization error when trying to compile a hip file.

```
fatal error: error in backend: unsupported libcall legalization
clang++: error: clang frontend command failed with exit code 70 (use -v to see invocation)
AMD clang version 17.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-6.1.2 24193 669db884972e769450470020c06a6f132a8a065b)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-6.1.2/llvm/bin
Configuration file: /opt/rocm-6.1.2/lib/llvm/bin/clang++.cfg
clang++: note: diagnostic msg: Error generating preprocessed source(s).
make[2]: *** [CMakeFiles/custom_ops.dir/build.make:127: CMakeFiles/custom_ops.dir/hip/file.cu.hip.o] Error 1
make[1]: *** [CMakeFiles/Makefile2:102: CMakeFiles/custom_ops.dir/all] Error 2
make: *** [Makefile:136: all] Error 2
```

### Operating System

Ubuntu 22.04

### CPU

AMD EPYC 7R32

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.1.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_