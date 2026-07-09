# The problem with device synchronization functions exposed by thread divergence

- **Issue #:** 4479
- **State:** closed
- **Created:** 2025-03-11T06:55:54Z
- **Updated:** 2025-03-26T15:17:16Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4479

**Problem Description**
When I ran the test cases designed by myself, I found logical errors in __all_sync and __match_all_sync;

**Environment**
OS: CentOS Linux release 7.6.1810

ROCm Version: 6.3.x

**Reproduction Steps**
1:__all_sync demo:If the threads diverge, this use case is plugging in, and by analogy there is a case where __all_sync and __all compute inconsistent data;It is possible to reason about and test the results at 32 differentiation, 48 differentiation, and 64 differentiation
```
#include <iostream>
#include <hip/hip_runtime.h>
#include <vector>
__device__ int A[64];
__device__ int result[64];
__device__ int result16[64];
__global__ void warp_all_sync_test() {
    unsigned long long mask = 0xffffffffffffffff;
    int tx = threadIdx.x;
    if (threadIdx.x < 16) {
        A[tx] = 0;
    } else {
        A[tx] = 1;
    }
    __syncthreads();
    if (threadIdx.x < 16) {
        result16[tx] = __all_sync(mask, A[tx]);
    } else {
        result16[tx] = __all_sync(mask, A[tx]);
    }
    printf("result16 = %d\n", result16[tx]);
}
int main () {
    warp_all_sync_test<<<1, 64>>>();
    return 0;
}
```

2:__match_all_sync demo:The following example causes the program to crash,It is possible to reason about and test the results at 32 differentiation, 48 differentiation, and 64 differentiation

```
#include <iostream>
#include <hip/hip_runtime.h>
#include <vector>
__device__ int A[64];
__device__ unsigned long long result16[64];
__global__ void warp_match_all_sync_test() {
    unsigned long long mask = 0xffffffffffffffff;
    int tx = threadIdx.x;
    if (threadIdx.x < 16) {
        A[tx] = 0;
    } else {
        A[tx] = 1;
    }
    int valueToMatch = 1;
    int *pred = &valueToMatch;
    __syncthreads();
    if (threadIdx.x < 16) {
        result16[tx] = __match_all_sync(mask, A[tx], pred);
    } else {
        result16[tx] = __match_all_sync(mask, A[tx], pred);
    }
    printf("result16[%d] = %llx\n", tx, result16[tx]);
}
int main () {
    warp_match_all_sync_test<<<1, 64>>>();
    return 0;
}
```

**Expected Result**
The program should compile and run successfully.

Actual Result
Error message:causes crush

Notes for Submission:
Compile with the following command:
hipcc xx.cu -o xx -DHIP_ENABLE_WARP_SYNC_BUILTINS