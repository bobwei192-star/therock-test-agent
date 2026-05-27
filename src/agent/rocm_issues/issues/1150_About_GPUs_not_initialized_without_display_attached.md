# About GPUs not initialized without display attached

> **Issue #1150**
> **状态**: closed
> **创建时间**: 2020-06-16T09:31:38Z
> **更新时间**: 2021-01-12T08:12:25Z
> **关闭时间**: 2021-01-12T08:12:25Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1150

## 描述

A number of users have been complaining about GPUs and OpenCL non initialized if no display is attached to the GPU.
This behavior only happens on some systems, on other systems (like computing RIGs) I have never encountered this bug.
Thus the bug must be system-configuration dependent or package-dependent, but it does not happen on all systems.
Do you have any idea why this happens only on some systems?


---

## 评论 (6 条)

### 评论 #1 — preda (2020-06-18T23:21:51Z)

I see (every time) a different variant of this issue: OpenCL is not initialized unless I do a login in the GUI. This is on Ubuntu 19.10 with ROCm. Doing a login through ssh (remotely) does not count.

---

### 评论 #2 — valeriob01 (2020-06-18T23:57:07Z)

I have never seen this error, though I have a display attached on the mainboard integrated graphics. But this does not count I suppose. I can do a test removing that display if necessary.

---

### 评论 #3 — valeriob01 (2020-06-18T23:58:00Z)

btw, I login via ssh not in the main display.


---

### 评论 #4 — c0d3st0rm (2020-06-19T09:02:13Z)

What GPUs/distro/kernel version?

---

### 评论 #5 — valeriob01 (2020-06-19T10:14:00Z)

Radeon VII, Ubuntu Focal, 5.4

---

### 评论 #6 — ROCmSupport (2021-01-12T08:12:25Z)

Thanks @valeriob01 for reaching out.
We have not seen this issue any time and most of our machines are without display connected only.
Hence request to file specific issue separately, if you see/find any.

---
