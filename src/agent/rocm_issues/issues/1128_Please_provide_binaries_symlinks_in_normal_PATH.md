# Please provide binaries symlinks in normal PATH

> **Issue #1128**
> **状态**: closed
> **创建时间**: 2020-06-04T13:52:54Z
> **更新时间**: 2022-02-08T10:52:52Z
> **关闭时间**: 2022-02-08T10:52:52Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1128

## 描述

Please provide versioned symlinks to `/opt/rocm-V/bin/X` in `/usr/bin/X-V` owned by packages, and also provide a relatrive symlink from `/usr/bin/X` to `/usr/bin/X-V`  managed using `update-alternatives(1)` ( https://manpages.debian.org/buster/dpkg/update-alternatives.1.en.html ) mechanism. https://wiki.debian.org/DebianAlternatives 

It is a real pain to use rocm right now.

---

## 评论 (5 条)

### 评论 #1 — icarus-sparry (2020-06-11T16:48:50Z)

We are looking into what is involved with doing this (i.e. no commitment) for 3.7.

---

### 评论 #2 — ROCmSupport (2021-06-03T08:36:07Z)

Hi @baryluk 
Most likely it will be fixed in 4.3.
I will keep you posted.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-08-04T10:00:18Z)

Hi @baryluk 
ROCm 4.3 released.
Can you please verify and confirm.
Thank you.

---

### 评论 #4 — baryluk (2021-08-08T12:57:03Z)

No change in ROCm 4.3. Same.

---

### 评论 #5 — ROCmSupport (2022-02-08T10:35:53Z)

Hi @baryluk 
Good news.
We have done many changes in the latest builds w.r.to packaging, I have verified just now with the internal 5.0 builds and issue is resolved now.
So you can check with the 5.0 builds(which will be released in very few days)

For example:
iamauser@B550M-AORUS-PRO-P:/usr/bin$ rocm <tab>
rocm_agent_enumerator  rocminfo  rocm-smi


---
