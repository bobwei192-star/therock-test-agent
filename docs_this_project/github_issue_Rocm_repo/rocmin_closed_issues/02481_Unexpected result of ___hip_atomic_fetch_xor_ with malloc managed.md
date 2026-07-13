# Unexpected result of `__hip_atomic_fetch_xor` with malloc managed

- **Issue #:** 2481
- **State:** closed
- **Created:** 2023-09-19T15:04:38Z
- **Updated:** 2023-09-19T17:02:49Z
- **URL:** https://github.com/ROCm/ROCm/issues/2481

In CUDA, managed memory allocated with `cudaMallocManaged` can be accessed on host and device without needing to prefetch. Since the HIP API is meant to match the CUDA API closely, I expect the same behaviour for `hipMallocManaged`.

However, this simple example fails when `__hip_atomic_fetch_xor` is used with memory allocated with `hipMallocManaged`.

```
#include "hip/hip_runtime.h"

#include <cassert>

constexpr int init = 0;
constexpr int n = 1;

__global__ void test_xor(int *data, int val) {
#ifdef MY_ATOMIC_ADD
  __hip_atomic_fetch_add(data, val, __ATOMIC_RELAXED,
                         __HIP_MEMORY_SCOPE_WAVEFRONT);
#else
  __hip_atomic_fetch_xor(data, val, __ATOMIC_RELAXED,
                         __HIP_MEMORY_SCOPE_WAVEFRONT);
#endif
}

#define CHECK(res)                                                             \
  if (res != hipSuccess) {                                                     \
    fprintf(stderr, #res " failed!\n");                                        \
    std::terminate();                                                          \
  }

int main(int argc, char **argv) {
  int *data = nullptr;
  CHECK(hipMallocManaged(&data, n * sizeof *data, hipMemAttachGlobal));
  hipStream_t s;
  CHECK(hipStreamCreate(&s));
  for (size_t i = 0; i < n; ++i)
    data[i] = init;

#ifdef MY_PREFETCH
  CHECK(hipMemPrefetchAsync(data, n * sizeof *data, 0));
#endif
  int xor_val = 1;
  hipLaunchKernelGGL(test_xor, 1, 1, 0, s, data, xor_val);
  CHECK(hipDeviceSynchronize());

  for (size_t i = 0; i < n; ++i)
    printf("Malloc managed ans: %d\tExpected: %d\n", data[i], init ^ xor_val);
  CHECK(hipFree(data));
}

```

Output:
```
$ hipcc hip_xor.cpp && ./a.out
Malloc managed ans: 0	Expected: 1
```
The example will work if `__hip_atomic_fetch_add` is used instead of `__hip_atomic_fetch_xor`:
```
$ hipcc hip_xor.cpp -DMY_ATOMIC_ADD && ./a.out
Malloc managed ans: 1	Expected: 1
```
The sample will also work with a prefetch and xor:
```
$ hipcc hip_xor.cpp -DMY_PREFETCH && ./a.out
Malloc managed ans: 1	Expected: 1
```

Is a prefetch needed in order to use atomic ops on the GPU? If so then why does it work without the prefetch for `__hip_atomic_fetch_add` and not for `__hip_atomic_fetch_xor`? Or is there a problem with this single builtin (`__hip_atomic_fetch_xor`)? Thanks in advance.

Ping @ldrumm

OS: Ubuntu 22.04 
GPU: W6800 gfx1030
ROCm: Tested on rocm/5.4.3 and rocm/5.6.1.
