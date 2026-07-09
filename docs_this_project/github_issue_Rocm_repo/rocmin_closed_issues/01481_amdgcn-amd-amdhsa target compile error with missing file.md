# amdgcn-amd-amdhsa target compile error with missing file.

- **Issue #:** 1481
- **State:** closed
- **Created:** 2021-05-26T02:06:10Z
- **Updated:** 2021-07-01T06:31:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/1481

I have very simple opencl kernel and wanted to compile it using amdgpu as target:
https://llvm.org/docs/AMDGPUUsage.html#target-triples

system:
Ubuntu180405
rocm 4.1 installed including llvm. 


file: p25k.c

#include <CL/cl.h>
#include <stdio.h>

kernel void kernelfcn(      global uint *dev_c,   global uint * dev_a,  global uint * dev_b)
{
  uint tid = get__id(0);
 *dev_c = 100;
 *dev_a = 200;
}
But it errors out with that:

clang --target=amdgcn-amd-amdhsa -c p25k.c -o p25k.o
In file included from p25k.c:1:
In file included from /usr/local/include/CL/cl.h:33:
In file included from /usr/local/include/CL/cl_platform.h:224:
In file included from /opt/rocm-4.1.0/llvm/lib/clang/12.0.0/include/stdint.h:52:
/usr/include/stdint.h:26:10: fatal error: 'bits/libc-header-start.h' file not found
#include <bits/libc-header-start.h>
         ^~~~~~~~~~~~~~~~~~~~~~~~~~