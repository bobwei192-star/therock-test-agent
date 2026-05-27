# ROCm on Debian Bullseye

> **Issue #1243**
> **状态**: closed
> **创建时间**: 2020-09-25T08:14:22Z
> **更新时间**: 2020-12-03T11:59:40Z
> **关闭时间**: 2020-12-03T11:59:40Z
> **作者**: piodag
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1243

## 描述

Hi folks,

after fixing the deps I got ROCm running on my Debian Bullseye. Tensorflow works. But I have this error with the
rocm-smi tool

WARNING: GPU[0]	: Unable to read /sys/class/drm/card0/device/gpu_busy_percent

Any Idea?

Best regards

Giorgio

---

## 评论 (4 条)

### 评论 #1 — piodag (2020-09-25T08:15:39Z)

Sorry for the duplicate (see below). I cannot erase it.

---

### 评论 #2 — baryluk (2020-09-25T17:00:08Z)

You need to provide more details.

1) Version of rocm-smi package
2) Kernel version
3) Do you use rocm-dkms or not (rocm amdgpu custom driver, or the upstream driver)
4) GPU used
5) CPU used
6) Exact path and parameters used by your invokation of rocm-smi

I have rocm-smi3.8.0 ( version 1.0.0-204-rocm-rel-3.8-30-g08ebddd ) working on vanilla upstream amdgpu driver. It shows a lot of info just fine. It has no other dependencies other than python and kernel.

It should work just fine from both root and non-root users.


---

### 评论 #3 — ROCmSupport (2020-11-18T10:47:07Z)

Hi @gfwp 
Thanks for reaching out.
Please help us with more data points as @baryluk mentioned already.
Else request you to close this issue as its open around 50 days.

---

### 评论 #4 — streamhsa (2020-12-03T11:59:40Z)

Closing this as there is no update from reporter for a long time.
Request reporter to open a new issue, if the same/new occurs.
Thank you.

---
