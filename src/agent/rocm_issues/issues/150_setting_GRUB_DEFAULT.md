# setting GRUB_DEFAULT 

> **Issue #150**
> **状态**: closed
> **创建时间**: 2017-07-05T12:24:03Z
> **更新时间**: 2017-07-05T16:23:52Z
> **关闭时间**: 2017-07-05T16:23:52Z
> **作者**: newling
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/150

## 描述

This part of the README install instructions is not super-clear, I don't know what `GRUB_DEFAULT` should be set to.

> If using grub2 as your bootloader, you can edit the `GRUB_DEFAULT` variable in the following file:
> ```
> sudo vi /etc/default/grub
> sudo update-grub
> ```



---

## 评论 (1 条)

### 评论 #1 — gstoner (2017-07-05T13:49:17Z)

I have been working on new getting started instructions

https://rocm.github.io/ROCmInstall.html

Install or update ROCm

sudo apt-get update
sudo apt-get install rocm rocm-opencl-dev


Then, make the ROCm kernel your default kernel. If using grub2 as your bootloader, you can edit the GRUB_DEFAULT variable in the following file:

sudo nano /etc/default/grub


set the GRUB_Default Edit: GRUB_DEFAULT=”Advanced options for Ubuntu>Ubuntu, with Linux 4.9.0-kfd-compute-rocm-rel-1.6-77”

sudo update-grub



On Jul 5, 2017, at 7:24 AM, James Newling <notifications@github.com<mailto:notifications@github.com>> wrote:


This part of the README install instructions is not super-clear, I don't know what GRUB_DEFAULT should be set to.

If using grub2 as your bootloader, you can edit the GRUB_DEFAULT variable in the following file:

sudo vi /etc/default/grub
sudo update-grub


—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/150>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuRXCMrprOpmmvgqHbmTlVpkH06YPks5sK4BkgaJpZM4OOQxd>.



---
