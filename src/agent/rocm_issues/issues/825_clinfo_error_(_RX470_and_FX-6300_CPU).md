# clinfo error ( RX470 and FX-6300 CPU)

> **Issue #825**
> **状态**: closed
> **创建时间**: 2019-06-20T06:13:59Z
> **更新时间**: 2019-06-28T13:38:01Z
> **关闭时间**: 2019-06-28T13:38:00Z
> **作者**: MikhailKlemin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/825

## 描述

Hello there!
I have followed instructions on https://rocm.github.io/install.html to install the rocm on default Ubuntu 18.04.2 server to the letter. 

Everything installed well, but clinfo gives error, I guess it caused by that PCE-E thing because of very old CPU/mobo I have there. 

I then removed rocm and installed amdgpu-pro 19.20 drivers, it also installed very well, but same error on clinfo (ERROR: clGetPlatformIDs(-1001) ) ... 

I have working rocm on another machine (xeon  v3 and rx-470) ubuntu 18.04.2 desktop with no issues.  

I also had amdgpu-pro worked on same machine I have troubles now, but it was 16.04 I think, and not sure what version of amd drivers it was I think one+ year old.  

Any help would be very appreciated!

---

## 评论 (1 条)

### 评论 #1 — kentrussell (2019-06-28T13:38:00Z)

We require Atomics for ROCm for GFX8 GPUs, and if the motherboard doesn't support it, then we can't run ROCm on that GPU .

The GPU is supported in ROCm by itself (hence it working on the Xeon), but because your RX470 is GFX8 (Polaris10), it requires PCIe atomics in order to run ROCm. 

GFX9-and-newer (Vega) can get by without PCI atomics. Your Xeon V3 supports PCI atomics, but the FX6300 (Piledriver) doesn't, which is why that combo of FX6300+RX470 can't work for ROCm. Sorry that I don't have better news for you. If you want to keep using that CPU+board, you'll need a GFX9-or-newer GPU. And if you want to use that GPU, you'll need a CPU+board that supports PCI atomics.

For more information, see https://github.com/RadeonOpenCompute/ROCm_Documentation/blob/master/Installation_Guide/More-about-how-ROCm-uses-PCIe-Atomics.rst 

You can also refer to https://github.com/RadeonOpenCompute/ROCm#supported-gpus for the whole supported list of GPUs and below that the supported GPUs, with the atomics caveats.

---
