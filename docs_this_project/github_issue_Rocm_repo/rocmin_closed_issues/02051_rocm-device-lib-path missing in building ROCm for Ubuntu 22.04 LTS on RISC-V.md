# rocm-device-lib-path missing in building ROCm for Ubuntu 22.04 LTS on RISC-V 

- **Issue #:** 2051
- **State:** closed
- **Created:** 2023-04-15T02:36:26Z
- **Updated:** 2024-02-16T16:45:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/2051

I've been working on building ROCm (target Radeon VII + HiFive Unmatched), with Ubuntu 22.04 LTS. I've successfully built rocm-llvm, rocm-cmake, roct-thunk-interface, rocm-device-libs, rocminfo, rocr-runtime, rocm-compilersupport and hip for RISC-V so far. 

However, when I start to build rocBLAS, rocFFT etc. I found that the hipcc fail to find the rocm-device-lib-path, where in this case, locate in /usr/lib/riscv64-linux-gnu/amdgcn/bitcode, And this stuck my building procedure. I have no idea where I can pass the --rocm-device-lib-path to hipcc in the compiling procedure. 

btw: Is AMD interested in RISC-V & ARM support for ROCm?