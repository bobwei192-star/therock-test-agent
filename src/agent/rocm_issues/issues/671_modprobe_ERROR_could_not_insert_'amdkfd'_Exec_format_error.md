# modprobe: ERROR: could not insert 'amdkfd': Exec format error

> **Issue #671**
> **状态**: closed
> **创建时间**: 2019-01-15T05:32:08Z
> **更新时间**: 2019-01-16T02:25:50Z
> **关闭时间**: 2019-01-15T17:30:48Z
> **作者**: emerth
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/671

## 描述

Install fresh Ubuntu 18.04.1 Workstation.
System:
R5 2600X
RX Vega 64
X470 ASUS board
kernel 4.15.0-43-generic #46-Ubuntu SMP
GCC 7.3.0


Follow instructions on ROCm page.

Reboot.

No amdkfd loaded. Load it manually...

> sudo modprobe  amdkfd
_modprobe: ERROR: could not insert 'amdkfd': Exec format error_

I am actually getting this on above machine and another with same specs but an RX470 instead of a Vega 64.

I have upgraded kernel to 4.18: romc-dkms install says kernel 4.18 HEADERS(!) not supported.
I have upgraded kernel to 4.19: romc-dkms install says kernel 4.19 not supported.
I have upgraded kernel to 4.20: romc-dkms install says kernel 4.20 not supported.

Using amdkfd driver from Ubuntu's 4.18 kernel series the HIP sampels run, but for example hipCaffe fails most of it's unit tests.

I haven't got much hair left... has anyone else seen this, and manage to make the damned thing install?

---

## 评论 (7 条)

### 评论 #1 — jlgreathouse (2019-01-15T06:10:54Z)

The ROCm 2.0 DKMS driver is not supported on kernel versions above 4.15 at this time. If you would like to use an upstream kernel, please [follow these directions](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#using-debian-based-rocm-with-upstream-kernel-drivers) and install `rocm-dev` instead of `rocm-dkms`. This will avoid the installation of the `rock-dkms` driver package.

As of ROCm 2.0, there is no need to have the `amdkfd` module loaded. The KFD code has been integrated into the `amdgpu.ko` driver. And you can't easily modprobe `amdgpu` after your system boots, since it is bringing up your GPU. Instead, it should be part of your initramfs.

If you are on 4.15.0-43 and you are having problems, could you show me the output of:
- `dmesg | grep amd`
- `dkms status`
- `modinfo amdgpu`

If you would prefer an automated way of installing ROCm you might look through the deb installation scripts that are available in the [Experimental ROC project](https://github.com/RadeonOpenCompute/Experimental_ROC).

Finally, I will note that ROCm 2.0 does not currently work with upstream Pytorch. Please see [this note](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#pytorchcaffe2-with-vega-7nm-support).

---

### 评论 #2 — emerth (2019-01-15T14:32:21Z)

@jlgreathouse - thanks!

The ROCm home page is rather misleading in this case. I quote:

"Supported Operating Systems - New operating systems available

The ROCm 2.0.x platform supports the following operating systems:

    Ubuntu 16.04.x and 18.04.x (Version 16.04.3 and newer or kernels 4.13 and newer)
    CentOS 7.4, 7.5, and 7.6 (Using devtoolset-7 runtime support)
    RHEL 7.4, 7.5, and 7.6 (Using devtoolset-7 runtime support)"


Which really does not say "kernels 4.13 to 4.15, otherwise use the in kernel driver".

---

### 评论 #3 — emerth (2019-01-15T14:35:26Z)

The computer gods must be angry at me.

I cannot edit my post immediately above.

I scrubbed the install, so can't post the info you requested.

---

### 评论 #4 — jlgreathouse (2019-01-15T17:30:48Z)

@emerth For what it's worth, Ubuntu 16.04.5 and Ubuntu 18.04.1 use kernel version 4.15.0 with Canonical-backported patches. If you are installing other custom kernels, you are not running a supported configuration and I cannot claim that we will offer technical support. I don't think it's our responsibility to test every possible thing you could change on your system and then list whether we support it or not.

Anyway, if you can't post the requested info, then I don't think we have a way to try to solve this problem for you. I have been unable to reproduce any such problems on Ubuntu 18.04 when using supported kernel configurations.

---

### 评论 #5 — emerth (2019-01-15T23:20:48Z)

For what it's worth, Ubuntu has a repo for kernels. This is where I was getting updated kernels. I was not building them by hand.

Description:  https://wiki.ubuntu.com/Kernel/MainlineBuild
Files for download: https://kernel.ubuntu.com/~kernel-ppa/mainline/?C=N;O=D

For example, IIRC, the 4.18.x kernels from kernel.ubuntu.com contain an amdkfd module that ROCm works with ROCm, as described here - https://github.com/RadeonOpenCompute/ROCm#rocm-support-in-upstream-linux-kernels.

 

---

### 评论 #6 — jlgreathouse (2019-01-16T00:35:15Z)

Hi @emerth 

Yep, I'm familiar with Ubuntu's mainline kernel PPA. I use it quite frequently for testing various kernel / userland software configurations when issues are ROCm issues are raised by users. It's much nicer than compiling kernels by hand, for sure.

That said, PPA is not an "official" distribution channel like the Ubuntu [Main or even Universe](https://help.ubuntu.com/community/Repositories/Ubuntu) repositories. To wit: "[By default, Ubuntu systems run with the Ubuntu kernels provided by the Ubuntu repositories. ... These [mainline] kernels are not supported and are not appropriate for production use.](https://wiki.ubuntu.com/Kernel/MainlineBuilds)"

I'm not saying it's a bad thing to use them, only that when we say "ROCm is supported on Ubuntu x", we mean that it is supported on the listed Ubuntu version(s) running the Ubuntu kernels from the Ubuntu repositories as supported by Canonical. Other configurations, while perfectly valid for many uses, are outside of our hands and we do not claim that AMD will support them. :)

---

### 评论 #7 — emerth (2019-01-16T02:25:50Z)

Hi @jlgreathouse - received and understood! 

---
