# Question: Supported Ryzen motherboard with dual Fiji setup.

> **Issue #92**
> **状态**: closed
> **创建时间**: 2017-03-02T17:37:34Z
> **更新时间**: 2017-07-02T17:26:14Z
> **关闭时间**: 2017-07-02T17:26:14Z
> **作者**: briansp2020
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/92

## 描述

Hi,
I was wondering what motherboard to get for Ryzen 7 1700 + dual Fiji setup for ROCm. Does B350 chipset support dual setup using ROCm? I'm looking at uATX setup and it looks like only B350 chipset is available on uATX form factor.

So far, I found two ASUS Prime B350M-A/CSM and Gigabyte AB350M-D3H. But they are out of stock at the moment. :(

---

## 评论 (2 条)

### 评论 #1 — gstoner (2017-03-02T19:53:21Z)

Even we do not have these boards yet.   We just getting your commercial board like you.  We only had internal development boards.   We let you know which one we like.

G
On Mar 2, 2017, at 11:37 AM, Brian <notifications@github.com<mailto:notifications@github.com>> wrote:


Hi,
I was wondering what motherboard to get for Ryzen 7 1700 + dual Fiji setup for ROCm. Does B350 chipset support dual setup using ROCm? I'm looking at uATX setup and it looks like only B350 chipset is available on uATX form factor.

So far, I found two ASUS Prime B350M-A/CSM and Gigabyte AB350M-D3H. But they are out of stock at the moment. :(

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/92>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8Dua8w3uIlsbMoygrviYiilaqisEGlks5rhv5fgaJpZM4MRTM0>.



---

### 评论 #2 — gstoner (2017-07-02T17:26:14Z)

On the Ryzen CPU it only supports 32 Lane of PCIe Gen3,  for Computing you want your GPU close to the CPU.  you need a motherboard that supports a x16 lane and second x8 lane with full x16 slot 

---
