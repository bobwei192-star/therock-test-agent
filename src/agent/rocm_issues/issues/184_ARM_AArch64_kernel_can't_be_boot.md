# ARM AArch64: kernel can't be boot

> **Issue #184**
> **状态**: closed
> **创建时间**: 2017-08-22T06:36:47Z
> **更新时间**: 2020-11-18T01:38:35Z
> **关闭时间**: 2017-10-01T15:24:52Z
> **作者**: lintcoder
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/184

## 标签

- **Question** (颜色: #cc317c)

## 描述

I have been trying to build ROCK-Kernel-Driver on my ubunu16.04-arm64 server, here are my steps:
1. make defconfig
2. make
3. sudo make modules_install
4. sudo make install

On the 4th step, there is some message like 'W: mdadm: /etc/mdadm/mdadm.conf defines no arrays.' , 
and when I restart the operating system and select the new kernel, it gets stuck,  and the system can't be started. Output of the terminal is as follows:

Loading Linux 4.9.0 ...
Loading initial ramdisk ...
EFI stub: Booting Linux Kernel...
EFI stub: Using DTB from configuration table
EFI stub: Exiting boot services and installing virtual address map...

please tell me how can I fix it? @gstoner 

---

## 评论 (7 条)

### 评论 #1 — gstoner (2017-08-22T13:34:07Z)

The current most driver is using Kernel 4.11.   

Greg

---

### 评论 #2 — lintcoder (2017-08-24T02:15:31Z)

I use Kernel 4.11 on branch roc-1.6.1 instead, while it still doesn't work, output of the terminal is as follows:
Loading Linux 4.11.0 ...
Loading initial ramdisk ...
EFI stub: Booting Linux Kernel...
EFI stub: Using DTB from configuration table
EFI stub: Exiting boot services and installing virtual address map...
@gstoner 


---

### 评论 #3 — gstoner (2017-08-24T03:07:13Z)

What CPU are you using ?

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: tonglin <notifications@github.com>
Sent: Wednesday, August 23, 2017 7:15:33 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] kernel can't be boot (#184)


I use Kernel 4.11 on branch roc-1.6.1 instead, while it still doesn't work, output of the terminal is as follows:
Loading Linux 4.11.0 ...
Loading initial ramdisk ...
EFI stub: Booting Linux Kernel...
EFI stub: Using DTB from configuration table
EFI stub: Exiting boot services and installing virtual address map...
@gstoner<https://github.com/gstoner>

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/184#issuecomment-324513251>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Duco7nhOooA9hKuA3KRHeghdZgDuBks5sbNzEgaJpZM4O-LKw>.


---

### 评论 #4 — lintcoder (2017-08-24T03:18:19Z)

I am building it on my qemu virtual machine

---

### 评论 #5 — gstoner (2017-08-24T23:49:25Z)

The PCIe Atomics are not passing through the qemu virtual machine 

---

### 评论 #6 — Uditkr (2018-01-12T10:22:24Z)

Did you manage to get fix for this 

---

### 评论 #7 — ericdraken (2020-11-18T01:38:35Z)

Yes, any success?

---
