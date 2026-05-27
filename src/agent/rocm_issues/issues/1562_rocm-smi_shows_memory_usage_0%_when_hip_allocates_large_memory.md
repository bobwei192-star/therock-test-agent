# rocm-smi shows memory usage 0% when hip allocates large memory

> **Issue #1562**
> **状态**: closed
> **创建时间**: 2021-08-21T04:02:21Z
> **更新时间**: 2024-01-10T17:09:13Z
> **关闭时间**: 2024-01-10T17:09:12Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1562

## 描述

There are some benchmark for which the rocm-smi reports the >0% percentage memory usage appropriately when run, however when I allocate simple but large vector data space on GPU and copy, the rocm-smi reports nothing:...
Following simple example creates on host the 512M data and copies to GPU and after some kernel compute, it copies back. But before hipFree, I inserted getChar() and run rocm-smi but it will reports 9% usage. 
```

#include <stdio.h>
#include "hip/hip_runtime.h"

// 1. if N is set to up to 1024, then sum is OK.
// 2. Set N past the 1024 which is past No. of threads per blocks, and then all iterations of sum results in
// even the ones within the block.

// 3. To circumvent the problem described in 2. above, since if N goes past No. of threads per block, we need multiple block$
// The trick is describe in p65 to use formula (N+127) / 128 for blocknumbers so that when block number starts from 1, it is
// (1+127) / 128.

#define N 536870912 // alloc 512M data.
#define MAX_THREAD_PER_BLOCK 1024

__global__ void add( int * a, int * b, int * c ) {
    int tid = hipThreadIdx_x + hipBlockIdx_x * hipBlockDim_x ;
    if (tid < N)
        c[tid] = a[tid] + b[tid];
}

int main (void) {
    int *a, *b, *c;
    int *dev_a, *dev_b, *dev_c;
    int stepSize;

    int count = 0;

    hipGetDeviceCount(&count);

    printf("\nDevice count: %d.", count);
    // allocate dev memory for N size for pointers declared earlier.

    printf("\nAllocating memory...(size %u array size of INT).\n", N );

    a = (int*)malloc(N * sizeof(int));
    b = (int*)malloc(N * sizeof(int));
    c = (int*)malloc(N * sizeof(int));

    for (int i = 0; i < N; i++) {
        a[i] = i;
        b[i] = i+2;
        c[i] = 999;
    }

    for (int i = 0 ; i < count; i++) {
        hipSetDevice(i);
        hipMalloc( (void**)&dev_a, N * sizeof(int));
        hipMalloc( (void**)&dev_b, N * sizeof(int));
        hipMalloc( (void**)&dev_c, N * sizeof(int));

        // copy the initialized local memory values to device memory.

        printf("\nCopy host to device... %d.", i);
        hipMemcpy(dev_a, a, N * sizeof(int), hipMemcpyHostToDevice);
        hipMemcpy(dev_b, b, N * sizeof(int), hipMemcpyHostToDevice);
        hipMemcpy(dev_c, c, N * sizeof(int), hipMemcpyHostToDevice);

        const unsigned blocks = 512;
        const unsigned threadsPerBlock = 256;

        // invoke the kernel:
        // block count: (N+127)/128
        // thread count: 128

        hipLaunchKernelGGL(add, blocks, threadsPerBlock, 0, 0, dev_a, dev_b, dev_c);
        hipMemcpy(a, dev_a, N * sizeof(int), hipMemcpyDeviceToHost);
        hipMemcpy(b, dev_b, N * sizeof(int), hipMemcpyDeviceToHost);
        hipMemcpy(c, dev_c, N * sizeof(int), hipMemcpyDeviceToHost);

        stepSize =  N /20 ;
        for (int i = 0; i < N; i+=stepSize) {
            printf("%d + %d = %d\n", a[i], b[i], c[i]);
        }
        getChar()
        hipFree(dev_a);
        hipFree(dev_b);
        hipFree(dev_c);
    }
    free(a);
    free(b);
    free(c);
}


```

ROCM-SMI:
```
======================= ROCm System Management Interface =======================
============================== Current Memory Use ==============================
GPU[0]          : GPU memory use (%): 0
GPU[1]          : GPU memory use (%): 0
================================================================================
============================= End of ROCm SMI Log ==============================

```

---

## 评论 (10 条)

### 评论 #1 — kentrussell (2021-08-23T12:27:05Z)

The "memory use" flag there is a little ambiguous, as it references the memory utilization, namely how "busy" the VRAM is. If you run:
rocm-smi --showmeminfo vram
You should see the appropriate usage.

--showmemuse takes a poll of how often the VRAM is being accessed in the last window (let's say 1 second). If you were to do a single 32GB allocation on a 32GB card, then the utilization would be 0% unless you managed to execute the --showmemuse command over the window where the allocation occurred, while the --showmeminfo would show that the VRAM is 100% allocated. If you managed to get the --showmemuse to be timed just right, you'd still hit memory usage of <10% (since there are 10+ polls in the polling window, the exact number depending on the GPU in question)

--showmemuse is mostly to ensure that VRAM is being accessed. --showmeminfo shows how much memory is actually being used, and uses the kernel's internal auditing to report that. Hopefully this helps!

If you wanted to test the --showmemuse flag, a more suitable test would be to allocate multiple small allocations in a row. That should show the --showmemuse more effectively, since the allocations are happening more frequently and thus the polling window has more accesses reported.

---

### 评论 #2 — gggh000 (2021-08-23T19:24:26Z)

ok, i will try that differently, thx

---

### 评论 #3 — gggh000 (2021-08-23T23:17:32Z)

I changed the code by introducing loop starting before hipMemcpy (host to dev) till hipMemcpy (dev to host) but still showing 0% as usage. I initially i set 1 second interval ( and removed it) in both app and rocm-smi probe but still showing 0%. 

```
    for (int j = 0 ; j < 2000 ; j++ ) {

        // copy the initialized local memory values to device memory.

        printf("\nCopy host to device... Loop %d.\n", j);
        hipMemcpy(dev_a, a, N * sizeof(int), hipMemcpyHostToDevice);
        hipMemcpy(dev_b, b, N * sizeof(int), hipMemcpyHostToDevice);
        hipMemcpy(dev_c, c, N * sizeof(int), hipMemcpyHostToDevice);
...
...
...
        stepSize =  N /20 ;
        for (int i = 0; i < N; i+=stepSize) {
            printf("%d + %d = %d\n", a[i], b[i], c[i]);
        }
        //sleep(1);

```
From another terminal:
`or i in {1..100} ; do echo loop $i ; rocm-smi --showmemuse ; sleep 1 ; done
`




---

### 评论 #4 — kentrussell (2021-08-24T11:50:18Z)

Odd, it should definitely be yielding something there. What GPU are you using? I can see if we can get it reproduced in-house.

---

### 评论 #5 — gggh000 (2021-08-30T07:38:56Z)

Using MI100. Thanks,

---

### 评论 #6 — kentrussell (2021-09-01T13:16:44Z)

Thanks, we're looking into this internally. I'll update once we have something noteworthy

---

### 评论 #7 — gggh000 (2021-09-23T04:16:26Z)

any update? thx,

---

### 评论 #8 — gggh000 (2021-10-28T02:47:53Z)

rocm4.3.1: with "watch -n 1 rocm-smi --showmeminfo vram" I see hip code above does appear to show allocated memory. It seems just --showmemuse which display percentage fails to correctly show percentage thus showing 0% all the time. 

---

### 评论 #9 — abhimeda (2024-01-02T15:49:13Z)

Is this still reproducible with the latest ROCm?  If not, can we please close it?  Thanks!

---

### 评论 #10 — nartmada (2024-01-10T17:09:12Z)

Issue was fixed around ROCm4.3 timeframe.  Please re-open if the issue still exists in ROCm6.0.0.  Thanks.

---
