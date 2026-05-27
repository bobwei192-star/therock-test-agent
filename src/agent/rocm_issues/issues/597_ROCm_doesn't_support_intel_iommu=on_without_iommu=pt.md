# ROCm doesn't support intel_iommu=on without iommu=pt

> **Issue #597**
> **状态**: closed
> **创建时间**: 2018-11-02T01:34:30Z
> **更新时间**: 2023-12-12T21:51:05Z
> **关闭时间**: 2023-12-12T21:51:04Z
> **作者**: TheGoddessInari
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/597

## 描述

Are there any technical reasons for not supporting regular Intel IOMMU usage without passthrough-only mode? I don't see this problem/limitation documented anywhere.

Using an X99 chipset with IOMMU with full DMAR/interrupt-remapping/x2apic features, ROCm will only give protection faults, unless SWIOTLB is used instead of the IOMMU for any OpenCL-based apps. 

Anything that doesn't use ROCm works correctly in this situation.

---

## 评论 (3 条)

### 评论 #1 — TheGoddessInari (2018-12-06T10:03:37Z)

It's looking as if this may only apply to the second GPU. GPU1 on an ASUS X99-A USB/3.1 is on bus3, and GPU2 is on bus6.

 The error messages always reference bus 6, despite the IOMMU groups being setup correctly.

If GPU2 is set offline, the errors don't occur.

I'm hoping the ROCm developers become active on issues again. ROCm not working with GPU2 when the IOMMU is used for DMA remapping is pretty serious.

And yes, ROCm is the only thing that doesn't work in this case. ROCm also tends to randomly freeze if the IOMMU is used in passthrough mode, without listing any errors.

---

### 评论 #2 — tasso (2023-12-08T17:16:59Z)

Is this still an issue? If not, can we please close it?  Thanks!

---

### 评论 #3 — tasso (2023-12-12T21:51:04Z)

Original ticket is more than a year old and the person that originally opened ticket  has not responded to the latest request.  If this is still an issue, please file a new ticket and we will be happy to investigate it.  Thanks!

---
