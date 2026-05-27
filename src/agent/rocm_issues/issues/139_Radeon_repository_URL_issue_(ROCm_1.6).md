# Radeon repository URL issue (ROCm 1.6)

> **Issue #139**
> **状态**: closed
> **创建时间**: 2017-06-30T17:27:45Z
> **更新时间**: 2017-06-30T17:35:07Z
> **关闭时间**: 2017-06-30T17:35:07Z
> **作者**: ekondis
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/139

## 描述

According to the documentation the repository URL is not correct. For instance, the GPG key in the wget command should be available at:

`http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key`

However, the actual URL seems to be:

`http://repo.radeon.com/rocm/apt/debian/debian/rocm.gpg.key`

So, one has to add the "debian/" suffix to all URLs for the commands to work.


---

## 评论 (2 条)

### 评论 #1 — jedwards-AMD (2017-06-30T17:33:19Z)

A symbolic link was causing an extra level of indirection. This has been corrected. The correct URL is:

 http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key 


---

### 评论 #2 — ekondis (2017-06-30T17:35:07Z)

Yes, it seems to be correct now.

---
