# FR: OpenCL global memory single-pass read or write: bypass the L1 cache

> **Issue #1500**
> **状态**: closed
> **创建时间**: 2021-06-23T12:58:11Z
> **更新时间**: 2021-06-24T20:02:02Z
> **关闭时间**: 2021-06-24T20:02:02Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1500

## 描述

In OpenCL, when accessing global memory, I see two distinct cases: in one case, a large region of data is sequentially read once, or sequentially wrote once. In another case, a smaller block of data is accessed repeteadly.

In the first case (let's call it "single pass sequential"), going through the L1 cache provides no speed benefit AFAIK, but it does pollute the L1 cache with data that is not going to be accessed again. So, it would be useful to have a way to indicate this access pattern for an OpenCL buffer, and the compiler would skip the L1 cache in that case -- hopefully resulting in both faster access and better use of L1 (by avoiding evicting other cached data).

Maybe a mecanism already exist for achieving this?


---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-06-24T08:01:54Z)

Thanks @preda for reaching out.
I have assigned to compiler team to have a look.
Thank you.

---

### 评论 #2 — b-sumner (2021-06-24T14:24:28Z)

@preda AMD is not in control of the OpenCL specification, although it does participate in the working group.  So if you want to raise issues with them, I would try an issue at https://github.com/KhronosGroup/OpenCL-Docs .

Also, FWIW, clang does have __builtin_nontemporal_load and __builtin_nontemporal_store and the amdgcn target supports those, if you want to go nonstandard and nonportable.

---

### 评论 #3 — preda (2021-06-24T20:01:30Z)

@b-sumner thank you for pointing to the LLVM nontemporal load/store builtins, I wasn't aware of them.

About OpenCL, I may consider raising issues there, though I'm not too optimistic about results.


---
