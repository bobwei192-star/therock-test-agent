# AMDGPU-pro 17.30 OpenCL: spurious warning about "-I ."

> **Issue #209**
> **状态**: closed
> **创建时间**: 2017-09-14T12:34:43Z
> **更新时间**: 2017-10-23T14:36:35Z
> **关闭时间**: 2017-10-23T14:36:35Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/209

## 描述

On Ubuntu 17.04, AMDGPU-pro 17.30 (--compute), RX Vega 64, OpenCL.
If the kernel includes a file from the current directory, like:
#include "foo.h"

Passing "-I." as argument to clBuildProgram() generates the warning:
warning: argument unused during compilation: '-I .'

But not passing that argument produces:
#include "foo.h"
         ^~~~~~~~~~~
1 error generated.
OpenCL compilation log (error -11):
Error: Failed to compile opencl source (from CL to LLVM IR).

I guess the warning shouldn't be generated if the "-I ." is actually needed, or otherwise consider the current directory by default for #include "".


---

## 评论 (10 条)

### 评论 #1 — gstoner (2017-10-17T13:57:06Z)

Can you check the new ROCm 1.6.4  just to see if the this fixes your compiler issue, until 17.40 comes out 

---

### 评论 #2 — preda (2017-10-19T05:08:30Z)

Can I check ROCm 1.6.4 on Ubuntu 17.04 or 17.10? (these are the only OSes I have installed)


---

### 评论 #3 — gstoner (2017-10-19T13:45:13Z)

we had others who have installed it. 

---

### 评论 #4 — gstoner (2017-10-19T13:48:16Z)

Have you looked at new 17.40 Linux beta this is using old compiler 

---

### 评论 #5 — gstoner (2017-10-19T13:49:02Z)

http://support.amd.com/en-us/kb-articles/Pages/AMDGPU-Pro-Beta-Mining-Driver-for-Linux-Release-Notes.aspx


---

### 评论 #6 — preda (2017-10-20T00:09:09Z)

I tried an install of ROCm as per https://rocm.github.io/ROCmInstall.html on Ubuntu 17.10 and it doesn't boot. I'll be looking into AMDGPU-pro 17.40 next.

---

### 评论 #7 — gstoner (2017-10-20T00:44:02Z)

I should say only 17.04 has it been tested for ROCm recently 

---

### 评论 #8 — preda (2017-10-23T09:30:20Z)

So, should I try the binary ROCm 1.6.4 on Ubuntu 17.04 and it should work?

Alternativelly, I would attempt a build from source, but I didn't find documentation for that.


---

### 评论 #9 — preda (2017-10-23T14:31:53Z)

After all, I did re-install my Ubuntu to move down to 16.04... (not very user-friendly, to force the OS)
And thus, I was able to experience ROCm first-hand!

The issue (-I . warning) seems fixed.

---

### 评论 #10 — gstoner (2017-10-23T14:36:35Z)

Preda,   We very clear in our instruction what we support which is 16.04 LTS not 17.x release if you follow the instructions,  again we focus on LTS because ROCm really is for headless servers.   

---
