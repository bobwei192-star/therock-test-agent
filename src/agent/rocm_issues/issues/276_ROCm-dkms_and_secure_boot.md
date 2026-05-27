# ROCm-dkms and secure boot

> **Issue #276**
> **状态**: closed
> **创建时间**: 2017-12-20T19:38:03Z
> **更新时间**: 2018-04-10T00:30:17Z
> **关闭时间**: 2018-04-10T00:30:17Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/276

## 描述

Does secure boot need to be disabled for the new DKMS version of ROCm ?

---

## 评论 (6 条)

### 评论 #1 — steemandlinux (2017-12-21T10:03:36Z)

RTFM? https://wiki.archlinux.org/index.php/Secure_Boot

---

### 评论 #2 — boxerab (2017-12-21T23:29:13Z)

anyways, I disabled secure boot on my system. Everything seems to be working fine. 

---

### 评论 #3 — boxerab (2017-12-21T23:29:47Z)

But, if it is _required_ to disable secure boot, this should be put in the docs somewhere.

---

### 评论 #4 — gstoner (2017-12-21T23:30:42Z)

Arron, we look into this after the Christmas break. 

---

### 评论 #5 — seesturm (2018-01-06T13:48:23Z)

https://wiki.ubuntu.com/UEFI/SecureBoot/DKMS appears to provide a brief overview on the options of using DKMS together with SecureBoot. If I get it right it is not strictly required to disable secure boot with DKMS. Here are the options shown:

1. Sign the kernel module using a trusted key (probably requires interaction with mokutil, MOK stands for MachineOwnerKey). Maybe this does not happen automatically since something is missing from the AMD install scripts.
2. Disable secure boot in UEFI.
3. Disable secure boot in SHIM.

Note1: I don't have an UEFI PC myself so I cannot test anything. I intend to buy a new PC and am collecting information about restrictions due to UEFI.

---

### 评论 #6 — boxerab (2018-01-08T17:13:50Z)

re-opening this as this seems to be an issue for a number of users

---
