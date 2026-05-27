# Codegen: missed optimization: v_bfe

> **Issue #989**
> **状态**: closed
> **创建时间**: 2020-01-02T09:51:13Z
> **更新时间**: 2023-12-18T15:47:40Z
> **关闭时间**: 2023-12-18T15:47:39Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/989

## 描述

Using ROCm 2.10, RadeonVII, OpenCL
```
int lowBits(int u, unsigned bits) { return ((u << (32 - bits)) >> (32 - bits)); }
```

Is compiled to
```
        v_sub_u32_e32 v3, 0, v3
	v_and_b32_e32 v3, 31, v3
	v_lshlrev_b32_e32 v2, v3, v2
	v_ashrrev_i32_e32 v2, v3, v2
```

While it could be compiled to a single fast instruction:
```
	v_bfe_i32 v2, v2, 0, v3
```

There should be a way to get the compiler to use the v_bfe without having to use assembly.


---

## 评论 (10 条)

### 评论 #1 — b-sumner (2020-01-02T16:09:52Z)

There are multiple ways to avoid assembly.

Use the amd_bfe() function from the OpenCL cl_amd_media_ops2 extension.

Use the __builtin_amdgcn_ubfe() clang builtin.

---

### 评论 #2 — b-sumner (2020-01-02T16:30:59Z)

Also, we're going to look into why we're missing this in the first place.

---

### 评论 #3 — preda (2020-01-04T22:50:36Z)

Thank you! it's good to know about the alternatives to __asm(), but neither amd_bfe() or __builtin_amdgcn_ubfe() are OpenCL-portable. Ideally we'd like a pure-C (OpenCL) solution that is compiled optimized by clang targeting GCN, but is also portable e.g. to OpenCL on Nvidia GPUs.

The "pure C" candidate I see for low-bits is ((word32 << (32 - bits)) >> (32 - bits)), or for bits between n and m: (words32 << (32 - m)) >> (32 - n); hopefully the optimizer will be able to mach such expressions to BFE.

As you're tracking this optimization, feel free to close this issue if you prefer.


---

### 评论 #4 — b-sumner (2020-01-05T17:42:45Z)

Understood.

FWIW, it is "portable" to use preprocessor symbols to guard code for a given platform or extension, e.g. in this case you could use #ifdef cl_amd_media_ops2 to guard use of amd_bfe.

---

### 评论 #5 — preda (2020-01-07T10:34:17Z)

> FWIW, it is "portable" to use preprocessor symbols to guard code for a given platform or extension, e.g. in this case you could use #ifdef cl_amd_media_ops2 to guard use of amd_bfe.

Yes #ifdef is fine; portable without #ifdef is even better.

In gpuowl we do use __asm() when targeting GCN, can't do without as the performance gradient to naive ROCm OpenCL is too important unfortunately. In order to have the code also compile on CUDA OpenCL we do use #ifdefs indeed. (it is unfortunate that there is not an #if guard for detecting whether __asm() is supported, so we had to make up an approximation; but that's another story)

---

### 评论 #6 — preda (2020-03-17T10:04:33Z)

Another real life example (ROCm 3.1):
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

It seems as if the compiler is not aware of the existence of this instruction (v_bfi_b32) otherwise it makes no sense why it wouldn't use it.


---

### 评论 #7 — b-sumner (2020-03-17T15:04:59Z)

v_bfi_b32 computes

    (src1 & src0) | (src2 & ~src0)

thus the HAS_ASM code is producing

    (u & mask) | (bits & ~mask)

Maybe you know that (bits & ~mask) == bits, but the compiler probably doesn't.

Also, FWIW, GFX10 adds a v_and_or_b32 which should be generated for this function.

---

### 评论 #8 — preda (2020-03-19T03:45:14Z)

@b-sumner Thank you for the correction. I tried to write the correct equivalent to v_bfi_b32 in C, but it is still compiled to a pair of v_and_b32_e32 + v_or_b32_e32 instead of a single v_bfi_b32
```
u32 bfi(u32 u, u32 mask, u32 bits) {
#if HAS_ASM
  u32 out;
  __asm("v_bfi_b32 %0, %1, %2, %3" : "=v"(out) : "v"(mask), "v"(u), "v"(bits));
  return out;
#else
  return (u & mask) | (bits & ~mask);
  // return (u & mask) | bits;
#endif
}
```
Do you think the compiler ever generates v_bfi_b32 (i.e. other than by way of __asm())? if so, in what situation?


---

### 评论 #9 — nartmada (2023-12-14T02:31:49Z)

Hi @preda, please close the ticket if this is no longer an issue for you.  Thanks.

---

### 评论 #10 — nartmada (2023-12-18T15:47:39Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
