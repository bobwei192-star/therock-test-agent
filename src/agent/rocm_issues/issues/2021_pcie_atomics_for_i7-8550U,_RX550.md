# pcie atomics for i7-8550U, RX550

> **Issue #2021**
> **状态**: closed
> **创建时间**: 2023-04-06T02:20:46Z
> **更新时间**: 2025-04-23T09:55:39Z
> **关闭时间**: 2024-09-23T20:05:07Z
> **作者**: d7zda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2021

## 描述

howdy,
i would like to use pcie atomics for rocm but im not sure if my hardware can do it.

it seems this is a common problem with laptop motherboards that are using these specific components
my laptop : Lenovo Thinkpad e480 i7-8550Ucpu , RX550gpu  - Ubuntu 22.04

i understand that in many cases its a hardware limitation, so i included some outputs with more detail in hopes of pinpointing the problem,  please have a quick look and thanks in advance :

[pcieatomics-issue.txt](https://github.com/RadeonOpenCompute/ROCm/files/11165682/pcieatomics-issue.txt)


---

## 评论 (4 条)

### 评论 #1 — xuhuisheng (2023-04-06T03:23:23Z)

I spent a lot of time to try to challenge this atomic issue on polaries card, two years ago.

The fact is, if you used RDNA1/2 on a old version of amgpu firmware, the dkms report reject device for atomic feature, too. If you upgrade your amdgpu firmeware to latest version, like ROCm-5.x, the dkms will get the new firmware won't need atomic feature, so we can use RDNA1/2 without atomic feature support.

This taught me that the AMD just don't want to modify their codes to support the old polaris card. the RDNA1/2 is just a new card, so they want to cost time to modify fireware to let them run property without atomic.

So our question is how to beg AMD to let us study and modify their firmware?

But they wont feedback to how to debug polaris card. So I wont give any hope on it.
<https://github.com/RadeonOpenCompute/ROCm/discussions/1838>

---

### 评论 #2 — harkgill-amd (2024-08-21T15:29:46Z)

Hi @d7zda, apologies for the lack of response. To check for PCIe atomic support, please run the following command `grep flags /sys/class/kfd/kfd/topology/nodes/*/io_links/0/properties` and provide the output.

---

### 评论 #3 — harkgill-amd (2024-09-23T20:05:07Z)

@d7zda, closing this issue out. If you are still experiencing issues related to PCIe atomics, please leave a comment and I will re-open this ticket. Thanks!

---

### 评论 #4 — mikhailnov (2025-04-23T09:55:38Z)

Did you try HDMI sound when atomics is not supported? Does it work well?

---
