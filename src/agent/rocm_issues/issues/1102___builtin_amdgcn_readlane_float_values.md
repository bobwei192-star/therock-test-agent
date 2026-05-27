# __builtin_amdgcn_readlane float values?

> **Issue #1102**
> **状态**: closed
> **创建时间**: 2020-05-08T10:18:18Z
> **更新时间**: 2020-09-14T01:29:30Z
> **关闭时间**: 2020-09-14T01:29:30Z
> **作者**: WenbinHou
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1102

## 描述

Hi,

I would like to do `v_readlane_b32` on float values. `v_readlane_b32` doesn't really care about the type (as long as it's 32 bit), but `__builtin_amdgcn_readlane` does.

Is there something (or override) like:
```c++
float __builtin_amdgcn_readlane(float src, uint lane);

// Besides uint __builtin_amdgcn_readlane(uint src, uint lane);
```
Or let `llvm.amdgcn.readlane` work on float values?

<br>

I tried this (compile error):
```c++
extern float __llvm_amdgcn_readlane(float src, uint lane) __asm("llvm.amdgcn.readlane");
```

<br>

I also tried a bit with inlining LLVM `bitcast`, but without fortune :(

Thanks a lot!

---

## 评论 (4 条)

### 评论 #1 — WenbinHou (2020-05-08T10:19:02Z)

Never mind I'm working on OpenCL or HIP. Both are OK.

---

### 评论 #2 — preda (2020-05-09T06:22:20Z)

you can use as_uint2(double).x, .y

---

### 评论 #3 — WenbinHou (2020-05-15T12:54:27Z)

> you can use as_uint2(double).x, .y

Thanks! How about using HIP? 

---

### 评论 #4 — arsenm (2020-05-26T20:15:07Z)

You should never declare intrinsics using asm declarations. You can access this from the source with __builtin_amdgcn_readlane. You could define your own wrapper with as_float(__builtin_amdgcn_readlane(as_uint(x), y))

---
