# Linking for amdgcn--amdhsa target

> **Issue #61**
> **状态**: closed
> **创建时间**: 2016-12-23T13:12:52Z
> **更新时间**: 2017-07-02T17:16:37Z
> **关闭时间**: 2017-07-02T17:16:37Z
> **作者**: rjfnobre
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/61

## 描述

I have LLVM bytecode files representing OpenCL kernels.
They were generated from LLVM IR representing OpenCL with:
/opt/rocm/llvm/bin/llvm-link function.ll /opt/rocm/lib/opencl.amdgcn.bc -o function.linked.bc

How can I compile them to a ROCm compatible executable?

I get the following error:
error: <unknown>:0:0: in function Convolution2D_kernel void (float addrspace(1)*, float addrspace(1)*, i32, i32): unsupported call to function get_global_id

The command in question is:
/opt/rocm/llvm/bin/clang -target amdgcn--amdhsa function.linked.bc -S -o function.amdgcn

'function.linked.bc' was linked with:
/opt/rocm/llvm/bin/llvm-link function.optim.ll /opt/rocm/lib/opencl.amdgcn.bc -o function.linked.bc

I tried using LIBCLC instead of the ROCm-Device-Libs but the error was exactly the same.

What could be the cause?

