# Q: how to build ROCm OpenCL for kernel 4.18

- **Issue #:** 513
- **State:** closed
- **Created:** 2018-08-24T11:41:19Z
- **Updated:** 2018-12-24T21:39:28Z
- **Labels:** Feature Request
- **URL:** https://github.com/ROCm/ROCm/issues/513

I would like to try OpenCL on kernel 4.18 on Ubuntu 18.04. I have this plan:

1. checkout master branch of rock-dkms, compile and install.
2. install these pre-built packages:
Setting up hsa-ext-rocr-dev (1.1.8-15-ge851b7a) ...
Setting up hsakmt-roct (1.0.8-1-ge3dd067) ...
Setting up hsakmt-roct-dev (1.0.8-1-ge3dd067) ...
Setting up hsa-rocr-dev (1.1.8-15-ge851b7a) ...
Setting up rocm-opencl (1.2.0-2018071109) ...

Would it work? what do I need to do differently?
thanks