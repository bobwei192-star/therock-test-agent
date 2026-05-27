# PCI rejecting atomics on a Radeon RX580 supported chipset

> **Issue #722**
> **状态**: closed
> **创建时间**: 2019-02-28T22:31:56Z
> **更新时间**: 2024-10-02T11:15:20Z
> **关闭时间**: 2019-03-05T17:11:08Z
> **作者**: jjmoody
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/722

## 描述

I am attempting to use ROCm on a large 50+ GPU RX580 cluster and the README lists the RX580's as a supported chipset:
> ROCm officially supports AMD GPUs that use following chips:
> GFX8 GPUs
> "Fiji" chips, such as on the AMD Radeon R9 Fury X and Radeon Instinct MI8
> "Polaris 10" chips, such as on the AMD **Radeon RX 580** and Radeon Instinct MI6
> "Polaris 11" chips, such as on the AMD Radeon RX 570 and Radeon Pro WX 4100
> "Polaris 12" chips, such as on the AMD Radeon RX 550 and Radeon RX 540

I first noticed the problem when got this error code:
`hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.1/rocminfo/rocminfo.cc. Call returned 4104`

I'm on Ubuntu Server 18.04.1 using the 4.15.0-45-generic kernel:
`Linux host 4.15.0-45-generic #48-Ubuntu SMP Tue Jan 29 16:28:13 UTC 2019 x86_64 x86_64 x86_64 GNU/Linux`

After installing ROCm without any issues _dmesg | grep kfd_ returns the following:
```
[    5.737933] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[output omitted]
```
Output of _lspci -nn_ to show that my chipset is in fact an RX580:
```
01:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 470/480/570/570X/580/580X] [1002:67df] (rev e7)
01:00.1 Audio device [0403]: Advanced Micro Devices, Inc. [AMD/ATI] Ellesmere [Radeon RX 580] [1002:aaf0]
[output omitted]
```
What am I missing? Are there steps that I can take to remedy this? Thanks in advance!

---

## 评论 (6 条)

### 评论 #1 — jjmoody (2019-02-28T22:56:36Z)

Just realized that when I installed the AMD drivers that I may not have used the proper flags.

I read here [https://www.amd.com/en/support/kb/release-notes/amdgpu-installation](url) that the --opencl=rocm flag must be used when installing the drivers. I'll do this and get back to you.

`./amdgpu-pro-install -y --opencl=rocm`

EDIT: Using the flag made no difference this support chipset still gives the same "call returned 4104" error and rejects atomics. But It is likely due to the CPU which I didn't bother to check not being supported... Looking for some Intel Xeon E5 v3's as I type this.

---

### 评论 #2 — valeriob01 (2019-03-01T12:55:42Z)

I have installed rocm from the repository (not from amdgpu-pro) in a fresh system and my RX580 is working.

---

### 评论 #3 — jjmoody (2019-03-01T16:02:33Z)

> I have installed rocm from the repository (not from amdgpu-pro) in a fresh system and my RX580 is working.

With what repository... Ubuntu's default repo?
Also, if you don't mind, what CPU and motherboard are you using?

Thank you in advance!

---

### 评论 #4 — valeriob01 (2019-03-01T16:26:08Z)

https://rocm.github.io/ROCmInstall.html

I am using multiple systems...


---

### 评论 #5 — jlgreathouse (2019-03-01T18:12:17Z)

Note that this repo is focused on the open source ROCm platform that should be installed using the installation directions [hosted on this repo](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.1.0/README.md#installing-from-amd-rocm-repositories) or the directions e.g. linked bin @valeriob01 on our github.io page (or the installation directions in our readthedocs documentation). If you have problems with the amdgpu-pro drivers, which are a separate software platform, I recommend posting them in the AMD community forum. The ROCm team here does not offer support if you have simultaneously installed both on your system.

That said, your gfx803 GPU (Polaris 10) requires your CPU platform to support PCIe atomics. See [this hardware support information](https://rocm.github.io/hardware.html#supported-cpus) for more details. What CPU is in your system?

---

### 评论 #6 — psyborg55 (2024-10-02T11:15:20Z)

laptop with dual amd graphics:

kfd kfd: amdgpu: added device 1002:9874
kfd kfd: amdgpu: skipped device 1002:67ef, PCI rejects atomics 730<0

it is not CPU issue

---
