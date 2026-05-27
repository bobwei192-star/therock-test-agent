# Stuck on OpenCl 1.1

> **Issue #601**
> **状态**: closed
> **创建时间**: 2018-11-05T11:37:49Z
> **更新时间**: 2018-11-16T15:02:53Z
> **关闭时间**: 2018-11-16T15:02:53Z
> **作者**: shahratin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/601

## 描述

Added repo http://repo.radeon.com/rocm/yum/rpm/
Installed rocm-opencl-1.2.0
clinfo says:
```
Number of platforms:				 2
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 1.1 Mesa 18.0.5
  Platform Name:				 Clover
  Platform Vendor:				 Mesa
  Platform Extensions:				 cl_khr_icd
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 1.2 pocl 1.1 RelWithDebInfo, LLVM 6.0.1, SPIR, SLEEF, DISTRO, POCL_DEBUG
  Platform Name:				 Portable Computing Language
  Platform Vendor:				 The pocl project
  Platform Extensions:				 cl_khr_icd
```
My system:
Fedora 28 on linux 4.18
Cpu: Intel core i5 8600k
Gpu: Amd RX 560

Is it a mesa issue?

---

## 评论 (6 条)

### 评论 #1 — jlgreathouse (2018-11-05T16:42:05Z)

You appear to have two platforms installed. The first appears to be Mesa, and the second is POCL. Neither of these are supported by AMD.

What are the directory `/etc/OpenCL/vendors/`? What are the contents of all files in that directory?

---

### 评论 #2 — jlgreathouse (2018-11-05T16:43:17Z)

Further questions: have you installed ROCr and libhsakmt (the ROCm Thunk)? Note that while you don't need to install our kernel drivers on Linux kernel 4.18, you do need the runtime and thunk runtime/driver interface layer for ROCm user-level software to talk to your GPU.

---

### 评论 #3 — shahratin (2018-11-05T17:29:24Z)

`/etc/OpenCL/vendors/ ` contains
`amdocl64.icd  mesa.icd  pocl.icd`

I did not have ROCr and libhsakmt installed. So installed `hsakmt rocm-runtime` packages from fedora repo.

---

### 评论 #4 — jlgreathouse (2018-11-05T17:50:26Z)

From what Fedora repo? AMD does not offer a Fedora-specific repo. Do you mean our yum repo on repo.radeon.com (which is meant for RHEL and CentOS)?

---

### 评论 #5 — shahratin (2018-11-05T18:13:11Z)

```
sudo dnf install hsakmt rocm-runtime
Last metadata expiration check: 0:10:55 ago on Tue 06 Nov 2018 00:00:21 +06.
Dependencies resolved.
==============================================================================================================================================================================
 Package                                 Arch                              Version                                                    Repository                         Size
==============================================================================================================================================================================
Installing:
 hsakmt                                  x86_64                            1.0.6-5.20171026git172d101.fc28                            fedora                             50 k
 rocm-runtime                            x86_64                            1.6.1-7.fc28                                               fedora                            204 k

Transaction Summary
==============================================================================================================================================================================
Install  2 Packages
```
I did add repo.radeon.com though and installed `rocm-opencl rocm-clang-ocl rocminfo rocm-smi rocm-utils` from there. Those and above two packages as you have mentioned are all I have installed. Tried to install rock-dkms first but it won't compile so removed that.

Also tried removing mesa.icd from /etc/OpenCL/vendors/, did not help.

---

### 评论 #6 — jlgreathouse (2018-11-05T18:22:30Z)

The versions of the thunk and runtime that are in the fedora 28 controlled repos are not compatible with the newest kernel changes and thus shouldn’t be used with current versions of ROCm.

See this post for more information about getting OpenCL working on your distro. https://github.com/RadeonOpenCompute/ROCm/issues/513#issuecomment-421643966

---
