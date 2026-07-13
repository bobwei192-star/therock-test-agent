# On RX Vega, OpenCL with the new Rocm compiler on Linux, memory/cache problem?

- **Issue #:** 182
- **State:** closed
- **Created:** 2017-08-21T01:17:49Z
- **Updated:** 2018-06-03T15:17:21Z
- **Labels:** Bug_Functional_Issue
- **URL:** https://github.com/ROCm/ROCm/issues/182

I use AMDGPU-Pro 17.30 on Linux. On RX Vega 64 GPU. I see that the OpenCL compiler changed for this combination to the new Rocm compiler.

I see a regression in my application gpuOwL https://github.com/preda/gpuowl
The application has two modes (two equivalent sets of OpenCL kernels), the "slow" mode enabled with "-legacy" flag, and the "fast" mode used by default. This "fast" mode breaks with the new compiler.

The concerned kernel that breaks is the "amalgamation" kernel, which uses a trick "staircase workgroups" which involves memory communication between workgroups (workgroup K reading data that was written by workgroup K-1) of the same kernel launch.

I tried to debug this as a bug in my application, but I can't find a cause there yet. It seems related to memory/cache behavior and is timing sensitive. It clearly only triggers with the new Rocm compiler. Unfortunately I don't have a "stripped down" small repro case yet. I did try using both OpenCL 1.2 atomics, and OpenCL 2.0 atomics, but this didn't fix the behavior.

This seemed sufficiently alarming to me to point this to you early.