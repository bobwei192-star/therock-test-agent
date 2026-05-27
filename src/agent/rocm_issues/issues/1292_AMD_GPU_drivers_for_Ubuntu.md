# AMD GPU drivers for Ubuntu

> **Issue #1292**
> **状态**: closed
> **创建时间**: 2020-11-14T06:40:01Z
> **更新时间**: 2020-11-18T17:27:42Z
> **关闭时间**: 2020-11-18T17:27:42Z
> **作者**: YuriyTigiev
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1292

## 描述

Should I install the latest AMD drivers befor install ROCm ?

If yes, then which options I should use if I have a one or multiple cards?
https://amdgpu-install.readthedocs.io/en/latest/install-installing.html

---

## 评论 (3 条)

### 评论 #1 — xuhuisheng (2020-11-14T08:09:09Z)

Neednot install amdgpu-pro driver before ROCm.
ROCm provider a module named rock-dkms, this is the driver for GCN GPU.

And this is another way, that using upstream kernel driver.
That means if we plugin in a GCN GPU on ubuntu-18.04 or ubuntu-20.04, the built-in driver can be used as well as rock-dkms. we have to install only rocm-devs and rocm-libs to enable ROCm.

But AMD said upstream driver could only using 3/8 memory of GPU, which rock-dkms could use 15/16 memory of GPU.
https://github.com/radeonopencompute/ROCm#rocm-support-in-upstream-linux-kernels
Current version (which is NON-LTS) of ubuntu is 20.10, using kernel-5.8, so I think upstream driver is as well as rock-dkms.

---

### 评论 #2 — rkothako (2020-11-16T06:10:25Z)

Thanks @YuriyTigiev and @xuhuisheng 
Request to close this ticket if the above answers are reasonable.

---

### 评论 #3 — ROCmSupport (2020-11-18T07:15:01Z)

Hi @YuriyTigiev, Can you please close this ticket now.
Thank you.

---
