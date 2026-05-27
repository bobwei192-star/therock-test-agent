# MSI 970A- G46 (AMD) Motherboard - ROCm - Question on Why PCIe Gen2 x1 lanes to not work -Work Around Found

> **Issue #192**
> **状态**: closed
> **创建时间**: 2017-09-01T18:32:27Z
> **更新时间**: 2017-10-17T14:01:41Z
> **关闭时间**: 2017-10-17T14:01:41Z
> **作者**: Angel996
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/192

## 描述

Hello.

I am trying to use ROCm platform with amdgpu-pro-17.30.465504 drivers on my mining rig with 4 AMD GPUs (RX 470/480/570, mixed), motherboard MSI 970A- G46 (AMD), as remedy for lowered hashrate when mining with ETHash algorithm (the DAG issue). 

ROCm does seem to solve this issue (by adding `amdgpu.vm_fragment_size=9` to grub), however, my rig does not boot with 4 GPUs as usual, it only boots with 3 GPUs. I tried moving GPUs around the slots, it seems the problem is not the GPU count, but a certain PCIE 1x slot that causes ROCm to fail, but I'm not sure about this. After removing the 4th GPU the system gets all unstable and I have to reboot it several times (also using nomodeset option) to get it back to working state. If I choose previous kernel (4.4.0-62-generic) in grub menu, motherboard boots fine with 4 GPUs and works as intended.

The error msg I see in boot log with ROCm kernel and 4 GPUs looks something like this:

`AMD-Vi: Completion-Wait loop timed out` (lots of these messages)
`AMD-Vi: Event logged [IOTLB_INV_TIMEOUT] device=06:00.0 address=0x00000000798e0840` (these messages repeating for a while, then motherboard hangs dead exactly at this msg)

PCIE device #6 is actually the 4th GPU I am trying to add to that 1x slot.

Tried both BIOS and UEFI mode. All GPUs have vbios modded. I have 3 rigs with identical motherboards, and they all have this same issue. Tried moving GPUs around, same problem.

---

## 评论 (18 条)

### 评论 #1 — AirSquirrels (2017-09-02T00:22:56Z)

Is the 1x slot perhaps PCIe 2.0? ROCm requires PCIe 3.0 due to the use of PCIe atomics

---

### 评论 #2 — gstoner (2017-09-02T00:50:33Z)

It depends on the system



Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: AirSquirrels <notifications@github.com>
Sent: Friday, September 1, 2017 7:22:58 PM
To: RadeonOpenCompute/ROCm
Cc: Subscribed
Subject: Re: [RadeonOpenCompute/ROCm] ROCm 1.6 problem with 4 GPUs onboard (#192)


Is the 1x slot perhaps PCIe 2.0? ROCm requires PCIe 3.0 due to the use of PCIe atomics

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/192#issuecomment-326709142>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuZO0y8v73tWHypzkJkbeWwKoOAb1ks5seJ_igaJpZM4PKfci>.


---

### 评论 #3 — Angel996 (2017-09-02T08:07:49Z)

AirSquirrels, there are two 16x and two 1x slots. Only one 1x solt is causing problems.

---

### 评论 #4 — gstoner (2017-09-02T11:31:17Z)


Ok is this an AMD® FX, Phenom II system? 
 
Is it this motherboard? 

https://www.msi.com/Motherboard/970A-G46.html#hero-specification
CPU • 64bit AMD® FX, Phenom II X6/X4/X3/X2, Athlon II X4/X3/X2 and Sempron CPU in AM3 / AM3+ package.Please refer to CPU Support for compatible CPU; the above description is for reference only.Hyper Transport Bus
--

If so one issue I am not PCIe Gen3 slot on the motherboard 
• 2 PCI Express 2.0 x16 slots 
• 2 PCI Express 2.0 x1 slots
• 2 PCI slots, support 3.3V/ 5V PCI bus Interface.

Currently, for multi-gpu testing, we use Xeon E5, Intel core i7 Extreme Editions, AMD EPYC and Threadripper processor.    We have 4 and 8 GPU system we load at standard config for testing.  

---

### 评论 #5 — gstoner (2017-09-02T11:39:19Z)

One thing the configs i sent out for ROCm driver for Polaris will not work with amdgpu-pro-17.30.465504 this is using a different the historical OpenCL driver Foundation.  The same foundation we had on old Catalyst Linux drivers.  Compiler + Userland System Runtime ( ORCA).    Also, the ROCm packages will not work on this driver since they did not enable the correct capabilities in the base driver for GFX 8 based devices.  



ROCm system runtime needs a CPU that supports PCIe atomics to operate user-mode queues properly. 

---

### 评论 #6 — Angel996 (2017-09-02T12:41:34Z)

 It's not really the issue of not working at all. It's just that 4th GPU is not working. When I boot the motherboard with 3 GPUs, the slots are still PCIE 2.0 and CPU is still AMD AM3. How come it all works with 3 GPUs and adding 4th GPU messes it up? There must be a fix for this.

Should I try an older version of amdgpu then?

---

### 评论 #7 — Angel996 (2017-09-02T12:52:41Z)

FOUND A FIX!

adding `amd_iommu=on iommu=pt` to GRUB_CMDLINE_LINUX seems to fix the problem. I was able to boot with 4 GPUs fine, no any of the mentioned err messages appeared.

p.s. I'm no Linux Guru. I just searched the net for people who had the same err message, and found that this fix helped them. Looks like, this error is not related to ROCm, but to amdgpu. Because I also have this error on default Linux kernal too, when shutting down the computer (sometimes). Computer would get stuck in `AMD-Vi: Completion-Wait loop timed out` loop and I'd have to turn it off forcefully.

---

### 评论 #8 — gstoner (2017-09-02T13:22:34Z)

@Angel996 What processor are you ussing?

---

### 评论 #9 — Angel996 (2017-09-02T14:02:08Z)

CPU is Athlon II X2 245.

---

### 评论 #10 — gstoner (2017-09-02T14:03:06Z)

@Angel996  Your running ROCm 1.6.3 from our repo?

---

### 评论 #11 — Angel996 (2017-09-02T14:17:36Z)

I got it from `http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key`

---

### 评论 #12 — fxkamd (2017-09-05T19:16:25Z)

Please don't install amdgpu-pro and ROCm at the same time. Depending on the order in which you install them, you may get very different results. ROCm installs a complete kernel. amdgpu-pro compiles just the kernel module on the target machine against the running kernel with DKMS.

Parts of ROCm are included in amdgpu-pro, but only supported on Vega10.

Looks like you're trying to run ROCm on Polaris10 GPUs. So just don't install amdgpu-pro.

To see what's going on on your system, I'd need to see a complete kernel log and the output from lspci -vv as root.

---

### 评论 #13 — Angel996 (2017-09-05T21:44:14Z)

I had Ubuntu general kernel installed. Then I installed amdGpu. Then I installed ROCm kernel. I did not reinstall amdgpu AFTER installing ROCm kernel.

I have an update. I had to shut down my rigs today. So, after a few hours I turned them on, and I had the same error again. One rig started ok, the other two started spurting out `AMD-Vi: Completion-Wait loop timed out` messages again and hanging on boot. All I could do is try to reboot them several times, so finally, I got them to boot normally, also using booting with `nomodeset` flag and rebooting afterwards.

It seems that somethings happens when machines are powered down.

So, I guess the complete fix is not found yet. 

---

### 评论 #14 — fxkamd (2017-09-05T21:46:53Z)

DKMS may try to compile the amdgpu-pro kernel module against the ROCm kernel. Your configuration is complicated and unusual enough as it is (with multiple mismatched GPUs). Let's not make it worse by adding unnecessary variables.

Still waiting to see kernel logs and lspci -vv. Without that I can't give you any more help.

---

### 评论 #15 — Angel996 (2017-09-05T22:01:10Z)

I'm sorry, I seem to have overlooked the request for logs. Attached them now. Thanks for your help.

[logs.zip](https://github.com/RadeonOpenCompute/ROCm/files/1279081/logs.zip)




---

### 评论 #16 — fxkamd (2017-09-05T22:11:39Z)

Your main board doesn't support PCIe atomics, and the KFD initialization is failing. That means, whatever you're testing isn't actually using ROCm. You're probably just using the older non-ROCm OpenCL from the amdgpu-pro driver. As it is, your system can't support ROCm. You'll need a mainboard with PCIe v3 support. The relevant log messages are below:

[    9.331640] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[    9.331845] [drm] Initialized amdgpu 3.18.0 20150101 for 0000:01:00.0 on minor 0
...
[   10.940075] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[   10.941977] [drm] Initialized amdgpu 3.18.0 20150101 for 0000:02:00.0 on minor 1
...
[   12.572303] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[   12.574191] [drm] Initialized amdgpu 3.18.0 20150101 for 0000:04:00.0 on minor 2
...
[   14.268456] kfd kfd: skipped device 1002:67df, PCI rejects atomics
[   14.270339] [drm] Initialized amdgpu 3.18.0 20150101 for 0000:07:00.0 on minor 3
...


---

### 评论 #17 — Angel996 (2017-09-05T22:14:58Z)

Ok, but `amdgpu.vm_fragment_size=9` fixed the low hashrate problem with mining. If I remove it, hashrate drops about 20%. Does that mean, it's being done simply by amdgpu itself and it has no relation to ROCm?

---

### 评论 #18 — fxkamd (2017-09-05T22:23:17Z)

Yes, the fragment size is an amdgpu parameter. It affects all clients running on amdgpu, including OpenGL and the amdgpu-pro OpenCL. I'm not sure if the fragment size fix is already included in the latest amdgpu-pro release.

---
