# Q: OpenCL preprocessor define to identify ROCm or __asm() support

> **Issue #805**
> **状态**: closed
> **创建时间**: 2019-05-29T10:55:12Z
> **更新时间**: 2024-10-04T09:06:52Z
> **关闭时间**: 2024-10-04T09:06:52Z
> **作者**: preda
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/805

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

Is there a way, in the OpenCL source, to identify whether it's the ROCm OpenCL that is compiling the code (as opposed to, e.g. amdgpu-pro or something else).

In particular, I'd like to be able to #if case in OpenCL whether __asm() is supported. Being able to identify ROCm would bring me halfway there as I know that ROCm-OpenCL supports __asm().


---

## 评论 (6 条)

### 评论 #1 — nartmada (2024-01-26T04:19:58Z)

@preda, I have forwarded your question to internal team.  

---

### 评论 #2 — schung-amd (2024-07-24T15:40:21Z)

Hi @preda, are you still experiencing this issue? If so, can you provide more details on your workflow?

---

### 评论 #3 — preda (2024-07-24T18:05:16Z)

Here is an example:
```
u32 bfi(u32 u, u32 mask, u32 bits) {
#if HAS_ASM
  u32 out;
  __asm("v_bfi_b32 %0, %1, %2, %3" : "=v"(out) : "v"(mask), "v"(u), "v"(bits));
  return out;
#else
  return (u & mask) | bits;
#endif
}
```
(taken from https://github.com/preda/gpuowl/blob/88383e11b63331264dbda70df767519bc61fb9ef/src/cl/weight.cl#L36 )

As you see, the decision whether to use __asm() is based on an outside custom define (HAS_ASM). I would like a solution that does not require this outside-generated define.

Please ask if this usage example is not clear.


---

### 评论 #4 — schung-amd (2024-07-24T19:20:21Z)

Thanks for the reply @preda, I can see how this could be useful to you. Since asm support is non-standard, it's going to depend on the compiler and platform being used. Currently, the ROCm compilers are built around clang (https://rocm.docs.amd.com/en/latest/reference/rocmcc.html), so you might be able to check for the clang definitions (https://github.com/cpredef/predef/blob/master/Compilers.md#clang). Let me know if this works for you, I'll continue digging for other preprocessor defines you might be able to grab.

---

### 评论 #5 — sohaibnd (2024-10-03T20:00:43Z)

Hi @preda, you can use the clGetPlatformInfo and clGetDeviceInfo functions to get information about the platform (i.e implementation of OpenCL such as ROCm OpenCL) and the device that you are using which you can use when compiling your OpenCL program. Is that what you are looking for?

---

### 评论 #6 — preda (2024-10-04T09:06:52Z)

@schung-amd Indeed using the clang defines (such as __clang__ ) should allow me to infer whether the OpenCL compiler is supporting asm().

@sohaibnd Using the host runtime such as clGetPlatformInfo, clGetDeviceInfo is not as straightforward as I'd still need to infer from that the nature of the OpenCL compiler, to know whether various special features such as asm() are supported by the compiler.

Overall I consider this issue as addressed, thank you!


---
