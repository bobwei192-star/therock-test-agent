# Is OpenGL supported on ROCm 1.5

> **Issue #131**
> **状态**: closed
> **创建时间**: 2017-06-16T09:39:15Z
> **更新时间**: 2017-07-01T21:42:32Z
> **关闭时间**: 2017-07-01T21:42:32Z
> **作者**: zhaojunfan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/131

## 描述

I want to know if OpenGL is supported on ROCm 1.5.0

---

## 评论 (3 条)

### 评论 #1 — grmat (2017-06-20T22:32:32Z)

No.

But all the GPUs supported by ROCm are also supported by mesa, which provides OpenGL 4.5.

---

### 评论 #2 — gsedej (2017-06-21T10:12:43Z)

You can use `oibaf ppa` to get the lastest mesa opengl drivers. I am not 100% sure what gl driver is in use, but you are limited with the current ROCm kernel driver  `4.9.0-kfd-compute-rocm-rel-1.5-99`.
I have ubuntu 16.04, ROCm 1.5, and oibaf ppa is "installed" (installed before ROCm) and I can play new steam games. This is my glxinfo:
```
Extended renderer info (GLX_MESA_query_renderer):
    Vendor: X.Org (0x1002)
    Device: AMD POLARIS10 (DRM 3.13.0 / 4.9.0-kfd-compute-rocm-rel-1.5-99, LLVM 4.0.1) (0x67df)
    Version: 17.2.0
    Accelerated: yes
    Video memory: 7315MB
    Unified memory: no
    Preferred profile: core (0x1)
    Max core profile version: 4.5
    Max compat profile version: 3.0
    Max GLES1 profile version: 1.1
    Max GLES[23] profile version: 3.1
```

---

### 评论 #3 — gstoner (2017-07-01T21:42:32Z)

It is via the MesaGL stack,  we support OpenGL over EGL in headless config and also GL with X11 when you have head. 

---
