# [Documentation]: Example in documentation does not compile

- **Issue #:** 3079
- **State:** closed
- **Created:** 2024-05-02T15:14:06Z
- **Updated:** 2024-10-02T18:39:26Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/3079

### Description of errors

This example from [HIP Porting Guide - MemcpyToSymbol](https://rocm.docs.amd.com/projects/HIP/en/latest/how-to/hip_porting_guide.html#memcpytosymbol) documentation does not compile with `hipcc` in rocm-6.1.0 out of the box. 

The compile command is:
```
hipcc -O3 -o test test.cpp
```
The following errors are seen when compiling for a MI210 GPU:
```
test.cpp:33:5: error: too few arguments to function call, expected 2, have 1
   33 |     hipLaunchKernelGGL(Get, dim3(1,1,1), dim3(LEN,1,1), 0, 0, Ad);
      |     ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/opt/rocm-6.1.0/include/hip/amd_detail/amd_hip_runtime.h:244:46: note: expanded from macro 'hipLaunchKernelGGL'
  244 | #define hipLaunchKernelGGL(kernelName, ...)  hipLaunchKernelGGLInternal((kernelName), __VA_ARGS__)
      |                                              ^~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
/opt/rocm-6.1.0/include/hip/amd_detail/amd_hip_runtime.h:241:89: note: expanded from macro 'hipLaunchKernelGGLInternal'
  241 |         kernelName<<<(numBlocks), (numThreads), (memPerBlock), (streamId)>>>(__VA_ARGS__);         \
      |         ~~~~~~~~~~                                                                      ^
test.cpp:13:17: note: 'Get' declared here
   13 | __global__ void Get(hipLaunchParm lp, int *Ad)
      |                 ^   ~~~~~~~~~~~~~~~~~~~~~~~~~
1 error generated when compiling for gfx90a.
```
Please fix this.

### Attach any links, screenshots, or additional evidence you think will be helpful.

The following changes made to the code helps this compile and run successfully:
```
13c13
< __global__ void Get(hipLaunchParm lp, int *Ad)
---
> __global__ void Get(int *Ad)
33c33
<     hipLaunchKernelGGL(Get, dim3(1,1,1), dim3(LEN,1,1), 0, 0, Ad);
---
>     Get <<<dim3(1,1,1), dim3(LEN,1,1)>>>(Ad);
```