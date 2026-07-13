# Failing to install amdgpu-dkms on OEM Kernel

- **Issue #:** 1906
- **State:** closed
- **Created:** 2023-02-13T19:43:58Z
- **Updated:** 2024-01-16T22:26:59Z
- **URL:** https://github.com/ROCm/ROCm/issues/1906

Hello,

I am running Ubuntu 22.04 and I installed the `linux-image-5.17.0-1020-oem` kernel. Although that kernel is listed as supported I was unable to install ROCm 5.3.3 since the installation of the amdgpu dkms module failed as described below (https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.3.3/page/Introduction_to_ROCm_Installation_Guide_for_Linux.html)

When I run `apt install `amdgpu-dkms` I get the following error:
[amdgpu-dkms-firmware.0.log](https://github.com/RadeonOpenCompute/ROCm/files/10725726/amdgpu-dkms-firmware.0.log)

System Information
HIP version  : 5.3.22062-659cc197

== hipconfig
HIP_PATH     : /opt/rocm-5.3.3
ROCM_PATH    : /opt/rocm-5.3.3
HIP_COMPILER : clang
HIP_PLATFORM : amd
HIP_RUNTIME  : rocclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I/opt/rocm-5.3.3/include -I/opt/rocm-5.3.3/llvm/bin/../lib/clang/15.0.0 -I/opt/rocm-5.3.3/hsa/include

== hip-clang
HSA_PATH         : /opt/rocm-5.3.3/hsa
HIP_CLANG_PATH   : /opt/rocm-5.3.3/llvm/bin
AMD clang version 15.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-5.3.3 22414 b4eabb4b000fedc027fe0075b2b1ea4becc5d6bd)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-5.3.3/llvm/bin
AMD LLVM version 15.0.0git
  Optimized build.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: znver2

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags :  -std=c++11 -isystem "/opt/rocm-5.3.3/llvm/lib/clang/15.0.0/include/.." -isystem /opt/rocm-5.3.3/hsa/include -isystem "/opt/rocm-5.3.3/include" -O3
hip-clang-ldflags  :  -L"/opt/rocm-5.3.3/lib" -O3 -lgcc_s -lgcc -lpthread -lm -lrt

=== Environment Variables
PATH=/home/aschroeter/.local/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/usr/local/cuda/bin/:/opt/rocm/bin/

== Linux Kernel
Hostname     : dev08
Linux dev08 5.17.0-1020-oem #21-Ubuntu SMP PREEMPT Fri Oct 14 09:33:24 UTC 2022 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 22.04.1 LTS
Release:        22.04
Codename:       jammy

Thanks Alex