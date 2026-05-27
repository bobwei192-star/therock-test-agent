# Using OpenCL/ROCm on device running display

> **Issue #675**
> **状态**: closed
> **创建时间**: 2019-01-16T19:43:14Z
> **更新时间**: 2020-05-15T21:51:30Z
> **关闭时间**: 2019-03-14T20:51:50Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/675

## 描述

The Hardware I'm using: Ryzen 3 2200G with an XFX Radeon RX 560 (Confirmed to be Polaris 11 by lspci -vnn) on an Asrock A320M-DGS. The GPU is inserted into the only PCIe 3.0 slot which has 16 lanes. I'm using the ROCm repository as outlined in "Getting Started" with an up-to-date version of Ubuntu 18.04.1.

I initially just tried to run the rocminfo and clinfo binaries, and then tried to compile and run the square sample code. I'd expect them all to work as intended, however, they all experience a segmentation fault.

I uninstall rocm-dkms, reboot, and install clinfo by itself without ROCm and friends. I find that the only device that clinfo can find is the Ryzen 3 2200G.

So, is it possible to use ROCm or OpenCL on the device that is currently running the screen, or do I have to switch my display over to the 2200G?

---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2019-01-16T21:54:51Z)

At this time, [we do not support](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/issues/66) running ROCm on a system that has both an integrated GPU as well as discrete GPU(s). This is a known problem, but I do not have a public timeline for when it will be fixed.

If you would like to use ROCm 2.0 on your discrete GPU, you will need to disable your integrated GPU in your system BIOS.

---

### 评论 #2 — akostadinov (2020-05-15T21:51:30Z)

@Knuckl3head , could you confirm whether Asrock A320M-DGS has proper wiring for PCI atomics?

---
