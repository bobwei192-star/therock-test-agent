# How to figure out the CPUStr e.g. "gfx1010" at runtime with HIP functions?

- **Issue #:** 1362
- **State:** closed
- **Created:** 2021-01-20T05:15:03Z
- **Updated:** 2021-01-20T15:59:56Z
- **Labels:** Question
- **URL:** https://github.com/ROCm/ROCm/issues/1362

My application uses LLVM's AMDGPU backend to generate GPU kernels at runtime. In order to instantiate the correct TargetMachine I'd need to have the "CPUString" like "gfx908", "gfx1010", etc.

The HIP functions hipDeviceComputeCapability and hipDeviceGetName get me close but not really there without some educated guessing. Compute capability is returned as major=10, minor=1. How do I arrive from that to the correct CPU string "gfx1010"? It can't be "gfx${major}${minor}0" since that wouldn't work for "gfx908". This needs to work for any card.

If this is currently not possible can I suggest adding those features?
