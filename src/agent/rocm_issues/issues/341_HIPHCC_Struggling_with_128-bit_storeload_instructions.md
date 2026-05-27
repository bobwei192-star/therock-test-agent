# HIP/HCC: Struggling with 128-bit store/load instructions

> **Issue #341**
> **状态**: closed
> **创建时间**: 2018-02-20T18:18:42Z
> **更新时间**: 2018-06-03T14:41:25Z
> **关闭时间**: 2018-06-03T14:41:25Z
> **作者**: 949f45ac
> **标签**: Compiler Functional Bug
> **URL**: https://github.com/ROCm/ROCm/issues/341

## 标签

- **Compiler Functional Bug** (颜色: #d847b6)

## 描述

I am struggling to utilize global/flat load/store **dwordx4** instructions via HIP / HCC under ROCm 1.7. The problems are as follows:

~~### 1. dwordx4 instructions are apparently not generated for (some?) HIP vector types
Without writing inline assembly, the obvious way to get the compiler to emit 128-bit memory instructions would be to use 128-bit wide types. This did not work for me with `ulonglong2` and I think neither with `uint4`. The only type that reliably gets dwordx4 ops is `__uint128_t`, which is *not portable to CUDA.*~~

### 2. Writing dwordx4 inline asm gives "invalid in/output constraint"
Even with `__uint128_t`, directly writing asm to do a 128-bit mem instructions (because you want to add glc/slc flags, maybe) does not work.
```cpp
__uint128_t dst;
asm volatile( "global_load_dwordx4 %0, %1, off glc slc" : "=v" (dst) : "r" (address) );
```
This code gives **error: couldn't allocate output register for constraint 'v'**. Same for the store instruction. The only way I’ve found to make this work is to explicitly move your 32-bit pieces into contiguous registers before the instruction, and then just use them explicitly, like this:
```cpp
uint32_t data[4];
fill_data(data);
asm volatile(
                "v_mov_b32 v27, %1\n\t"
                "v_mov_b32 v28, %2\n\t"
                "v_mov_b32 v29, %3\n\t"
                "v_mov_b32 v30, %4\n\t"
                "global_store_dwordx4 %0, v[27:30], off\n\t"
                :
                : "r" (address), "v" (data[0]), "v" (data[1]), "v" (data[2]), "v" (data[3])
                : "v27", "v28", "v29", "v30", "memory" );
```
Which is obviously pretty clunky and costs you registers.

### 3. (How) does the explicit register constraint work?
In the [LLVM Language Reference Manual](https://llvm.org/docs/LangRef.html) there is a small note about AMDGPU asm constraints.
>r: A 32 or 64-bit integer register.
>[0-9]v: The 32-bit VGPR register, number 0-9.
>[0-9]s: The 32-bit SGPR register, number 0-9.

I’ve tried to utilize it like this (to get around problem number 2), but to no avail:
```cpp
uint32_t data[4];
fill_data(data);
asm volatile(
                "global_store_dwordx4 %0, v[6:9], off\n\t"
                :
                : "r" (address), "6v" (data[0]), "7v" (data[1]), "8v" (data[2]), "9v" (data[3])
                : "memory" );
```
The error message is 
>invalid input constraint '6v' in asm
____
If you need more complete code samples in order to reproduce this, please let me know. :) 

---

## 评论 (9 条)

### 评论 #1 — scchan (2018-02-20T20:34:34Z)

hcc defines some short vector types in hc_short_vector.inl.
To use them, add `#include hc_short_vector_vector.hpp` and you declare a vector of 4 integers as

`hc::short_vector::int4 my_int4_vector;`

The load/store of this vector would leverage the dwordx4 mem ops.  
You could also take a look at this code example using short vector types: https://github.com/RadeonOpenCompute/hcc/blob/clang_tot_upgrade/tests/Unit/AmpShortVectors/hc_short_vector_device2.cpp



---

### 评论 #2 — 949f45ac (2018-02-21T10:11:34Z)

Thank you, but I am using HIP, not HCC directly. Hence this also lacks portability in a way, although of course I can just do a typedef depending on `#ifdef __HCC__`, using the native CUDA types (or HIP types) otherwise.

(As an aside: Why doesn’t HIP pull in the native HCC/CUDA types directly, rather than defining its own?)

I also get plenty of errors trying to `#include <hc_short_vector.hpp>` in my code right now. I think this is due to trying to include HCC headers side by side with HIP/hcc_detail headers.

---

### 评论 #3 — scchan (2018-02-22T18:12:11Z)

Another way to get around this is to create a type with the vector extension in llvm:

`// short vector type of 4 integers`
`typedef int myint4_t  __attribute__((ext_vector_type(4)));`

`myint4_t v1;`
`v1.x = 0;`

For the HIP related question, I'd suggest creating a new issue under HIP because that's the forum to discuss this kind of issues.
https://github.com/ROCm-Developer-Tools/HIP

---

### 评论 #4 — 949f45ac (2018-02-23T08:34:49Z)

Alright, thank you so far. I have rechecked and it actually seems like both uint4 and ulonglong2 yield a 128-bit load (now), so maybe I was plain wrong here or it was under certain conditions that I didn’t get what I wanted.

This still leaves the issue of not being able to use the 128-bit instructions in asm directly. (Works for neither `__uint128_t` (HCC type, as far as I understand) nor `ulonglong2` (HIP type).) `+glc` can be critical for performance sometimes, so it would be great to be able to use this, even if the four `v_mov` in the workaround don’t hurt all that bad.

The error still is `error: couldn't allocate output register for constraint 'v'` in code like this
```cpp
ulonglong2 * address;
ulonglong2 dst;
asm volatile( "global_load_dwordx4 %0, %1, off glc slc" : "=v" (dst) : "r" (address) );
```

---

### 评论 #5 — arsenm (2018-03-27T14:17:18Z)

What is the source where you aren't getting 128-bit loads? That is a more important problem. I'm guessing you're trying to access a flat pointer kernel argument

---

### 评论 #6 — 949f45ac (2018-03-27T15:39:58Z)

@arsenm I want to set `glc` / `slc` flags (as shown in the example) and afaik there is no way to do this without asm; correct me if I’m wrong.

As outlined in my latest comment before yours, I am otherwise getting the correct 128-bit load instructions generated now.

---

### 评论 #7 — arsenm (2018-03-27T15:55:53Z)

These are set for some atomic operations, and non temporal accesses from the IR. I'm not sure what the source looks like for hcc to use those

---

### 评论 #8 — 949f45ac (2018-03-27T16:49:30Z)

In my case `glc` improves performance (even if I have to issue 4 additional `v_mov_b32` to be able to use it) – semantically it is not needed. Hence there probably isn’t a specific way to write my code without asm and still get `glc` set in the eventual isa asm output.

Another use case for issuing load/store in asm is to fine-tune `s_waitcnt vmcnt(n)` calls. Without asm, the compiler will (always?) use `float_op_dwordx4` over `global_op_dwordx4` (maybe because it just can’t tell where the data is, or because it’s not been updated with these gfx900 opcodes, no idea) and then issue `s_waitcnt vmcnt(0) lgkmcnt(0)` , presumably according to the ISA guide which says:

>9.2.2. Importing Timing Consideration
>Since the data for a FLAT load can come from either LDS or the texture cache, and because
these units have different latencies, there is a potential race condition with respect to the
VM_CNT and LGKM_CNT counters. Because of this, the only sensible S_WAITCNT value to
use after FLAT instructions is zero.

However, if I *know* that none of my data is in LDS, I can call `global_load_…` and then `s_waitcnt vmcnt(n)` with n > 0 step-by-step, as I consume the data from loads I have issued, which is obviously faster than blocking until all memory ops have completed before consuming the first bit of loaded data.

---

### 评论 #9 — atamazov (2018-04-03T16:53:44Z)

\cc myself @atamazov

---
