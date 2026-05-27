# installed rock-dkms package post-installation script subprocess returned error exit status 10

> **Issue #1375**
> **状态**: closed
> **创建时间**: 2021-02-10T13:40:44Z
> **更新时间**: 2021-02-11T06:03:06Z
> **关闭时间**: 2021-02-11T06:03:06Z
> **作者**: QEU-B-458
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1375

## 描述

Removing old amdgpu-4.0-23 DKMS files...

------------------------------
Deleting module version: 4.0-23
completely from the DKMS tree.
------------------------------
Done.
Loading new amdgpu-4.0-23 DKMS files...
Building for 5.8.0-43-generic
Building for architecture x86_64
Building initial module for 5.8.0-43-generic
ERROR: Cannot create report: [Errno 17] File exists: '/var/crash/rock-dkms-firmw
are.0.crash'
Error! Bad return status for module build on kernel: 5.8.0-43-generic (x86_64)
Consult /var/lib/dkms/amdgpu/4.0-23/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error 
exit status 10
dpkg: dependency problems prevent configuration of rocm-dkms:
 rocm-dkms depends on rock-dkms; however:
  Package rock-dkms is not configured yet.

dpkg: error processing package rocm-dkms (--configure):
 dependency problems - leaving unconfigured
No apport report written because the error message indicates its a followup erro
r from a previous failure.
                          Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)

---

## 评论 (2 条)

### 评论 #1 — xuhuisheng (2021-02-10T16:50:57Z)

This is a kernel-5.8 issue. ROCm-4.0 cannot support kernel-5.8.
#1367
RadeonOpenCompute/ROCK-Kernel-Driver#107

ROCm-4.1 maybe support linux-5.8.

Recently, we should install linux-5.4 and remove linux-5.8, before installing ROCm-4.0

---

### 评论 #2 — ROCmSupport (2021-02-11T06:03:06Z)

Hi @zena1 
This is the duplicate of #1367 and request you to wait till ROCm 4.1 which is going to support it.
Thank you.

---
