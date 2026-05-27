# A clean install of rocm-opencl on debian unstable does not work because of missing libtinfo5

> **Issue #1477**
> **状态**: closed
> **创建时间**: 2021-05-20T03:20:26Z
> **更新时间**: 2021-11-16T10:11:24Z
> **关闭时间**: 2021-11-16T10:11:24Z
> **作者**: dreifachstein
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1477

## 描述

libamd_comgr.so depends on libtinfo.so.5 but the package "comgr" does not list "libtinfo5" as a dependency. 

---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2021-06-01T11:03:25Z)

Thanks @dreifachstein for reaching out.
We are already aware of this issue and team is working on the fix.
I will share an update once is merged into release branch.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-11-16T10:11:24Z)

Hi @dreifachstein 
Good news, the fix is integrated into 4.5 and so request to check with 4.5.
We verified locally and issue is no more noe.
Thank you.

---
