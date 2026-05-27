# Centos 7.9 based on kernel 5.4 shows no message about amdkfd 

> **Issue #1415**
> **状态**: closed
> **创建时间**: 2021-03-22T07:22:55Z
> **更新时间**: 2021-03-22T09:46:13Z
> **关闭时间**: 2021-03-22T09:43:05Z
> **作者**: Biu-G
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1415

## 描述

my amdgpu module boots greatly, while there isn't any message about amdkfd in dmesg. Which leads to rocminfo shows "Unable to open /dev/kfd read-write: No such file or directory". Don't know how to continue.

---

## 评论 (3 条)

### 评论 #1 — Biu-G (2021-03-22T07:23:05Z)

Linux localhost.localdomain 5.4.105-1.el7.elrepo.x86_64 #1 SMP Thu Mar 11 08:28:06 EST 2021 x86_64 x86_64 x86_64 GNU/Linux

---

### 评论 #2 — ROCmSupport (2021-03-22T09:43:05Z)

Hi @Biu-G 
Thanks for reaching out.
As per our ROCm documentation, ROCm 4.0 validated and supports 3.10.0-x kernel officially for CentOS 7.9.
Request you to follow our docs: [https://github.com/RadeonOpenCompute/ROCm#list-of-supported-operating-systems](url)
Hope it clarifies.
Thank you.
 

---

### 评论 #3 — ROCmSupport (2021-03-22T09:44:46Z)

ROCm 4.1 is going to be released very soon and request you to try with ROCm 4.1 once.
Thank you.

---
