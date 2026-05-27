# Atomic operation producing incorrect results

> **Issue #1645**
> **状态**: closed
> **创建时间**: 2021-12-18T19:16:11Z
> **更新时间**: 2022-06-14T15:28:16Z
> **关闭时间**: 2022-06-14T15:28:16Z
> **作者**: JieyangChen7
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1645

## 描述

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

---

## 评论 (13 条)

### 评论 #1 — ex-rzr (2021-12-20T05:12:55Z)

I wonder what you'll get if you replace `*data = 10000000;` with `atomicExch(data, 10000000)` and `printf("Atoimc Min: %d\n", *data);` with `printf("Atoimc Min: %d\n", atomicExch(data, 10000000));`

---

### 评论 #2 — ROCmSupport (2021-12-20T11:30:45Z)

Thanks @JieyangChen7 for reaching out.
I will reach HIP team to take a look. Thank you.

---

### 评论 #3 — seesturm (2021-12-20T12:15:11Z)

[Programming guide](https://rocmdocs.amd.com/en/latest/Programming_Guides/Kernel_language.html#cooperative-groups-functions) states:

> HIP does not support any of the kernel language cooperative groups types or functions.

Is this still true?

---

### 评论 #4 — JieyangChen7 (2021-12-20T14:13:11Z)

@ex-rzr I still get the same results after replacing those statements with ```atomicExch```.

---

### 评论 #5 — JieyangChen7 (2021-12-20T14:20:01Z)

@seesturm It seems that Cooperative Groups are being supported according to the latest [HIP Programming Guide](https://github.com/RadeonOpenCompute/ROCm/blob/master/AMD_HIP_Programming_Guide.pdf).

---

### 评论 #6 — ex-rzr (2021-12-20T15:10:52Z)

I'm just guessing so don't take my ideas too seriously but I would check how it works with
```cpp
__global__ __launch_bounds__(256) void test_atomic_min(int* data)
...
  int thr_per_blk = 256;
  int blk_in_grid = 16;
```

Is the incorrect value always 3200?


---

### 评论 #7 — zjin-lcf (2021-12-20T15:41:13Z)

Thanks for the example. With 256 threads and 16 blocks, the results are correct on a vega20 GPU.

  int thr_per_blk = 256;
  int blk_in_grid = 16;
 

---

### 评论 #8 — JieyangChen7 (2021-12-20T16:13:00Z)

@ex-rzr Thanks for the suggestion. I tried the multiple block sizes (128, 256, 512, and 1024), it seems that this issue only occurs when the block size is 1024.
No, it is not always 3200. It can be any number in between MIN_RANGE and MAX_RANGE. It can also be just the initial value.

---

### 评论 #9 — Rmalavally (2021-12-20T21:29:20Z)

Please refer to the latest version of the HIP Programming Guide for more information. I have attached the PDF for your reference. You can access the latest ROCm v4.5 documentation at the following link:

https://rocmdocs.amd.com/en/latest/Programming_Guides/Programming-Guides.html

AMD ROCm Documentation Team

[AMD_HIP_Programming_Guide.pdf](https://github.com/RadeonOpenCompute/ROCm/files/7748024/AMD_HIP_Programming_Guide.pdf)


---

### 评论 #10 — ROCmSupport (2022-01-25T13:12:22Z)

Hi @JieyangChen7 , can we close this issue now considering the above comments/suggestions.
Please share your thoughts. Thank you.

---

### 评论 #11 — jlgreathouse (2022-02-09T22:14:04Z)

> Hi @JieyangChen7 , can we close this issue now considering the above comments/suggestions. Please share your thoughts. Thank you.

No, please do not close this issue. There is a real ROCm bug here, and we are tracking it internally. We plan to fix it in a future ROCm version.

---

### 评论 #12 — ROCmSupport (2022-02-10T08:15:36Z)

Sure @jlgreathouse , thanks for the help and support.

---

### 评论 #13 — jlgreathouse (2022-03-16T22:14:46Z)

Hi @JieyangChen7 This should be fixed as of ROCm 5.0.2.

---
