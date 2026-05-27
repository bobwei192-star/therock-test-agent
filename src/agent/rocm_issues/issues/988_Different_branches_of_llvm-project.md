# Different branches of llvm-project

> **Issue #988**
> **状态**: closed
> **创建时间**: 2019-12-31T11:38:47Z
> **更新时间**: 2022-05-01T09:06:41Z
> **关闭时间**: 2022-05-01T09:06:41Z
> **作者**: justxi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/988

## 描述

There are currently different repositories and branches to build components of ROCm.

To build ROCm-OpenCL-Runtime "roc-ocl-3.0.0" branch from https://github.com/RadeonOpenCompute/llvm-project (fork) should be used.

To build ROCm-Device-Libs "amd-std-open" branch from https://github.com/RadeonOpenCompute/llvm-project.git (fork) should be used.

And to build AOMP "AOMP-191029" branch from https://github.com/ROCm-Developer-Tools/llvm-project (mirror) is used. According to the clone script, for "ROCm-Device-Libs" "roc-ocl-3.0.x" branch, the same compiler is used.


It seems that building "ROCm-OpenCL-Runtime" and "AOMP" (OpenMP) needs two different branches of compilers(?).

Will this be merged together, to get one repository and one branch to build them all?


---

## 评论 (4 条)

### 评论 #1 — justxi (2020-06-15T04:39:27Z)

No comment? =)

---

### 评论 #2 — ronlieb (2020-06-16T21:49:57Z)

Yes, the two different branches of LLVM are in the process of being merged so that one branch can build(rule) them all.

---

### 评论 #3 — searlmc1 (2020-06-16T21:51:13Z)

@gregrodgers @acmeman925 


---

### 评论 #4 — justxi (2020-06-17T05:20:03Z)

Good to hear =).

---
