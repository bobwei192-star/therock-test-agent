# Beginner: error: use of undeclared identifier 'threadIdx' etc

> **Issue #1922**
> **状态**: closed
> **创建时间**: 2023-03-10T07:27:04Z
> **更新时间**: 2024-02-25T15:10:58Z
> **关闭时间**: 2024-02-25T15:10:58Z
> **作者**: fftfp64
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1922

## 描述

Hi,
Trying to convert opencl to hip. GPU Radeon VII.  ROCm rocm-5.4.3. 
But i get:

/opt/rocm/hip/bin/hipcc  -c  -D__HIP_PLATFORM_AMD__     t.c
t.c:14:10: error: use of undeclared identifier 'threadIdx'
 int i = threadIdx.x + blockIdx.x*blockDim.x;
         ^
t.c:14:24: error: use of undeclared identifier 'blockIdx'
 int i = threadIdx.x + blockIdx.x*blockDim.x;
                       ^
t.c:14:35: error: use of undeclared identifier 'blockDim'
 int i = threadIdx.x + blockIdx.x*blockDim.x;
                                  ^
3 errors generated-D__HIP_PLATFORM_HCC__  -D__HIP_PLATFORM_AMD__  -I/opt/rocm-5.4.3/include



Simple code:

#include <stdlib.h>
#include <stdio.h>
#include <time.h>
#include <sys/time.h>
#include <hip/hip_runtime.h>

__global__ void aa( double *U )
{
 int i = threadIdx.x + blockIdx.x*blockDim.x;
  printf("\n %d  \n", i );
}

int main(void)
{
int count, device;
hipGetDeviceCount(&count);
hipGetDevice(&device);
printf("TRIVIAL TEST %d %d \n", device, count);
return 0;
}


What is missing?
Thank you.






---

## 评论 (5 条)

### 评论 #1 — briansp2020 (2023-03-11T02:50:10Z)

I wrote a post on how to covert CUDA program to HIP one very long time ago. I'm not sure if the step by step instruction is still valid. But it should give you some idea as to how to get stuff going with hip if you are coming from a different environment. Check out https://briansp2020.github.io/

For this specific problem, hip uses hipBlockDim_x, hipBlockIdx_x, hipThreadIdx_x instead of threadIdx.x, blockIdx.x, blockDim.x. The official documentation also has a porting guide https://sep5.readthedocs.io/en/latest/Programming_Guides/HIP-porting-guide.html which shows the difference between hip and CUDA. threadIdx is CUDA variable.

Hope this helps.

---

### 评论 #2 — fftfp64 (2023-03-12T06:25:09Z)

Thanks Brian.

I have found a way round it all. Renamed file t.c to t.cpp. With this, the hipcc uses the llvm/clang which have the correct header files. But it throws up a cmath header not found error. This got fixed with

sudo apt install libstdc++-12-dev

Everything works now.


---

### 评论 #3 — cloudhan (2023-09-14T15:25:21Z)

`#include "hip/hip_runtime.h"` will fix this problem.

@briansp2020 Please don't recommend those macro, they unofficially confess that is a big bad mistake. https://github.com/ROCm-Developer-Tools/HIP-CPU/issues/8#issuecomment-756188453

---

### 评论 #4 — nartmada (2024-02-22T02:58:39Z)

Hi @fftfp64, just checking to see if your issue has been resolved?  If resolved, please close the ticket.  Thanks.

---

### 评论 #5 — nartmada (2024-02-25T15:10:58Z)

Closing the ticket as "Everything works now" for @fftfp64.  Thanks @briansp2020 and @cloudhan for your inputs. 

---
