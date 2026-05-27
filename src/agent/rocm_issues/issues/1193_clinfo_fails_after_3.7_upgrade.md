# clinfo fails after 3.7 upgrade

> **Issue #1193**
> **状态**: closed
> **创建时间**: 2020-08-21T02:07:51Z
> **更新时间**: 2020-08-22T21:36:21Z
> **关闭时间**: 2020-08-21T02:12:05Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1193

## 描述

no platforms are recognized.

---

## 评论 (1 条)

### 评论 #1 — iszotic (2020-08-22T21:34:07Z)

In Ubuntu 20.04 `/dev/kfd` belongs to `render` so you also have to execute `sudo usermod -a -G render $LOGNAME` to add yourself to this group, or change `/dev/kfd` to `video` group

---
