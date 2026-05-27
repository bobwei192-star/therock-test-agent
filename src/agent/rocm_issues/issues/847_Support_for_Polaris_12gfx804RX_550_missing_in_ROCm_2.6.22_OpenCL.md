# Support for Polaris 12/gfx804/RX 550 missing in ROCm 2.6.22 OpenCL

> **Issue #847**
> **状态**: closed
> **创建时间**: 2019-07-17T02:44:06Z
> **更新时间**: 2024-02-03T03:48:40Z
> **关闭时间**: 2024-02-03T03:48:40Z
> **作者**: skoulik
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/847

## 描述

We are running CentOS 6.5 with the latest (version 2.6.22) rocm-opencl, rocm-opencl-devel, rocm-libs installed from the public repository,

According to https://github.com/RadeonOpenCompute/ROCm#supported-gpus and https://rocm.github.io/hardware.html Polaris 12 architecture is supported by ROCm, however when running LLVM compiler from rocm-opencl-devel, neither gfx804, nor polaris12 architectures are present in the list:
> ./clang-ocl test.cl -o test -mcpu=gfx804
error: unknown target CPU 'gfx804'
note: valid target CPU values are: gfx600, tahiti, gfx601, hainan, oland, pitcairn, verde, gfx700, kaveri, gfx701, hawaii, gfx702, gfx703, kabini, mullins, gfx704, bonaire, gfx801, carrizo, gfx802, iceland, tonga, gfx803, fiji, polaris10, polaris11, gfx810, stoney, gfx900, gfx902, gfx904, gfx906, gfx909, gfx1010

Additional observation: 
It turns out that as of ROCm 1.8 gfx804 was supported and present in the list, however it has been removed later. What was the reason for this?

We need to support RX 550 GPU, which is polaris 12 as well as new architectures, such as gfx904 and gfx906, so staying at version 1.8 is not an option.

Either, the links above contain incorrect information and polaris 12 is actually not supported by ROCm, or our assumption that we should use gfx804 as target architecture is incorrect.  What option should we use instead?


---

## 评论 (4 条)

### 评论 #1 — Djip007 (2019-08-03T23:04:14Z)

I think rocm 2.6 only support with 
"CentOS/RHEL 7 (7.4, 7.5, 7.6) Support"
and centos 6.5 is realy out off date last centos 6 release is base on 6.10...

---

### 评论 #2 — nartmada (2024-02-02T22:39:18Z)

Hi @skoulik, do you still need this ticket to be opened?  Please check latest ROCm6.0.2 for the supported configuration.  Thanks.

https://rocm.docs.amd.com/projects/install-on-linux/en/latest/reference/system-requirements.html

---

### 评论 #3 — skoulik (2024-02-03T01:55:36Z)

We have since moved to CentOS 7 and ROCm 5 where all required configurations are supported. You can go ahead and close the ticket.

---

### 评论 #4 — nartmada (2024-02-03T03:48:40Z)

Closing the ticket as it is not needed anymore.  

---
