# This starts to be serious

> **Issue #1031**
> **状态**: closed
> **创建时间**: 2020-02-29T13:16:05Z
> **更新时间**: 2020-12-01T19:11:24Z
> **关闭时间**: 2020-12-01T18:00:22Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1031

## 描述

It seems there is lack of quality control on ROCm development.


---

## 评论 (12 条)

### 评论 #1 — valeriob01 (2020-02-29T13:24:47Z)

> It seems there is lack of quality control on ROCm development.

maybe you can explain your thumbs down where most applications fail to run.
I have been following ROCm from version 1.9, it has been a battle to keep my system running, with multiple downgrades after upgrades.


---

### 评论 #2 — nikAizuddin (2020-03-01T06:19:53Z)

> where most applications fail to run.

Hi @valeriob01  which applications that you failed to run?

---

### 评论 #3 — valeriob01 (2020-03-01T06:40:42Z)

> > where most applications fail to run.
> 
> Hi @valeriob01 which applications that you failed to run?

gpuowl

---

### 评论 #4 — preda (2020-03-01T12:13:18Z)

I propose to close this issue, as there is a separate one tracking the concrete case.

I do appreaciate a lot the existence of the communication channel with AMD developers represented by this forum. I think both the internal team as well as us on the outside do wish to make ROCm better, and I imagine they may be operating under various constraints that are not readily visible to us on the outside.


---

### 评论 #5 — valeriob01 (2020-03-02T04:53:59Z)

Moved back to ROCm 2.10 again. Will not try to upgrade again until there is a clear statement that things work.

---

### 评论 #6 — stefan-reich (2020-03-02T21:34:20Z)

@valeriob01 Why 2.10 exactly? I am curious as to which version you recommend as installation of ROCm 3.1 on my Ryzen 5 2500U has apparently just failed.

---

### 评论 #7 — valeriob01 (2020-03-03T05:29:03Z)

> @valeriob01 Why 2.10 exactly? I am curious as to which version you recommend as installation of ROCm 3.1 on my Ryzen 5 2500U has apparently just failed.

2.10 is the last working version.
Other people have upgraded and moved back again, on different systems than my system, thus there is an evident problem with 3.1

---

### 评论 #8 — stefan-reich (2020-03-03T11:25:12Z)

I installed 2.10.14 as in #284, but clinfo still segfaults. It didn't compile anything this time, maybe it's still having some 3.1 files around?

---

### 评论 #9 — valeriob01 (2020-03-03T12:22:24Z)

> I installed 2.10.14 as in #284, but clinfo still segfaults. It didn't compile anything this time, maybe it's still having some 3.1 files around?

Rarely I do a rollback, more often I do a fresh install and it works all the times.


---

### 评论 #10 — valeriob01 (2020-03-10T14:12:22Z)

> I propose to close this issue, as there is a separate one tracking the concrete case.
> 
> I do appreaciate a lot the existence of the communication channel with AMD developers represented by this forum. I think both the internal team as well as us on the outside do wish to make ROCm better, and I imagine they may be operating under various constraints that are not readily visible to us on the outside.

apparently pestering here about quality has effects:
https://www.phoronix.com/scan.php?page=news_item&px=AMD-Linux-Hire-Lead-Kernel-Dev


---

### 评论 #11 — jlgreathouse (2020-12-01T18:00:22Z)

I'm sorry to hear about the issues you had during the upgrade cycle that was going on at the time. Hopefully things have improved in recent releases. If not, I hope that you will submit focused reports on the exact issues so that we can trace them down and fix them. Thank you!

---

### 评论 #12 — valeriob01 (2020-12-01T19:11:24Z)

Since then I moved to Ubuntu and solved the issue.


---
