# "AMDKFD_IOC_ACQUIRE_VM failed" on linux-4.18-rc1 with Vega 64

> **Issue #438**
> **状态**: closed
> **创建时间**: 2018-06-20T02:28:05Z
> **更新时间**: 2018-06-27T16:38:46Z
> **关闭时间**: 2018-06-27T16:38:46Z
> **作者**: Narthorn
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/438

## 描述

Tested with roc-1.8.x and master branches of ROCT-Thunk-Interface and ROCR-Runtime:

```
# uname -a
Linux localhost 4.18.0-rc1-mainline #1 SMP PREEMPT Wed Jun 6 19:43:20 CEST 2018 x86_64 GNU/Linux

# lspci | grep VGA
08:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Vega 10 XT [Radeon RX Vega 64] (rev c1)

# HSAKMT_DEBUG_LEVEL=7 rocminfo 
acquiring VM for 86f3 using 5
AMDKFD_IOC_ACQUIRE_VM failed
hsa api call failure at line 896, file: /home/narthorn/dev/rocm/rocminfo/rocminfo.cc. Call returned 4104
```
It looks like /dev/kfd is successfully opened, but this ioctl fails with EINVAL during hsa initialization.

---

## 评论 (1 条)

### 评论 #1 — fxkamd (2018-06-27T16:38:46Z)

ROCm 1.8 is incompatible with the upstream KFD's ioctl APIs. ROCm 1.9 will be compatible. In the mean time you can use my hacked thunk to experiment with the upstream KFD: https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/tree/fxkamd/drm-next-wip

---
