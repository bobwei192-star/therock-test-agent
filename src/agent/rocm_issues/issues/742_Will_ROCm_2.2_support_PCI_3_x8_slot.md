# Will ROCm 2.2 support PCI 3 x8 slot ?

> **Issue #742**
> **状态**: closed
> **创建时间**: 2019-03-18T19:12:23Z
> **更新时间**: 2019-03-18T19:58:16Z
> **关闭时间**: 2019-03-18T19:58:16Z
> **作者**: boxerab
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/742

## 标签

- **Question** (颜色: #cc317c)

## 描述

I have two cards on my system, one on x16 slot and one on x8 slot.

Only the x16 card has been detected by ROCm for OpenCL, although
`rocm-smi` sees both cards. 

Why can `rocm-smi` see both cards, but `clinfo` only detects one ?

And will both cards be usable for OpenCL in the future ?



---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2019-03-18T19:40:21Z)

It depends on [your GPUs, your motherboard, and potentially your CPU](https://github.com/RadeonOpenCompute/Experimental_ROC/blob/master/distro_install_scripts/Ubuntu/common/component_scripts/01_09_hcc.sh).

 - If your GPUs are from the gfx8 generation, they require the ability to access system memory using PCIe atomics in order for the KFD driver to allow ROCm computation kernels to run.
 - Your motherboard may or may not connect the x8 slot to the system with proper PCIe atomics support.
 - Whether your motherboard's PCIe 3.0 x8 slot has working atomics may depend on your CPU. For instance, a Ryzen APU may have fewer working PCIe connections than a Ryzen CPU even if they both use AM4 sockets.

`rocm-smi` can see any GPU that has a working graphics driver. `rocminfo` and `clinfo` require a working KFD compute connection to show the device.

If you run `dmesg | grep kfd` you will probably find that your second GPU does not have a working PCIe atomics connection to the host.

---

### 评论 #2 — boxerab (2019-03-18T19:58:16Z)

Thanks, @jlgreathouse . Yes, my GPU is a gfx8. I was just hoping that with 2.2 update I wouldn't require atomics to use the card. 

---
