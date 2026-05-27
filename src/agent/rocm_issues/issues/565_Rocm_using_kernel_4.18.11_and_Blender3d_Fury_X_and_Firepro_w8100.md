# Rocm using kernel 4.18.11 and Blender3d Fury X and Firepro w8100

> **Issue #565**
> **状态**: closed
> **创建时间**: 2018-10-01T08:44:27Z
> **更新时间**: 2021-01-07T08:37:01Z
> **关闭时间**: 2021-01-07T08:37:01Z
> **作者**: delolat
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/565

## 描述

After installing Rocm 1.9.0 with kernel 4.18.11, I noticed that out of the 2 cards I only see my Fury X. Furthermore upon entering blender I don't see any opencl cards unlike amdgpu-pro. I'm trying to figure out if Rocm 1.9 currently work with blender 2.79, and does Rocm even support Firepro w8100? Or is the kernel version too new? I don't see great documentation on what actually has been tested officially. 

---

## 评论 (5 条)

### 评论 #1 — jlgreathouse (2018-10-08T18:59:33Z)

Documentation for supported and enabled hardware is available [here](https://rocm.github.io/hardware.html). We have code that enables FirePro W8100 (Hawaii) GPUs, but we do not guarantee support for these devices.

Note that to enable Hawaii (Sea Islands) support, you may need to pass the kernel boot parameter `amdgpu.cik_support=1`. `cik_support` defaults to `1` in our custom ROCK kernel drivers, but depending on how your drivers were built in your 4.18.11 kernel (I don't know what distribution you're using, nor what their kernel compile-time parameters are), Sea Islands support may be disabled. You may also need to blacklist the older `radeon` driver to ensure it doesn't also load and try to take control of your Hawaii GPU.

`echo 'blacklist radeon' | sudo tee /etc/modprobe.d/blacklist-radeon.conf`

Could you show me the output of the following commands?
* `dmesg | grep amd`
* `dmesg | grep radeon`
* `dmesg | grep kfd`
* `lsmod`
* `cat /sys/module/amdgpu/parameters/cik_support`

---

### 评论 #2 — jlgreathouse (2018-10-08T19:01:26Z)

Blender questions have been raised in [other](https://github.com/RadeonOpenCompute/ROCm/issues/503) [issues](https://github.com/RadeonOpenCompute/ROCm/issues/555), so I would recommend following those for your other question.

---

### 评论 #3 — delolat (2018-10-09T06:41:48Z)

Am using Kubuntu 18.04 sorry. I switched back to pro, since I was able to get amdgpu-pro installed and working again after figuring out what kernel version it needed to be installed under. 

xorg.log doesn't list Firepro w8100 so it is turned off. I didn't know it was a matter of turning off and on, thanks. When you guys get rocm and blender working in cycles I will be back. 

---

### 评论 #4 — delolat (2018-11-26T07:33:00Z)

So I recently had problems trying to  upgrade the amdgpu-pro drivers from 18.20 to 18.30 where it couldn't install correctly on kernel 4.15.0-39, so I gave rocm another chance. It works. 

I was following some set of instructions to install on kernel 4.18, where I didn't install rocm-dkms or rock-dkms which somewhat worked as they displayed opencl properties in clinfo, but did not display opencl options in blender. I encountered the same problem when I went to install opencl only with rock-dkms. The rocm-dkms gave me an error when installing that kernel 4.18.20 was not a valid kernel or something, but after restarting it registered in clinfo and shows up in blender and is able to render.  

Am currently using this on Kubuntu 18.10. Had to create an amdgpu.conf that I placed in /etc/modprobe.d with
options radeon cik_support=0
options amdgpu cik_support=1
to enable my firepro w8100 as well. 

---

### 评论 #5 — ROCmSupport (2021-01-07T08:37:01Z)

Hawaii is no more officially supported with ROCm, please check: https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support
Thank you.

---
