# KMDUMPISA environment variable still valid?

- **Issue #:** 1321
- **State:** closed
- **Created:** 2020-12-05T21:33:25Z
- **Updated:** 2020-12-08T04:42:30Z
- **URL:** https://github.com/ROCm/ROCm/issues/1321

I'm building a HIP application with ROCm as backend (ver 3.9) and I'm trying to dump the ISA of the kernels by having KMDUMPISA environment variable set during build (via `export KMDUMPISA=1`), but that seems to be ignored. No `xxx.isa` files are produced.
Is this environent variable still valid in the latest ROCm releases? Is there any alternative option for ISA dumps?

The hipconfig output follows in case that helps:

```
HIP version  : 3.9.20412-6d111f85

== hipconfig
HIP_PATH     : /opt/rocm/hip
ROCM_PATH    : /opt/rocm
HIP_COMPILER : clang
HIP_PLATFORM : hcc
HIP_RUNTIME  : ROCclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__=  -I/opt/rocm/hip/include -I/opt/rocm/llvm/bin/../lib/clang/12.0.0 -I/opt/rocm/hsa/include -D__HIP_ROCclr__

== hip-clang
HSA_PATH         : /opt/rocm/hsa
HIP_CLANG_PATH   : /opt/rocm/llvm/bin
clang version 12.0.0 (/src/external/llvm-project/clang 60f39e2924d51c1e8606f2135f95e9047fb1da5d)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/llvm/bin
LLVM (http://llvm.org/):
  LLVM version 12.0.0git
  Optimized build.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: znver2

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags : hipcc-cmd: /opt/rocm/llvm/bin/clang++  -L/opt/rocm/hip/lib -O3 -lgcc_s -lgcc -lpthread -lm  --cxxflags -Wl,--enable-new-dtags -Wl,--rpath=/opt/rocm/hip/lib:/opt/rocm/lib -lamdhip64  -L/opt/rocm/llvm/bin/../lib/clang/12.0.0/lib/linux -lclang_rt.builtins-x86_64
-D__HIP_ROCclr__ -std=c++11 -isystem /opt/rocm-3.9.0/llvm/lib/clang/12.0.0/include/.. -isystem /opt/rocm/hsa/include -D__HIP_ROCclr__ -isystem /opt/rocm/hip/include -D__HIP_ARCH_GFX1012__=1  -D__HIP_ARCH_GFX803__=1  -O3
hip-clang-ldflags  : hipcc-cmd: /opt/rocm/llvm/bin/clang++  -L/opt/rocm/hip/lib -O3 -lgcc_s -lgcc -lpthread -lm  --ldflags -Wl,--enable-new-dtags -Wl,--rpath=/opt/rocm/hip/lib:/opt/rocm/lib -lamdhip64  -L/opt/rocm/llvm/bin/../lib/clang/12.0.0/lib/linux -lclang_rt.builtins-x86_64
 -L/opt/rocm/hip/lib -O3 -lgcc_s -lgcc -lpthread -lm

=== Environment Variables
PATH=/home/elias/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin:/opt/rocm/bin:/opt/rocm/profiler/bin:/opt/rocm/opencl/bin:/opt/rocm/hip/bin
HIP_PRINT_ENV=1
HIP_PATH=/opt/rocm/hip
HIPCC_VERBOSE=1

== Linux Kernel
Hostname     : Neptune
Linux Neptune 5.4.0-54-generic #60-Ubuntu SMP Fri Nov 6 10:37:59 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID: Ubuntu
Description:    Ubuntu 20.04.1 LTS
Release:        20.04
Codename:       focal

```