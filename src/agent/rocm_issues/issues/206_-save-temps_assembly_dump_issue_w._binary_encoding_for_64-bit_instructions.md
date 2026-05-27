# -save-temps assembly dump issue w. binary encoding for 64-bit instructions

> **Issue #206**
> **状态**: closed
> **创建时间**: 2017-09-13T08:34:46Z
> **更新时间**: 2017-11-15T22:47:18Z
> **关闭时间**: 2017-11-15T22:47:18Z
> **作者**: preda
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/206

## 标签

- **Question** (颜色: #cc317c)

## 描述

On AMDGPU-pro 17.30, RX Vega 64, Linux.
Passing -save-temps when compiling the OpenCL kernel dumps assembly in a file like _0_gfx900.s, e.g.
```
flat_load_dwordx4 v[19:22], v[2:3]                   // 00000000C0EC: DC5C0000 DC5C0000
flat_load_dwordx4 v[35:38], v[10:11]                 // 00000000C0F4: DC5C0000 DC5C0000
```
In the comment is the address and the binary encoding of the instruction. For 64 bits instructions, the binary encoding is wrong, being one word written twice (DC5C0000 DC5C0000) instead of the correct encoding.


---

## 评论 (6 条)

### 评论 #1 — gstoner (2017-09-14T11:29:10Z)

@preda Do you see the same issue on 1.6.3 compiler,  I am checking this out 

---

### 评论 #2 — preda (2017-09-14T12:26:52Z)

I'm on Ubuntu 17.04 thus I don't have ROCm 1.6.3 (that's why I still use AMDGPU-pro)...

---

### 评论 #3 — preda (2017-10-23T14:37:08Z)

This is still ON in ROCm 1.6-180. (Ubuntu 16.04, R9-Nano).

---

### 评论 #4 — dfukalov (2017-10-30T15:32:01Z)

Hi @preda whould you please provide example kernel an compilation switches (e.g. dumped .cl file) ?

---

### 评论 #5 — preda (2017-10-30T21:48:14Z)

Please have a look at the attached ISA here for an example:
https://github.com/RadeonOpenCompute/ROCm/issues/241

Compile any kernel that contains any 64-bit instructions. Dump with -save-temps=folder/
This is 100% reproducible and affects every kernel and dump.

---

### 评论 #6 — dfukalov (2017-11-15T22:47:18Z)

https://github.com/RadeonOpenCompute/llvm/commit/21d31c0bdc85ec696a15e2b5366edd054b3906d5
fixes the issue

---
