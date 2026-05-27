# apt repo: rocm-dkms contains outdated firmware

> **Issue #527**
> **状态**: closed
> **创建时间**: 2018-09-14T07:26:11Z
> **更新时间**: 2018-12-24T22:48:50Z
> **关闭时间**: 2018-12-24T22:44:28Z
> **作者**: marvind
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/527

## 描述

The rocm-dkms package (currently ver 1.8.199) in the apt repo contains really old firmware, e.g., VCN version 1.24 for raven ridge (linux-firmware.git is at 1.73). From linux kernel 4.19 onwards, raven ridge fails to boot linux with the old firmware (see https://bugs.freedesktop.org/show_bug.cgi?id=107880).

Best regards
Marvin

---

## 评论 (6 条)

### 评论 #1 — kentrussell (2018-09-14T12:14:52Z)

The firmware will be updated in the 1.9 release which should be out later today

---

### 评论 #2 — jlgreathouse (2018-09-14T22:46:58Z)

Hi @marvind 

ROCm 1.9.0 was released. Could you check and see if this fixes your issue?

---

### 评论 #3 — marvind (2018-09-17T07:30:46Z)

Hi,

at least for raven the firmware is still the old one. md5sums:
b54c55d3bfe4ae27303012a48a7f1f1b  /usr/src/amdgpu-1.9-211/firmware/amdgpu/raven_vcn.bin
b54c55d3bfe4ae27303012a48a7f1f1b  amdgpu-1.8-199/firmware/amdgpu/raven_vcn.bin

should be (linux-firmware.git):
467978df90449115c306219500c32767  linux-firmware/amdgpu/raven_vcn.bin

---

### 评论 #4 — kentrussell (2018-09-17T10:00:54Z)

Yep I can confirm that. Some of the firmware didn't get updated, so Raven VCN is still the one from 2017. I'll see if I can sneak it into 1.9.1, if not it'll be 1.9.2 but thanks for pointing this out. We have had some issues aligning some of the firmware through our automated testing and the VCN firmware slipped through the cracks.

---

### 评论 #5 — kentrussell (2018-09-25T11:16:02Z)

It will have to be 1.9.2. 1.9.1 is already in testing and is very focused on Vega20. 

---

### 评论 #6 — jlgreathouse (2018-12-24T22:44:28Z)

I believe this was fixed as of ROCm 1.9.2, and (checking the md5sums for raven_vcn.bin) it should also be fixed in ROCm 2.0.0.

---
