# Unsuccessful installation on Ubuntu 20.04 RX 580

> **Issue #1412**
> **状态**: closed
> **创建时间**: 2021-03-20T08:02:54Z
> **更新时间**: 2021-03-22T08:34:06Z
> **关闭时间**: 2021-03-22T08:34:06Z
> **作者**: facorazza
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1412

## 描述

Followed the installation process: https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu
When I run:
```
/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo
```
I get:
```
zsh: no such file or directory: /opt/rocm/bin/rocminfo
dlerror: libamd_comgr.so.1: cannot open shared object file: No such file or directory
ERROR: clGetPlatformIDs(-1001)
```

Kernel: 5.4.0-42-generic


---

## 评论 (6 条)

### 评论 #1 — xuhuisheng (2021-03-20T08:10:35Z)

Seems some deb didn't install correctly. libamd_comgr.so should be in /opt/rocm/lib/.

BTW: AMD drop RX580 offical support on ROCm-4.0.
https://github.com/xuhuisheng/rocm-build/tree/develop/gfx803

---

### 评论 #2 — facorazza (2021-03-20T08:29:22Z)

Well that's unfortunate

---

### 评论 #3 — facorazza (2021-03-20T08:31:30Z)

Does that mean that the installation won't work at all or that it might work but it's not guaranteed?

---

### 评论 #4 — xuhuisheng (2021-03-20T08:50:55Z)

Actually, we can install ROCm-4.0 successfully. But there are some NaN loss situation when running tensorflow/pytorch.

Emm~, and rocSPARSE need compile by yourselves, othewise you will meet a noBinaryForGpu error.

---

### 评论 #5 — facorazza (2021-03-20T08:52:36Z)

I'm actually planning on using openmp but some tf would be nice. Should I try to install it again and check for errors before rebooting?

---

### 评论 #6 — ROCmSupport (2021-03-22T08:34:06Z)

Hi @facorazza 
Thanks for reaching out.
We are not officially supporting gfx8 devices now.
But some things might work. In your case, looks like installation did not go well.
Request you to clean the system from rocm and reinstall freshly.
Thank you.

---
