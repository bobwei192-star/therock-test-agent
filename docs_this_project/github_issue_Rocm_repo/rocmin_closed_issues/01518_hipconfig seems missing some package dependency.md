# hipconfig seems missing some package dependency

- **Issue #:** 1518
- **State:** closed
- **Created:** 2021-07-12T02:44:59Z
- **Updated:** 2021-07-12T08:54:21Z
- **URL:** https://github.com/ROCm/ROCm/issues/1518

When manually installed HIP according to here: [HIP-Installation](https://rocmdocs.amd.com/en/latest/Installation_Guide/HIP-Installation.html). And run the following command:

`/opt/hip/bin/hipconfig --full`

shows:

```
HIP version  : 4.2.21155-37cb3a34

== hipconfig
HIP_PATH     : /opt/hip
ROCM_PATH    : /opt/rocm
HIP_COMPILER : clang
HIP_PLATFORM : amd
HIP_RUNTIME  : rocclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I"/opt/hip/include" -I"/opt/rocm/llvm/bin/../lib/clang/12.0.0" -I/opt/rocm/hsa/include

== hip-clang
HSA_PATH         : /opt/rocm/hsa
HIP_CLANG_PATH   : /opt/rocm/llvm/bin
clang version 12.0.0 (https://github.com/RadeonOpenCompute/llvm-project.git b204d7f0cae65b6cd4446eec50fc1fb675d582af)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/llvm/bin
LLVM (http://llvm.org/):
  LLVM version 12.0.0git
  Optimized build with assertions.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: znver1

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags : Can't exec "/opt/rocm/bin/rocm_agent_enumerator": No such file or directory at /opt/hip/bin/hipcc line 592.
Use of uninitialized value $targetsStr in substitution (s///) at /opt/hip/bin/hipcc line 593.
Use of uninitialized value $targetsStr in split at /opt/hip/bin/hipcc line 599.
 -std=c++11 -isystem "/opt/rocm/llvm/lib/clang/12.0.0/include/.." -isystem /opt/rocm/hsa/include -isystem "/opt/hip/include" -O3
hip-clang-ldflags  : Can't exec "/opt/rocm/bin/rocm_agent_enumerator": No such file or directory at /opt/hip/bin/hipcc line 592.
Use of uninitialized value $targetsStr in substitution (s///) at /opt/hip/bin/hipcc line 593.
Use of uninitialized value $targetsStr in split at /opt/hip/bin/hipcc line 599.
--driver-mode=g++ -L"/opt/hip/lib" -O3 -lgcc_s -lgcc -lpthread -lm -lrt

=== Environment Variables
PATH=/home/yimin/anaconda3/bin:/home/yimin/anaconda3/condabin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/games:/usr/local/games:/snap/bin

== Linux Kernel
Hostname     : yimin-System-Product-LatexWorkstation
Linux yimin-System-Product-LatexWorkstation 5.4.0-050400-lowlatency #201911242031 SMP PREEMPT Mon Nov 25 01:44:43 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04.5 LTS
Release:	18.04
Codename:	bionic

```

it says: Can't exec "/opt/rocm/bin/rocm_agent_enumerator" ...... , how to fix it?
