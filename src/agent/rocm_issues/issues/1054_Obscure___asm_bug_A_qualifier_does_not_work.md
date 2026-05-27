# Obscure __asm bug:  "A" qualifier does not work

> **Issue #1054**
> **状态**: closed
> **创建时间**: 2020-03-20T04:56:56Z
> **更新时间**: 2021-04-05T10:19:53Z
> **关闭时间**: 2021-04-05T10:19:53Z
> **作者**: gwoltman
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1054

## 描述

__asm("v_bfe_u32 %0, %1, %2, 1" : "=v" (b1) : "v" (b2), "A" (i));

where b1 and b2 are variables and "i" is a constant, generates this error:

error: invalid input constraint 'A' in asm

The "A" constraint means a constant in the -16 to 64 range according to https://gcc.gnu.org/onlinedocs/gcc/Machine-Constraints.html#Machine-Constraints


---

## 评论 (2 条)

### 评论 #1 — arsenm (2020-05-26T15:06:03Z)

Support for the A modifier added here: https://reviews.llvm.org/rGb087b91c917087bc53d47282a16ee4af78bfe286

A lot of these other constraints GCC apparently has are still missing though.

---

### 评论 #2 — ROCmSupport (2021-04-05T10:19:53Z)

Thanks @gwoltman for reaching out.
As per the update from our dev(@arsenm), I am closing this ticket now.
Feel free to open a new issue, if any, for quick resolution.
Thank you.

---
