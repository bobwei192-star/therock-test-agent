# does rocm2.10 support printf in kernel?

- **Issue #:** 1512
- **State:** closed
- **Created:** 2021-07-07T06:45:33Z
- **Updated:** 2021-07-07T06:58:59Z
- **URL:** https://github.com/ROCm/ROCm/issues/1512

i tried a demo code like this:
`
#include "hip/hip_runtime.h"
#define HIP_ENABLE_PRINTF
 __global__ void run_printf()
{
   printf("hello world\r\n");
}

int main(int argc, char ** argv) {
   hipLaunchKernelGGL(HIP_KERNEL_NAME(run_printf), dim3(1), dim3(1), 0, 0);
   hipDeviceSynchronize();
   return 0;
}
`
and compile 
/opt/rocm/bin/hipcc $(/opt/rocm/bin/hipconfig --cpp_config) -L/opt/rocm/lib/ check_large_bar.c -o check_large_bar
and run check_large_bar, it prints nothing, does anybody know how to printf trace in kernel? thanks
