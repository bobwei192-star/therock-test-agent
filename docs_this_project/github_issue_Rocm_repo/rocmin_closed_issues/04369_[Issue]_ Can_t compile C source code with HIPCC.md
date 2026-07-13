# [Issue]: Can't compile C source code with HIPCC

- **Issue #:** 4369
- **State:** closed
- **Created:** 2025-02-12T16:08:47Z
- **Updated:** 2026-03-19T10:32:57Z
- **Labels:** Under Investigation, ROCm 6.3.2
- **URL:** https://github.com/ROCm/ROCm/issues/4369

### Problem Description

Hello everyone!

I'm pretty new to GPU programming and specially with ROCm. While I was doing some experiments to learn how things worked I came across a pretty interesting issue. If I try to compile a **C program** using the HIP API I got the following error:

![Image](https://github.com/user-attachments/assets/917a63f8-b2e8-455c-b1ec-d57cdc119990)

Here's the source code for the program (if it's relevant):
```
#include "hip/hip_runtime.h"
#include <stdio.h>

// HIP kernel function
__global__ void helloFromGPU() {
    printf("Hello, World from GPU!\n");
}

int main() {
    printf("Hello, World from CPU!\n");
    
    // Launch the kernel with 1 block and 1 thread
    helloFromGPU<<<1, 1>>>();
    
    // Wait for GPU to finish before accessing printf output
    int ret = hipDeviceSynchronize();
    
    return 0;
}
```

But if simply rename the file to have the .cpp extension, I can compile it perfectly and execute the output program with no issues:

![Image](https://github.com/user-attachments/assets/42383946-383a-4405-83de-de10eebd16cc)

Why is this happening? Am I doing the correct compilation procedure for HIP programs?

Thanks in advance for any help!

### Operating System

Linux Mint 22.1 (Xia)

### CPU

AMD Ryzen 5 5500U with Radeon Graphics

### GPU

AMD Radeon Graphics gfx90c

### ROCm Version

ROCm 6.3.2

### ROCm Component

HIPCC

### Additional Information

Here's the output of my `hipconfig -f` to better understand the environment I'm running ROCm:
```

HIP version: 6.3.42134-a9a80e791

==hipconfig
HIP_PATH           :/opt/rocm-6.3.2
ROCM_PATH          :/opt/rocm-6.3.2
HIP_COMPILER       :clang
HIP_PLATFORM       :amd
HIP_RUNTIME        :rocclr
CPP_CONFIG         : -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I/opt/rocm-6.3.2/include -I/include

==hip-clang
HIP_CLANG_PATH     :/opt/rocm-6.3.2/lib/llvm/bin
AMD clang version 18.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.3.2 25012 e5bf7e55c91490b07c49d8960fa7983d864936c4)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-6.3.2/lib/llvm/bin
Configuration file: /opt/rocm-6.3.2/lib/llvm/bin/clang++.cfg
AMD LLVM version 18.0.0git
  Optimized build.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: znver2

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags :
 -O3
hip-clang-ldflags :
--driver-mode=g++ -O3 --hip-link

== Environment Variables
PATH =/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/rocm-6.3.2/bin

== Linux Kernel
Hostname      :
LinuxMint-Henrique
Linux LinuxMint-Henrique 6.11.0-17-generic #17~24.04.2-Ubuntu SMP PREEMPT_DYNAMIC Mon Jan 20 22:48:29 UTC 2 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID:	Linuxmint
Description:	Linux Mint 22.1
Release:	22.1
Codename:	xia
```