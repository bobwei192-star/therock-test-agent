# Kubuntu 18.04 fresh install - hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call returned 4104

> **Issue #662**
> **状态**: closed
> **创建时间**: 2019-01-04T12:15:52Z
> **更新时间**: 2019-01-04T17:20:53Z
> **关闭时间**: 2019-01-04T17:20:53Z
> **作者**: thehamzan6
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/662

## 描述

This is a fresh Kubuntu 18.04 install, fully updated and using the kernel 4.15.0-43-generic. running on Intel I7-8550U CPU.

```
$ lspci -vnn | grep Display -A 12
Advanced Micro Devices, Inc. [AMD/ATI] Topaz XT [Radeon R7 M260/M265 / M340/M360 / M440/M445] [1002:6900] (rev c1)
        Subsystem: Dell Topaz XT [Radeon R7 M260/M265 / M340/M360 / M440/M445] [1028:0810]
        Flags: fast devsel, IRQ 129
        Memory at c0000000 (64-bit, prefetchable) [size=256M]
        Memory at d0000000 (64-bit, prefetchable) [size=2M]
        I/O ports at e000 [size=256]
        Memory at d0200000 (32-bit, non-prefetchable) [size=256K]
        Expansion ROM at d0240000 [disabled] [size=128K]
        Capabilities: [48] Vendor Specific Information: Len=08 <?>
        Capabilities: [50] Power Management version 3
        Capabilities: [58] Express Legacy Endpoint, MSI 00
        Capabilities: [a0] MSI: Enable+ Count=1/1 Maskable- 64bit+
        Capabilities: [100] Vendor Specific Information: ID=0001 Rev=1 Len=010 <?>
```

I've followed the install instructions provided here: https://rocm.github.io/ROCmInstall.html#ubuntu-support---installing-from-a-debian-repository

`$ /opt/rocm/bin/rocminfo 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call returned 4104`

`$ /opt/rocm/opencl/bin/x86_64/clinfo 
ERROR: clGetPlatformIDs(-1001)`

`$ groups
thehamzan6 adm cdrom sudo dip video plugdev lpadmin sambashare`

`$ dmesg | grep kfd
[    1.422345] amdgpu 0000:01:00.0: kfd not supported on this ASIC`

In one of the issues, someone suggested to add AMDKFD before AMDGPU in initramfs, how can that be done?

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-01-04T17:20:32Z)

[Iceland / Topaz GPUs are not supported in ROCm at this time.](https://rocm.github.io/hardware.html)

---
