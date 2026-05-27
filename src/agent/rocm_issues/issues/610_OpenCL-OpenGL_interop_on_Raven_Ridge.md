# OpenCL-OpenGL interop on Raven Ridge

> **Issue #610**
> **状态**: closed
> **创建时间**: 2018-11-13T20:07:54Z
> **更新时间**: 2023-12-12T21:51:55Z
> **关闭时间**: 2023-12-12T21:51:54Z
> **作者**: exilef
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/610

## 描述

Hi,

I have been trying to get the OpenCL-OpenGL interop working on [Raven Ridge APUs](https://en.wikichip.org/wiki/amd/cores/raven_ridge) (e.g. the Ryzen 5 2400G), unfortunately without any luck.

I have tried two different approaches:

1. Ubuntu 18.04.1 with kernel 4.15 and the DKMS module, following the standard install procedure
2. Ubuntu 18.04.1 or 18.10 with kernel 4.19, without the DKMS module, as also discussed in Issue #588.

While the first approach results in a system with a working and usable OpenCL-OpenGL interop when using a discrete Vega 64 card ([using this repo to test](https://github.com/9prady9/CLGLInterop)), the interop does not work on Raven Ridge APUs (while pure OpenCL works, just the interop is broken).

Am I correct in my assumption that CL-GL interop is not supported in the DKMS for Raven Ridge? This also seems to be related to the kernel version, as the 4.15 kernel seems to be the latest one still supported by DKMS (as @jlgreathouse [suggested here](https://github.com/RadeonOpenCompute/ROCm/issues/576#issuecomment-432433555): `rock-dkms is currently broken on kernels newer than 4.15`)?  

This lead me to trying another approach using a newer kernel (4.19, tried both Ubuntu 18.04 and 18.10) that out of the box supports Raven Ridge via `amdgpu`. I installed it like described in Issue #588. But here again, we get a working OpenCL platform with broken CL-GL interop.

Any hints on how I could get this to work??

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-01-07T10:08:53Z)

Hi @exilef 
Can you please verify with the latest kernels on ROCm 4.0 and update asap.
Thank you.

---

### 评论 #2 — tasso (2023-12-08T17:18:15Z)

Is this still an issue RCOm? If not; can we please close it?  Thanks!

---

### 评论 #3 — tasso (2023-12-12T21:51:55Z)

Original ticket is more than a year old and the person that originally opened ticket  has not responded to the latest request.  If this is still an issue, please file a new ticket and we will be happy to investigate it.  Thanks!

---
