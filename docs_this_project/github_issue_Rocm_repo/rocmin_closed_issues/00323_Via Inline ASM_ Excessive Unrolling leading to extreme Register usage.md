# Via Inline ASM, Excessive Unrolling leading to extreme Register usage 

- **Issue #:** 323
- **State:** closed
- **Created:** 2018-02-02T13:14:42Z
- **Updated:** 2018-10-11T23:39:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/323

I have been running into what I can best describe as register leakage (perhaps incorrect liveness tracking is a better way to describe it?) when using inline assembly in large kernels.  

The symptoms of this bug are greatly increased vgpr usage, that often overflows to the private segment, and non-functioning builds.  I have spent a fair amount of time attempting to create a simple example that produces the problem but have had no success.  I have found a reproducible example by applying a small patch to an existing public code base in this git repo https://github.com/signatumd/sgminer.

The patch: [reg_leak.txt](https://github.com/RadeonOpenCompute/ROCm/files/1689450/reg_leak.txt)

Steps to reproduce:
1. Clone above repo.
2. Compile kernel/skunk.cl targeting Vega
3. Inspect the search2 kernel and note the vgpr and private segment usage.
4. Apply attached patch by running "patch -p1 < reg_leak.txt" in root of git tree
5. Compile kernel/skunk.cl targeting Vega (this includes the modified fugue.cl file)
6. Inspect the search2 kernel and compare vgpr and private segment usage to previous build.

Without the patch, the search2 kernel uses 103 vgpr and no private segment.  With the patch, the search2 kernel uses 256 vgpr and 386 bytes of private segment.  As can easily be seen, the changes in the patch should have no effect on register allocation.  It should also be noted that, in this case, this change also causes the compiler to emit incorrect assembly that does not functionally match the source code.  In other situations I have seen the compiler generate excessive vgpr usage but the resulting build still functions correctly.

I am using rocm 1.7 and running on a Vega card.

Let me know if there's anything more I can do to help with this bug.