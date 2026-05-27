# Dotted I errors in amdgpu-install if one has Turkish or Azerbaijani as the locale

> **Issue #1873**
> **状态**: closed
> **创建时间**: 2022-12-12T10:24:52Z
> **更新时间**: 2024-03-22T17:08:37Z
> **关闭时间**: 2024-02-02T22:58:01Z
> **作者**: erkinalp
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1873

## 描述

Steps to reproduce: 
Run `sudo amdgpu-install`

Expected:
Everything goes normally

Actual:
`/usr/bin/amdgpu-install: satır 436: ${USECASE_GRAPHİCS_PACKAGES[*]}: hatalı ikame`

---

## 评论 (3 条)

### 评论 #1 — abhimeda (2024-01-30T04:08:54Z)

@erkinalp Hi, is your issue resolved on the latest ROCm? If so can we close this ticket?

---

### 评论 #2 — nartmada (2024-02-02T22:58:01Z)

Closing the ticket as no response from @erkinalp.  Please re-open the ticket if you still have issue with latest ROCm 6.0.2.  Thanks.

---

### 评论 #3 — erkinalp (2024-03-22T17:08:36Z)

ROCm 6.x counterpart: https://github.com/ROCm/ROCm/issues/2888

---
