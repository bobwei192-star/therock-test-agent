# ROCm + Vulkan = hang on Vega FE

> **Issue #603**
> **状态**: closed
> **创建时间**: 2018-11-06T03:52:19Z
> **更新时间**: 2023-12-12T21:51:36Z
> **关闭时间**: 2023-12-12T21:51:35Z
> **作者**: TheGoddessInari
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/603

## 描述

It doesn't matter if AMDVLK or RADV is used with Vega FE, anything touching ROCm will cause sooner or later cause an unrecoverable hang if Vulkan is used at the same time.

This isn't observed with OpenGL or other facilities, only Vulkan that I can tell.

It doesn't occur if only ROCm or only Vulkan is used, but occurs frequently when the two are combined. Most reliably seen with Overwatch, but happens on anything that uses Vulkan, including native Linux games.

---

## 评论 (8 条)

### 评论 #1 — TheGoddessInari (2018-11-14T20:18:14Z)

As of latest `amd-staging-drm-next`, this is just freezing the GPUs (still can't switch to console or recover), and not the entire system as sysrq still works. It won't let me trigger a kernel crashdump when this occurs.

Does this need more information?

---

### 评论 #2 — boberfly (2018-11-14T21:47:50Z)

Hi @TheGoddessInari

I haven't tried them at the same time here yet but I can test easily (also running Vega FE).

---

### 评论 #3 — TheGoddessInari (2018-11-16T02:34:25Z)

@boberfly Would be nice if someone else could confirm. Sometimes it takes a while, sometimes it's instant. For me it's been happening on every DXVK game, and HITMAN for Linux very reliably.

I've mostly been using xmr-stak with ROCm, but it didn't seem to matter what was using ROCm to trigger it.

I've tried different kernels, different mesa versions and `amd-staging-drm-next` at different times, but nothing's resolved it so far. I don't know if there's someone I could get in touch with more directly to try and help, as I'm programmatically literate but this bug ends up being the only reason I'm not on Linux full-time yet.

---

### 评论 #4 — TheGoddessInari (2018-11-20T12:44:43Z)

Still occurs with latest Mesa git, ROCm 1.9.2, and Vega 10 firmware version 18.40.

---

### 评论 #5 — dlight (2020-09-19T14:35:51Z)

Does this occur with ROCm 3.7?

---

### 评论 #6 — ROCmSupport (2021-01-07T09:41:59Z)

Thanks @TheGoddessInari 
Can you please check with the latest ROCm 4.0 and share an update asap to move this issue to next level.
Thank you.

---

### 评论 #7 — tasso (2023-12-08T17:17:47Z)

Is this still an issue with the latest RCOm? If not, can we please close it?  Thanks!

---

### 评论 #8 — tasso (2023-12-12T21:51:35Z)

Original ticket is more than a year old and the person that originally opened ticket  has not responded to the latest request.  If this is still an issue, please file a new ticket and we will be happy to investigate it.  Thanks!

---
