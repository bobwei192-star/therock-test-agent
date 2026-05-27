# hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104

> **Issue #624**
> **状态**: closed
> **创建时间**: 2018-11-26T10:40:28Z
> **更新时间**: 2019-04-15T20:06:17Z
> **关闭时间**: 2018-11-29T08:53:48Z
> **作者**: ctangv99
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/624

## 描述

Hi, I am trying to install ROCm 1.9.2 on desktop with vega10
CPU AMD Ryzen 7 1700 Eight-Core Processor

> uname -a
Linux wukong 4.4.0-139-generic #165-Ubuntu SMP Wed Oct 24 10:58:50 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

> dmesg | grep amd
[    0.000000] Linux version 4.4.0-139-generic (buildd@lcy01-amd64-006) (gcc version 5.4.0 20160609 (Ubuntu 5.4.0-6ubuntu1~16.04.10) ) #165-Ubuntu SMP Wed Oct 24 10:58:50 UTC 2018 (Ubuntu 4.4.0-139.165-generic 4.4.160)
[    0.566793] amd_nb: Cannot enumerate AMD northbridges
[    0.988289] perf: amd_iommu: Detected. (0 banks, 0 counters/bank)

> lspci | grep -i vga
0b:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1)

> dkms status
amdgpu, 1.9-307: added

The rocminfo doesn't work, and looks the gpu driver is not installed correctly.
Do you have any suggestion on this issue? Thanks.

---

## 评论 (6 条)

### 评论 #1 — jlgreathouse (2018-11-27T06:03:53Z)

As noted in [the installation directions for ROCm](https://github.com/RadeonOpenCompute/ROCm#supported-operating-systems---new-operating-systems-available), the kernel module currently does not build with kernel 4.4 on Ubuntu. You will need 4.13 or above.

---

### 评论 #2 — Avatat (2018-11-29T01:15:06Z)

> You will need 4.13 or above.

And lower than 4.17, right?

---

### 评论 #3 — jlgreathouse (2018-11-29T01:15:49Z)

Yes.

Edit: Though I should be clear, if you have kernel 4.17 (or 4.18 if you have a Vega 10 GPU), you should be able to use ROCm without the DKMS kernel module supplied by AMD, as our required changes have been upstreamed. See [this note](https://github.com/RadeonOpenCompute/ROCm#rocm-19-is-abi-compatible-with-kfd-in-upstream-linux-kernels).

---

### 评论 #4 — ctangv99 (2018-11-29T08:53:48Z)

Working after change linux kernel to 4.15

---

### 评论 #5 — ctangv99 (2018-11-29T08:54:23Z)

Thanks for your help!

---

### 评论 #6 — kolserdav (2019-04-15T20:06:17Z)

I have now reinstalled the system. With a kernel 4.15 and I have the same problem. do not repeat my mistake(

> uname -a
`Linux server 4.15.0-041500-generic #201802011154 SMP Thu Feb 1 11:55:45 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux`

> dmesg | grep amd
`[    3.353284] [drm] amdgpu kernel modesetting enabled.`

> lscpi | grep VGA
`01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Pitcairn PRO [Radeon HD 7850 / R7 265 / R9 270 1024SP]`

> dkms status
`amdgpu, 2.3-14, 4.15.0-041500-generic, x86_64: installed`

> /opt/rocm/bin/rocminfo
`hsa api call failure at line 900, file: /data/jenkins_workspace/compute-rocm-rel-2.3/rocminfo/rocminfo.cc. Call returned 4104`

> /opt/rocm/opencl/bin/x86_64/clinfo 
`ERROR: clGetPlatformIDs(-1001)`

---
