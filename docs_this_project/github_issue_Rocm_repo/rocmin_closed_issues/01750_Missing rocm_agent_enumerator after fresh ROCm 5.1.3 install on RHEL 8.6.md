# Missing rocm_agent_enumerator after fresh ROCm 5.1.3 install on RHEL 8.6

- **Issue #:** 1750
- **State:** closed
- **Created:** 2022-06-08T18:32:40Z
- **Updated:** 2022-06-09T13:46:55Z
- **URL:** https://github.com/ROCm/ROCm/issues/1750

After 
>sudo amdgpu-install --usecase=rocm,hiplibsdk

following the instructuctions at https://docs.amd.com/bundle/ROCm-Installation-Guide-v5.1.3/page/How_to_Install_ROCm.html

/opt/rocm/bin/rocm_agent_enumerator is missing and a simple test compilation using hip fails. However the ~complete set of expected libraries and compilers appears to have been successfully installed and the GPU module is recognized by rocminfo.

```
$ hipconfig
HIP version  : 5.1.20532-f592a741

== hipconfig
HIP_PATH     : /opt/rocm-5.1.3/hip
ROCM_PATH    : /opt/rocm
HIP_COMPILER : clang
HIP_PLATFORM : amd
HIP_RUNTIME  : rocclr
CPP_CONFIG   :  -D__HIP_PLATFORM_HCC__= -D__HIP_PLATFORM_AMD__= -I/opt/rocm-5.1.3/hip/include -I/opt/rocm/llvm/bin/../lib/clang/14.0.0 -I/opt/rocm/hsa/include

== hip-clang
HSA_PATH         : /opt/rocm/hsa
HIP_CLANG_PATH   : /opt/rocm/llvm/bin
AMD clang version 14.0.0 (https://github.com/RadeonOpenCompute/llvm-project roc-5.1.3 22114 5cba46feb6af367b1cafaa183ec42dbfb8207b14)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm/llvm/bin
AMD LLVM version 14.0.0git
  Optimized build.
  Default target: x86_64-unknown-linux-gnu
  Host CPU: znver2

  Registered Targets:
    amdgcn - AMD GCN GPUs
    r600   - AMD GPUs HD2XXX-HD6XXX
    x86    - 32-bit X86: Pentium-Pro and above
    x86-64 - 64-bit X86: EM64T and AMD64
hip-clang-cxxflags : Can't exec "/opt/rocm/bin/rocm_agent_enumerator": No such file or directory at /opt/rocm-5.1.3/hip/bin//hipcc.pl line 609.
Use of uninitialized value $targetsStr in substitution (s///) at /opt/rocm-5.1.3/hip/bin//hipcc.pl line 610.
Use of uninitialized value $targetsStr in split at /opt/rocm-5.1.3/hip/bin//hipcc.pl line 616.
 -std=c++11 -isystem "/opt/rocm-5.1.3/llvm/lib/clang/14.0.0/include/.." -isystem /opt/rocm/hsa/include -isystem "/opt/rocm-5.1.3/hip/include" -O3
hip-clang-ldflags  : Can't exec "/opt/rocm/bin/rocm_agent_enumerator": No such file or directory at /opt/rocm-5.1.3/hip/bin//hipcc.pl line 609.
Use of uninitialized value $targetsStr in substitution (s///) at /opt/rocm-5.1.3/hip/bin//hipcc.pl line 610.
Use of uninitialized value $targetsStr in split at /opt/rocm-5.1.3/hip/bin//hipcc.pl line 616.
 -L"/opt/rocm-5.1.3/hip/lib" -O3 -lgcc_s -lgcc -lpthread -lm -lrt

=== Environment Variables
deleted

== Linux Kernel
Hostname     : deleted 
Linux  4.18.0-372.9.1.el8.x86_64 #1 SMP Fri Apr 15 22:12:19 EDT 2022 x86_64 x86_64 x86_64 GNU/Linux
```

Attempted hip compilation suggests an incomplete install or I missed a configuration step:
```
$ hipcc --offload-arch=gfx906 vectoradd.cpp 
clang-14: error: cannot find ROCm device library; provide its path via '--rocm-path' or '--rocm-device-lib-path', or pass '-nogpulib' to build without ROCm device library
```

This machine previously ran ROCm 4.5 without issues.

Suggestions welcome. I assume a missed environment or configuration setting. Will move this issue to https://github.com/ROCm-Developer-Tools/HIP if considered more appropriate.

