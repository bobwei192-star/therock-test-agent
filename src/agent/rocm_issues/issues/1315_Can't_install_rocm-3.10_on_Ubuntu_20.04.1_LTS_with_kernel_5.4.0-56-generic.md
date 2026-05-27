# Can't install rocm-3.10 on Ubuntu 20.04.1 LTS with kernel 5.4.0-56-generic

> **Issue #1315**
> **状态**: closed
> **创建时间**: 2020-12-02T04:17:26Z
> **更新时间**: 2020-12-14T06:10:24Z
> **关闭时间**: 2020-12-11T04:36:33Z
> **作者**: elliottbinder
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1315

## 描述

First off, I don't know if this is the appropriate place for this but I first ran into this error when trying to install rocm-3.10. I'm getting a similar error to that [listed here](https://community.amd.com/t5/drivers-software/can-t-install-amdgpu-drivers-on-ubuntu-20-04-1-5-4-0-56-generic/m-p/426676).

I can't install rock-dkms, rocm-dkms, or rocm-dev via apt. Similarly when trying to install the Radeon Software for Linux 20.20 Release using the amdgpu-install script, which tries to install amdgpu-dkms. I run into the same issue of this snippet:

```
...
Setting up amdgpu-dkms (1:5.6.0.15-1098277) ...
Loading new amdgpu-5.6.0.15-1098277 DKMS files...
Building for 5.4.0-56-generic
Building for architecture x86_64
Building initial module for 5.4.0-56-generic
Error! Bad return status for module build on kernel: 5.4.0-56-generic (x86_64)
Consult /var/lib/dkms/amdgpu/5.6.0.15-1098277/build/make.log for more information.
dpkg: error processing package amdgpu-dkms (--configure):
 installed amdgpu-dkms package post-installation script subprocess returned error exit status 10
dpkg: dependency problems prevent configuration of amdgpu:
 amdgpu depends on amdgpu-dkms (= 1:5.6.0.15-1098277); however:
  Package amdgpu-dkms is not configured yet.

dpkg: error processing package amdgpu (--configure):
 dependency problems - leaving unconfigured
...
```

I've attached the make log here: [make.log](https://github.com/RadeonOpenCompute/ROCm/files/5626862/make.log)

It looks like it's complaining about some ‘pci_platform_rom’ function not being defined. I wasn't able to find that function anywhere in the included source files under /var/lib/dkms/amdgpu/source, but I was able to find it under the [ROCK-Kernel repo](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/36767d92bdfecb49f2c5f112285b483549420267/drivers/pci/rom.c).

If anyone can help me figure out what's wrong here or what I can do to fix it, I would greatly appreciate it.

---

## 评论 (18 条)

### 评论 #1 — xuhuisheng (2020-12-02T04:30:26Z)

Dumplicate of https://github.com/RadeonOpenCompute/ROCm/issues/1307

---

### 评论 #2 — ROCmSupport (2020-12-02T04:41:16Z)

Hi @elliottbinder 
Thanks for reaching out.
We are able to reproduce this issue locally and working with Kernel team on the fix.
I will update once the fix is available.
Thank you.

---

### 评论 #3 — Dantali0n (2020-12-02T07:38:28Z)

Another ROCm release, another one that is broken flashbacks to 3.9.1~

---

### 评论 #4 — Dantali0n (2020-12-02T07:41:30Z)


[rock-dkms-firmware.0.txt](https://github.com/RadeonOpenCompute/ROCm/files/5627655/rock-dkms-firmware.0.txt)


---

### 评论 #5 — ROCmSupport (2020-12-02T08:43:11Z)

Thanks @Dantali0n 
We are aware of this issue, which is specific to 5.4.0-56, our kernel team is working on the fix.
Thank you.

---

### 评论 #6 — ROCmSupport (2020-12-04T05:35:31Z)

Hi All,
Until the fix is available, we recommend to install ROCm on 5.4.0-54 kernel or hwe kernels.
Thank you.

---

### 评论 #7 — fgnm (2020-12-06T11:59:42Z)

Using 5.6.0 Kernel fixed the compiling issue, I had to update because even switching to 5.4.0-54 compiling fails.

---

### 评论 #8 — Dantali0n (2020-12-07T09:26:22Z)

> Hi All,
> Until the fix is available, we recommend to install ROCm on 5.4.0-54 kernel or hwe kernels.
> Thank you.

Compilation on kernel 5.4.0-54 fails much the same way as 5.4.0-56, however, 5.4.0-53 works for me.

---

### 评论 #9 — ROCmSupport (2020-12-07T09:45:25Z)

Thanks @Dantali0n 
Strange that ROCm works for me with 5.4.0-54.
Anyway my recommendation is to use any working kernel. Good to know that 5.4.0-53 works.
Thank you.

---

### 评论 #10 — boxerab (2020-12-08T21:06:24Z)

I had a similar issue on ubuntu 20.1 with kernel 5.8, with the same error. Will the upcoming fix address 5.8 ?

---

### 评论 #11 — ROCmSupport (2020-12-09T04:33:21Z)

Hi @boxerab 
Its not clear about Ubuntu version and kernel version from your side.
If you are talking about 20.10, I can say NO as we do not officially support non-LTS versions like 20.10.

---

### 评论 #12 — boxerab (2020-12-09T13:35:39Z)

@ROCmSupport I use 20.10 because my RX 480 freezes when I use 20.04 LTS.  Something to do with amdgpu dc settings, I think.

---

### 评论 #13 — ROCmSupport (2020-12-09T13:43:33Z)

Hi All,
Good news is that fix for this issue is ready, validation is in progress and it will be pushed soon.
Thank you.

---

### 评论 #14 — Silverfox28 (2020-12-10T10:43:22Z)

Is the fix ready?

---

### 评论 #15 — ROCmSupport (2020-12-10T12:02:11Z)

Hi @Silverfox28 
Fix is ready, validation is in progress. It will be pushed in a day.

---

### 评论 #16 — ROCmSupport (2020-12-11T04:36:33Z)

Hi @Dantali0n , @boxerab , @elliottbinder , @Silverfox28 
Fix for 5.4.0-56 is ready and pushed too. Updated Documentation accordingly.
Request to try the new packages.

**_Note: AMD ROCm v3.10 fails to install on Ubuntu kernel v5.4.0-56. To resolve the installation issue, new packages for 'rock-dkms' and 'rock-dkms-firmware' are created and replaced. It is recommended to perform a clean and fresh installation with the new packages._**

Thank you.

---

### 评论 #17 — advancingu (2020-12-12T11:53:09Z)

@ROCmSupport So someone in the ROCm team honestly replaced already published packages with a different build and did _not_ release a new package version? Why on earth would anyone think this is a good idea? The ROCm team should _really_ work on establishing a better release process.

---

### 评论 #18 — ROCmSupport (2020-12-14T06:10:24Z)

Hi @advancingu 
As per the management decision, we replaced faulty kernel packages with working ones.
This is not always the process, we have defined rules to follow and based on situation, we act accordingly.
This time management discussed and came up with resolution of replacing both kernel packages with fixed ones and so happened.
Hope you got the point.
Thank you.

---
