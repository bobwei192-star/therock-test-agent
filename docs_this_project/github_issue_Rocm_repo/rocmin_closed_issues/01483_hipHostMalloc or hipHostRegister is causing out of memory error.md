# hipHostMalloc or hipHostRegister is causing out of memory error.

- **Issue #:** 1483
- **State:** closed
- **Created:** 2021-05-28T05:32:27Z
- **Updated:** 2021-07-01T05:38:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/1483

On MI-25, hipMalloc is OK, but I see hipHostRegister returns 2 which by definition appears to be:
hipErrorOutOfMemory 

looking at /root/ROCm-4.2/HIP/build/include/hip/hip_runtime_api.h
typedef enum __HIP_NODISCARD hipError_t {
    hipSuccess = 0,  ///< Successful completion.
    hipErrorInvalidValue = 1,  ///< One or more of the parameters passed to the API call is NULL
                               ///< or not in an acceptable range.
    hipErrorOutOfMemory = 2,

Here is the code compiled by hipcc <filename> on ROCm4.2 installed Ubuntu 1804 machine:
```

#include <stdio.h>
#include <stdbool.h>
#include "hip/hip_runtime.h"

#define ALLOC_NORMAL 1
#define ALLOC_PAGE_LOCKED 2
#define SIZE (10*1024*1024)

float hip_mem_alloc_test(int size, bool up, int allocType) {
    int debug = 0, stat = 0;
    hipEvent_t start, stop;
    int *a, *dev_a;
    float elapsedTime;

    if (debug) {
        printf("hip_mem_alloc_test: entered.\n");
        printf("creating events...");
    }

    hipEventCreate( &start);
    hipEventCreate( &stop);

    if (debug)
        printf("allocating on host...");

    if (allocType == ALLOC_PAGE_LOCKED) {
        stat = hipHostRegister((void**)&a, size * sizeof(*a), hipHostRegisterDefault);
        if (stat != hipSuccess) {
            printf("Err: hipHostRegister failed with code: %d.", stat);
            return 0;
        }
        hipHostMalloc((void**)&a, size * sizeof(*a), hipHostRegisterDefault);
        if (stat != hipSuccess) {
            printf("Err: hipHostMalloc failed with code: %d.", stat);
            return 0;
        }
    } else if  (allocType == ALLOC_NORMAL ) {
        a = (int*) malloc(size*sizeof(a));
    }

    if (debug)
        printf("allocating on gpu...");

    hipMalloc((void**)&dev_a, size * sizeof(&dev_a));

    hipEventRecord( start, 0);
    for (int i = 0; i < 100 ; i ++ ) {
        if (up) {
            hipMemcpy(dev_a, a, size * sizeof(a), hipMemcpyHostToDevice);
        } else {
            hipMemcpy(a, dev_a, size * sizeof(a), hipMemcpyDeviceToHost);
        }

    }
    hipEventRecord(stop, 0);
    hipEventSynchronize(stop);
    hipEventElapsedTime( &elapsedTime, start, stop);
    return elapsedTime;
}

int main()
{
    float elapsedTime;
    printf("main: entered.\n");

    float MB  = (float)100 * SIZE * sizeof(int) / 1024 / 1024;
    elapsedTime = hip_mem_alloc_test(SIZE, true, ALLOC_NORMAL);
    printf("Time using hipMalloc: %3.1f ms.\n", elapsedTime);
    printf("\tMB/s during copy up: %3.1f.\n", MB / (elapsedTime / 1000));

    elapsedTime = hip_mem_alloc_test(SIZE, false, ALLOC_NORMAL);
    printf("Time using hipMalloc: %3.1f ms.\n", elapsedTime);
    printf("\tMB/s during copy down: %3.1f.\n", MB / (elapsedTime / 1000));

    elapsedTime = hip_mem_alloc_test(SIZE, true, ALLOC_PAGE_LOCKED);
    if (elapsedTime != 0) {
        printf("Time using hipHostMalloc: %3.1f ms.\n", elapsedTime);
        printf("\tMB/s during copy up: %3.1f.\n", MB / (elapsedTime / 1000));
    } else {
        printf("Returned 0...\n");
    }

    elapsedTime = hip_mem_alloc_test(SIZE, false, ALLOC_PAGE_LOCKED);
    if (elapsedTime != 0) {
        printf("Time using hipHostMalloc: %3.1f ms.\n", elapsedTime);
        printf("\tMB/s during copy down: %3.1f.\n", MB / (elapsedTime / 1000));
    } else {
        printf("Returned 0...\n");
    }

}

```

With resulting output being:
```

main: entered.
Time using hipMalloc: 1211.5 ms.
        MB/s during copy up: 3301.8.
Time using hipMalloc: 1152.7 ms.
        MB/s during copy down: 3470.1.
Err: hipHostRegister failed with code: 2.Returned 0...
Err: hipHostRegister failed with code: 2.Returned 0...
root@guest:/git.co/dev-learn/rocm/hip/cuda-conversion/p188#

```