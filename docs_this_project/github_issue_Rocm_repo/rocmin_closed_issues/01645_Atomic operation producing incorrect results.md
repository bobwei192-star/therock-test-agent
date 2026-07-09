# Atomic operation producing incorrect results

- **Issue #:** 1645
- **State:** closed
- **Created:** 2021-12-18T19:16:11Z
- **Updated:** 2022-06-14T15:28:16Z
- **URL:** https://github.com/ROCm/ROCm/issues/1645

When I use atomic operations with Cooperative Groups, the atomic operations can sometimes produce incorrect results. For example, given the following example code:

```
#include <hip/hip_runtime.h>
#include <hip/hip_cooperative_groups.h>
#include <iostream>
namespace cg = cooperative_groups;

#define MIN_RANGE 3187
#define MAX_RANGE 3896

__global__ void test_atomic_min(int* data)
{
  int i = blockDim.x * blockIdx.x + threadIdx.x;
  cg::this_grid().sync();
  if (i == 0) {
    *data = 10000000;
  }
  cg::this_grid().sync();
  if(i < MAX_RANGE && i >= MIN_RANGE)
  { 
    atomicMin(data, i);
  }
  cg::this_grid().sync();
  if (i == 0) {
    printf("Atoimc Min: %d\n", *data);
  }
}

int main()
{
  int thr_per_blk = 1024;
  int blk_in_grid = 4;
  std::cout << "True Min: " << MIN_RANGE << std::endl;
  int* data;
  hipMalloc(&data, sizeof(int));
  void * Args[] = { &data };
  hipLaunchCooperativeKernel((void*)test_atomic_min, dim3(blk_in_grid), dim3(thr_per_blk ), Args, 0, 0);
  hipDeviceSynchronize();
  hipFree(data);
  return 0;
}
```
If I run the above code multiple times, I can get the following results:

```
$ ./a.out 
True Min: 3187
Atoimc Min: 3187
$ ./a.out 
True Min: 3187
Atoimc Min: 3187
$ ./a.out 
True Min: 3187
Atoimc Min: 3200
$ ./a.out 
True Min: 3187
Atoimc Min: 3200
$ ./a.out 
True Min: 3187
Atoimc Min: 3187
```
The code is compiled with command ```hipcc --amdgpu-target=gfx908 -std=c++17 test.cpp```. The ROCm version is 4.3.0. The testing GPU is MI100. 

I get similar issues for both ```atomicMin``` and ```atomicMax``` for both device and system scoped versions. I have not verified other atomic operations.  Also, I can reproduce this issue on both ROCm 4.3.0 and 4.2.0. I run the test 1000 times and the correctness rate is only about 9.6% for ROCm 4.3.0 and 16.6% for ROCm 4.2.0. I cannot verify it on newer ROCm releases since those are not available on my testing system (Spock@OLCF). 

The only way to guarantee correct results is to void using Cooperative Group and break the kernel into several smaller kernels with device synchronizations in between. But it brings high kernel launch overhead, which we are specifially trying to avoid in our code.

This issue was discovered when developing the [Huffman encoding algorithm](https://github.com/JieyangChen7/MGARD/blob/mgard-x/include/mgard-x/Lossless/ParallelHuffman/GenerateCW.hpp#L84) for the MGARD lossy compressor. The compressor software is designed to have multiple backends for supporting different devices. The same code runs correctly in CUDA for Nvidia GPUs and serial for x86 CPUs, but it gets incorrect results when using HIP on AMD GPUs.