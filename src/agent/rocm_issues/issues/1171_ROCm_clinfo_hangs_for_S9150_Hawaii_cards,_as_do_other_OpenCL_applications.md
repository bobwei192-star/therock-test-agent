# ROCm clinfo hangs for S9150 Hawaii cards, as do other OpenCL applications

> **Issue #1171**
> **状态**: closed
> **创建时间**: 2020-07-01T17:39:23Z
> **更新时间**: 2021-06-13T19:19:16Z
> **关闭时间**: 2020-12-17T04:21:37Z
> **作者**: aeronth
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1171

## 描述

The S9150 is still a very reasonably spec'd card for scientific computing, it would be great to see support for these cards under the ROCm framework.

As it stands from browsing numerous other issues, support for gfx701 cards has been thin at best. Any updates on when we can expect to regain functionality in the ROCm universe?

---

## 评论 (4 条)

### 评论 #1 — JMadgwick (2020-07-09T16:21:55Z)

Hawaii/gfx701 used to be supported by ROCm (which is why the Readme still says it has limited support). However, since a bug was introduced in ROCm 2.0, Hawaii GPUs have not worked with ROCm (see #871). ROCm 1.9 is the last version where Hawaii GPUs worked (I have confirmed this myself).
Unhelpfully AMD don't make it clear that old versions of the binaries are available. [E.g. Debian pkgs for 1.9 are available here.](http://repo.radeon.com/rocm/apt/1.9.3/) Installing this older version will get a working ROCm, although Tensorflow etc. were never supported on this platform. HIP/HCC does mostly work.
There has been no word from AMD on gfx701 support, considering the state on Navi support I can't see it ever being reintroduced/fixed.

---

### 评论 #2 — aeronth (2020-09-22T01:33:55Z)

Thank you for the excellent information regarding 1.9 versus 2.0+, I also had the cards working on a previous version of ROCm, but wasn't sure why they stopped functioning after a system upgrade to the latest ROCm. Please give use a fully functional support for your back catalog of hardware AMD. :)

---

### 评论 #3 — ROCmSupport (2020-12-17T04:21:37Z)

Thanks @aeronth 
Due to the latest series of new hardware getting added, we can not support old versions of Asic family. 
Currently we do not support gfx7 devices anymore.
Request to try with gfx9 devices for better performance like MI50(Vega20).
Thank you.

---

### 评论 #4 — TByte007 (2021-06-13T19:19:16Z)

Just a quick question. Are you insane ? Currently the ONLY affordable GPUs are GFX7 and GFX8 ... and GFX8 is NOT REALLY. I'm not buying another AMD card ever. How come nVidia is able to support their older cards and you cant ?!?

---
