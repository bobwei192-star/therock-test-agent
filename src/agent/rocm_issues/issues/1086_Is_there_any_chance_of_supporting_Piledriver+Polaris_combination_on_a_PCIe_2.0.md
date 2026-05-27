# Is there any chance of supporting Piledriver+Polaris combination on a PCIe 2.0?

> **Issue #1086**
> **状态**: closed
> **创建时间**: 2020-04-21T18:49:35Z
> **更新时间**: 2020-12-01T17:55:14Z
> **关闭时间**: 2020-12-01T17:55:14Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1086

## 描述

Currently Polaris GPUs such as AMD RX 580 and 590 do not work with ROCm when paired with AMD FX processors such as FX 8300, the kfd module shows an error regarding atomics.

> kfd: skipped device 1002:67df, PCI rejects atomics.

I know it is not stated in the documentation that this combo is supported, but will it be supported in the future on a PCIe 2.0?

---

## 评论 (5 条)

### 评论 #1 — boxerab (2020-04-27T17:07:11Z)

I highly doubt it. Time to upgrade ?

---

### 评论 #2 — boxerab (2020-04-27T17:07:36Z)

Nobody wants to be reminded of piledriver these days :)

---

### 评论 #3 — ghost (2020-04-29T09:04:14Z)

Well until AMD decides to stop integrating the PSP chip into its chipsets, or decides to release the source codes of that chip so that we would know what is happening inside our computers in the background, I am not willing to upgrade past Piledriver and related motherboard chipsets.

I am not dumb enough to pay for a backdoor to be implemented into my computer.

---

### 评论 #4 — beatboxa (2020-06-04T13:46:39Z)

I am (and have been) running rocm on an AMD FX 8370 + PCIe 2.0 (+ Vega 64).

See my thread here from last year (and last updated recently for rocm 3.3)

https://github.com/RadeonOpenCompute/ROCm/issues/768

---

### 评论 #5 — jlgreathouse (2020-12-01T17:55:14Z)

Hi @MJaoune

At this time, no, we do not expect to support gfx8 GPUs such as Polaris on systems with PCIe atomics. Please see my responses in #451 (starting from [this post](https://github.com/RadeonOpenCompute/ROCm/issues/451#issuecomment-422835753)) for many more details about why this is the case.

---
