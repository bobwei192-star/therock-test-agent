# Unofficial RHEL/CentOS 8.0 support??

> **Issue #904**
> **状态**: closed
> **创建时间**: 2019-10-09T11:40:45Z
> **更新时间**: 2020-02-04T16:09:46Z
> **关闭时间**: 2019-10-24T19:24:54Z
> **作者**: wsphillips
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/904

## 描述

I haven't been able to find any open or closed issues asking this:

What's the status of RHEL/CentOS 8.0? Since they natively run kernel 4.18 can we already (or soon) expect support from ROCm kernel drivers?

---

## 评论 (4 条)

### 评论 #1 — kentrussell (2019-10-22T15:07:07Z)

The official stance on supported OSes is detailed at the ROCm README (https://github.com/RadeonOpenCompute/ROCm). We don't officially support 8.0 at this time, and there is no specific timeframe promised, as there are always potential issues that can arise but we are working towards supporting it. Unfortunately, I can't guarantee a release for it right now.

---

### 评论 #2 — rkothako (2019-10-24T06:21:27Z)

Hi @wsphillips 
As per internal distro policy, we will support Cent/RHEL 8.0 from ROCm3.2(around Feb/March time) onwards.

---

### 评论 #3 — wsphillips (2019-10-24T19:24:54Z)

Thanks for the feedback! Good to know there's planned support in the works. Much appreciated.

---

### 评论 #4 — akostadinov (2020-02-04T16:09:46Z)

@rkothako, would you share whether there are chances to see this soon? Or should I expect that a longer delay is expected?

---
