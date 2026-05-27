# undefined symbol: omp_get_mapped_ptr

> **Issue #2413**
> **状态**: closed
> **创建时间**: 2023-08-28T23:36:07Z
> **更新时间**: 2024-03-21T04:02:39Z
> **关闭时间**: 2024-03-21T04:02:39Z
> **作者**: Ashutosh-Londhe
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2413

## 描述

I am getting an error for `undefined symbol: omp_get_mapped_ptr` when compiling for OpenMP offload 

I am using following command
` clang++ -O3 -fPIC -DUNIX -Wall -g -std=c++11 -fopenmp -fopenmp=libomp -fopenmp-targets=amdgcn-amd-amdhsa -Xopenmp-target=amdgcn-amd-amdhsa -march=gfx908 -I/ext-home/asl/OPS_cg/OPS/ops/c/include -L/ext-home/asl/OPS_cg/OPS/ops/c/lib/clang  laplace2d_ops.cpp  -I. ./openmp_offload/openmp_offload_kernels.cpp   -lops_ompoffload -lomptarget -o laplace2d_ompoffload`

I am using a Rocm5.4.3 version.
I have another clang installation, in its libomptarget i found the `omp_get_mapped_ptr` using `nm` command
but its not there in libomptarget.so file under Rocm/llvm/lib


