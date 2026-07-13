# AMDGPU-pro 17.30 OpenCL: spurious warning about "-I ."

- **Issue #:** 209
- **State:** closed
- **Created:** 2017-09-14T12:34:43Z
- **Updated:** 2017-10-23T14:36:35Z
- **URL:** https://github.com/ROCm/ROCm/issues/209

On Ubuntu 17.04, AMDGPU-pro 17.30 (--compute), RX Vega 64, OpenCL.
If the kernel includes a file from the current directory, like:
#include "foo.h"

Passing "-I." as argument to clBuildProgram() generates the warning:
warning: argument unused during compilation: '-I .'

But not passing that argument produces:
#include "foo.h"
         ^~~~~~~~~~~
1 error generated.
OpenCL compilation log (error -11):
Error: Failed to compile opencl source (from CL to LLVM IR).

I guess the warning shouldn't be generated if the "-I ." is actually needed, or otherwise consider the current directory by default for #include "".
