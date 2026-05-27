# [Kernel 5.5.X] drm/amdgpu: independent DMA-buf export/import breaks ROCm and AMDGPU-Pro OpenCL on Gentoo x64 w/ Vega 64

> **Issue #1050**
> **状态**: closed
> **创建时间**: 2020-03-17T21:39:50Z
> **更新时间**: 2021-04-05T11:43:59Z
> **关闭时间**: 2021-04-05T11:43:59Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1050

## 描述

I wanted to donate some GPU time to F@H due to COVID19, but even a simple clinfo is enough to cause a kernel panic. libdrm used is version 2.4.100, ocl-icd is 2.2.12. Mesa 20.0.1 was compiled without OpenCL support to rule out conflicts. amdgpu is compiled into the kernel and not a separate module. I'll attach a cut dmesg output and my /proc/config.gz. If more info is needed, I'll try to provide it.

[dmesg output (cut)](https://github.com/RadeonOpenCompute/ROCm/files/4345932/dmesg.log)

[zcat /proc/config.gz](https://github.com/RadeonOpenCompute/ROCm/files/4345937/kconfig.txt)

The system specs are the following: Ryzen 3900X stock, Gigabyte X570 Aorus Pro F11, 32GB DDR4 3733, Vega 64, 850W PSU.

---

## 评论 (4 条)

### 评论 #1 — ghost (2020-03-21T12:26:55Z)

A very nice person on reddit helped me find the issue with AMDGPU-PRO OpenCL (it threw the same "failed to pin userptr" error). Turns out userspace isn't yet compatible with these two commits:

https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=6e6db2722c287122bfc4d51e685872fb5031cf18

https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=a39414716ca08c08ce09d9e8409ef525e7a77eaf

ROCm now works aswell with the older Kernel 5.4.26 (tested with LuxMark 3.1, as folding@home isn't supported by ROCm).

---

### 评论 #2 — BuzzBumbleBee (2020-03-24T11:51:33Z)

Can you try apply the following patch set to your Linux kernel. It should fix the DMA issues in 5.5 and 5.6.

https://lists.freedesktop.org/archives/dri-devel/2020-March/260116.html

---

### 评论 #3 — BuzzBumbleBee (2020-03-31T10:07:05Z)

Can someone confirm that kernel 5.6 has the above issue fixed ? 

---

### 评论 #4 — ROCmSupport (2021-04-05T11:43:59Z)

Hi @ghost
Thanks for reaching out.
This issue is fixed and no more observed now. I recommend to try with the latest ROCm 4.1.
Feel free to open a new issue, if any, for quick resolution.
Thank you.

---
