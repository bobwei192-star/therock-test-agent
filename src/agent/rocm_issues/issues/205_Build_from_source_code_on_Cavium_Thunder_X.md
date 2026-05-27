# Build from source code on Cavium Thunder X

> **Issue #205**
> **状态**: closed
> **创建时间**: 2017-09-13T02:40:17Z
> **更新时间**: 2018-06-03T14:58:04Z
> **关闭时间**: 2018-06-03T14:58:04Z
> **作者**: lintcoder
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/205

## 标签

- **Question** (颜色: #cc317c)

## 描述

I am trying to build ROCK-Kernel-Driver from branch roc-1.6.3 on my ubunu16.04-arm64 server which is running on Cavium Thunder X. The kernel version in Makefile of this repo is 4.11.  Here is my environment : 
uname -a
Linux ubuntu 4.4.0-31-generic #50-Ubuntu SMP Wed Jul 13 00:06:30 UTC 2016 aarch64 aarch64 aarch64 GNU/Linux

Here are my steps：
1.make rock-dbg_defconfig
2.make
3.sudo make modules_install
4.sudo make install

there is no error during making. While when I restart the operating system and select the new kernel, it gets stuck, and the system can't be started. Output of the terminal is as follows:

EFI stub: Booting Linux Kernel...
EFI stub: Using DTB from configuration table
EFI stub: Exiting boot services and installing virtual address map...

 I also want to know that, if I can build other source code successfully  including ROCT-Thunk-Interface, ROCR-Runtime, ROCm-Device-Libs, HCC, HIP, etc, with failure on building ROCK-Kernel-Driver ?
@gstoner 


---

## 评论 (3 条)

### 评论 #1 — lintcoder (2017-09-13T02:48:14Z)

Ps: which branch/tag should I choose when I try to build other source code on my  ubunu16.04-arm64 server including ROCT-Thunk-Interface, ROCR-Runtime, ROCm-Device-Libs, HCC, HIP, etc. thanks
@gstoner 

---

### 评论 #2 — gstoner (2017-10-17T13:58:30Z)

One thing we found you had force Atomic Completer on ( PCIe atomics) one you do this it will boot. 

---

### 评论 #3 — gstoner (2017-10-17T13:59:31Z)

We now have been testing ROCm 1.6.4 with HCC,  working on HIP support now. 

---
