# [Issue]: No warning should be given when using CMAKE_HIP_ARCHITECTURES=gfx90a in CMake

- **Issue #:** 4296
- **State:** open
- **Created:** 2025-01-24T20:09:36Z
- **Updated:** 2025-03-08T09:40:39Z
- **Labels:** Under Investigation, N/A, ROCm 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4296

### Problem Description

I got misleading CMake warnings and it should be printed at all. See details in the "steps to reproduce"
The underlying issue is why `hip-config-amd.cmake` tries to detect AMD GPUs even `CMAKE_HIP_ARCHITECTURES` has been given explicitly. It is completely unnecessary and slow down CMake invocation.

### Operating System

SLES 15.4

### CPU

N/A

### GPU

N/A

### ROCm Version

ROCm 6.3.0

### ROCm Component

HIP

### Steps to Reproduce

To reproduce the warning, AMD GPU should not be available.
Reproducer https://github.com/ye-luo/cmake_gpu/blob/master/test_rocm/CMakeLists.txt
When I give explicit architecture via `CMAKE_HIP_ARCHITECTURES`
```
mkdir build; cd build
cmake -DCMAKE_CXX_COMPILER=amdclang++ -DCMAKE_HIP_ARCHITECTURES=gfx90a ..
```
I should not see the following warning since I'm using well documented option "CMAKE_HIP_ARCHITECTURES"
`AMDGPU_TARGETS` should not be exposed to users at all.

```
CMake Warning (dev) at /soft/compilers/rocm/rocm-6.3.0/lib/cmake/hip/hip-config-amd.cmake:91 (message):
   AMDGPU_TARGETS was not set, and system GPU detection was unsuccsesful.
   
   The amdgpu-arch tool failed:
   Error: 'Failed to get device count'
   Output: ''
   
   As a result, --offload-arch will not be set for subsuqent
   compilations, and the default architecture
   (gfx906 for dynamic build / gfx942 for static build) will be used

Call Stack (most recent call first):
  /soft/compilers/rocm/rocm-6.3.0/lib/cmake/hip/hip-config.cmake:149 (include)
  /soft/buildtools/cmake/3.28.3/share/cmake-3.28/Modules/CMakeFindDependencyMacro.cmake:76 (find_package)
  /soft/compilers/rocm/rocm-6.3.0/lib/cmake/hipblas/hipblas-config.cmake:90 (find_dependency)
  CMakeLists.txt:9 (find_package)
This warning is for project developers.  Use -Wno-dev to suppress it.
```
This warning is actually misleading. The final generated commands do correctly pick up `gfx90a` instead of what are mentioned in the warning.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_