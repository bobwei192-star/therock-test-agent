# ROCm and HCC - Compilation issues and level of support for Tonga GPU

> **Issue #467**
> **状态**: closed
> **创建时间**: 2018-07-25T10:19:14Z
> **更新时间**: 2018-07-25T15:32:16Z
> **关闭时间**: 2018-07-25T15:32:15Z
> **作者**: DGASUK
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/467

## 描述

I posted this issue [https://github.com/RadeonOpenCompute/hcc/issues/810] originally on the AMD drivers site, then on the HCC site and a reference to it here, as someone suggested that gitHub would be a more appropriate place.
it seems as though there may be some pre-requisites for ROCm and HCC (not identified in the installation instructions) that weren't met.
I made some progress and possibly linked the issue with kfdid but wasn't sure what the next step should be - could anyone give me some definitive advice, please?


---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2018-07-25T15:32:15Z)

Hi @DGASUK ,

At the moment, this looks like either an HCC problem or a problem with how you've built and tested HCC. I'm not an HCC developer, however, so I can't debug that problem. That said, since you have a bug open in that issue tracker, I'm going to close this to prevent duplication.

If the bug hunting in the HCC repository finds that this is a problem higher in the software stack (such as with the ROCm installation directions), then please feel free to reopen this bug at that time.

---
