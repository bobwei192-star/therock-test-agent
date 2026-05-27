# Rocm compiler -- improper warning

> **Issue #1076**
> **状态**: closed
> **创建时间**: 2020-04-07T20:13:48Z
> **更新时间**: 2021-06-02T12:00:25Z
> **关闭时间**: 2021-06-02T12:00:11Z
> **作者**: gwoltman
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1076

## 描述

Using rocm 3.1.

MIDDLE is a passed to the compiler using -D, as in -DMIDDLE=10
I assume the compiler would also barf if I used "#define MIDDLE 10"

Rocm is complaining about valid C code (messages at end of this message):

length = (MIDDLE <= 12 || MIDDLE == 15) ? 1 : 2;
and
if ((MIDDLE >= 6 && MIDDLE <= 8) || (MIDDLE >= 11 && MIDDLE <= 13) ...

It also seems that after warning several times, the compiler aborts.

/tmp/comgr-01e5ad/input/CompileSource:1663:24: warning: use of logical '||' with constant operand
length = (MIDDLE <= 12 || MIDDLE == 15) ? 1 : 2;
                       ^  ~~~~~~~~~~~~
/tmp/comgr-01e5ad/input/CompileSource:1663:24: note: use '|' for a bitwise operation
length = (MIDDLE <= 12 || MIDDLE == 15) ? 1 : 2;
                       ^~
                       |
/tmp/comgr-01e5ad/input/CompileSource:1834:18: warning: use of logical '&&' with constant operand
if ((MIDDLE >= 6 && MIDDLE <= 8) || (MIDDLE >= 11 && MIDDLE <= 13) {
                 ^  ~~~~~~~~~~~
/tmp/comgr-01e5ad/input/CompileSource:1834:18: note: use '&' for a bitwise operation
if ((MIDDLE >= 6 && MIDDLE <= 8) || (MIDDLE >= 11 && MIDDLE <= 13) {
                 ^~
                 &


---

## 评论 (3 条)

### 评论 #1 — gwoltman (2020-04-07T20:19:58Z)

Correction:  The compiler aborting after several warnings was something else (mismatched paren).

---

### 评论 #2 — ROCmSupport (2021-03-17T08:13:35Z)

Thanks @gwoltman for reaching out.
Can you please verify with ROCm 4.0 and share an update asap for moving this ticket to next level in a faster manner.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-06-02T12:00:11Z)

Closing this as there is no response from the user for more than a month.
Thank you.

---
