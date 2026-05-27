# AMD Vega Frontier causes system hang/boot failure in thunderbolt 3 breakout box with ROCm driver.

> **Issue #613**
> **状态**: closed
> **创建时间**: 2018-11-16T01:06:44Z
> **更新时间**: 2023-12-08T17:46:36Z
> **关闭时间**: 2023-12-08T17:21:09Z
> **作者**: brian-maher
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/613

## 描述

First off, some configuration:

System: Apple iMac (2017).
CPU: i7 7700
Internal GPU: Radeon Pro 580
OS: Ubuntu 18.04.1
ROCm Version: 1.9.1

Thunderbolt Breakout: HP Omen Accelerator (Thunderbolt 3)
eGPU: Vega Frontier (Air Cooled)

Having gotten further than before, I still cannot get this configuration (which should be supported, to work).

I have verified that:

 - ROCm 1.9.1 is installed and working. With the eGPU disconnected, ROCm works and shows the internal graphics card (albeit as a 480 rather than a 580 in clinfo).
 - The TB3 enclosure works. With power disconnected to the GFX card, the TB3 enclosure is detected in Ubuntu. Other features (e.g. USB hub) work, direct access is enabled and the box is authorised.
 - The card/setup work fine under Mac OS - which detects the eGPU perfectly.

I'm experiencing 2 scenarios - if I boot ubuntu then hot plug the eGPU, I get an instant system lockup - to the point where the mouse cursor doesn't move.

If I boot with the eGPU connected, the boot process hangs at "A start job is running for Detect the available GPUs and deal with any system changes). There is a timer on this message, which at the point of writing says 3 hours 30 minutes / no limit - so I think it's safe to say it's hung indefinitely.

Any ideas on this? Happy to do any debugging/changes necessary.

---

## 评论 (7 条)

### 评论 #1 — brian-maher (2018-11-16T01:18:09Z)

Also to note - during a standard apt upgrade I get a message about missing AMD firmware (specifically regarding Vega) - but a quick search shows this is normal and not the cause?

---

### 评论 #2 — brian-maher (2018-12-18T22:54:40Z)

Any suggestions? I have some free time over Christmas so would like to spend some time debugging this!

---

### 评论 #3 — brian-maher (2019-01-08T20:23:16Z)

This is still occurring on 2.0 and I cannot get to the bottom of it. Does anyone have _any_ suggestions at all?

---

### 评论 #4 — ROCmSupport (2021-01-07T10:22:02Z)

Hi @brian-maher 
Request you to verify with the latest ROCm 4.0 and share an update asap.
Thank you.

---

### 评论 #5 — tasso (2023-12-08T17:18:56Z)

Is this still an issue with the latest RCOm? If not; can we please close it?  Thanks!

---

### 评论 #6 — brian-maher (2023-12-08T17:21:09Z)

I cannot confirm as it's been 5 years now and no longer have the hardware.

---

### 评论 #7 — tasso (2023-12-08T17:46:35Z)

Understood!  Thanks for the reply!

---
