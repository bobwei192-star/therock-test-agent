# Install ROCm packages without root permission

> **Issue #1610**
> **状态**: closed
> **创建时间**: 2021-11-03T22:42:10Z
> **更新时间**: 2021-11-10T11:04:17Z
> **关闭时间**: 2021-11-10T11:03:16Z
> **作者**: ye-luo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1610

## 描述

It seems that amdgpu-dkms is the only piece needs to root to install.
All the rest ROCM components can be installed without root.
In the rocm user-guide, both the installer and package manager methods need root. It will be nice to allow me manually install ROCm without root in a preferred location.

---

## 评论 (2 条)

### 评论 #1 — Rmalavally (2021-11-05T02:18:55Z)

You must have root privileges to install ROCm or the driver because multiple steps during installation require root privileges. 
 
We do not support the ability to install ROCm at a location of your choice at this time. A solution may be provided in a future release.

AMD ROCm Documentation 

---

### 评论 #2 — ROCmSupport (2021-11-10T11:03:16Z)

Hi @ye-luo 
Thanks for reaching out.
As the integration of amdgpu and ROCm happened, so called Unified driver, amdgpu needs root privileges as it needs to access kernel components. ROCm userpsace does not need root access and so we can install them without root access.
So for simplification, we recommend to install ROCm+amdgpu using sudo using amdgpu-install script.

You can install ROCm userspace alone using "sudo amdgpu-install --no-dkms --usecase=rocm"
Installing ROCm in a preferred location is not possible now, all ROCm components will go to /opt/rocm as usual.
Hope this helps.
Thank you.


---
