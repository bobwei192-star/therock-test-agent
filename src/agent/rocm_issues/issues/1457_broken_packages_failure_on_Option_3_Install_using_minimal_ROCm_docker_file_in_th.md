# "broken packages" failure on "Option 3: Install using minimal ROCm docker file" in the Rocmdocs site

> **Issue #1457**
> **状态**: closed
> **创建时间**: 2021-04-19T14:16:30Z
> **更新时间**: 2021-06-02T11:55:37Z
> **关闭时间**: 2021-06-02T11:55:37Z
> **作者**: AGenchev
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1457

## 描述

I'm performing step 3 of the manual: https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html#pytorch
and during command "`sudo docker build .`"
I get:
```
The following packages have unmet dependencies:
 rocm-dev : Depends: rocm-gdb but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```


---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-04-20T06:20:34Z)

Thanks @AGenchev for reaching out.
I am able to reproduce the problem.
I will share an update very soon.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-04-22T05:45:10Z)

Assigned to dev for modification of steps in the documentation.
I will update you once I receive.

---

### 评论 #3 — ROCmSupport (2021-05-31T10:55:14Z)

Got update:
Stpes updated @ https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html#pytorch 
Please review and update. Thank you.

---

### 评论 #4 — ROCmSupport (2021-06-02T11:55:37Z)

Issue resolved by updating the docs.
This ticket can be closed now.
Thank you.

---
