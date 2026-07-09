# OpenCL does not detect second RX5500 gpu

- **Issue #:** 1416
- **State:** closed
- **Created:** 2021-03-22T17:41:10Z
- **Updated:** 2021-07-08T11:11:25Z
- **URL:** https://github.com/ROCm/ROCm/issues/1416

Hello, I have two rx5500xt and only the one from the motherboards main slot is properly detected in opencl.
I have rocm-smi and rocm-opencl-runtime installed and I am using arch linux with amdgpu. The problem also happens with opencl-amd.
rocm-smi detects both GPU properly, but I can only control the fans for a GPU that is in use (either connected to a monitor or mining for example).