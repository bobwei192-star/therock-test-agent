# I can't install ROCm on Kali linux with kernel 4.19

> **Issue #696**
> **状态**: closed
> **创建时间**: 2019-02-03T16:05:28Z
> **更新时间**: 2022-02-04T13:23:43Z
> **关闭时间**: 2019-02-04T17:14:09Z
> **作者**: antonioprudenzano
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/696

## 描述

When come the time to build the module it gives me an error:

```Unpacking rocm-dkms (2.0.89) ...
Setting up comgr (1.1.0) ...
Setting up rocr_debug_agent (1.0.0) ...
Setting up rocm-smi (1.0.0-95-g3512a29) ...
Setting up rocm-device-libs (0.0.1) ...
Setting up hip_base (1.5.18494) ...
Setting up rock-dkms (2.0-89) ...
Loading new amdgpu-2.0-89 DKMS files...
Building for 4.19.0-kali1-amd64
Building for architecture amd64
Building initial module for 4.19.0-kali1-amd64
Error! Bad return status for module build on kernel: 4.19.0-kali1-amd64 (amd64)
Consult /var/lib/dkms/amdgpu/2.0-89/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
installed rock-dkms package post-installation script subprocess returned error exit status 10
Setting up hsa-ext-rocr-dev (1.1.9-45-ge88639f) ...
Setting up hsakmt-roct (1.0.9-99-g3ba20ce) ...
Setting up rocminfo (1.0.0) ...
Setting up hsa-amd-aqlprofile (1.0.0) ...
Setting up hip_doc (1.5.18494) ...
etting up hip_samples (1.5.18494) ...
dpkg: dependency problems prevent configuration of rocm-dkms:
 rocm-dkms depends on rock-dkms; however:
  Package rock-dkms is not configured yet.

dpkg: error processing package rocm-dkms (--configure):
 dependency problems - leaving unconfigured
Setting up hsakmt-roct-dev (1.0.9-99-g3ba20ce) ...
Setting up hsa-rocr-dev (1.1.9-45-ge88639f) ...
Setting up rocm-opencl (1.2.0-2018121317) ...
Setting up rocm-opencl-dev (1.2.0-2018121317) ...
Setting up rocm-clang-ocl (0.4.0-e605688) ...
Setting up rocm-utils (2.0.89) ...
Setting up hcc (1.3.18482) ...
Setting up hip_hcc (1.5.18494) ...
Setting up rocm-dev (2.0.89) ...
Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
```

I have an RX 580 sapphire nitro, kali linux, kernel 4.19

EDIT:
If i run `hashcat -b -m 0` it uses the AMD Gpu power, but the error in dkms remain.

---

## 评论 (4 条)

### 评论 #1 — jlgreathouse (2019-02-04T17:14:09Z)

The `rock-dkms` module (and thus the `rocm-dkms` meta-package that installs `rock-dkms` and `rocm-dev`) is not supported on kernels above 4.15 at this time. You may be able to [use the upstream kernel driver](https://github.com/RadeonOpenCompute/ROCm#rocm-support-in-upstream-linux-kernels) with your distro. Though I will note that Kali Linux is not a supported distribution for ROCm, so we do not guarantee that it will work.

---

### 评论 #2 — adamluco (2019-07-12T06:37:50Z)

Kernel 4.18 is now supported, any plans to support 4.19?

---

### 评论 #3 — Q2Learn (2020-06-28T03:50:43Z)

For others coming to this problem in the future: Check your available space in your /boot partition. There needs to be enough space for the kernel images. This issue may not be ROCm's fault. I had to delete old initrd images because my /boot was full and it couldn't write the new kernel. And it worked after that. See https://github.com/RadeonOpenCompute/ROCm/issues/1107#issuecomment-628261849

---

### 评论 #4 — octan5 (2022-02-04T13:23:43Z)

https://www.youtube.com/watch?v=BEaCGJtpPP8&ab_channel=%D0%90%D0%BD%D1%82%D0%BE%D0%BD%D0%91%D0%B5%D0%BB%D1%8F%D0%B5%D0%B2)

---
