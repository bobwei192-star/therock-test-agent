# invalid argument to reshape in toy autoencoder

> **Issue #931**
> **状态**: closed
> **创建时间**: 2019-11-08T06:14:48Z
> **更新时间**: 2019-11-13T21:00:22Z
> **关闭时间**: 2019-11-13T21:00:22Z
> **作者**: boldingd
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/931

## 描述

Summary of your hardware:
CPU: Ryzen 7 1700x
GPU: Radeon RX Vega 64
Motherboard: ASRock X370 Gaming X

PCIe Information: output of lshw attached

Something is throwing up InvalidArgumentError at a random point during training.

I built a toy autoencoder using keras; at a random point during training, it dies with an error.  My code is never using tf.reshape, so presumably this is something internal.

The failure happens at a random point several epochs in; it's failed as early as the 7th epoc, and its failed after the 100th.

I have attached a minimal program that reproduces the bug, and sample output.

[random crash.py.txt](https://github.com/RadeonOpenCompute/ROCm/files/3823173/random.crash.py.txt)
[error snipped.txt](https://github.com/RadeonOpenCompute/ROCm/files/3823178/error.snipped.txt)



---

## 评论 (2 条)

### 评论 #1 — boldingd (2019-11-08T06:15:29Z)

oops, forgot lshw
[hw.txt](https://github.com/RadeonOpenCompute/ROCm/files/3823185/hw.txt)


---

### 评论 #2 — sunway513 (2019-11-13T21:00:22Z)

Hi @boldingd , please refer to the following issue:
https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/325
We have pushed out a fix in HIP runtime, which will be part of ROCm3.0 release.
Before that, you can use the following docker container:
sunway513/tensorflow:rocm2.9-tf1.15-dev-hipEventRecord-patch

---
