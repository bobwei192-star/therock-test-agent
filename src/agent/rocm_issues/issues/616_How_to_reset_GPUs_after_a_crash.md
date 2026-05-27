# How to reset GPUs after a crash

> **Issue #616**
> **状态**: closed
> **创建时间**: 2018-11-19T00:37:59Z
> **更新时间**: 2023-10-06T00:49:22Z
> **关闭时间**: 2019-10-22T15:42:43Z
> **作者**: MoneroCrusher
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/616

## 标签

- **Question** (颜色: #cc317c)

## 描述

Hi there,

I usually run 12 GPUs in my system and it can happen that a GPU crashes.
I know there is a way to reset the GPU and/or amdgpu kernel module but I don't know how.
Could you please tell me how to put the whole AMD system back in "mint" condition like after a reboot?
Requirement: no reboot
@jlgreathouse @gstoner 

Thanks

---

## 评论 (8 条)

### 评论 #1 — jlgreathouse (2018-12-31T22:42:04Z)

Hi @MoneroCrusher 

Have you tried the `gpu_recovery` mechanism that is [part of our GPU drivers now](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-2.0.0/drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c#L493)? In particular, if you set the kernel driver parameter `amdgpu.gpu_recovery=1`, then [whenever there is a GPU timeout detected](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-2.0.0/drivers/gpu/drm/amd/amdgpu/amdgpu_job.c#L31), it will automatically attempt to reset the GPU and bring it back up.

If you do not want to have these resets attempted automatically, you should be able to [use the debugfs mechanism](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-2.0.0/drivers/gpu/drm/amd/amdgpu/amdgpu_fence.c#L717) to perform a manual GPU reset, even if you have not set the `gpu_recovery` parameter. To do this, (as root) read `/sys/kernel/debug/dri/N/amdgpu_gpu_recover`. `N` in this case is the number of the GPU you wish to reset in the DRI subsystem.

---

### 评论 #2 — MoneroCrusher (2019-01-01T17:08:51Z)

Hi @jlgreathouse 

Thanks for the potential solution.
I am currently not using ROCm because 11 out of 12 of my RX 550 GPUs don't get detected because of lacking PCIe atomics on the PCIe x1 slots.
So I am using AMDGPU-PRO 16.60 for now. Checking out the sysfs folder you mentioned, there was no file called /sys/kernel/debug/dri/N/amdgpu_gpu_recover, however, there was one called /sys/kernel/debug/dri/N/amdgpu_gpu_reset. Is a certain min kernel required for this?

What do you mean by "reading" it automatically resets the GPU (in the manual way)?
Just cat it or what (that didn't work, it just made my machine hang, (ssh'd in it and I had to physically go reset it)?
Also does your solution work for both core crashed GPUs as well as Mem crashed GPUs? And does it unload the faulty GPU from the amdgpu kernel? Because when I try to quit the program with the crashed GPU it's not possible to do so and I have to hard-reset the machine, not even a reboot works.

---

### 评论 #3 — jlgreathouse (2019-01-01T18:56:56Z)

Hi @MoneroCrusher 

I can't really offer any support for amdgpu-pro software here. I don't work with it, and this issue tracker is specifically for ROCm software. That said, in the open source amdgpu (which is also used as a base for amdgpu-pro), the name of that file was changed from `amdgpu_gpu_reset` in [Linux 4.15](https://elixir.bootlin.com/linux/v4.15/source/drivers/gpu/drm/amd/amdgpu/amdgpu_fence.c#L730) to `amdgpu_gpu_recover` in [Linux 4.16](https://elixir.bootlin.com/linux/v4.16/source/drivers/gpu/drm/amd/amdgpu/amdgpu_fence.c#L703). As shown above, the ROCm 2.0 `rock-dkms` driver uses the latter naming scheme, as a number of changes from post-4.15 have been pulled in for it.

It appears that the capability was initially made visible in [Linux 4.6](https://elixir.bootlin.com/linux/v4.6/source/drivers/gpu/drm/amd/amdgpu/amdgpu_fence.c#L644), but I can't speak towards whether it actually works well in kernels that old.

Yes, you should be able to just `sudo cat /sys/kernel/debug/dri/N/amdgpu_gpu_reset`. Maybe this reset mechanism doesn't work in that version of amdgpu-pro. [The mechanism at play here](https://elixir.bootlin.com/linux/v4.20/source/drivers/gpu/drm/amd/amdgpu/amdgpu_device.c#L3151) is logically similar to completely resetting the GPU, so I suspect it should work for both types of lockups.

---

### 评论 #4 — MoneroCrusher (2019-01-02T00:51:21Z)

Hi @jlgreathouse 

I have tried every kernel from 4.12 all the way to 4.20. I provocated a GPU crash by overclocking memory and also core too much, while undervolting and the running the miner program, the GPU would crash after about a minute and the system and ssh access remain intact. I then tried to cat the file but upon doing that the system would immediately freeze. Not even any kernel panics would be displayed on the screen hooked up to the worker, but the screen would just freeze on the spot.

I also changed the core clock of the lowest SCLK table from 200 something to 800SCLK without ever crashing the GPU, so amdgpu_pm_info would show 800 SCLK. I then read the file again, it read successfully and I called pm info again but the SCLK would still be at 800. I would expect a GPU reset to truly reset it, in this case it didn't?

But I found another way: echo 1 > sys/class/drm/cardN/device/remove and then echo 1 > sys/bus/pci/rescan would bring it back in mint condition and with all mods stripped (OC; UV), just like after a reboot. But unfortunately it doesn't do anything when the GPU is crashed, it just waits there indefinitely and doesn't remove it.

I feel like this is a general Linux/AMD GPU issue and not related to drivers, but maybe I'm wrong. Anyhow, I hope we can find a way to do this because it would add big value to the community because I've seen so many posts and complaints about this on dozens of forums.

I also tried AMDGPU-PRO 17.40 and it didn't make a difference. If necessary I can also test ROCm on one GPU but I doubt it would be any different.

Can you recreate the issue on your side?

---

### 评论 #5 — kentrussell (2019-03-12T12:06:59Z)

There were some bugs in the GPU reset code previously (that have been addressed upstream), but I have tested it with the latest amd-staging-drm-next code and it seems to be working correctly when I caused a VM Fault. Can you give it a shot on 2.2 and see if the issue persists? If so, can you grab a dmesg and copy it in? 

The other issue is that the GPU might be stuck due to how you crashed it, since it might not be the traditional "wptr!=rptr" check caused by your undervolting, and could be that the GPU is stuck in a hardware loop, which the GPU reset cannot address, since it's being undervolted. It could be a HW limitation, and thus wouldn't be able to utilize the amdgpu_gpu_recover functionality.

---

### 评论 #6 — kentrussell (2019-03-21T11:37:57Z)

Also, I will be adding a --gpureset flag to the SMI, which will hopefully make it into 2.3, which does the "cat amdgpu_gpu_recover" command. It doesn't work for all GPU hangs, but definitely works for some (from experience)

---

### 评论 #7 — kentrussell (2019-10-22T15:42:43Z)

GPU Reset is available from 2.3. 

---

### 评论 #8 — Tectract (2023-10-06T00:48:40Z)

gpu_reset seems to kill my user session :/ Is there a way to gpu_reset and restore my old user session?

---
