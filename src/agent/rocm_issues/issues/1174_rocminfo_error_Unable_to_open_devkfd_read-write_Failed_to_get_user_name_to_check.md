# rocminfo error Unable to open /dev/kfd read-write Failed to get user name to check for video group membership

> **Issue #1174**
> **状态**: closed
> **创建时间**: 2020-07-03T19:17:02Z
> **更新时间**: 2021-01-28T11:09:02Z
> **关闭时间**: 2021-01-28T11:09:02Z
> **作者**: Shreyashwaghe
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1174

## 描述

my system - Linux shreyash-Nitro-AN515-42 4.15.0-99-generic #100~16.04.1-Ubuntu SMP Wed Apr 22 23:56:30 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
acer nitro 5 ryzen 5 
processor - AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx × 8 
graphics - AMD RAVEN (DRM 3.36.0 / 4.15.0-99-generic, LLVM 6.0.0) in all setting-> details
                 amd radeon rx560x real hardware from manufacturer, are these same or not

(base) shreyash@shreyash-Nitro-AN515-42:~$ /opt/rocm/bin/rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
Failed to get user name to check for video group membership
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

(base) shreyash@shreyash-Nitro-AN515-42:~$ groups
shreyash adm cdrom sudo dip video plugdev lpadmin sambashare






---

## 评论 (4 条)

### 评论 #1 — xuhuisheng (2020-07-04T16:55:53Z)

try `dmesg | grep kfd`, check info like `[ 5.737933] kfd kfd: skipped device 1002:67df, PCI rejects atomics`, GFX8(like rx580) need both cpu and motherboard support 'PCIe atomics', please refer the offical readme : https://github.com/RadeonOpenCompute/ROCm#supported-cpus

---

### 评论 #2 — ROCmSupport (2020-12-17T04:14:17Z)

Hi @Shreyashwaghe 
Thanks for reaching out.
Can you please try with the latest ROCm 3.10 and share me an update.
Thank you.

---

### 评论 #3 — Karthikeyan564 (2021-01-09T11:46:12Z)

Hi
I have the same system.
The problem still persists on ROCm v4
`dmesg | grep kfd`
does not give any output.

---

### 评论 #4 — ROCmSupport (2021-01-28T11:09:02Z)

Hi @Shreyashwaghe 
As per the info @ [https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support](url), Raven is not an official supported hardware. Only OpenCL things might work. 
Thank you.

---
