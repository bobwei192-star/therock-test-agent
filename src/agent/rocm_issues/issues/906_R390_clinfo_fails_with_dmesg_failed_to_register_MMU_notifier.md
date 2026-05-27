# R390 clinfo fails with dmesg failed to register MMU notifier

> **Issue #906**
> **状态**: closed
> **创建时间**: 2019-10-10T18:31:41Z
> **更新时间**: 2021-01-07T05:26:49Z
> **关闭时间**: 2021-01-07T05:26:48Z
> **作者**: PhilipDeegan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/906

## 描述

```
uname -a
Linux xfer 5.3.4 #1 SMP Sat Oct 5 22:39:14 CEST 2019 x86_64 GNU/Linux

grep HSA /boot/config-5.3.4
CONFIG_HSA_AMD=y

sudo lsmod | grep amdgpu
amdgpu               4677632  3
gpu_sched              36864  1 amdgpu
i2c_algo_bit           16384  1 amdgpu
ttm                   118784  1 amdgpu
drm_kms_helper        212992  1 amdgpu
drm                   548864  7 gpu_sched,drm_kms_helper,amdgpu,ttm
mfd_core               16384  2 lpc_ich,amdgpu

rocm-smi


========================ROCm System Management Interface========================
================================================================================
GPU  Temp   AvgPwr   SCLK    MCLK    Fan     Perf  PwrCap  VRAM%  GPU%
0    35.0c  15.201W  300Mhz  150Mhz  26.67%  auto  208.0W    0%   0%
1    30.0c  17.001W  300Mhz  150Mhz  26.67%  auto  208.0W    0%   0%
================================================================================
==============================End of ROCm SMI Log ==============================
```

I understand that atomics blocks the use of HCC, I dont' see why this extends to openCL tho

Please advise.

rocm-smi shows the GPUs correctly.

---

## 评论 (6 条)

### 评论 #1 — PhilipDeegan (2019-10-10T20:09:38Z)

```
sudo dmesg | grep kfd
[sudo] password for philix:
[    6.291801] kfd kfd: Allocated 3969056 bytes on gart
[    6.293305] kfd kfd: added device 1002:67b1
[    6.713104] kfd kfd: Allocated 3969056 bytes on gart
[    6.713317] kfd kfd: added device 1002:67b1
[  392.761278] kfd2kgd: init_user_pages: Failed to register MMU notifier: -19
[  392.761290] kfd2kgd: init_user_pages: Failed to register MMU notifier: -19
[  392.761297] kfd2kgd: init_user_pages: Failed to register MMU notifier: -19
[  392.761304] kfd2kgd: init_user_pages: Failed to register MMU notifier: -19
```

---

### 评论 #2 — JMadgwick (2019-10-10T20:27:31Z)

R9 390 (Hawaii) has been broken since December. AMD refuse to recognize this and update the readme to show that it is broken. [See this issue](https://github.com/RadeonOpenCompute/ROCm/issues/871), you're not the only one. Solution is to use AMDGPU-PRO for OpenCL.
The problem is in the driver that is why OpenCL also fails. AMDGPU-PRO works fine for OpenCL.

---

### 评论 #3 — acowley (2019-10-17T18:58:00Z)

I'm also seeing those dmesg errors on Linux 5.3.6 with an RX 580 (no ROCm components work; `rocminfo` bails out with an error at line 1102 of `rocminfo.cc`).

All is fine with Kernels 5.2.x.

---

### 评论 #4 — acowley (2019-10-17T22:57:16Z)

I was able to resolve this for myself by changing my kernel config to add:

```
CONFIG_ZONE_DEVICE=y
CONFIG_HMM_MIRROR=y
CONFIG_DRM_AMDGPU_USERPTR=y
```

---

### 评论 #5 — PhilipDeegan (2019-10-18T11:41:33Z)

thanks @acowley I will try that

---

### 评论 #6 — ROCmSupport (2021-01-07T05:26:48Z)

Hi All,
Hawaii is no more officially ROCm supported device. Please check for more details:
[https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url)
Thank you.

---
