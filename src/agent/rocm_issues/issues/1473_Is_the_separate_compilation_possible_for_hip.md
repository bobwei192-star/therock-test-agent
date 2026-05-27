# Is the separate compilation possible for hip?

> **Issue #1473**
> **状态**: closed
> **创建时间**: 2021-05-18T00:43:37Z
> **更新时间**: 2021-05-18T16:31:09Z
> **关闭时间**: 2021-05-18T16:31:09Z
> **作者**: brad-mengchi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1473

## 描述

Hi all,

I did not find it in the HIP programming guide but is the separate compilation possible for hip?

And is that possible for link-time optimization?

For example, we have a function file a.c and main file main.c:
--a.c
extern __device__ foo() {
...
}

---a.h
extern __device__ foo();

--main.c
#include "a.h"

__global__ kernel() {
...
fool();
...
}

I tried to compile:
>hipcc -flto -c a.c -o a.o
>hipcc -c main -o main.o
>hipcc a.o main.o -o main

The command line will give me "lld: error: undefined hidden symbol:foo()".
P.S.: I compiled llvm to use for hipcc and compile the LLVMgold.so to use lto.


---

## 评论 (3 条)

### 评论 #1 — scchan (2021-05-18T12:38:01Z)

You have to add the -fgpu-rdc flag if a kernel calls a device function in a difference source file.

---

### 评论 #2 — brad-mengchi (2021-05-18T16:26:06Z)

HI @scchan! Thanks for your answer. So we can compile the device function file with -fgpu-rdc -c and then at link time, which option do we need to use to link up the relocatable device code?

---

### 评论 #3 — brad-mengchi (2021-05-18T16:31:05Z)

Oh I found the solution for the link option. Thanks @scchan !
https://github.com/ROCm-Developer-Tools/HIP/issues/2203

---
