# Rpm distros (Fedora, CentOS, etc) support

> **Issue #312**
> **状态**: closed
> **创建时间**: 2018-01-25T04:32:50Z
> **更新时间**: 2018-03-04T16:16:33Z
> **关闭时间**: 2018-01-25T19:41:34Z
> **作者**: uentity
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/312

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Dear AMD devs!

PLEASE, please restore the `rpm` repository support for your `ROCm` project, as it were in release 1.6. A vast majority of Linux distros are left behind now.

I'm running Fedora 27 and can't manage the whole `ROCm` thing to work. My RX 480 and RX 580 GPUs are working just fine with 'legacy' OpenCL driver from AMDGPU-PRO 17.50. But `ROCm` doesn't 'see' nor my Vega, nor Polaris-based cards at all.

If I plug in my Vega 64, Linux kernel 4.11 provided by you in 1.6 release hangs on very early boot stage. I installed pre-release kernel v. 4.15 and dkms-patched (by AMDGPU-PRO 17.50) kernel v. 4.11.11 (from official Fedora 26 repo) and both of them are booting fine with Vega and 3D acceleration works. But ROCm driver bundled with AMDGPU-PRO 17.50 fails (to discover GPUs? or what?) in all cases.

That's why I'm asking kindly to build rpm packages for ROCm v. 1.7. Or should I just give up and install Ubuntu?

BTW, please clarify one question. My system is driven by AMD FX 8120 CPU. **Is it suitable for ROCm when I only want GPU (not CPU) OpenCL computing?**

---

## 评论 (10 条)

### 评论 #1 — matszpk (2018-01-25T08:22:54Z)

Firstly, in the ROCm documentation is written that only Intel Haswell and later and AMD Ryzen processors are supported. You can check whether your graphics card are detected or skipped by AMD KFD (part of the ROCM Kernel driver). If you find similar message in dmesg (just run `dmesg` in root privileges): `kfd kfd: skipped device 1002:XXXX, PCI rejects atomics` then your hardware does not support required PCIE atomics (very likely).

---

### 评论 #2 — uentity (2018-01-25T09:52:52Z)

@matszpk, yep, I see that messages in dmesg (

ROCm documentation (I've read only statement on github and several articles) is a little bit confusing: I was thinking that `Supported CPU` means `support CPU as OpenCL computational device`. Does ROCm aims to support CPU as well as GPU or it is only GPU computing related?

As a developer I can understand AMD position like "Let's start brand new project and support only bleeding edge hardware". But from consumer point of view disabling **all** AMD processors besides the very recent generation is... just bad. And it seems like they DO enable Vega computing on Windows with wider CPU range (not 100% sure about this).

Anyway, thank you very much for your answer.

---

### 评论 #3 — gstoner (2018-01-25T14:54:21Z)

Currently, ROCm does not support the older CPU aka Opeteron, nor AMD FX Processors

- The official install instruction for ROCm https://rocm.github.io/ROCmInstall.html
- Supported hardware https://rocm.github.io/hardware.html
- More on PCIe Atomics or by there other name which is really what they do Atomic Completors https://rocm.github.io/ROCmPCIeFeatures.html 

---

### 评论 #4 — gstoner (2018-01-25T15:07:28Z)

Understand AMD has others stacks that do not need PCIe atomics like AMDGPUpro stack you can use for this combo of hardware.  Also our Windows Stack works without PCIe Atomics. 

This is only required for ROCm stack which when it started was focused on really Enterprise Server Computing which means they are installed in Xeon E5 v3 or newer when we started the project 3 years ago.   We started with HSA technology that more aggressively used Atomic Completor on APU. 

 But  for ROCm we need this capability for number of reason around performance and functionality. 
 The only way we get it is via PCIe Generation 3 devices with Atomics Completor support,  Understand from Intel since Haswell with Core i3,i5,i7 and Xeon E3 and E5  family of products since 2013 so now 5 years ago, they ship about 300+ million CPU per year,  so we have over 1.5 Billion processor install base with PCIe Atomics now.   Also Ryzen, and EPYC now support this.  Which build on this install base.  

  Note key thing we been experimenting with it multi-writer queues which it is not possible to do without atomic support with performance.      

---

### 评论 #5 — gstoner (2018-01-25T15:08:21Z)

On RPM we are bring them back we just had to make the transition to DKMS install first.  We adding Centos and REHL support. 

---

### 评论 #6 — uentity (2018-01-25T17:04:53Z)

@gstoner, there's nothing wrong with ROCm project itself, and I really appreciate your amazing work first of all because 1) it is open source and will be partially shipped with Linux kernel; 2) it has real advantages and performance benefits.

The main disappointment is that I bought a perfect (and relatively expensive) Vega 64 GPU and now if I want decent OpenCL support on Linux **I have to** additionally upgrade whole lot of other equipment including CPU, motherboard and RAM. Yes, I own a fast 8-core AMD FX processor with huge L2/L3 and I don't want to change it, but I simply don't have a choice. Correct me if I'm wrong.

> Understand AMD has others stacks that do not need PCIe atomics like AMDGPUpro stack you can use for this combo of hardware.

How exactly can I use AMDGPUpro stack for OpenCL support on Vega? If this is possible, please, point me on any guideline.

---

### 评论 #7 — uentity (2018-01-25T17:05:59Z)

Nice to hear that rpm repo is upcoming. Thumbs up!

---

### 评论 #8 — gstoner (2018-01-25T18:51:50Z)

AMDGPUpro in 18.10 should remove this for Vega10,  Platform Atomics need only ROCm Driver will need it they are going to OpenCL on different abstraction.  One thing I tell you i worked with both CPU and EPYC is game changer, 

---

### 评论 #9 — uentity (2018-01-25T19:34:00Z)

Great move! So looking for 18.10 release with hope. 
On CPU topic: I bet it is :) will get Ryzen-family CPU one day for sure. But inside software stack you anyway should build this "bridge" from Vega to older CPUs.  👍 

---

### 评论 #10 — alecuba16 (2018-03-04T16:16:33Z)

@gstoner And you will publish the sources for distros like gentoo?

---
