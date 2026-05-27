# Linux Ubuntu 20.04 Blender HIP Radeon RX 6800 XT Crash

> **Issue #1840**
> **状态**: closed
> **创建时间**: 2022-10-17T15:23:34Z
> **更新时间**: 2024-04-21T13:19:47Z
> **关闭时间**: 2024-04-21T13:19:46Z
> **作者**: raydeepx
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1840

## 描述

Blender Version
3.3+

When using HIP Gpu render in view port after few seconds all freeze and getting this error.
drm.amdgpu_cs_ioctl [amdgpu] *ERROR* failed to initialize parser - 125!
Only reboot or restart X may bring control

What is interesting i can render with HIP gpu without any problems, only using view port rendering (when using HIP) getting this error. Only cpu render works fine

I know about some kernel problems making this kind of crash but in my case the only program making this is Blender.That;s why i reporting this bug here. All Games, programs working stable without this error.

Radeon Pro renderer works fine also . The only problem is GPU render in view port with cycles.

similar problem described here:
https://developer.blender.org/T100353


---

## 评论 (7 条)

### 评论 #1 — raydeepx (2022-11-01T22:59:00Z)

Another description:
https://gitlab.freedesktop.org/drm/amd/-/issues/2145

---

### 评论 #2 — nartmada (2024-02-02T23:01:54Z)

Hi @raydeepx, please check latest ROCm 6.0.2 to see if your still has been fixed.  If fixed, please close the ticket.  Thanks.

---

### 评论 #3 — raydeepx (2024-02-06T19:09:42Z)

Hi @nartmada, I've updated to 6.0.2 and it change nothing. Blender works around 20s and crash

---

### 评论 #4 — nartmada (2024-02-06T19:12:01Z)

Thank you @raydeepx.  Which GPU and OS are you using?  I will create an internal ticket for investigation.  

---

### 评论 #5 — raydeepx (2024-02-06T21:46:27Z)

Operating System: KDE neon 5.27  (Ubuntu 22.04 jammy)
KDE Plasma Version: 5.27.10
KDE Frameworks Version: 5.114.0
Qt Version: 5.15.12
Kernel Version: 6.5.0-15-generic (64-bit)
Graphics Platform: Wayland
Processors: 32 × AMD Ryzen 9 5950X 16-Core Processor
Memory: 62.7 GiB of RAM
Graphics Processor: AMD Radeon RX 6800 XT

related more or less to
https://gitlab.freedesktop.org/drm/amd/-/issues/2145
https://projects.blender.org/blender/blender/issues/100353

---

### 评论 #6 — nartmada (2024-04-17T04:01:15Z)

@raydeepx, please re-test with ROCm 6.1.0.  Thanks.

---

### 评论 #7 — nartmada (2024-04-21T13:19:47Z)

Closing the ticket.  @raydeepx, please re-open if you still see the issue with ROCm 6.1.0.  Thanks.

---
