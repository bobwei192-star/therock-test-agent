# Easier documentation for installing on Ubuntu 18.10

> **Issue #653**
> **状态**: closed
> **创建时间**: 2018-12-31T02:07:35Z
> **更新时间**: 2019-01-07T23:53:11Z
> **关闭时间**: 2018-12-31T16:18:08Z
> **作者**: HubKing
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/653

## 描述

I understand that you only support up to Ubuntu 18.04, but Ubuntu 18.10 is the latest version and thus there should be a lot of users. It would be helpful to a lot of users if you just provide some a concise installation note for this specific distribution of Linux.

The current README.md is too complicated and long because it tries to cover lots of versions of lots of distributions. If one has a simple goal of enabling OpenCL on Ubuntu 18.10, the commands that need to be executed should be the same for all Ubuntu 18.10 users.

I have tried to follow the README, but installling rock-dkms caused "Error! Bad return status for module build on kernel: 4.18.0-13-generic (x86_64)" I assumed that this is because this kernel is not supped. So, I have tried the "upstream" way, whatever it is, but when I executed rocminfo, I got "hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-2.0/rocminfo/rocminfo.cc. Call returned 4104", and for "clinfo", I got, "ERROR: clGetPlatformIDs(-1001)".

As I said before, the instruction is scattered throughout the page so it is not really easy to follow for an average user. I mean, not all users are Linux experts. Could you add some concise, easy-to-follow set of commands for popular OS like Ubuntu 18.10?

---

## 评论 (11 条)

### 评论 #1 — nano1900 (2018-12-31T05:47:04Z)

I have same issue[https://github.com/RadeonOpenCompute/ROCm/issues/646](url)

---

### 评论 #2 — jlgreathouse (2018-12-31T16:18:08Z)

@nano1900 your issue is different than what is being requested in this issue,. You are trying to use ROCm 2.0 on Ubuntu 18.04 with a Hawaii-based GPU, a configuration that is (I believe) broken at this time. This issue is about installation directions for Ubuntu 18.10.

@HubKing Ubuntu 18.10 is not an officially supported target for ROCm. In other words, AMD does not give any guarantee that it will work properly on our supported hardware devices, as Ubuntu 18.10 does not go through AMD-internal QA before versions of ROCm are released. While we strive to enable ROCm on as many platforms as possible, we only _officially_ support Ubuntu 16.04, Ubuntu 18.04, and CentOS/RHEL 7.4, 7.5, and 7.6.

I make this distinction because there are dozens of other distros that ROCm _may_ work on, but which AMD does not support. We have tried to write the directions for installing on non-supported distros in a generic way, but we do not plan on adding step-by-step directions for every non-supported distribution. 

First, this list could become unwieldy very quickly: you want Ubuntu 18.10, others want Fedora 28, Fedora 29, Arch, Manjaro, OpenSUSE Leap, OpenSUSE Tumbleweed, SLES, Debian sid, Debian stretch, Gentoo, RHEL-derived flavors like Scientific Linux, various Ubuntu-derived flavors like Mint, etc. etc. 

Second: because AMD does not officially support these distros, any such *specific* directions that we write could quickly go out of date and stop working, and we may not notice.

As such, we have instead written [relatively generic directions](https://github.com/RadeonOpenCompute/ROCm#using-debian-based-rocm-with-upstream-kernel-drivers) and explanations for [what those directions mean](https://github.com/RadeonOpenCompute/ROCm#rocm-binary-package-structure). We do not expect all users to be Linux experts, but at some point we cannot personally walk every user through setting up their unsupported configuration.

All that being said, we *do* have tools for installint ROCm on various not-supported distros available as part of our [Experimental ROC](https://github.com/RadeonOpenCompute/Experimental_ROC) project. At this time, this includes scripts that will ROCm on a fresh Ubuntu 18.10 installation (in `./distro_install_scripts/Ubuntu/Ubuntu_18.10/deb_install/`) as well as Fedora 28 and Fedora 29. Note that this project is not officially supported by AMD (please see the word "experimental" in the name). However, it may help you install ROCm on Ubuntu 18.10.

---

### 评论 #3 — nano1900 (2019-01-01T04:36:56Z)

@jlgreathouse 
i got it, looking forward to good news

---

### 评论 #4 — HubKing (2019-01-01T05:01:21Z)

Thank you for the explanation and the link the the experimental project. I will try the script on the experimental version in a few days. I think that should work for me.

I can understand that you cannot do rigorous testings on all of the versions. Since Ubuntu 18.10 is the latest version, I did not expect ROCm to run perfectly. I was willing to take some minor bugs and occasional crashes. The problem for me was that Ubuntu 18.04 had screen tearing and even after applying fixes, the screen was not as smooth as Ubuntu 18.10. Manjaro Linux uses even newer kernel than Ubuntu 18.10 but the user-supplied (not available for Ubuntu) opencl-amd just works without issues, so I thought it should not be impossible on Ubuntu 18.10.

---

### 评论 #5 — jlgreathouse (2019-01-01T05:27:12Z)

If you only want OpenCL (and you do not want to run HCC, HIP, or any of our libraries), you should be able to do the following on Ubuntu 18.10:

- [Make sure your system is up to date](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#first-make-sure-your-system-is-up-to-date)
- [Add the ROCm repository to your system](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#add-the-rocm-apt-repository)
- Either install all of the ROCm user-level tools, or install just the OpenCL tools:
   - Option 1: [Install the ROCm user-level tools and set up udev permissions](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#using-debian-based-rocm-with-upstream-kernel-drivers)
   - Option 2: [Install `rocm-opencl-dev` instead of `rocm-dev` in the above directions](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#using-debian-based-rocm-with-upstream-kernel-drivers). You can see [this section of the README](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#rocm-binary-package-structure) for more information about the difference between these two packages.
- [Add your user to the `video` group](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#next-set-your-permissions) and [optionally add `/opt/rocm/opencl/bin/x86_64/` to your PATH environment variable](https://github.com/RadeonOpenCompute/ROCm/blob/roc-2.0.0/README.md#test-basic-rocm-installation)

You do not need the `rocm-dkms` or `rock-dkms` packages, because you can use the upstream kernel driver in Ubuntu 18.10.

---

### 评论 #6 — HubKing (2019-01-06T03:15:13Z)

That (installing only rocm-opencl-dev as the comment above) did not work. I still got the same error for "clinfo" and OpenCL was not detected. 

Unfortunately, the experimental script did not work either. I think I will just use Manjaro, or switch to Nvidia.

---

### 评论 #7 — jlgreathouse (2019-01-06T03:52:49Z)

What CPU and GPU do you have? And could you show me the output of `dmesg | grep kfd`?

---

### 评论 #8 — HubKing (2019-01-06T04:27:19Z)

Here is the output of that:

> [    1.113213] kfd kfd: Initialized module
> [    1.114805] kfd kfd: skipped device 1002:67ef, PCI rejects atomics


The CPU is i5-3570K.
The GPU is HIS RX 560 14CU 2GB (http://www.hisdigital.com/un/product2-958.shtml)

PS: I searched the web and found that the ROCm needs Atomics and it is only supported from the Intel's 4th generation. Unfortunately, mine is of 3rd generation. So, my CPU is not supported. I had not read the CPU requirements, because I thought it was for AMD integrated GPU.

---

### 评论 #9 — okovjogurtu (2019-01-07T17:16:48Z)

I use RX Vega 64 on i7-3770k, 

---

### 评论 #10 — jlgreathouse (2019-01-07T17:39:56Z)

Hi @okovjogurtu 

As per [the ROCm hardware requirements](https://rocm.github.io/hardware.html), we currently require PCIe atomics with any "gfx8" based GPU. Your Vega 64 is a "gfx9" based GPU and does not require PCIe atomics. As such, it can be used with your older CPU.

---

### 评论 #11 — HubKing (2019-01-07T23:53:11Z)

I have been deferring the CPU upgrade for the 7nm processor. If the rumour about Ryzen 3700 is true, I will upgrade it. 

---
