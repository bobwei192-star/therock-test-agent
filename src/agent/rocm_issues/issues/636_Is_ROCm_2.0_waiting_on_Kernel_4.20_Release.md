# Is ROCm 2.0 waiting on Kernel 4.20 Release?

> **Issue #636**
> **状态**: closed
> **创建时间**: 2018-12-18T17:13:47Z
> **更新时间**: 2018-12-21T14:49:49Z
> **关闭时间**: 2018-12-21T14:49:49Z
> **作者**: emerth
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/636

## 标签

- **Question** (颜色: #cc317c)

## 描述

Is ROCm 2.0 waiting on kernel 4.20 release?

I know I keep bugging you guys about this, and I am truly grateful for the work that has gone into ROCm. I just want to understand where it is at in terms of release. 

Places like phoronix report ROCm 2.0 is essentially ready, but my experiences this summer/fall with the Linux 4.19 and 4.20 release candidates make me think the hold up is official OS support. Is this correct?

Thanks again!

---

## 评论 (3 条)

### 评论 #1 — bill-mcgonigle (2018-12-18T20:54:12Z)

Previous messages said 4.19 and EOY for 2.0 (it's not EOY yet...)  I sure hope that's still the case as many distros are targeting 4.19 as the next platform for their releases (e.g. Debian Buster).  Eagerly awaiting solid OpenCL on Buster here...

---

### 评论 #2 — emerth (2018-12-18T21:05:23Z)

> 
> 
> ...it's not EOY yet...

To be sure. It just almost EOY.

;-)

---

### 评论 #3 — jlgreathouse (2018-12-21T14:49:49Z)

Couldn't answer this before the release, since we always like to have a bit of wiggle room on release dates. For example, we might have to delay a release if we find any new major bugs right before release. That didn't happen this time. :)

ROCm 2.0 is out now, and no, we were not waiting on 4.20. We hope to keep on a regular release cycle, so hopefully we'll have ROCm working there soon after it's official.

---
