# Is SDMA currently enabled for Polaris on Ubuntu 16.04 ?

> **Issue #650**
> **状态**: closed
> **创建时间**: 2018-12-26T22:22:54Z
> **更新时间**: 2019-01-03T23:18:45Z
> **关闭时间**: 2019-01-03T23:18:45Z
> **作者**: boxerab
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/650

## 标签

- **Question** (颜色: #cc317c)

## 描述

A quote from an older issue :
"One thing that may be hurting this is your using BLIT kernel right now GFX8 for transfers. We had shut off SDMA on Polaris and FIJI due firmware bug, we chased down. Waiting for Firmware developer time to fix it."

So, has this been fixed ? Thanks.

---

## 评论 (4 条)

### 评论 #1 — jlgreathouse (2019-01-03T19:21:00Z)

Hi @boxerab 

At this time our gfx8 GPUs are not using SDMA engines. We have been unable to find enough firmware developer time across our various projects to bring these engines back online for gfx8 on the ROCm stack.

That said, we have made changes to our drivers to enable PCIe extended tags. This allows more outstanding PCIe requests, which allows us to achieve significantly higher bandwidth from our blit kernels on gfx8 GPUs.

---

### 评论 #2 — boxerab (2019-01-03T22:41:21Z)

Thanks @jlgreathouse .  My application is very memory-intense, so the more bandwidth the better. 
Should I expect SDMA to eventually be enabled on gfx8 ?  Or perhaps not, as new chips are on the horizon ?

---

### 评论 #3 — jlgreathouse (2019-01-03T23:10:33Z)

Unfortunately, I can't comment on any timelines for when, or if, the required changes to our SDMA engine firmware would be made. We would obviously like to have this feature, but the development, debug, and verification effort for this needs to be balanced against adding features and squashing bugs on new hardware, and other feature requests etc. on existing hardware.

---

### 评论 #4 — boxerab (2019-01-03T23:18:45Z)

Thanks! 

---
