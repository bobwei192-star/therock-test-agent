# cross-lane operation intrinsics in OpenCL

> **Issue #189**
> **状态**: closed
> **创建时间**: 2017-08-29T14:56:30Z
> **更新时间**: 2018-06-03T15:03:41Z
> **关闭时间**: 2018-06-03T15:03:41Z
> **作者**: pszi1ard
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/189

## 描述

In particular exposing the `ds_permute`, `ds_swizzle` would be useful, but given that hcc defines shfl ops too, why not add those too via some OpenCL extensions.

In addition, the wavefront voting instrinsics `__any`, `__all`, `__ballot` would also be valuable.

As an intermediate solution, is it possible to somehow write in-line ASM equivalent of these or somehow use hc along OpenCL in kernels?

---

## 评论 (12 条)

### 评论 #1 — gstoner (2017-08-29T19:01:45Z)

In OpenCL there are intrinsics for 

uint __builtin_amdgcn_ds_swizzle(uint src, uint pattern);
uint __builtin_amdgcn_readfirstlane(uint src);
uint __builtin_amdgcn_readlane(uint src, uint lane);
uint __builtin_amdgcn_mov_dpp(uint src, uint dpp_ctrl, uint row_mask, uint bank_mask, bool bound_ctrl);
uint __builtin_amdgcn_ds_permute(uint index, uint src);
uint __builtin_amdgcn_ds_bpermute(uint index, uint src);

---

### 评论 #2 — b-sumner (2017-08-29T19:52:43Z)

The exec mask can be obtained with

ulong __builtin_amdgcn_read_exec(void);

You can get the 64 bit result of a compare (e.g. a != b) using

ulong __builtin_amdgcn_sicmp(int a, int b, int c)

where c indicates the type of comparison.  32:=EQ, 33:=NE, 40:=LT

This can be used to produce ballot, any, and all

---

### 评论 #3 — pszi1ard (2017-08-31T13:26:09Z)

Great, thanks for the feedback! Can you point me to the right documentation on this?

Also, not directly related, but I could really use some documentation on wavefront scheduling and instruction throughput/latency tables. Do such things exist?



---

### 评论 #4 — pszi1ard (2017-08-31T18:50:40Z)

+ additionally, I'd like to know how to check whether these intrinsics are supported i) by the compiler ii) by the hardware (is it GCN3 only? are there fallbacks implemented?). If there are docs on these, I can read up, just please point me to it.

---

### 评论 #5 — b-sumner (2017-09-01T14:38:38Z)

You're going outside the scope of standard language features when you directly call __builtin_*.  These are implementation details that may change.  You're best bet to check for support of these prior to some kind of compilation failure is to examine https://github.com/llvm-mirror/clang/blob/master/include/clang/Basic/BuiltinsAMDGPU.def for the compiler you are using.

However, also note that whether these are actually implemented depends on the target, although all of the builtions mentioned here should be available on most targets except for swizzle and mov_dpp which you'll likely only want to use one of anyway.

What heterogeneous languages need are portable high-level constructs for cross-lane access, and until those are available, these low level vendor and device specific mechanisms will have to be used.  Standard OpenCL does at least provide some portable (for those who support the sub-group extension like AMD) built-in functions that may satisfy some of your needs.

---

### 评论 #6 — pszi1ard (2017-09-01T15:04:37Z)

> You're going outside the scope of standard language features when you directly call _builtin*.

I know, that's why I asked whether OpenCL extensions could be added.

> You're best bet to check for support of these prior to some kind of compilation failure is to examine https://github.com/llvm-mirror/clang/blob/master/include/clang/Basic/BuiltinsAMDGPU.def for the compiler you are using.

That doesn't sound like a solution that can be used outside of tinkering, can it? I want to use this in a production code that might be compiled with the ancient fglrx compiler by some and with the latest ROCm compilers by others. Without some means to test for compiler support for these buildtins, I don't see how can we use them in GROMACS (without awkward workarounds in the build system to test the compiler).

> What heterogeneous languages need are portable high-level constructs for cross-lane access, and until those are available, these low level vendor and device specific mechanisms will have to be used.

I understand and have no problem with it. I care more about performance than pretty high-level constructs, I'd just like to be able to write e.g. 
```
#if HAVE__BUILTIN_AMDGCN_DS_SWIZZLE
   // fast foo using ds_swizzle
    void foo() { /*...*/ }
#else 
   // fallback foo w/o ds_swizzle
    void foo() { /*...*/ }
#endif

```

---

### 评论 #7 — pszi1ard (2017-09-01T15:06:18Z)

...or is there a clang-way to programmatically  test for the existence of these intrinsics?

---

### 评论 #8 — b-sumner (2017-09-01T15:36:01Z)

It wouldn't make sense to have a multitude of OpenCL extensions for fine grain hardware specific features.

I don't think you want the HAVE_* guards, particularly if more that one can actually be true.  What you want, I think, is a guard like AMD_SWIZZLE_IS_BEST.  You will be able to construct such guards when clang starts defining target macros such as `__gfx803__` etc.  With target specific guards, the impact of one of those __builtin_amdgcn_* being dropped should be reduced.

clang does support a __has_builtin macro, see https://clang.llvm.org/docs/LanguageExtensions.html


---

### 评论 #9 — pszi1ard (2017-09-01T17:10:39Z)

Thanks! For our current code release the clang `__has_builtin` should be good enough.

First performance-related observation/question: is it reasonable to expect that a wavefront "any" collective implemented using sicmp does not outperform a shared memory-based implementation?

---

### 评论 #10 — b-sumner (2017-09-01T17:54:23Z)

I would not expect that.

---

### 评论 #11 — pszi1ard (2017-09-25T14:11:15Z)

@b-sumner Looks like increased register usage could be the cause for 30% performance drop in one of the kernels. Is it normal for sicmp to require an extra register?

---

### 评论 #12 — pszi1ard (2017-10-06T00:40:26Z)

For the record, I get the same 25-30% regression when using sicmp on Vega too, same register usage (one extra wrt local mem-based collective).

---
