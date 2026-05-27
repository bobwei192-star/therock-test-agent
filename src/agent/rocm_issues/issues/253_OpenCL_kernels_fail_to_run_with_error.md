# OpenCL:  kernels fail to run with error

> **Issue #253**
> **状态**: closed
> **创建时间**: 2017-11-13T13:51:54Z
> **更新时间**: 2018-02-20T01:48:50Z
> **关闭时间**: 2018-02-16T02:30:13Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/253

## 描述

     Memory access fault by GPU node-1 on address 0x916dd3000. Reason: Page not present or supervisor privilege.

I have two sequences of kernels,  the first sequence works fine, and the second gives this error.

I am running the latest package of ROCm. Hardware is an RX 470 on Asus Z170-K mobo.

---

## 评论 (8 条)

### 评论 #1 — preda (2017-11-14T06:16:02Z)

The first suspect is a genuine illegal memory access in your kernel. Can you post the source of the kernels, or a repro case? Or, why do you think it's something else?

---

### 评论 #2 — boxerab (2017-11-15T12:01:48Z)

Thanks. I think it is a compiler bug. I reduced the kernel to a minimal case, and the error could be turned on or off with small changes to the code.  If it is not fixed in 1.7, I will put together a reproducer. 

---

### 评论 #3 — boxerab (2017-12-20T19:05:07Z)

Still broken with 1.7

---

### 评论 #4 — boxerab (2018-02-16T02:30:13Z)

I have submitted a reproducer for this one.

---

### 评论 #5 — arsenm (2018-02-19T22:10:30Z)

The code here seems to be trying to rely on the order of evaluation of the select function to do avoid an out of bounds access. Since select is a function call, all of the arguments are evaluated before the function. Additionally the order of evaluation of arguments to a function is undefined in C. In any case, the select can't be used to avoid the out of bounds access. If you rewrite this with if/then or the ternary operator which do have short circuiting behavior it should do what is expected.

---

### 评论 #6 — preda (2018-02-19T22:22:55Z)

Where can one see "the code here"? (where is the reproducer)

---

### 评论 #7 — jlgreathouse (2018-02-20T00:53:25Z)

@preda: @boxerab submitted a reproducer to AMD. I don't think we can share it on GitHub without his permission.

That said, @boxerab, if you would like, I can send you an updated copy of your reproducer that uses ternary (a ? b : c) statements in the kernel instead of select(c, b, a) statements. It prevents the crashes, as suggested by arsenm.

---

### 评论 #8 — preda (2018-02-20T01:48:50Z)

No, that's fine. I understand that if the code has some reason for confidentiality, it should not be public here, that's fine.

It also sounds that you nailed the cause.

---
