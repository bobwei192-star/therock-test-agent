# Can I install ROCm 1.8.1 and amdgpu-pro 18.20 at the same time?

> **Issue #440**
> **状态**: closed
> **创建时间**: 2018-06-21T03:32:12Z
> **更新时间**: 2018-06-21T13:31:54Z
> **关闭时间**: 2018-06-21T13:31:54Z
> **作者**: JamesJ-Yuan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/440

## 描述

So I have a rig with a X58 board and a RX 580 and Vega 64 card. Based on my understanding Vega 64 needs ROCm 1.8 to work in Linux with a PCIe 2.0 slot whereas the RX580 needs the old amdgpu-pro drivers for PCIe 2.0. Is it possible to have both drivers installed concurrently?

Alternatively is there any plan to support PCIe 2.0 on Polaris in ROCm? Also are there any other drivers that work for Vega 64 on PCIE 2.0 other than ROCm 1.8?

---

## 评论 (1 条)

### 评论 #1 — gstoner (2018-06-21T13:31:54Z)

No, you can not run both drivers at the same time.   We are looking at Getting GFX8 aka Polaris and FIJI, so they can support PCIe Gen2 slot, but we need updated firmware for this.  This will be in future release,  we waiting on ETA from the respective firmware teams 

---
