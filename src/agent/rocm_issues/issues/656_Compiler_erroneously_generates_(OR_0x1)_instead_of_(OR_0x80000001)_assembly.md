# Compiler erroneously generates (OR 0x1) instead of (OR 0x80000001) assembly

> **Issue #656**
> **状态**: closed
> **创建时间**: 2019-01-02T08:54:56Z
> **更新时间**: 2019-01-25T23:28:55Z
> **关闭时间**: 2019-01-25T23:28:55Z
> **作者**: 949f45ac
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/656

## 描述

Consider the following line: https://github.com/949f45ac/xmrig-HIP/blob/476c50d7aa449bee8cef77168d5f3b9a121a10c1/src/nvidia/fast_int_math_v2.hpp#L79

If I use either `__uint2float_rn(a & 0xFF)` or `(float)(a & 0xFF)` here, the compiler will generate a `v_cvt_f32_ubyte0_e32` instruction. Seems fair enough – however, it produces incorrect results.
Somehow if I force the same instruction without `_e32`, it works. Another solution is to just use `V_CVT_F32_U32_E32` and pass in `(a & 0xFF)` already calculated.

If I compile for an NVidia card, I get correct results with `__uint2float_rn`, so I think that this function should be the correct one to use in this case, and the ROCm/HIP implementation slightly off.
Tried on both gfx900 and gfx803.

Cheers!

---

## 评论 (8 条)

### 评论 #1 — b-sumner (2019-01-02T14:59:54Z)

Thanks, we'll take a look.

---

### 评论 #2 — b-sumner (2019-01-02T18:05:08Z)

Would it be possible to provide a reduced test case?  Or does the problem only show up in the full code?

---

### 评论 #3 — 949f45ac (2019-01-02T18:12:03Z)

Is it a problem to compile the whole project? I haven’t tested whether the problem shows up in reduced cases.
Maybe I can paste a bit more of the ISA that is generated in the bugged case so you can get a better understanding of what the compiler might be doing?

---

### 评论 #4 — b-sumner (2019-01-02T18:29:38Z)

We certainly appreciate the fact that you were have narrowed things down.  But from a compiler perspective, we're not familiar with the project or the code, and it is not small.  If you could provide us with a simple example in, e.g. a single source file that we can build with a simple hipcc command, then we can focus on actual problem much more quickly.

---

### 评论 #5 — preda (2019-01-03T10:38:15Z)

@949f45ac were you able to identify the problem in the generated ISA? e.g. by comparing the "good" ISA with the bad case? That may help the compiler team find the cause.

About with/without _e32 seems a red-herring to me. Did you try asm ("V_CVT_F32_UBYTE0_e32 %0, %1" : "=v"(a_lo) : "v"(a)); -- I expect it would be not affected by the _e32.

---

### 评论 #6 — 949f45ac (2019-01-03T12:04:45Z)

Aah, you are right, of course: It still works when I add `_e32`.
What actually changes is that for this line: https://github.com/949f45ac/xmrig-HIP/blob/476c50d7aa449bee8cef77168d5f3b9a121a10c1/src/nvidia/phase2.cu#L582 (`din` is the variable that ends up as argument `a` inside the function)
The compiler starts issuing
`v_or_b32_e32 v14, 1, v14`
instead of
`v_or_b32_e32 v14, 0x80000001, v14`

Apparently it reasons that the high-order bits are irrelevant?

Here’s the full context, for comparison:
incorrect:
```asm
	v_add_u32_e32 v14, v16, v62
        v_or_b32_e32 v14, 1, v14
        v_lshrrev_b32_e32 v49, 8, v14
        v_add_u32_e32 v49, 0x4e800000, v49
        v_rcp_f32_e32 v51, v49
        v_cvt_f32_ubyte0_e32 v50, v14
        v_sub_u32_e32 v53, 0, v14
        v_fma_f32 v49, v49, v51, -1.0
        v_add_u32_e32 v52, 0x20000000, v51
        v_fma_f32 v49, v50, v51, v49
        v_mul_f32_e32 v49, v49, v52
        v_rndne_f32_e32 v49, v49
        v_cvt_i32_f32_e32 v49, v49
        v_lshlrev_b32_e32 v54, 9, v51
	v_sub_u32_e32 v49, v54, v49
        v_mul_hi_u32 v51, v18, v49
        v_mad_u64_u32 v[49:50], s[0:1], v19, v49, v[18:19]
        v_add_co_u32_e32 v49, vcc, v49, v51
        v_addc_co_u32_e32 v50, vcc, v50, v61, vcc
```
correct:
```asm
        v_add_u32_e32 v14, v16, v62
        v_or_b32_e32 v14, 0x80000001, v14
        v_lshrrev_b32_e32 v49, 8, v14
        v_add_u32_e32 v49, 0x4e800000, v49
        v_rcp_f32_e32 v51, v49
        ;;#ASMSTART
        V_CVT_F32_UBYTE0_E32 v50, v14
        ;;#ASMEND
        v_sub_u32_e32 v53, 0, v14
        v_fma_f32 v49, v49, v51, -1.0
        v_add_u32_e32 v52, 0x20000000, v51
        v_fma_f32 v49, v50, v51, v49
        v_mul_f32_e32 v49, v49, v52
        v_rndne_f32_e32 v49, v49
        v_cvt_i32_f32_e32 v49, v49
        v_lshlrev_b32_e32 v54, 9, v51
        v_sub_u32_e32 v49, v54, v49
        v_mul_hi_u32 v51, v18, v49
        v_mad_u64_u32 v[49:50], s[0:1], v19, v49, v[18:19]
        v_add_co_u32_e32 v49, vcc, v49, v51
        v_addc_co_u32_e32 v50, vcc, v50, v61, vcc
```

Interestingly, as I said, I can also circumvent the problem with
`asm ("V_CVT_F32_U32_E32 %0, %1" : "=v"(a_lo) : "v"(a & 0xFF));`
over
`__uint2float_rn(a & 0xFF)`
even though in both cases the compiler should be able to deduct the same information about which parts of `a` are being used.

---

### 评论 #7 — b-sumner (2019-01-03T19:25:53Z)

Thanks for looking further into this.    We wrote a tiny test case that simply calls get_reciprocal() with 0x80000001 OR'd to an input and see the same problem.  Or releases are rather behind the tip of the compiler, so you will need to use your workaround for a while.

---

### 评论 #8 — b-sumner (2019-01-25T23:28:55Z)

The fix went into LLVM on January 8th and will be included in a future release.  Thanks again for reporting this.

---
