# OpenCL Crash Reproducer

- **Issue #:** 383
- **State:** closed
- **Created:** 2018-04-10T00:37:47Z
- **Updated:** 2018-04-17T20:04:32Z
- **URL:** https://github.com/ROCm/ROCm/issues/383

I get the following error when I run a relatively simple OpenCL kernel on the latest ROCM 1.7, with RX 470:

    Memory access fault by GPU node-1 on address 0x901b09000. Reason: Page not present or supervisor privilege.

I am quite sure that there are no out-of-bounds memory accesses.
I've attached a complete reproducer to this issue: see if you can prove me wrong !

[opencl_crash.tar.gz](https://github.com/RadeonOpenCompute/ROCm/files/1892395/opencl_crash.tar.gz)


