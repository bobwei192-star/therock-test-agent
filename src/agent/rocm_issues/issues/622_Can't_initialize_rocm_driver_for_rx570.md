# Can't initialize rocm driver for rx570

> **Issue #622**
> **状态**: closed
> **创建时间**: 2018-11-25T11:35:29Z
> **更新时间**: 2019-01-02T22:54:05Z
> **关闭时间**: 2019-01-02T22:54:05Z
> **作者**: nazarpechka
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/622

## 描述

I am currently running such a setup:
MB - Msi z270 A pro
CPU - intel core i3-7100
GPU - AMD Rx 570, installed in second x16 pcie 3.0 slot
RAM - 8gb ddr4
Kernel - 4.10.17
OS - Ubuntu 16.04

Before i had amdgpu-pro drivers installed, but now i want to use tensorflow with my amd gpu. So i uninstalled amdgpu-pro, installed rocm, but when i try running python tensorflow script, i get an error:
`2018-11-25 13:14:06.572026: I tensorflow/core/platform/cpu_feature_guard.cc:141] Your CPU supports instructions that this TensorFlow binary was not compiled to use: SSE4.1 SSE4.2 AVX AVX2 FMA
terminate called after throwing an instance of 'ihipException'
  what():  std::exception`

Command `dmesg | grep 'kfd'` gives this output:
`[   17.588141] kfd kfd: Initialized module
[   17.642852] kfd kfd: skipped device 1002:67df, PCI rejects atomics`

Overall, something seems to be wrong with PCIe atomics support in my setup, but all components seem to be compatible. Thanks.

---

## 评论 (6 条)

### 评论 #1 — briansp2020 (2018-11-25T15:09:28Z)

> GPU - AMD Rx 570, installed in **second** x16 pcie 3.0 slot

Why second slot? Usually, unless the MB support Cross Fire or SLI, only the first slot supports PCIe 3 with atomic operation.

---

### 评论 #2 — nazarpechka (2018-11-25T15:11:27Z)

> Why second slot? Usually, unless the MB support Cross Fire or SLI, only the first slot supports PCIe 3 with atomic operation.

 First slot isnt working, it burned out a year ago for some reason. i have another motherboard with working slot, but i can replace it if its really necessary

---

### 评论 #3 — maxcr (2018-11-25T15:27:28Z)

amdkfd needs to be added to initramfs BEFORE video driver. Second AMDGPU-PRO does not work with this. You need regular open-source AMDGPU kernel module. If you're using Arch Linux binaries must be rebuilt with every kernel upgrade.

---

### 评论 #4 — nazarpechka (2018-11-25T15:29:47Z)

> amdkfd needs to be added to initramfs BEFORE video driver. 

Could you share how to do this?

>Second AMDGPU-PRO does not work with this

I mentioned in post that i had it before, but uninstalled it before installing rocm. Can it still be a problem?

>Third, if you're using Arch Linux binaries must be rebuilt with every kernel upgrade.

I'm on ubuntu

---

### 评论 #5 — maxcr (2018-11-25T15:43:37Z)

`https://wiki.ubuntu.com/Initramfs`

I haven't used Ubuntu in years but it shouldn't be too difficult. Just make sure you have `radeon` and `amdgpu-pro` blacklisted in `modprobe.d` and `amdgpu` DOES show up when you type `sudo lsmod |grep amdgpu`

---

### 评论 #6 — jlgreathouse (2018-11-27T06:21:01Z)

Hi @nazarpechka 

The issue is that the PCIe slot you're using does not support PCIe 3.0 atomics between your CPU and your GPU. Looking at your [motherboard's specification page](https://www.msi.com/Motherboard/Z270-A-PRO/Specification), this board claims that the 2-slot solution is supported in "x16/x4 mode". However, if I look at the [Ark specification page for your processor](https://ark.intel.com/products/97455/Intel-Core-i3-7100-Processor-3M-Cache-3-90-GHz-), your CPU only supports a total of 16 directly-connected lanes (in "1x16, 2x8, 1x8+2x4" modes).

As such, I strongly suspect that the second PCIe slot on your motherboard is connected through the chipset and does not support forwarding PCIe atomics between the processor and the GPU. You can see this in the KFD output that says `[ 17.588141] kfd kfd: Initialized module [ 17.642852] kfd kfd: skipped device 1002:67df, PCI rejects atomics`.

That said, if you really want to verify this, you can build a new version of [lspci](https://github.com/pciutils/pciutils) (the one in Ubuntu 18.04 is too old to show atomics) and see the connections between your CPU and your GPU using `./lspci -t`. You can then look at each of the devices between your CPU and GPU and see if they support atomics using `./lspci -vvv` and looking for `AtomicOpsCap:` field.

---
