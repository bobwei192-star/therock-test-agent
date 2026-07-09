# [Issue]: RuntimeError: HIP error: invalid argument  when running  any model

- **Issue #:** 3999
- **State:** closed
- **Created:** 2024-11-06T16:22:53Z
- **Updated:** 2025-01-13T21:22:59Z
- **Labels:** Under Investigation, ROCm 5.7.0, AMD Instinct MI50 (Radeon Instinct MI50 32GB)
- **URL:** https://github.com/ROCm/ROCm/issues/3999

### Problem Description


**Error details:**
When I try to run any model (including the example: https://rocm.blogs.amd.com/artificial-intelligence/pytorch-lightning/README.html) it returns following error:

RuntimeError: HIP error: invalid argument
HIP kernel errors might be asynchronously reported at some other API call, so the stacktrace below might be incorrect.
For debugging consider passing AMD_SERIALIZE_KERNEL=3
Compile with `TORCH_USE_HIP_DSA` to enable device-side assertions.


**Comments**
We have invested in  ROCm AMD instead of NVIDIA CUDA but this is stopping us from using these GPUs in any meaningful way. Can you please let me know how to fix this issue please?



**setup details**:

$  echo "OS:" && cat /etc/os-release | grep -E "^(NAME=|VERSION=)";
OS:
NAME="Rocky Linux"
VERSION="8.6 (Green Obsidian)"

$   echo "CPU: " && cat /proc/cpuinfo | grep "model name" | sort --unique;
CPU: 
model name      : AMD EPYC 7642 48-Core Processor

$   echo "GPU:" && /opt/rocm/bin/rocminfo | grep -E "^\s*(Name|Marketing Name)";
GPU:
  Name:                    AMD EPYC 7642 48-Core Processor    
  Marketing Name:          AMD EPYC 7642 48-Core Processor    
  Name:                    gfx906                             
  Marketing Name:          AMD Instinct MI50/MI60             
      Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
  Name:                    gfx906                             
  Marketing Name:          AMD Instinct MI50/MI60             
      Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
  Name:                    gfx906                             
  Marketing Name:          AMD Instinct MI50/MI60             
      Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-
  Name:                    gfx906                             
  Marketing Name:          AMD Instinct MI50/MI60             
      Name:                    amdgcn-amd-amdhsa--gfx906:sramecc+:xnack-


**ROCm details**:

$ rpm -qa | grep rocm
rocm-opencl-sdk-5.7.0.50700-63.el8.x86_64
rocm-hip-sdk-5.7.0.50700-63.el8.x86_64
rocm-core-5.7.0.50700-63.el8.x86_64
rocm-hip-runtime-5.7.0.50700-63.el8.x86_64
rocm-opencl-runtime-5.7.0.50700-63.el8.x86_64
rocm-cmake-0.10.0.50700-63.el8.x86_64
rocm-hip-runtime-devel-5.7.0.50700-63.el8.x86_64
rocm-hip-libraries-5.7.0.50700-63.el8.x86_64
rocm-llvm-17.0.0.23352.50700-63.el8.x86_64
rocm-ocl-icd-2.0.0.50700-63.el8.x86_64
rocm-device-libs-1.0.0.50700-63.el8.x86_64
rocm-llvm5.7.0-17.0.0.23352.50700-63.el8.x86_64
rocminfo-1.0.0.50700-63.el8.x86_64
rocm-opencl-2.0.0.50700-63.el8.x86_64
rocm-smi-lib-5.0.0.50700-63.el8.x86_64
rocminfo5.7.0-1.0.0.50700-63.el8.x86_64
rocm-language-runtime-5.7.0.50700-63.el8.x86_64
rocm-opencl-devel-2.0.0.50700-63.el8.x86_64
rocm-core5.7.0-5.7.0.50700-63.el8.x86_64




### Operating System

Rocky Linux(VERSION="8.6 (Green Obsidian)")

### CPU

model name      : AMD EPYC 7642 48-Core Processor

### GPU

AMD Instinct MI50 (Radeon Instinct MI50 32GB)

### ROCm Version

ROCm 5.7.0

### ROCm Component

_No response_

### Steps to Reproduce

just try to run your example code: https://rocm.blogs.amd.com/artificial-intelligence/pytorch-lightning/README.html

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_