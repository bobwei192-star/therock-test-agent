# Long memory copy duration

> **Issue #1041**
> **状态**: closed
> **创建时间**: 2020-03-14T00:41:56Z
> **更新时间**: 2020-06-28T09:43:52Z
> **关闭时间**: 2020-06-28T09:43:52Z
> **作者**: onur-v
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1041

## 描述

Hi,

I have a piece of code that had been working properly until ROCm 3.1 arrived. Currently the function hipMemCpy takes unnecessary long times to complete for arbitrary sizes of arrays that is, it takes approximately 2 seconds to complete for exactly 15000000000 bytes compared to almost 30 seconds for 2974320000 bytes, which is around 5 times smaller. It seems like the long duration happens on arbitrary sizes. 

In another project I'm using ROCALUTION and since 3.1 I have been experiencing a similar problem (returns error after it fails to compute the norm of residual in sufficient time), which i suspect is related to the same issue. 

The software and hardware:
* CPU - 3900x
* Graphics card - Radeon VII
* OS - Ubuntu 18.04 on kernel 5.3.0-40
* ROCm - 3.1 (3.1.1 also displays the same issue)
* Compiler - hipcc with -O2 -std=c++11 -march=znver2 flags

Just to make sure, I have once reverted to 3.0 and observed no issues. Minimal working example I could come up with is this:

```c++
#include <iostream>
#include <chrono>
#include "hip/hip_runtime.h"

int main(){

    unsigned int arr_lngth = 371790000;
    unsigned long long arr_sz = arr_lngth*sizeof(double);
    double *array = new double [arr_lngth];

    double *array_device;

    //auto begin = std::chrono::high_resolution_clock::now();

    hipMalloc(&array_device, arr_sz);
    hipDeviceSynchronize();

    //auto diff = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::high_resolution_clock::now() - begin).count();
    //std::cout << "malloc time " << diff << " milliseconds\n";  

    //begin = std::chrono::high_resolution_clock::now();

    hipMemcpy(array_device, array, arr_sz, hipMemcpyHostToDevice);
    hipDeviceSynchronize();
    
    //diff = std::chrono::duration_cast<std::chrono::milliseconds>(std::chrono::high_resolution_clock::now() - begin).count();
    //std::cout << "copy time " << diff << " milliseconds\n";  

    hipFree(array_device);
    delete[] array; 

    return 0;
}
```

---

## 评论 (1 条)

### 评论 #1 — onur-v (2020-04-03T14:42:36Z)

The problem persists with ROCm version 3.3. Latest working version for me is 2.10.

---
