# Beginner: error: use of undeclared identifier 'threadIdx' etc

- **Issue #:** 1922
- **State:** closed
- **Created:** 2023-03-10T07:27:04Z
- **Updated:** 2024-02-25T15:10:58Z
- **URL:** https://github.com/ROCm/ROCm/issues/1922

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




