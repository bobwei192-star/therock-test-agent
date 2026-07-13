# hipLaunchCooperativeKernel slowdown

- **Issue #:** 3410
- **State:** closed
- **Created:** 2024-07-10T12:39:51Z
- **Updated:** 2025-04-17T13:01:57Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon VII
- **URL:** https://github.com/ROCm/ROCm/issues/3410

### Problem Description

I wanted to try using Cooperative groups as appears as if it would be helpful in some future work. I began by trying to launch a kernel using hipLaunchCooperativeKernel. Note that this kernel did not use any cooperative features I was just trying to get the framework in place to start implementing them. The kernel ran correctly but was an order of magnitude slower than when launched in the normal way. I tried running it with only 1 thread block and observed the same behavior. My question is if this is the expected behavior for the current implementation. If so I'll just shelve the idea for now.

### Operating System

22.04.4 LTS (Jammy Jellyfish)

### CPU

AMD EPYC 7443P 24-Core Processor

### GPU

AMD Radeon VII

### ROCm Version

ROCm 6.0.0

### ROCm Component

HIP

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_