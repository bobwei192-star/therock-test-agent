# hip-samples provides *.hipref.* files without explaining them

- **Issue #:** 1138
- **State:** closed
- **Created:** 2020-06-06T19:19:50Z
- **Updated:** 2021-02-15T10:28:14Z
- **URL:** https://github.com/ROCm/ROCm/issues/1138

I believe `/opt/rocm-3.5.0/hip/samples/0_Intro/square/square.hipref.cpp` is not actually used for anything. And shipping it is confusing. Please remove it.

Even better, make the `0_Intro/square`, be separated into two projects. First one, not using CUDA, but native manually written HIP code and just uses `hipcc`, a second one, that uses CUDA and `hipify+hcc`, and `nvcc`.
