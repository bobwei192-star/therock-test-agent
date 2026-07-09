# For an unknown Proprietary application - OpenCL - ROCm LLVM Compiler is spilling registers to  scratch registers where the PAL drivers did not with large performance hit.

- **Issue #:** 553
- **State:** closed
- **Created:** 2018-09-21T09:56:10Z
- **Updated:** 2018-09-21T13:14:59Z
- **URL:** https://github.com/ROCm/ROCm/issues/553

The PAL drivers used 114 VGPRs. 82 + 2 x 16 (two arrays of 16 floats).

The ROCm 1.9 driver uses scratch space instead and is ~60% slower.
                enable_sgpr_flat_scratch_init = 1
                workitem_vgpr_count = 82
 
