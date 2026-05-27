# amdgcn-amd-amdhsa target compile error with missing file.

> **Issue #1481**
> **状态**: closed
> **创建时间**: 2021-05-26T02:06:10Z
> **更新时间**: 2021-07-01T06:31:07Z
> **关闭时间**: 2021-07-01T06:31:07Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1481

## 描述

I have very simple opencl kernel and wanted to compile it using amdgpu as target:
https://llvm.org/docs/AMDGPUUsage.html#target-triples

system:
Ubuntu180405
rocm 4.1 installed including llvm. 


file: p25k.c

#include <CL/cl.h>
#include <stdio.h>

kernel void kernelfcn(      global uint *dev_c,   global uint * dev_a,  global uint * dev_b)
{
  uint tid = get__id(0);
 *dev_c = 100;
 *dev_a = 200;
}
But it errors out with that:

clang --target=amdgcn-amd-amdhsa -c p25k.c -o p25k.o
In file included from p25k.c:1:
In file included from /usr/local/include/CL/cl.h:33:
In file included from /usr/local/include/CL/cl_platform.h:224:
In file included from /opt/rocm-4.1.0/llvm/lib/clang/12.0.0/include/stdint.h:52:
/usr/include/stdint.h:26:10: fatal error: 'bits/libc-header-start.h' file not found
#include <bits/libc-header-start.h>
         ^~~~~~~~~~~~~~~~~~~~~~~~~~

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-06-03T11:43:45Z)

Hi @gggh000 
Thanks for reaching out.
Let me check this for you quickly.

---

### 评论 #2 — ROCmSupport (2021-06-03T12:36:34Z)

Looks like the file is missed in your system.
Its no where related to ROCm.
Request you to check your machine/environment for the same.

I am able to find the header properly in my machine(which I newly installed ROCm 4.2 on a clean system).


taccuser@taccuser-X399-DESIGNARE-EX:~$ locate libc-header-start.h
**/usr/include/x86_64-linux-gnu/bits/libc-header-start.h**


---

### 评论 #3 — ROCmSupport (2021-07-01T06:31:07Z)

As its specific to your machine, request you to flash with a clean OS and check.
I checked in 3 machines and able to find the file in all machines.
Thank you.

---
