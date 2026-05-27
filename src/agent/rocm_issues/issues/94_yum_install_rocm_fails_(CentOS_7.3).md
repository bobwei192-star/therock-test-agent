# yum install rocm fails (CentOS 7.3)

> **Issue #94**
> **状态**: closed
> **创建时间**: 2017-03-06T14:35:43Z
> **更新时间**: 2017-03-07T15:52:59Z
> **关闭时间**: 2017-03-06T15:31:28Z
> **作者**: jrprice
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/94

## 描述

After adding the ROCm repo on CentOS 7.3, running `yum install rocm` fails with the following error:

    Error: Package: llvm-amdgpu-3.9.dev-1.x86_64 (remote)
               Requires: libclang.so.40()(64bit)

Is there some dependency missing here?


---

## 评论 (4 条)

### 评论 #1 — gstoner (2017-03-06T14:46:08Z)

Did you develop bootleg linux kernel for CentOS 7.3,  if no the base AMDGPU driver does not have right kernel driver.

greg

On Mar 6, 2017, at 8:35 AM, James Price <notifications@github.com<mailto:notifications@github.com>> wrote:


After adding the ROCm repo on CentOS 7.3, running yum install rocm fails with the following error:

Error: Package: llvm-amdgpu-3.9.dev-1.x86_64 (remote)
           Requires: libclang.so.40()(64bit)


Is there some dependency missing here?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/94>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuSdyNBISLHwdvaZRoaOTj1SFT-X8ks5rjBm_gaJpZM4MUOZf>.



---

### 评论 #2 — gstoner (2017-03-06T15:31:28Z)

We currently we do not support CentOS 7.3 with ROCm,  reminder for supported OS use this link https://rocm.github.io/install.html

---

### 评论 #3 — jrprice (2017-03-07T15:21:55Z)

Thanks for the information, I've installed a fresh copy of Fedora 23 and the main ROCm installation now succeeds. Installing `amdllvm-clang-omp` fails however (complains about a conflict on `/` with the `filesystem` package), but maybe this package isn't ready for widespread use yet?

I'm unable to run the `vector_copy` sample on the R9 295x2 in this machine (`hsa_init` fails). I notice that this card isn't listed as a supported GPU, even though the R9 290X is. Will this card be supported in the future?


---

### 评论 #4 — jedwards-AMD (2017-03-07T15:52:59Z)

The 295x2 based on the Hawaii architecture, so it could be supported by the ROCm framework. Currently there are no plans to add the device, but I will talk with the development team to see if it can be added.

---
