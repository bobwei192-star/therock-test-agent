# OpenCL head: "Intrinsic has incorrect return type!"

> **Issue #340**
> **状态**: closed
> **创建时间**: 2018-02-20T02:40:19Z
> **更新时间**: 2018-12-30T03:17:25Z
> **关闭时间**: 2018-02-26T22:20:45Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/340

## 描述

Ubuntu 17.10, Vega 64.
With freshly built opencl, I get this on clGetPlatformIDs() invocation, e.g.:

$ LD_LIBRARY_PATH=/home/preda/rocm/opencl/build/lib clinfo
Intrinsic has incorrect return type!
i8 addrspace(2)* ()* @llvm.amdgcn.dispatch.ptr
Intrinsic has incorrect return type!
i8 addrspace(2)* ()* @llvm.amdgcn.implicitarg.ptr
Intrinsic has incorrect return type!
i8 addrspace(2)* ()* @llvm.amdgcn.implicitarg.ptr
Intrinsic has incorrect return type!
i8 addrspace(2)* ()* @llvm.amdgcn.implicitarg.ptr
Intrinsic has incorrect return type!
i8 addrspace(2)* ()* @llvm.amdgcn.dispatch.ptr
Number of platforms                               0


---

## 评论 (4 条)

### 评论 #1 — dfukalov (2018-02-26T14:18:15Z)

fixed in https://github.com/RadeonOpenCompute/ROCm-Device-Libs/commit/0f4a9922bd3b0ce15821257645b026d1b1fc6d4d

---

### 评论 #2 — projenix (2018-05-24T21:46:00Z)

I have the same problem on 18.04, I think that we'll have to revert to the older driver.

---

### 评论 #3 — kode54 (2018-09-02T02:27:29Z)

I also have the same problem on 18.04, with the padoka PPA.

---

### 评论 #4 — codedcosmos (2018-12-30T03:17:25Z)

If you are having this issue in ubuntu 18.04
you likely need to install Rocm

https://rocm.github.io/ROCmInstall.html#ubuntu-support---installing-from-a-debian-repository

---
