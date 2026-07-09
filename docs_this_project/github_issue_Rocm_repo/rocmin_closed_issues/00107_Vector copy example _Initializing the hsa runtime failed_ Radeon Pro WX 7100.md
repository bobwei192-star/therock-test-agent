# Vector copy example "Initializing the hsa runtime failed" Radeon Pro WX 7100

- **Issue #:** 107
- **State:** closed
- **Created:** 2017-04-24T10:38:09Z
- **Updated:** 2017-05-15T11:48:03Z
- **URL:** https://github.com/ROCm/ROCm/issues/107

## Problem
We've been trying to use HIP and HCC to run some ported CUDA code on Radeon Pro WX 7100.
We follow ROCm installation instructions from https://radeonopencompute.github.io/install.html

At the stage of install check (following the tutorial) we observe the following output:
1. ``Hello, world!'' example

```shell
wget https://raw.githubusercontent.com/bgaster/opencl-book-samples/master/src/Chapter_2/HelloWorld/HelloWorld.cpp
wget https://raw.githubusercontent.com/bgaster/opencl-book-samples/master/src/Chapter_2/HelloWorld/HelloWorld.cl
g++ -I /opt/rocm/opencl/include/ ./HelloWorld.cpp -o HelloWorld -L/opt/rocm/opencl/lib/x86_64 -lOpenCL
./HelloWorld: /usr/local/cuda/lib64/libOpenCL.so.1: no version information available (required by ./HelloWorld)
Executed program succesfully.
```

2. ``Vector copy'' example

```shell
cd /opt/rocm/hsa/sample
make
./vector_copy

Initializing the hsa runtime failed.
```

What could be our possible steps for solving this problem?

## System Specifications
OS: Ubuntu 16.04.2 64bit
Processor: Intel Core i7-4790 @ 3.60Ghz
Memory: 31,4 GiB
Graphics: Radeon Pro WX 7100
Driver Version: amdgpu-pro-17.10-401251