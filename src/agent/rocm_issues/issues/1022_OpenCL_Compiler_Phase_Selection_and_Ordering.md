# OpenCL Compiler Phase Selection and Ordering

> **Issue #1022**
> **状态**: closed
> **创建时间**: 2020-02-24T14:19:47Z
> **更新时间**: 2021-04-19T12:50:43Z
> **关闭时间**: 2021-04-19T12:50:43Z
> **作者**: Moading
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1022

## 描述

Howdy OpenCL fans,
I came across a paper called "Improving OpenCL Performance by Specializing Compiler Phase Selection and Ordering" (https://arxiv.org/pdf/1810.10496.pdf). I am wondering if the same technique could be applied to OpenCL kernels in ROCm as well. If what the authors claim is true, there might be a significant gain in performance for OpenCL kernels. There have been numerous posts here where users report that the compiler generates imperfect assembly.

I would like to hear the opinion of someone from the ROCm team, before I try get something working. I am not sure if ROCm uses the same compilers as the authors. I am also not sure if a binary created in that way would run under ROCm.

OK, here is what the authors are doing:
1. Compile an OpenCL kernel to an intermediate representation (device independent) using clang
2. Modify the code using different sequences of transformation steps using opt (part of LLVM). The result is a new version of the code in intermediate representation. There are numerous (even endless) different sequences of transformations that produce a certain number of different versions of the original kernel in intermediate representation.
3. Link with libclc to get all the built in OpenCL functions.
4. Generate device code that runs on a GPU using clang and the gpu target.

Each version of the device code is validated and benchmarked.
I think this is very exciting, check out the paper an let me know what you think!

If anyone involved in the development of ROCm could comment on this, that would be great!

Greetings

---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-04-19T12:50:43Z)

Thanks @Moading for the information.
Thank you.

---
