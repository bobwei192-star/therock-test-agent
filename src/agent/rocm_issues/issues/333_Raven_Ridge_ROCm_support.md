# Raven Ridge ROCm support

> **Issue #333**
> **状态**: closed
> **创建时间**: 2018-02-14T08:29:48Z
> **更新时间**: 2018-03-11T14:37:57Z
> **关闭时间**: 2018-03-11T14:37:57Z
> **作者**: ekondis
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/333

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Hello,
Since first Raven ridge desktop APUs are out, I would love to know what is the plan for supporting raven ridge on ROCm. This gets even more important as currently raven ridge seems to be the only affordable way for doing research on Vega GPU compute.

Thanks in advance.

---

## 评论 (7 条)

### 评论 #1 — zpodlovics (2018-02-14T13:31:37Z)

Hi,
I am also interested. I would like to also know the support plans, especially for the long support plan including the long term versioning support plan (hint: Kaveri support dropped). I would like to also know the known working or recommended products (eg.: used internally for development something like ASUS A88XM-A for HSA)  and bios versions, as it was really important in the past eg.: https://github.com/HSAFoundation/HSA-Drivers-Linux-AMD/issues/7, https://github.com/HSAFoundation/HSA-Drivers-Linux-AMD/issues/6

It's really hard to enable HSA/ROCm/ROCr software support without affordable and easily available hardware in the market and _stable and long term supported software_.

---

### 评论 #2 — ob7 (2018-02-21T13:25:31Z)

does this mean vega laptops are now available?

---

### 评论 #3 — simonwaid (2018-02-23T06:33:29Z)

Vega laptops have been available for some months. Now Raven Ridge Desktop CPUs are out. Unfortunately, Linux support is rather limited. Read: [Phoronix: AMD's Raven Ridge Botchy Linux Support](https://www.phoronix.com/scan.php?page=news_item&px=AMD-Raven-Ridge-Mobo-Linux)

---

### 评论 #4 — smartbitcoin (2018-03-10T17:21:07Z)

no offence , but AMD 's driver always later than the product launch!  should AMD software team feel it's a shame? 

---

### 评论 #5 — gstoner (2018-03-10T18:07:15Z)

No it not a principle priority for ROCm project  It is not primary target for the project .  There is a AMD driver that supports it.  It is called  AMDGPUPRO for Linux.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: SmartBitCoin <notifications@github.com>
Sent: Saturday, March 10, 2018 10:21:08 AM
To: RadeonOpenCompute/ROCm
Cc: Subscribed
Subject: Re: [RadeonOpenCompute/ROCm] Raven Ridge ROCm support (#333)


no offence , but AMD 's driver always later than the product launch! should AMD software team feel it's a shame?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/333#issuecomment-372046457>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuabhqMSQPIJHW-4mXt-2DU9ghcmUks5tdAuEgaJpZM4SE8yr>.


---

### 评论 #6 — ekondis (2018-03-11T11:03:05Z)

@gstoner , though not a primary target for ROCm, this raises a question regarding the particular statement in the readme file:

> Support for future APUs
> We are well aware of the excitement and anticipation built around using ROCm with an APU system which fully exposes Shared Virtual Memory alongside and cache coherency between the CPU and GPU. To this end, in mid 2017 we plan on testing commercial AM4 motherboards for the Bristol Ridge and Raven Ridge families of APUs. Just like you, we still waiting for access to them! Once we have the first boards in the lab we will detail our experiences via our blog, as well as build a list of motherboard that are qualified for use with ROCm.

So, is supporting contemporary APUs still in the plans? Perhaps this paragraph requires an update.



---

### 评论 #7 — gstoner (2018-03-11T14:37:57Z)

We love to do day one support for everything, but we still a small team, the first focus is on building a rich in capability, a stable robust foundation for GPU Computing,  RIght now we been focusing on core driver so we can bring more distro support.     Please be patient with the team 


---
