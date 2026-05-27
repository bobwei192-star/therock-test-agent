# Performance: compiler not generating V_MAD_U64_U32

> **Issue #238**
> **状态**: closed
> **创建时间**: 2017-10-26T23:44:22Z
> **更新时间**: 2019-06-03T10:05:22Z
> **关闭时间**: 2018-06-03T15:14:52Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/238

## 描述

ROCm 1.6-180, Ubuntu 16.04, R9-Nano.

I prepared a small kernel which should be the ideal case for V_MAD_U64_U32:
```
KERNEL(256) test(global ulong *io) {
  uint p = get_global_id(0);
  ulong ab = io[p];
  uint a = ab >> 32;
  uint b = ab & 0xffffffff; 
  io[p] = ab + ((ulong ) a) * b;
}
```

Yet what is generated is:
```
	v_mul_lo_u32 v4, v3, v2                                    // 000000023054: D2850004 D2850004
	v_mul_hi_u32 v5, v3, v2                                    // 00000002305C: D2860005 D2860005
	v_add_i32_e32 v2, vcc, v2, v4                              // 000000023064: 32040902
	v_addc_u32_e32 v3, vcc, v5, v3, vcc
```

The generated code is inefficient. Apparently the code generator is not aware of the (powerful) instruction V_MAD_U64_U32. This is penalizing large integer arithmetic.


---

## 评论 (4 条)

### 评论 #1 — gstoner (2017-10-30T17:12:09Z)

Team looked at and already have fix underway it in the process of being up streamed in the LLVM base 

---

### 评论 #2 — preda (2017-11-08T12:50:57Z)

Thanks! how can I test the fix? is there a way to get the updated ROCM, or can I update only the compiler myself?

---

### 评论 #3 — psteinb (2017-11-08T13:00:01Z)

if this fix is upstreamed to LLVM, what was the issue? (just curious)


---

### 评论 #4 — TCS-SK (2019-06-03T10:05:22Z)

Hi  gstoner /team ,

I am facing the similar kind of issue, I would like to know the solution for below issue.
Issue:  compiler not generating V_MAD_U64_U32 #238

Thank you



---
