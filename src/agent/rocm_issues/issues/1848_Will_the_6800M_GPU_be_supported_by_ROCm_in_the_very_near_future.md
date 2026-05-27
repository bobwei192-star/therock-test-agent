# Will the 6800M GPU be supported by ROCm in the very near future?

> **Issue #1848**
> **状态**: closed
> **创建时间**: 2022-10-31T09:57:55Z
> **更新时间**: 2024-04-21T15:59:41Z
> **关闭时间**: 2024-04-21T15:59:41Z
> **作者**: greymogh
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1848

## 描述

Hello,

I just got an Advantage Edition laptop (full AMD) with an amd 6800M.

To my surprise I couldn't get hip and rocm to work.

Should this gpu be supported in the very near future? Otherwise very honestly I would have to return this machine which is useless to me and rather expensive.

Thank you in advance for your answers.

---

## 评论 (5 条)

### 评论 #1 — saadrahim (2022-10-31T16:00:59Z)

There are no announced plans to support 6800M for ROCm software packages. Some packages may work but no functionality is officially supported by AMD on that GPU.

---

### 评论 #2 — danielzgtg (2022-11-06T01:20:05Z)

@greymogh Does the `HSA_OVERRIDE_GFX_VERSION=10.3.0` hack, which is mentioned all over the place, work for you?

---

### 评论 #3 — greymogh (2022-11-19T13:13:23Z)

> @greymogh Does the `HSA_OVERRIDE_GFX_VERSION=10.3.0` hack, which is mentioned all over the place, work for you?

Thanks for your answer, It wasn't working first but I tried again after your post and it's working now, so thanks again. I think I just had to reboot...

---

### 评论 #4 — greymogh (2022-11-19T13:14:22Z)

> There are no announced plans to support 6800M for ROCm software packages. Some packages may work but no functionality is officially supported by AMD on that GPU.

It's a bad news, but thanks for answering.

---

### 评论 #5 — nartmada (2024-04-21T15:59:41Z)

Closing this ticket as @greymogh's question has been answered.  Thanks.

---
