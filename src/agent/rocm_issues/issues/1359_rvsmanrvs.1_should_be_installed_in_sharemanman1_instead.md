# rvs/man/rvs.1 should be installed in share/man/man1/ instead

> **Issue #1359**
> **状态**: closed
> **创建时间**: 2021-01-12T15:11:35Z
> **更新时间**: 2021-05-07T10:06:04Z
> **关闭时间**: 2021-05-07T10:05:09Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1359

## 描述

I believe this file

`/opt/rocm-4.0.0/rvs/man/rvs.1`

should be installed here instead:

`/opt/rocm-4.0.0/share/man/man1/rvs.1`

(And `/opt/rocm-4.0.0/rvs/man` directory removed).

`rocm-validation-suite4.0.0` 3.10.40000  on Debian / Ubuntu.

Regards,
Witold


---

## 评论 (5 条)

### 评论 #1 — ROCmSupport (2021-01-13T06:53:14Z)

Hi @baryluk ,
 
  Thank you for bringing this issue to our light. Request you to kindly let us know what is the problem you are facing for which you are giving this solution.


---

### 评论 #2 — baryluk (2021-01-13T09:40:36Z)

It is just a general packaging complain. When one sets up the paths in `/etc/manpath.config` or using `MANPATH` variable, it is better to set one canonical path, than two or three. It is more user friendly and more standards friendly.


---

### 评论 #3 — ROCmSupport (2021-01-28T06:39:59Z)

Go an update:
RVS team is going to incorporate the changes.
We will let you know once the changes are pushed, please stay tuned for the updates.
Thank you

---

### 评论 #4 — baryluk (2021-02-15T20:40:13Z)

Thanks. Appreciated.

---

### 评论 #5 — ROCmSupport (2021-05-07T10:05:09Z)

Hi @baryluk 
Good news. Issue is fixed and the changes are merged into ROCm 4.2 code.
Have verified internally and issue is fixed.

master@test:/opt/rocm-4.2.0/share/man/man1$ ls
rocgdb.1  rvs.1


---
