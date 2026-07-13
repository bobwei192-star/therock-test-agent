# Compute Support for RDNA2 - 6900XT / GFX1030 

- **Issue #:** 1390
- **State:** closed
- **Created:** 2021-02-21T22:30:33Z
- **Updated:** 2021-02-23T01:48:36Z
- **URL:** https://github.com/ROCm/ROCm/issues/1390

I have been able to cobble together a small kernel that can run intermittently on the 6900XT / GFX1030. I wanted to capture the issues filed / pull requests in one place so anyone interested can try it with just the public sources.  The biggest showstopper seems to be HIP doesn't work while HSA works (https://github.com/ROCm-Developer-Tools/HIP/issues/2238). 

This was all tested on a 5950x + 6900XT with Linux kernel 5.11rc7 

- [ ] - [HIP] HIP doesn't work with rocr while rocr seems to work with bandwith tests: https://github.com/ROCm-Developer-Tools/HIP/issues/2238 
- [ ] - [AOMP13] (likely defaults to COV4 but you have to force COV3): https://github.com/ROCm-Developer-Tools/aomp/issues/187
- [ ] - [AOMP13] requires this PR to avoid linking clang_rt.builtins on the host: https://github.com/ROCm-Developer-Tools/HIP/pull/2219
- [ ] - [Tensile] Requires a fix for https://github.com/ROCmSoftwarePlatform/Tensile/issues/1282 which is a revert of https://github.com/ROCmSoftwarePlatform/Tensile/commit/5791b7fc28c6c1264fc7941e14d6a4cbbedb8883
- [x] - [Tensile] I fixed this https://github.com/ROCmSoftwarePlatform/Tensile/pull/1283 so you don't rely on dpkg if you use custom AOMP
- [ ] - [Tensile] Here is an updated branch where you can run Tensile on GFX1030 to generate kernels but it will fail when you run them due to the HIP showstopper above https://github.com/powderluv/Tensile/tree/gfx10-rebase-fixes
- [x] - [GCN Example] I pushed up an updated example to use GCN on GFX10: https://github.com/Powderluv/LLVM-AMDGPU-Assembler-Extra 
- [x] - [ROCR-Runtime] Running the GCN example above fails intermittently: https://github.com/RadeonOpenCompute/ROCR-Runtime/issues/114
- [ ] - [HSA-Conformance] I updated the HSA-Conformance to build with latest version of check https://github.com/powderluv/HSA-Runtime-Conformance  but it fails a lot of tests
- [ ] - [Roc thunk interface / KFD] KFD Memory tests fail: https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/108 
- [ ] - [RocBLAS] Requesting for rocblas support (closed)
- [ ] - [ROCM] Request for official support (closed)


I hope the issues  / PRs above are useful for anyone determined to get compute working on the latest generation AMD GPUs. 
Hopefully soon we will see official support and all the above issues addressed. 
