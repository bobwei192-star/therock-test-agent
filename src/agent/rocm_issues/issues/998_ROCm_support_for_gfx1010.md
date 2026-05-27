# ROCm support for gfx1010?

> **Issue #998**
> **状态**: closed
> **创建时间**: 2020-01-14T08:29:16Z
> **更新时间**: 2020-01-21T23:38:23Z
> **关闭时间**: 2020-01-16T11:18:24Z
> **作者**: kalaluthien
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/998

## 描述

Is ROCm v3.0 fully support gfx1010? Especially `tensorflow-rocm` (tf2.0).

---

## 评论 (4 条)

### 评论 #1 — omerferhatt (2020-01-14T15:16:14Z)

#819 You can check it from "Supported Hardwares" on documentation. For now you can use ROCM like graphic driver, not for computational operations. tensorflow-rocm still don't have any support for gfx1010 (navi) based cards.

---

### 评论 #2 — kalaluthien (2020-01-16T11:18:24Z)

Thanks for your reply!

---

### 评论 #3 — mritunjaymusale (2020-01-17T11:09:26Z)

Agreed, I have a 5700xt and I pulled the pytorch docker image and it didn't run the examples 

---

### 评论 #4 — Rmalavally (2020-01-21T23:38:23Z)

Refer the "Hardware and Software Support" section in ROCm Release Notes or documentation. For now, you can use the ROCm-like graphic driver, however, not for computational operations. Tensorflow-rocm does not support gfx1010 (navi)-based cards.

---
