# Future of ROCm - desktop support?

> **Issue #181**
> **状态**: closed
> **创建时间**: 2017-08-16T09:26:44Z
> **更新时间**: 2017-08-16T09:33:10Z
> **关闭时间**: 2017-08-16T09:33:10Z
> **作者**: gsedej
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/181

## 描述

Hello,

the intended use of ROCm is trough SSH to powerful multi GPU machine (server). This makes ROCm desktop users a "second-tier". Breaking desktop usage of ROCm, would mean, one would need to develop ROCm-accelerated software on server trough SSH, which is not ideal (e.g. no root access, inability to install additional developer tools, not able/hard to use graphical IDE, etc... )

Will ROCm continue supporting all desktop features (display, 3d accel, video accel, ...) in the future?

---

## 评论 (2 条)

### 评论 #1 — gstoner (2017-08-16T09:31:53Z)

ROCm started as server focused product, but we will support X11/OpenGL/EGL in the base driver.   We use this for development as well.  

---

### 评论 #2 — gsedej (2017-08-16T09:33:10Z)

Thank you for reply and enabling ROCm desktop usage!

---
