# OpenCL codegen: poor optimization of #VGPR used

- **Issue #:** 1002
- **State:** closed
- **Created:** 2020-01-18T18:18:59Z
- **Updated:** 2023-12-18T17:24:14Z
- **URL:** https://github.com/ROCm/ROCm/issues/1002

On ROCm 2.10, RadeonVII

In GpuOwl, the change referenced below speeds-up a big kernel by more than 33% by passing two arguments referencing the same memory buffer (thus the same data) instead of one in order to disable the ROCm optimizer from caching the data, once read, into VGPRs. This reduces the number of VGPRs used by the kernel from 156 to 125 and thus increases occupancy from 1 to 2.

| tailFusedMulDelta | Before | After |
| --- | --- | --- |
| NumVGPRsForWavesPerEU | 156 | 125 |
| Occupancy | 1 | 2 |

https://github.com/preda/gpuowl/commit/1e0ce1d8abf9f8b189373085a6cbdc2e2d814d33

This change is a work-around-the-optimizer, because it actively hides information from the compiler (in this case it hides the equivalence of the two buffer arguments).

The optimizer should be able to balance the desire to cache once-read data into VGPRs versus the VGPR pressure. In this particular case the register pressure is extreme (as it reduces occupancy to 1) yet the optimizer still uses a lot of VGPRs to "keep data around".
