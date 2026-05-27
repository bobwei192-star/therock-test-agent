# Compilation Error "no matching function call" when passing kernel as an argument

> **Issue #1842**
> **状态**: closed
> **创建时间**: 2022-10-20T15:35:56Z
> **更新时间**: 2022-10-27T18:18:05Z
> **关闭时间**: 2022-10-27T18:18:05Z
> **作者**: bcaddy
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1842

## 描述

I'm not sure this is the right place to report this, if not please direct me to where to report it.

## Issue

I'm writing a struct to utilize the occupancy API for our kernel launches. It works fine on CUDA but no matter what I do I get this error when compiling for an AMD system. Note that we are using macros to convert between CUDA and HIP calls but the issue persists if I use HIP calls only.

```
src/hydro/../utils/cuda_utilities.h:145:17: error: no matching function for call to 'hipModuleOccupancyMaxPotentialBlockSize'
                cudaOccupancyMaxPotentialBlockSize(&numBlocks, &threadsPerBlock, kernel, (size_t)0, (int)0);
                ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
src/hydro/../utils/../utils/gpu.hpp:68:44: note: expanded from macro 'cudaOccupancyMaxPotentialBlockSize'
#define cudaOccupancyMaxPotentialBlockSize hipModuleOccupancyMaxPotentialBlockSize
                                           ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
src/hydro/hydro_cuda.cu:634:56: note: in instantiation of member function 'cuda_utilities::AutomaticLaunchParams<void (double *, int, int, double, double *, double)>::AutomaticLaunchParams' requested here
    cuda_utilities::AutomaticLaunchParams static const launchParams(Calc_dt_1D);
                                                       ^
/opt/rocm-5.1.0/include/hip/hip_runtime_api.h:3876:12: note: candidate function not viable: no known conversion from 'void (double *, int, int, double, double *, double)' to 'hipFunction_t' (aka 'ihipModuleSymbol_t *') for 3rd argument
hipError_t hipModuleOccupancyMaxPotentialBlockSize(int* gridSize, int* blockSize,
           ^
```

No matter what I do I get this issue. Even passing the kernel as a template argument results in this error. The only thing that doesn't is explicitly casting the kernel to type `hipFunction_t` but that results in a segfault.

## Code

### The Struct

```cpp
#define cudaOccupancyMaxPotentialBlockSize hipModuleOccupancyMaxPotentialBlockSize
template <typename T>
struct AutomaticLaunchParams
{
public:
    AutomaticLaunchParams(T &kernel, size_t numElements=0)
    {
        cudaOccupancyMaxPotentialBlockSize(&numBlocks, &threadsPerBlock, kernel, (size_t)0, (int)0);

        if (numElements > 0)
        {
            numBlocks = (numElements + threadsPerBlock - 1) / threadsPerBlock;
        }
    }

    /// Defaulted Destructor
    ~AutomaticLaunchParams()=default;

    /// The maximum number of threads per block that the device supports
    int threadsPerBlock;
    /// The maximum number of scheduleable blocks on the device
    int numBlocks;
}
```

### Call

And I'm calling it like

```cpp
AutomaticLaunchParams static const launchParams(KERNEL_NAME);
```

## System

I'm attempting to compile [Cholla](https://github.com/cholla-hydro/cholla) at commit [be9f728](https://github.com/bcaddy/cholla/tree/be9f728d95dc7d32ef8e96391b5350b36059b95b) on Crusher with the following modules loaded

```
Currently Loaded Modules:
  1) craype-x86-trento                       9) cray-dsmml/0.2.2       17) pinentry/1.1.1
  2) libfabric/1.15.0.0                     10) cray-mpich/8.1.16      18) git-lfs/2.11.0
  3) craype-network-ofi                     11) cray-libsci/22.06.1.3  19) cray-python/3.9.12.1
  4) perftools-base/22.06.0                 12) PrgEnv-cray/8.3.3      20) rocm/5.1.0
  5) xpmem/2.4.4-2.3_11.2__gff0e1d9.shasta  13) xalt/1.3.0             21) craype-accel-amd-gfx90a
  6) cray-pmi/6.1.3                         14) DefApps/default        22) cray-hdf5/1.12.1.5
  7) cce/14.0.2                             15) nano/4.9               23) cray-fftw/3.3.10.1
  8) craype/2.7.16                          16) hdf5/1.12.1
```

---

## 评论 (2 条)

### 评论 #1 — dmcdougall (2022-10-27T18:09:01Z)

I worked with @bcaddy offline to figure this out with another AMD colleague.

The problem is that this is a typo:
```cpp
#define cudaOccupancyMaxPotentialBlockSize hipModuleOccupancyMaxPotentialBlockSize
```

It should be this instead:
```cpp
#define cudaOccupancyMaxPotentialBlockSize hipOccupancyMaxPotentialBlockSize
```

Bob provided some useful feedback: The real issue is that it was difficult to navigate the public documentation on the HIP occupancy API.  It's not easy to discover what is implemented and available.

I've provided Bob's feedback to the internal engineering team.  Thanks @bcaddy.

This ticket can be closed now.  I don't have the power to close it.

---

### 评论 #2 — bcaddy (2022-10-27T18:18:05Z)

Thanks for you help @dmcdougall. I'll close the ticket now

---
