# NOTICE NOTICE NOTICE NOTICE

> **Issue #790**
> **状态**: closed
> **创建时间**: 2019-05-08T10:40:04Z
> **更新时间**: 2019-05-08T11:17:56Z
> **关闭时间**: 2019-05-08T11:17:56Z
> **作者**: Moading
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/790

## 描述

Hi,
after installing ROCm 2.4 the message below appears in the output of dmesg:

[   32.164728] **********************************************************
[   32.164729] **   NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE   **
[   32.164730] **                                                      **
[   32.164731] ** trace_printk() being used. Allocating extra memory.  **
[   32.164731] **                                                      **
[   32.164732] ** This means that this is a DEBUG kernel and it is     **
[   32.164733] ** unsafe for production use.                           **
[   32.164734] **                                                      **
[   32.164735] ** If you see this message and you are not debugging    **
[   32.164735] ** the kernel, report this immediately to your vendor!  **
[   32.164736] **                                                      **
[   32.164737] **   NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE NOTICE   **
[   32.164738] **********************************************************

---

## 评论 (3 条)

### 评论 #1 — Moading (2019-05-08T10:40:48Z)

first to see this :)

---

### 评论 #2 — thesleort (2019-05-08T10:55:02Z)

You sure this is related to ROCm? My dmesg is not saying this with 2.4. Just did a reboot to check again, when I saw your issue.

---

### 评论 #3 — Moading (2019-05-08T11:17:53Z)

You are right, it was something else, sorry for the confusion.

---
