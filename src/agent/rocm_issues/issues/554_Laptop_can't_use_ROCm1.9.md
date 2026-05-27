# Laptop can't use ROCm1.9.

> **Issue #554**
> **状态**: closed
> **创建时间**: 2018-09-21T15:21:37Z
> **更新时间**: 2018-09-30T00:35:31Z
> **关闭时间**: 2018-09-30T00:35:31Z
> **作者**: WeiChunyu
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/554

## 描述

model:OMEN by HP 15-ax211TX
CPU:i5 7300HQ
GPU:RX460
System:Ubuntu 18.04
kernel:4.15.0-20-generic
$ rocminfo 
hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.9/rocminfo/rocminfo.cc. Call returned 4104

$ /opt/rocm/opencl/bin/x86_64/clinfo 
terminate called after throwing an instance of 'cl::Error'
  what():  clGetPlatformIDs
Aborted (core dumped)

$ rocm-smi -p
====================    ROCm System Management Interface    ====================
GPU[0] 		: Cannot get Performance Level: Performance Level not supported
GPU[1] 		: Current PowerPlay Level: off
====================           End of ROCm SMI Log          ====================

$ rocm-smi -d1 -P
====================    ROCm System Management Interface    ====================
GPU[1] 		: WARNING: Empty SysFS value: power
GPU[1] 		: Cannot get GPU power Consumption: Average GPU Power not supported
====================           End of ROCm SMI Log          ====================


---

## 评论 (9 条)

### 评论 #1 — gstoner (2018-09-21T15:39:04Z)

Did you check your not getting blocked by iGPU 

---

### 评论 #2 — WeiChunyu (2018-09-21T16:33:09Z)

Sorry, I don't know.
When ROCm 1.6/1.7, I can used AMD GPU driver.
When ROCm 1.8, I don't need to do anything.

---

### 评论 #3 — jlgreathouse (2018-09-21T16:43:22Z)

Could you please show the outputs of the following commands? Please put them in code blocks (triple back ticks: ```) so that the formatting is reasonable. :)

- `lspci -tv`
- `lspci -n`
- `lsmod`
- `dkms status`
- `lsb_release -a`
- `uname -a`
- `dmesg | grep kfd`
- `dmesg | grep amd`

In addition, just to verify: ROCm 1.8 *did* work with this system? Has anything (including BIOS) changed since this?

---

### 评论 #4 — WeiChunyu (2018-09-22T03:36:21Z)

 ROCm 1.8 works on the same computer. And OS ubuntu16.04.4.  BIOS should not be updated. 

$ dkms status
amdgpu, 1.9-211, 4.15.0-20-generic, x86_64: installed

$ lsb_release -a
No LSB modules are available.
Distributor ID:	Ubuntu
Description:	Ubuntu 18.04 LTS
Release:	18.04
Codename:	bionic

$ uname -a
Linux OMEN-by-HP-Laptop 4.15.0-20-generic #21-Ubuntu SMP Tue Apr 24 06:16:15 UTC 2018 x86_64 x86_64 x86_64 GNU/Linux

$ dmesg | grep kfd
[    1.620048] kfd kfd: Initialized module
[    1.893271] kfd kfd: Allocated 3969056 bytes on gart
[    1.893407] kfd kfd: added device 1002:67ef

[dmesgamd.txt](https://github.com/RadeonOpenCompute/ROCm/files/2407489/dmesgamd.txt)
[lsmod.txt](https://github.com/RadeonOpenCompute/ROCm/files/2407490/lsmod.txt)
[lspci -n.txt](https://github.com/RadeonOpenCompute/ROCm/files/2407491/lspci.-n.txt)
[lspci -tv.txt](https://github.com/RadeonOpenCompute/ROCm/files/2407492/lspci.-tv.txt)




---

### 评论 #5 — jlgreathouse (2018-09-25T19:28:36Z)

Hm, it appears that the driver successfully installed and is loading. However, looking at your partial dmesg output, I see that the device is repeatedly turning off (likely for power control reasons, as your laptop appears to have both an Intel integrated and AMD discrete GPU).

This may be a blunt hammer, but what happens if you set the parameter `amdgpu.runpm=0` on your kernel line in Grub?

Second question: is it possible for you to update your kernel to 4.15.0-34? There have been some minor patches for things like VGA switcheroo backported into -34 since -20, I believe.

---

### 评论 #6 — jlgreathouse (2018-09-25T20:52:45Z)

Oh, and one really simple thing I should've asked right at the beginning. Could you run `groups` and show me the output? I want to make sure your user is still in `video`. :)

---

### 评论 #7 — WeiChunyu (2018-09-29T18:01:05Z)

Thank you very much @jlgreathouse .
/etc/default/grub
GRUB_CMDLINE_LINUX_DEFAULT="quiet splash"  ->  "quiet splash amdgpu.runpm=0"


---

### 评论 #8 — jlgreathouse (2018-09-29T22:59:00Z)

Hi @WeiChunyu 

If you then run `sudo update-grub` and reboot, does anything change? In addition, could you please run `groups` and show the output?

---

### 评论 #9 — WeiChunyu (2018-09-29T23:21:09Z)

I can use it.
close issue

---
