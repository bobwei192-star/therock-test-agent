# 6900xt + 6800xt setup: Cannot run OpenCL on second GPU due to missing PCI-E Atomics

> **Issue #1514**
> **状态**: closed
> **创建时间**: 2021-07-08T11:11:07Z
> **更新时间**: 2021-07-09T12:02:44Z
> **关闭时间**: 2021-07-09T08:21:43Z
> **作者**: Mushoz
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1514

## 描述

I am using ROCm to run OpenCL code on two 6xxx series GPUs. However, it is only running on the first GPU that's connected directly to the CPU PCI-E lanes (B550 motherboard). The second PCI-E slot is using PCI-E lanes from the chipset instead, and PCI atomics are not supported there. Dmesg confirms the issue:

`"skipped device XXX, PCI rejects atomics",`

Interestingly, I installed Windows 10 on a spare SSD and I can run OpenCL code on both devices just fine. I know I can simply dual boot, but I mainly use Linux myself. Having to reboot to Windows every single time I want to crunch OpenCL code is NOT a real solution. However, the fact it works flawlessly under Windows show that it is not a technical limitation. It should therefor be possible to get it in a working state under Linux as well.

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-07-09T08:21:43Z)

Thanks @Mushoz for reaching out.
I understood that you are using Navi21 cards.
ROCm currently does not support Navi21 and we have plans to support this card soon, most likely before the end of this year, please stay tuned for the updates.
Meanwhile I recommend to check the Hardware support page for more information: [https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url) and look for CPU section.
Hope this helps.
Thank you.

---

### 评论 #2 — seesturm (2021-07-09T10:27:01Z)

Regarding the "CPU section" in "Hardware support page" (btw the link does not work):
The CPU section was written at a time when PCIe atomics were quite new and ROCm had to use the platforms which were available. But now already several years have passed. The platform of the issue creator (Ryzen + B550 chipset) was developed after ROCm was first released and is in full control by AMD.

Why does this AMD platform not support PCIe atomics on the chipset's PCIe lanes?

---

### 评论 #3 — xuhuisheng (2021-07-09T12:02:44Z)

I think the PCIe atomics requirement is a disaster.
It is hard to explain why the CPU and motherboard cannot run ROCm on some AMD gpu - gfx803 or navi.
Or as this issue, one card can be detected successfully, the other not.

The gfx900, gfx906, gfx908 wont require PCIe atomics for CPU and motherboard, It will be appreciate that we could skip PCIe atomics requirement.

---
