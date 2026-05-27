# 2 RX 470s on ROCm 1.8 : OpenCL only sees single device

> **Issue #412**
> **状态**: closed
> **创建时间**: 2018-05-12T14:22:25Z
> **更新时间**: 2018-05-12T14:57:19Z
> **关闭时间**: 2018-05-12T14:57:19Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/412

## 描述

I have one GPU on PCI 3 slot, and one on PCI 2.
But clinfo only reports one device.  
My understanding was that 1.8 removes the PCI 3 restriction.


---

## 评论 (1 条)

### 评论 #1 — gstoner (2018-05-12T14:57:19Z)

Aaron, 
     We said this is the case only with Vega10 currently.  Fiji and Polaris right now still need PCIe Gen3 and PCIe Atomics, we looking into this 

---
