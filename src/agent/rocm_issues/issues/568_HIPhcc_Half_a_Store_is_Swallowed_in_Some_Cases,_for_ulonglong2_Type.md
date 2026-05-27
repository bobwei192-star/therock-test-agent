# HIP/hcc: Half a Store is Swallowed in Some Cases, for ulonglong2 Type

> **Issue #568**
> **状态**: closed
> **创建时间**: 2018-10-03T16:17:34Z
> **更新时间**: 2018-12-04T09:06:06Z
> **关闭时间**: 2018-12-04T09:06:06Z
> **作者**: 949f45ac
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/568

## 描述

Ubuntu 16.04, kernel 4.13, ROCm 1.9, gfx900 (gfx803 has same problem I think)

Consider this line I had to comment out:
https://github.com/949f45ac/xmr-stak-hip/blob/d0cd20c597dd9cfbe3c67e3bcb99a9bbf31a895c/hip_code/cuda_core.cu#L309
When I try using it instead of the line below (that actually works, by issuing the correct instruction via `asm`) then I can see in the generated ISA that only one `global_store_dwordx2` instruction is generated, instead of a `global_store_dwordx4` or at least 2 `store_dwordx2` instructions.
You can easily validate whether the whole thing works correctly by running `xmr-stak-test` after building. (Build instructions are in the repo’s README.)

Further below in the same function there is another such storage operation with the same data types and all, and that one actually works, so I think in the case where it doesn't work the compiler is confused by other circumstances – maybe he wants to actually split up the load into 2 (because the first half is already computed comparatively early) but forgets about one part somehow.

Cheers!

---

## 评论 (8 条)

### 评论 #1 — b-sumner (2018-10-03T18:16:21Z)

It looks like we have a problem in the definition of the long long and unsigned long long vector types in hip_vector_types.h.  Could you try adding an extra "long" to the first argument of the macro, e.g. change

`DECLOP_MAKE_TWO_COMPONENT(unsigned long, ulonglong2);`

to

`DECLOP_MAKE_TWO_COMPONENT(unsigned long long, ulonglong2);`


---

### 评论 #2 — 949f45ac (2018-10-04T15:18:04Z)

I edited `/opt/rocm/hip/include/hip/hcc_detail/hip_vector_types.h` locally with what you suggested and my code is unfortunately still broken in the same way, storing only dwordx2 in that line.
Like I said, it is not generally broken, I’m loading/storing `ulonglong2` in the same way in other places in my code and there it works fine. It must have something to do with the surrounding code lines as well.

---

### 评论 #3 — b-sumner (2018-10-04T16:01:22Z)

Do I assume correctly that all of the aliasing (and this code does appear to be breaking strict aliasing) is an attempt to force the compiler to use wider loads and stores?   Do you have a version that does not do all the aliasing?  The compiler does make an effort to combine multiple smaller load/store into fewer large ones.

---

### 评论 #4 — 949f45ac (2018-10-04T16:30:08Z)

What aliasing are you referring to, exactly?
I am casting the `uint64_t * long_state_64` to `ulonglong2 * long_state` to get wider loads and stores, that is correct. (All that initialization stuff before the loop is a bit untidy I admit, since I just hacked on it until it worked.)
And you mean I should try using the normal `long_state_64` pointer and doing 2 loads/stores everywhere, see if that works out correctly? I can do that.
But I can tell you that I already tried casting the pointer back to 64-bit and storing both halfes (`d_xored.x` and `d_xored.y`) separately: The compiler STILL swallowed one store. Even when I stored `fork_7` (which is a `uint64_t` already, instead of one half of a `ulonglong2`) directly instead of assigning back into `d_xored.y`.

---

### 评论 #5 — b-sumner (2018-10-04T16:33:56Z)

Lines 285-288 in the github code linked to above.

---

### 评论 #6 — 949f45ac (2018-10-04T16:48:04Z)

Yes, well, I got the wide vars for loading/storing and then I extract the 32-bit parts by casting to 32-bit pointers.
All the vars are inside 32-bit VGPRs anyway. So this should just access these individual registers directly.

---

### 评论 #7 — b-sumner (2018-10-04T16:53:18Z)

Those aliases may be doing more harm than good.  Can you try using ordinary 32 bit variables?

---

### 评论 #8 — 949f45ac (2018-12-04T09:06:06Z)

Thanks @b-sumner! Indeed it works without the aliasing. I also realised that the aliasing was pretty pointless in this case.

If anyone cares, here’s how I do it now: https://github.com/949f45ac/xmrig-HIP/blob/390dce6bdbbf17d799c202d1c1be9af2a17017e2/src/nvidia/cuda_core.cu#L564

---
