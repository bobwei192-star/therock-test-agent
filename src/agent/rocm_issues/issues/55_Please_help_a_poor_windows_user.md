# Please help a poor windows user

> **Issue #55**
> **状态**: closed
> **创建时间**: 2016-12-17T17:22:39Z
> **更新时间**: 2017-01-10T18:15:23Z
> **关闭时间**: 2017-01-10T18:15:23Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/55

## 描述

First of all, congratulations on the latest release.

My situation is:

1. C++ application with OpenCL 1.2 kernels, running on windows but is portable to Linux.
(video compression app, makes heavy use of OpenCL images, events )
2. Windows 10 Crimson with 2x 470 4GB cards
3. i7 6600 CPU, ASUS mb

I am looking for a simple, tested, step-by-step guide to getting my app running on ROCm.

i.e.

1. which operating system (hopefully xubuntu, since I am familiar with that)
2. which graphics drivers
3. how to do the ROCm install

I tried installing xubuntu 16.04 a few months ago when I got my system, but I wasn't able to get the graphics drivers to recognize the cards, so had to wipe and install windows 10.  But,  I would like to use Linux as my main target OS, so ROCm will be perfect if I can get it running.

Any guidance here would be greatly appreciated. 

Thanks!
Aaron 


---

## 评论 (4 条)

### 评论 #1 — rjfnobre (2016-12-18T20:53:12Z)

You just need to install ROCm as explained in the README.md.

Just do:
wget -qO - http://packages.amd.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add -
sudo sh -c 'echo deb [arch=amd64] http://packages.amd.com/rocm/apt/debian/ xenial main > /etc/apt/sources.list.d/rocm.list'
sudo apt-get update
sudo apt-get install rocm

Restart your computer and your good to go.

For the operating system I think Ubuntu 16.04 is a solid choice.

---

### 评论 #2 — boxerab (2016-12-18T22:31:43Z)

thanks @rjfnobre .  So, I would like to use 16.04. What about graphics drivers ? 

---

### 评论 #3 — rjfnobre (2016-12-19T08:59:15Z)

The drivers are included in ROCm.

**From the REAME.md:**
> As a result, the ROCK driver is composed of several components based on our efforts to develop the Heterogeneous System Architecture for APUs, **including the new AMDGPU driver**, the Kernel Fusion Driver (KFD), the HSA+ Runtime and an LLVM based compilation stack for the building of key language support.

---

### 评论 #4 — boxerab (2016-12-19T14:20:15Z)

Great, thanks! Have you managed to build an OpenCL app with ROCm ? I noticed you were having some difficulties earlier.

---
