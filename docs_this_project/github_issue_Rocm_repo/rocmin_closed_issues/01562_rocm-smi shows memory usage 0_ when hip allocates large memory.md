# rocm-smi shows memory usage 0% when hip allocates large memory

- **Issue #:** 1562
- **State:** closed
- **Created:** 2021-08-21T04:02:21Z
- **Updated:** 2024-01-10T17:09:13Z
- **URL:** https://github.com/ROCm/ROCm/issues/1562

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