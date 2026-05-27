# binary  compiled with hipcc uses 100% cpu forever

> **Issue #694**
> **状态**: closed
> **创建时间**: 2019-01-30T15:32:44Z
> **更新时间**: 2021-01-07T05:25:58Z
> **关闭时间**: 2021-01-07T05:25:58Z
> **作者**: loreson
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/694

## 描述

I have an Ubuntu18.04 System.
 Hardware : Xeon e5 1630-v3 with AMD Firepro W9100.
I installed ROCM according to this guide: https://github.com/ROCm/ROCm.github.io/blob/master/ROCmInstall.md
As all of the example applications would hang indefinitely, and there and the current version seems to be broken for Hawaii GPUS,  uninstalled it and installed the 1.92 version with the distro install script.
Unfortunately this does not work either:
I have a simple hello world.
[hallo.txt](https://github.com/RadeonOpenCompute/ROCm/files/2813197/hallo.txt)
compiled with clang it  works fine, and prints "Hello world".
Compiled with hipcc the resulting binary uses 100% CPU, and seems to never complete.  I have left it overnight and didn't see any output.
rocminfo gives me
[roc.txt](https://github.com/RadeonOpenCompute/ROCm/files/2813229/roc.txt)
and hipconfig --full:
[hipconf.txt](https://github.com/RadeonOpenCompute/ROCm/files/2813232/hipconf.txt)

Any sugesstions?




---

## 评论 (2 条)

### 评论 #1 — dragontamer (2019-01-31T19:12:16Z)

> AMD Firepro W9100.

That sounds like a Hawaii card (similar firmware / hardware to the R9 290x and R9 390x).

There have been a lot of issues reported for ROCm 2.0 for Hawaii: https://github.com/RadeonOpenCompute/ROCm/issues/691

It seems people have mitigated the issue by either downgrading to 1.8,  or by removing ROCm 2.0 and using AMDGPU-pro drivers instead.

---

### 评论 #2 — ROCmSupport (2021-01-07T05:25:58Z)

Hi All,
Hawaii is no more officially ROCm supported device. Please check for more details:
[https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url)

---
