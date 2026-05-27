# Asus STRIX Z270H Gaming, two GPUs is max, right?

> **Issue #366**
> **状态**: closed
> **创建时间**: 2018-03-18T21:01:06Z
> **更新时间**: 2018-05-12T13:12:33Z
> **关闭时间**: 2018-05-12T13:12:33Z
> **作者**: cucub
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/366

## 描述

Hi, just to confirm I got it right.
My Asus STRIX Z270H Gaming (consumer) motherboard has following PCIe slots:
one PCIe x16
one PCIe x8
one PCIe x2
three  PCIe x1

From this 6 PCIe slots, only the first two can be used by ROCm/atomics because the other four are less than x8, right? 
There is no "amd_iommu=on iommu=pt" GRUB kernel command line options that can enable any of the other PCIe slots so that more than two GPUs can be used, right?

---

## 评论 (2 条)

### 评论 #1 — gstoner (2018-03-18T21:28:29Z)

Currently you should use the x16 and x8 lanes 

---

### 评论 #2 — gstoner (2018-05-12T13:12:33Z)

Now with ROCm 1.8 you can use any slot

---
