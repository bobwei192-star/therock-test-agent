# SYCL program fails to link with ROCm 3.3.0 + Ubuntu 20.04

- **Issue #:** 1108
- **State:** closed
- **Created:** 2020-05-10T13:10:28Z
- **Updated:** 2021-06-03T09:36:10Z
- **URL:** https://github.com/ROCm/ROCm/issues/1108

First of all, I understand that my setup is wholly unsupported by the ROCm stack (Ubuntu 20.04 + ROCm 3.3.0 including dkms + Intel's DPC++ LLVM compiler). I'm trying to run a sycl-based program using one of Intel's daily DPC++ releases (from https://github.com/intel/llvm/releases), and I can successfully run this application on both the host target (without OpenCL) and on the CPU (with OpenCL) using Intel's compute runtime. However, when it comes to executing it on a Vega 56, the program ends up failing to execute with

```
OpenCL API failed. OpenCL API returns: -17 (CL_LINK_PROGRAM_FAILURE) -17 (CL_LINK_PROGRAM_FAILURE)
```

How can I go about debugging this on the ROCm side of things? Is there a `DEBUG_ENABLE` sort of environment variable?

(the chosen device is a gfx900, so I'm pretty sure it's choosing the Vega as a target)