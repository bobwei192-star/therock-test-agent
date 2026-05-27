# Suspected optimizer error

> **Issue #1096**
> **状态**: closed
> **创建时间**: 2020-05-03T17:45:53Z
> **更新时间**: 2020-05-07T03:07:56Z
> **关闭时间**: 2020-05-07T03:07:55Z
> **作者**: gwoltman
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1096

## 描述

To enable using OMOD mul:2, I have these asm instructions near the start of my kernel.
    __asm("s_setreg_imm32_b32 hwreg(HW_REG_MODE, 9, 1), 0");
    __asm("s_setreg_imm32_b32 hwreg(HW_REG_MODE, 4, 4), 7");
In looking at disassembly, the optimizer is happily moving floating point ops ahead of these instructions (presumably to hide memory load latency).  

Fortunately, my OMOD instructions are a little further down and I have not been affected by this potential problem.

---

## 评论 (4 条)

### 评论 #1 — seesturm (2020-05-03T18:07:37Z)

Did you try using "volatile" qualifier for asm statement?

---

### 评论 #2 — gwoltman (2020-05-04T00:25:30Z)

I had forgotten that it is my responsibility to put volatile in to prevent this.  Thanks for jogging my memory.

Nonetheless, adding volatile after __asm does not affect the generated code.  Thus, the bug report is still valid.

---

### 评论 #3 — gwoltman (2020-05-04T00:25:51Z)

BTW, I am using rocm 3.3

---

### 评论 #4 — gwoltman (2020-05-07T03:07:55Z)

More discussion of this problem here:
https://github.com/RadeonOpenCompute/ROCm/issues/1098

---
