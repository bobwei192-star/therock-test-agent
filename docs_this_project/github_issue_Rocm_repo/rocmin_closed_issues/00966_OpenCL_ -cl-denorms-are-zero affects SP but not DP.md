# OpenCL: -cl-denorms-are-zero affects SP but not DP

- **Issue #:** 966
- **State:** closed
- **Created:** 2019-12-15T06:40:33Z
- **Updated:** 2019-12-15T20:31:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/966

With ROCm 2.10, specifying -cl-denorms-are-zero at the OpenCL compilation changes the float_mode of the generated kernel from 240 (0xF0) to 192 (0xC0), so it seems that -cl-denorms-are-zero only affects the denorms flag of single precision but not that of double precision. Is this the intended behavior?

To repro: compile any OpenCL kernel with/without -cl-denorms-are-zero, and dump the generated ISA, looking for float_mode in kernel header.