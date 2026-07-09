# Wrong LDS size when build with hipcc on RDNA  => NOT

- **Issue #:** 3403
- **State:** closed
- **Created:** 2024-07-07T12:14:30Z
- **Updated:** 2024-07-08T23:13:38Z
- **Labels:** ROCm 6.0.0, AMD Radeon RX 7900 XTX, AMD Radeon Pro W6800, AMD Radeon RX 7900 XT, AMD Radeon Pro W7900, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3403

### Problem Description

I try to build a kernel using WGP with more than 64kB of LDS but il faild on RDNA3 .

I test with fedora native package (40 & 41) so romc 6.0 and 6.1 the build report the same size on LDS if using CU and WGP. did'nt the LDS have a size of 128k (ie 2x64k) of LDS?

I know that the GPU I have is not supported, but it did the same when build with other RDNA(3) suported  `offload-arch=gfx11nn`
(it did the same on RDNA2 but I am not sur for the hardware size on RDNA2 but report a the same with any `offload-arch=gfx10nn`)

### Operating System

Fedora Linux 40

### CPU

AMD Ryzen 9 7940HS w/ Radeon 780M Graphics

### GPU

AMD Radeon Pro W7900, AMD Radeon Pro W6800, AMD Radeon RX 7900 XTX, AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.1.0, ROCm 6.0.0

### ROCm Component

HIPCC

### Steps to Reproduce

code use: the code is "stupid" only for simple report the build error.
```cpp
/*
Build:

  hipcc --offload-arch=gfx1103 -mcumode     rdna_LDS.cpp
  hipcc --offload-arch=gfx1103 -mno-cumode  rdna_LDS.cpp


Erreur: (in both case:)

rdna_LDS.cpp:27:17: error: local memory (90000) exceeds limit (65536) in 'void fct<150>(float const*, float*)'
   27 | __global__ void fct(const float* A, float* B) {


*/

#include <hip/hip_runtime.h>

#define HIP_CHECK_ERROR(flag)                                                      \
    do                                                                             \
    {                                                                              \
        hipError_t _tmpVal;                                                        \
        if((_tmpVal = flag) != hipSuccess)                                         \
        {                                                                          \
            std::ostringstream ostr;                                               \
            ostr << "HIP Function Failed (" << __FILE__ << "," << __LINE__ << ") " \
                 << hipGetErrorString(_tmpVal);                                    \
            throw std::runtime_error(ostr.str());                                  \
        }                                                                          \
    } while(0)


template<int N>
__global__ void fct(const float* A, float* B) {

    __shared__ float tmp[N][N];

    for (int i=0; i<N; i++)
    for (int j=0; j<N; j++) {
        tmp[i][j] = A[N*i+j];
    }
    
    __syncthreads();
    
    for (int i=0; i<N; i++)
    for (int j=0; j<N; j++) {
         B[N*i+j] = tmp[j][j];
    }
}

constexpr int N = 150;

template<typename T>
T* allocateHost(const std::size_t size) {
  void * ptr;
  HIP_CHECK_ERROR(hipHostMalloc(&ptr, size*sizeof(T), hipHostMallocNonCoherent));
  return reinterpret_cast<T*>(ptr);
}

template<typename T>
void deallocateHost(T * ptr) {
  HIP_CHECK_ERROR(hipHostFree((void*)ptr));
}

template<typename T>
T* getDeviceMem(T* host_adr) {
  void * ptr=nullptr;
  HIP_CHECK_ERROR(hipHostGetDevicePointer(&ptr, host_adr, 0));
  return reinterpret_cast<T*>(ptr);
}

int main() {
    float* A = getDeviceMem(allocateHost<float>(N*N));
    float* B = getDeviceMem(allocateHost<float>(N*N));
    hipLaunchKernelGGL(HIP_KERNEL_NAME(fct<N>), 1, 1, 0, 0, A,B);
}
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_