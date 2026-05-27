# Kernel 5.10 LTS and ROCm status in kernel LTS

> **Issue #1346**
> **状态**: closed
> **创建时间**: 2020-12-19T10:16:39Z
> **更新时间**: 2020-12-21T06:04:15Z
> **关闭时间**: 2020-12-21T06:04:15Z
> **作者**: perestoronin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1346

## 描述

Now rocm support only 5.4 and oem 5.6 kernel :(

What about adopt rocm 4.0+ for new kernel LTS ?

May be exists patches from enthusiasts ?

---

## 评论 (4 条)

### 评论 #1 — xuhuisheng (2020-12-19T11:04:35Z)

@perestoronin I suggest to use upstream kernel to replace rock-dkms, and install rocm-dev and rocm-libs separately.
I test ubuntu-20.10 which including kernel-5.8, and rocm-dev and rocm-libs run properly.

Actually AMD said upstream kernel can use 15/16 system memory after kernel-5.6. So I think it may be more easy to using upstream kernel.
https://github.com/radeonopencompute/ROCm#rocm-support-in-upstream-linux-kernels

---

### 评论 #2 — lin7sh (2020-12-19T15:22:31Z)

@xuhuisheng Thanks for the information, It seems you have done lots of testing on the latest Linux kernel and Rocm, do you know whether I can compile ROCm 4.0 on arm64 server chip?

---

### 评论 #3 — xuhuisheng (2020-12-19T23:51:50Z)

@mko-io 
Maybe you can try compile llvm with LLVM_TARGETS_TO_BUILD="AMDGPU;X86", I don't have arm chip, cannot test it.

If you mean cross compile x86 target on arm server, I thnk it wont be any difference.

---

### 评论 #4 — ROCmSupport (2020-12-21T06:03:01Z)

Hi @perestoronin 
Thanks for reaching out.
We have not validated with 5.10 LTS and so can not claim official support.
But have 2 suggestions.
1. Though we do not claim official support, ROCm might work on 5.10 kernel, just give a try.
2. Instead of our kernel driver, you can directly use Ubuntu's upstream kernel with rocm-dev. In this case, you need to install ROCm as sudo apt install rocm-dev(which installs user space only on top of upstream kernel).
Hope it helps.
Thank you.

---
