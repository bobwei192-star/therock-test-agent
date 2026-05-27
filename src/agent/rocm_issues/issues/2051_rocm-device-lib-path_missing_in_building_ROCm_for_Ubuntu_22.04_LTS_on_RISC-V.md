# rocm-device-lib-path missing in building ROCm for Ubuntu 22.04 LTS on RISC-V 

> **Issue #2051**
> **状态**: closed
> **创建时间**: 2023-04-15T02:36:26Z
> **更新时间**: 2024-02-16T16:45:23Z
> **关闭时间**: 2024-02-16T16:45:23Z
> **作者**: luyanaa
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2051

## 描述

I've been working on building ROCm (target Radeon VII + HiFive Unmatched), with Ubuntu 22.04 LTS. I've successfully built rocm-llvm, rocm-cmake, roct-thunk-interface, rocm-device-libs, rocminfo, rocr-runtime, rocm-compilersupport and hip for RISC-V so far. 

However, when I start to build rocBLAS, rocFFT etc. I found that the hipcc fail to find the rocm-device-lib-path, where in this case, locate in /usr/lib/riscv64-linux-gnu/amdgcn/bitcode, And this stuck my building procedure. I have no idea where I can pass the --rocm-device-lib-path to hipcc in the compiling procedure. 

btw: Is AMD interested in RISC-V & ARM support for ROCm?

---

## 评论 (3 条)

### 评论 #1 — luyanaa (2023-04-15T02:43:44Z)

The ROCm RISC-V project statement: https://docs.google.com/presentation/d/1xl9hv_deK7bOOm5KRGZVa7CkRFfw2vOVNFSXS-WFpO0/edit#slide=id.g22d7b151e0f_14_0 (RISC-V Open Hour 2023-April-12)

---

### 评论 #2 — luyanaa (2023-04-16T03:23:30Z)

fixed, seems that declare -x DEVICE_LIB_PATH="/opt/rocm/amdgcn/bitcode" works. 

---

### 评论 #3 — nartmada (2024-02-16T16:45:23Z)

Thanks @luyanaa.  Closing the ticket as the reported issue has been fixed. 

---
