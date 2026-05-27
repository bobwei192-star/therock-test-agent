# Q: is it safe to "apt upgrade" on a system with ROCm 1.6?

> **Issue #315**
> **状态**: closed
> **创建时间**: 2018-01-29T05:33:56Z
> **更新时间**: 2018-01-29T10:04:55Z
> **关闭时间**: 2018-01-29T10:04:55Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/315

## 描述

I have a Ubuntu 16.04.3 system with ROCm 1.6. I do not intend to upgrade to 1.7 yet on this system.

If I do an "sudo apt upgrade" on this system (as I usually do periodically to update the various packages), would the system still work afterwards?

Specifically, I want a confirmation that the "apt upgrade" on top of ROCm 1.6 is handled correctly and does not break things by doing a half-way transition to 1.7.


---

## 评论 (1 条)

### 评论 #1 — preda (2018-01-29T10:04:18Z)

I tried it: "apt upgrade" on a Ubuntu 16.04.3 with ROCm 1.6, and it didn't work.

What is done is done, but may I suggest that in the future it would be nice to avoid this kind of breakage.

---
