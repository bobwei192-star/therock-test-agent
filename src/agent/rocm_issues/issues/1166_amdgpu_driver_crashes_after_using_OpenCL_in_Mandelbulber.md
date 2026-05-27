# amdgpu driver crashes after using OpenCL in Mandelbulber

> **Issue #1166**
> **状态**: closed
> **创建时间**: 2020-06-25T12:08:43Z
> **更新时间**: 2020-12-17T04:36:07Z
> **关闭时间**: 2020-12-17T04:36:07Z
> **作者**: proailurus
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1166

## 描述

Please see this issue for reference:
https://github.com/buddhi1980/mandelbulber2/issues/663

When rendering reflective or transparent images using ROCm's OpenCL implementation, the amdgpu Linux kernel driver crashes.
This leaves the desktop unusable - "X is wedged". In my case, I saw heavy graphical artifacts, a crashed KDE session and the desktop left in an unresponsive state.

Multiple users reported this issue with at least these cards:
AMD Radeon RX 580
AMD Radeon RX 570

---

## 评论 (2 条)

### 评论 #1 — baryluk (2020-11-18T19:24:59Z)

Works fine for me on AMD Radeon R9 Fury X (FIJI, GFX8), with ROCm 3.8 and ROCm 3.9. I tested Mandelbulber 2.23 appimage from the github.

Looks like it is related to specific GPU and kernel.

Could you try again with most recent kernel you can try, and ROCm 3.9?



---

### 评论 #2 — ROCmSupport (2020-12-17T04:36:07Z)

Thanks @clavinet 
Not able to reproduce this issue with the latest ROCm 3.10.
Recommend to try with the latest ROCm 3.10.
Thank you.

---
