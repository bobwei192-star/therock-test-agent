# Testing clBLAS with OpenCL produces "error: variables in the local address space can only be declared in the outermost scope of a kernel function"

> **Issue #674**
> **状态**: closed
> **创建时间**: 2019-01-16T19:27:14Z
> **更新时间**: 2019-01-17T08:57:52Z
> **关闭时间**: 2019-01-16T21:49:25Z
> **作者**: WaldemarH
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/674

## 描述

1. I've install ROCm on Centos 7.6 where the rocminfo and clinfo execute normally.
2. I've build clBLAS with OpenCL 2.0 and then started test_short which fails with
error: variables in the local address space can only be declared in the outermost scope of a kernel function
        __local float4 ascratch[4*16*4];

And if you check the kernel you will see that ascratch is defined almost at the end of the function.,

Now I have no knowledge on who generates the kernel and how, but I assume that you know and can fix this.

Best regards
Waldemar

[test_short.txt](https://github.com/RadeonOpenCompute/ROCm/files/2765736/test_short.txt)
[clinfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/2765737/clinfo.txt)
[rocminfo.txt](https://github.com/RadeonOpenCompute/ROCm/files/2765738/rocminfo.txt)




---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2019-01-16T21:49:25Z)

It appears that you [have opened an issue in the appropriate repo](https://github.com/clMathLibraries/clBLAS/issues/341) (for the library itself). That is the correct place to report the problem you are seeing, as it is a problem with the kernel and not ROCm or our OpenCL compiler.

Said kernel does not follow the [OpenCL C specifications](https://www.khronos.org/registry/OpenCL/specs/opencl-2.0-openclc.pdf) required by OpenCL 2.0. Specifically, in Section 6.5.2, "__local (or local)" and in the section "__local" in [this SDK specification](https://www.khronos.org/registry/OpenCL/sdk/2.0/docs/man/xhtml/local.html): 
> Variables allocated in the __local address space inside a kernel function must occur at kernel function scope.

---

### 评论 #2 — b-sumner (2019-01-16T22:15:43Z)

Right, that declaration is inside a for loop and hence not at kernel function scope.

---

### 评论 #3 — WaldemarH (2019-01-17T08:57:52Z)

Thanks guys.

---
