# Wrong int64 multiplication test case

- **Issue #:** 1383
- **State:** closed
- **Created:** 2021-02-16T13:23:06Z
- **Updated:** 2024-01-12T13:13:10Z
- **URL:** https://github.com/ROCm/ROCm/issues/1383

AMD OpenCL compiler used for RX 5700 XT with ROCM 4.0.1 sometimes generates invalid code for integer multiplication.

The self-contained example is here: https://github.com/develancer/amd-opencl-test-case

Disabling all compiler optimizations does not help.