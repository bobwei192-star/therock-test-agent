# OpenCL miscompilation

> **Issue #1817**
> **状态**: closed
> **创建时间**: 2022-09-30T22:51:51Z
> **更新时间**: 2024-05-09T16:34:45Z
> **关闭时间**: 2024-05-09T16:34:45Z
> **作者**: PlasmaPower
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1817

## 描述

I've encountered a scenario where the ROCm OpenCL codegen miscompiles a kernel and it returns the wrong result. Here is a collection of files which replicate the issue and verifies it's not just undefined behavior in the kernel code: https://gist.github.com/PlasmaPower/c8a650b3268dc5cd8a54755431427350

`kernel.cl` is the kernel in question. `run-kernel.c` is a program to execute the kernel on the first OpenCL device and print the result, and `host.c` is `kernel.cl` which a short preamble containing a main function that allows the same code to run on the host instead of the GPU, which has a different result.

To execute the program on the host, and enable sanitizers showing that it doesn't have undefined behavior:
```sh
$ clang host.c -Wall -fsanitize=memory,undefined,unsigned-integer-overflow,implicit-conversion -o host && ./host
Host result: 369c71
```

To execute the program on the GPU:
```sh
$ clang run-kernel.c -lOpenCL -o run-kernel && ./run-kernel
Running on GPU: gfx1010:xnack-
GPU result: 26c8c71
```

This issue has been replicated on a 5700 XT and a 6900 XT. I've reduced the test case as much as I could. You'll note that parts of it are entirely unused, but are needed to trick the optimizer into thinking they're used, which is necessary to replicate the issue. That's the reason for the `zero` argument, which is always set to zero.

---

## 评论 (6 条)

### 评论 #1 — Pierre-vh (2022-10-19T09:12:33Z)

Fix under review: https://reviews.llvm.org/D136059

---

### 评论 #2 — Pierre-vh (2022-10-21T13:56:54Z)

https://reviews.llvm.org/rG824dd811be421cd946f64c25eb8ef3ac47eb19f2

Should be solved now

---

### 评论 #3 — mwpastore (2023-02-26T00:04:27Z)

It looks like this patch will be included in a future release of rocm-llvm/llvm-16. Is there any way to patch a system running llvm-15 and the current release of ROCm installed by amdgpu-install? 

---

### 评论 #4 — madMAx43v3r (2023-02-26T09:40:59Z)

> Should be solved now

The question is when will AMD drivers be shipping the fix? This is a major issue making a lot of GPGPU applications fail.

Old GPUs like RX 480 work, but anything newer doesnt.

Correction, Vega 56 with older driver 20.40 works too, using `--opencl=pal,legacy` when installing.

---

### 评论 #5 — ppanchad-amd (2024-05-09T16:26:01Z)

@PlasmaPower Apologies for the lack of response. Can you please test with latest ROCm 6.1.0? If resolved, please close ticket. Thanks!

---

### 评论 #6 — PlasmaPower (2024-05-09T16:31:43Z)

Thanks for following up! Unfortunately I no longer have an AMD GPU. The gist I linked in the original post should be pretty easy to compile and test (just `clang run-kernel.c -lOpenCL -o run-kernel && ./run-kernel` as described in the OP), but I'd also be fine just closing this issue because it seems resolved and I'm no longer building the project I was.

---
