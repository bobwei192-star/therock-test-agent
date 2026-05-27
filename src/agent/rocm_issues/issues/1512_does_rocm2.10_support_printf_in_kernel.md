# does rocm2.10 support printf in kernel?

> **Issue #1512**
> **状态**: closed
> **创建时间**: 2021-07-07T06:45:33Z
> **更新时间**: 2021-07-07T06:58:59Z
> **关闭时间**: 2021-07-07T06:58:59Z
> **作者**: protoss1235
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1512

## 描述

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


---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2021-07-07T06:56:46Z)

Hi @hongbilu 
Thanks for reaching out.
I will take a look and do the needful for you.

---

### 评论 #2 — ROCmSupport (2021-07-07T06:57:42Z)

Hi @hongbilu 
ROCm 2.10 is very old, which is released around 2 years back. It did not support printf that time.
Recommend to try with the latest ROCm 4.2GA which has printf support.
Hope this helps.
Thank you.

---
