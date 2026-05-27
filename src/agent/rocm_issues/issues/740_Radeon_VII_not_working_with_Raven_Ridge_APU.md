# Radeon VII not working with Raven Ridge APU

> **Issue #740**
> **状态**: closed
> **创建时间**: 2019-03-15T19:56:39Z
> **更新时间**: 2019-03-15T21:04:17Z
> **关闭时间**: 2019-03-15T21:04:17Z
> **作者**: ewr002
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/740

## 描述

Hello,

I have been unable to find a Rocm/kernel version combination that will support my Radeon VII on a Raven Ridge system.

I have been able to use the integrated graphics in my Raven Ridge 2200G APU to run OpenCL code, using Rocm 2.1 and the 4.18 kernel. The system had no other GPU at the time. Everything seemed to work well.

Since then, I have installed a Radeon VII, and now neither device is usable in Rocm. Though in most cases Rocm installation appears to be successful, I have been unable to get any device to enumerate in /opt/rocm/opencl/bin/x86_64/clinfo.  I've tried kernels 4.15 and 4.18, and Rocm versions 2.0 through 2.2. Depending on the combination used, the errors include #1001 (Not found), or "Segmentation fault (core dumped)"

Has the Rocm team tested a Vega20 device on a Raven Ridge platform? If so, what Rocm and kernel versions are supposed to work together?

Although I had intended to use the Raven graphics to drive monitors and the VII to run compute kernels, I'd be happy if I could get the Radeon VII working on its own. Unfortunately, disabling the integrated graphics in BIOS doesn't seem to help.

Thanks!

---

## 评论 (2 条)

### 评论 #1 — briansp2020 (2019-03-15T20:38:06Z)

Try disabling the iGPU.

https://github.com/RadeonOpenCompute/ROCm/issues/717#issuecomment-471071285

---

### 评论 #2 — ewr002 (2019-03-15T21:04:17Z)

Thanks Brian.

With the Raven integrated graphics disabled, kernel 4.15 and Rocm 2.0, the Radeon VII shows up in clinfo.

I had tried disabling the Raven graphics previously, running a different kernel/Rocm version combination, but that didn't solve the problem. This time it did.

The issue can be considered closed! Thanks again.

---
