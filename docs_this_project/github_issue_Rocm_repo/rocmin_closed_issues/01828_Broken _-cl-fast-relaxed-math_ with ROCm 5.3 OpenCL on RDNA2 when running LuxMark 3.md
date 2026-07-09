# Broken `-cl-fast-relaxed-math` with ROCm 5.3 OpenCL on RDNA2 when running LuxMark 3

- **Issue #:** 1828
- **State:** closed
- **Created:** 2022-10-09T16:42:41Z
- **Updated:** 2022-10-17T00:28:23Z
- **URL:** https://github.com/ROCm/ROCm/issues/1828

Hi, I faced a bug on ROCm that I know well because it also affects Mesa Clover as the regression happened on LLVM side.

I reproduced the bug with ROCm on the Steam Deck's APU (“Custom 0405”, VanGhogh, RDNA 2.0). I know this one is not officially supported but despite owning about a dozen of AMD GPUs from GCN1 to RDNA2 this is the only graphic chip that currently works with ROCm on my end. I expect the bug to affect more hardware as the bug is known to exist in LLVM and is even reproduced on other drivers using LLVM like Mesa Clover with other hardware like Hawaii/Grenada GCN2 R9 390X.

So to get ROCm behaving as expected the root cause of the regression has to be found in LLVM and fixed.

Here is the render that is gotten with LuxMark default options (`-cl-fast-relaxed-math` is enabled)

[![luxmark on rocm with broken math](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221008-063923-000.rocm-luxmark-rdna2-cl-fast-relaxed-math.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221008-063923-000.rocm-luxmark-rdna2-cl-fast-relaxed-math.png)

Here is the expected render (I have to disable `-cl-fast-relaxed-math`, which is not the LuxMark default option):

[![luxmark on rocm](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221008-064150-000.rocm-luxmark-rdna2-no-fast-relaaxed-math.png)](https://dl.illwieckz.net/b/rocm/bugs/luxmark-cl-fast-relaxed-math-garbage/20221008-064150-000.rocm-luxmark-rdna2-no-fast-relaaxed-math.png)

The bug is not reproduced with Orca, PAL, fglrx, rusticl (for AMD radeonsi GPU), SRB and Beignet for Intel GPU, Nvidia OpenCL for Nvidia GPU, neither CPU implementations like old AMD CPU OpenCL driver (the one shipped in fglrx or early Orca versions), the Intel CPU one shipped with SRB, PoCL or Mesa rusticl with llvmpipe. That's why, while there is still a minor chance there is something wrong in LuxMark, it is very unlikely. The [luxmark.info](http://luxmark.info/) website validated more then 8000 runs on more than 700 hardware/driver combinations.

How to reproduce the bug.

- Get LuxMark 3: http://www.wiki.luxcorerender.org/LuxMark_v3
- Install ROCm 3.5 on a computer with a supported device;
- Run the Luxball benchmark (the default one) with the default compiler options;
  If you only have one OpenCL platform (ROCm) and only one GPU device, the benchmark would immediately start in a way it will reproduce the bug.

Because I already investigated the bug for Clover, I verified it behaves the exact same way with ROCm and Clover.

- If you enable `-cl-fast-relaxed-math`, the bug is reproduced.
- If you disable `-cl-fast-relaxed-math`, the bug disappears.

But `-cl-fast-relaxed-math` implies both `-cl-finite-math-only` and `-cl-unsafe-math-optimizations`, so I driven more tests. Those individual options are not offered by default LuxMark menu but I have patches on my end to make them easy to tweak.

So:

- `-cl-finite-math-only` enabled: no bug
- `-cl-unsafe-math-optimizations` enabled: no bug
- `-cl-finite-math-only` and `-cl-unsafe-math-optimizations`: bug

The bug comes when both `-cl-finite-math-only` and `-cl-unsafe-math-optimizations` are enabled at the same time, which is implied by enabling `-cl-fast-relaxed-math`.

Which is the exact same behavior I reproduced with Mesa Clover on both GCN2 Hawaii R9 390X and GCN1 Oland R7 240.

Here is the LLVM thread about it, with extensive research:

- https://github.com/llvm/llvm-project/issues/54947

The regression is known to have been introduced in LLVM between LLVM 9 and LLVM 11.

This is considered a regression on ROCm point of view as it is known in 2018 on APP 2679.0 ROCm produced the correct result on an Hawaii/Grenada GCN2 R9 390X.

Here is a table where we can see platforms and versions that reproduce the bug, they're all LLVM-based implementations:

- https://github.com/llvm/llvm-project/issues/54947#issuecomment-1136254537

It is worth noticing PoCL also reproduced the bug starting with LLVM 11 but stopped reproducing it with LLVM 12, while I reproduce the bug with Clover on both LLVM 11, 13 and 15. So maybe getting in touch with PoCL people may help to identify the root cause of the bug if they know how to workaround it.

I'm installing ROCm OpenCL by installing the `rocm-opencl` package, which also installs `amdgpu-core comgr hsa-rocr libdrm-amdgpu-amdgpu1 libdrm-amdgpu-common libdrm2-amdgpu rocm-core rocm-ocl-icd` as dependencies. I don't see any library in `/opt/rocm-5.3.0` that dynamically links to llvm or clang so I assume it is statically linked? You'll probably know what version of LLVM you use anyway.