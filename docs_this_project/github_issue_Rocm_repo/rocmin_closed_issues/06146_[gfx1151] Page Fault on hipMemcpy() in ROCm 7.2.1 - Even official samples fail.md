# [gfx1151] Page Fault on hipMemcpy() in ROCm 7.2.1 - Even official samples fail

- **Issue #:** 6146
- **State:** closed
- **Created:** 2026-04-13T17:00:15Z
- **Updated:** 2026-04-16T06:11:56Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6146

# [gfx1151] Page Fault on hipMemcpy() in ROCm 7.2.1

## Hardware Configuration
- **GPU**: AMD Radeon 8060S (0x1586, gfx1151)
- **Architecture**: RDNA 3 (Strix Halo, iGPU)
- **CPU**: AMD Ryzen AI MAX+ 395 w/ Radeon 8060S
- **System Memory**: 128GB DDR5 (shared with GPU)
- **Compute Units**: 40

## Software Configuration
- **ROCm**: 7.2.1 (70201-81~24.04)
- **Driver**: 6.16.13
- **OS**: Ubuntu 24.04.4 LTS
- **Kernel**: Linux 6.17.0-20-generic

## Kernel Parameters
```
amdgpu.vm_fragment_size=9
amdgpu.gttsize=126976
amdgpu.no_system_mem_limit=1
amdgpu.noretry=0
ttm.pages_limit=32505856
```

## Issue Description

### Problem Summary
When attempting to perform **GPU memory copies** (`hipMemcpy`) on the **gfx1151 (Radeon 8060S iGPU)**, the program crashes with a **GPU memory access fault (page fault)**.

### ⭐ Critical Finding
**Even the OFFICIAL ROCm HIP samples fail!** This confirms it's a fundamental ROCm compatibility issue with gfx1151, not a problem with our code.

### Symptom
```
Memory access fault by GPU node-1 (Agent handle: 0x...)
on address 0x...
Reason: Page not present or supervisor privilege.
```

### What Works
- ✅ `rocm-smi` correctly identifies the GPU
- ✅ `rocminfo` shows proper HSA agents
- ✅ `hipMalloc()` successfully allocates device memory
- ✅ `hipFree()` works fine
- ✅ All device query APIs work perfectly

### What Fails
- ❌ `hipMemcpy()` (Host to Device) - **PAGE FAULT**
- ❌ `hipMemcpy()` (Device to Host) - **PAGE FAULT**
- ❌ Any GPU memory copy operation
- ❌ **OFFICIAL ROCm HIP SQUARE SAMPLE** also fails!

## Reproduction Steps

### Minimal Reproducible Example: OFFICIAL HIP Sample

The issue is reproducible with **unmodified ROCm official sample code** from `/opt/rocm/share/hip/samples/0_Intro/square/`:

```cpp
#include <stdio.h>
#include "hip/hip_runtime.h"

#define CHECK(cmd)                                                                                 \
  {                                                                                                \
    hipError_t error = cmd;                                                                        \
    if (error != hipSuccess) {                                                                     \
      fprintf(stderr, "error: '%s'(%d) at %s:%d\n", hipGetErrorString(error), error, __FILE__,     \
              __LINE__);                                                                           \
      exit(EXIT_FAILURE);                                                                          \
    }                                                                                              \
  }

template <typename T> __global__ void vector_square(T* C_d, const T* A_d, size_t N) {
  size_t offset = (blockIdx.x * blockDim.x + threadIdx.x);
  size_t stride = blockDim.x * gridDim.x;

  for (size_t i = offset; i < N; i += stride) {
    C_d[i] = A_d[i] * A_d[i];
  }
}

int main(int argc, char* argv[]) {
  float *A_d, *C_d;
  float *A_h, *C_h;
  size_t N = 1000000;
  size_t Nbytes = N * sizeof(float);
  static int device = 0;
  CHECK(hipSetDevice(device));
  hipDeviceProp_t props;
  CHECK(hipGetDeviceProperties(&props, device));
  printf("info: running on device %s\n", props.name);
#ifdef __HIP_PLATFORM_AMD__
  printf("info: architecture on AMD GPU device is: %s\n", props.gcnArchName);
#endif

  A_h = (float*)malloc(Nbytes);
  CHECK(A_h == 0 ? hipErrorOutOfMemory : hipSuccess);
  C_h = (float*)malloc(Nbytes);
  CHECK(C_h == 0 ? hipErrorOutOfMemory : hipSuccess);
  for (size_t i = 0; i < N; i++) {
    A_h[i] = 1.618f + i;
  }

  CHECK(hipMalloc(&A_d, Nbytes));
  CHECK(hipMalloc(&C_d, Nbytes));

  printf("info: copy Host2Device\n");
  CHECK(hipMemcpy(A_d, A_h, Nbytes, hipMemcpyHostToDevice));  // CRASHES HERE!

  const unsigned blocks = 512;
  const unsigned threadsPerBlock = 256;

  printf("info: launch 'vector_square' kernel\n");
  hipLaunchKernelGGL(vector_square, dim3(blocks), dim3(threadsPerBlock), 0, 0, C_d, A_d, N);

  printf("info: copy Device2Host\n");
  CHECK(hipMemcpy(C_h, C_d, Nbytes, hipMemcpyDeviceToHost));

  printf("info: check result\n");
  for (size_t i = 0; i < N; i++) {
    if (C_h[i] != A_h[i] * A_h[i]) {
      CHECK(hipErrorUnknown);
    }
  }

  CHECK(hipFree(A_d));
  CHECK(hipFree(C_d));
  free(A_h);
  free(C_h);

  printf("PASSED!\n");
}
```

### Actual Behavior (FAILED)
```
info: running on device Radeon 8060S Graphics
info: architecture on AMD GPU device is: gfx1151
info: allocate host mem (  7.63 MB)
info: allocate device mem (  7.63 MB)
info: copy Host2Device
Memory access fault by GPU node-1 (Agent handle: 0x...)
on address 0x...
Reason: Page not present or supervisor privilege.
Aborted (core dumped)
```

## Key Findings

**1. Issue is NOT permission-related**
- Running with `sudo` produces the same result
- User is already in `render` group
- Device permissions are correct

**2. Issue is NOT PyTorch-specific**
- Native HIP C++ code also fails with identical error
- **OFFICIAL ROCm HIP SAMPLES FAIL** - this is definitive proof!
- Error occurs during `hipMemcpy()` call, not during `hipMalloc()`

**3. `amdgpu.vm_fragment_size=9` helps but doesn't fully fix**
- Before: Even simple `hipMalloc()` would fail
- After: `hipMalloc()` works, but `hipMemcpy()` still fails

## Request

1. **Confirmation** that this is a known issue with gfx1151 in ROCm 7.2
2. **Guidance** on whether a fix is planned for ROCm 7.3+
3. **Suggestions** for additional kernel parameters or workarounds to try

## Additional Information Available
- Full rocminfo output
- Complete dmesg/kernel logs
- Full package list of all 65 ROCm packages
- Any additional testing or debugging requested
