# RHEL/Fedora binaries?

> **Issue #7**
> **状态**: closed
> **创建时间**: 2016-04-27T12:33:52Z
> **更新时间**: 2016-05-01T20:33:29Z
> **关闭时间**: 2016-05-01T20:33:28Z
> **作者**: psteinb
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/7

## 描述

As long as the RHEL/Fedora rpms and contained binaries are not around, where do I find some documentation how to build ROCm from source?


---

## 评论 (2 条)

### 评论 #1 — jedwards-AMD (2016-04-27T14:38:19Z)

Each of the components have instructions on building the specific component, so you can go that route if you like. However, there are two features planned in the near future that will aleiviate this issue for you:

1) We are planning on creating a universal build script that will build all the core components from the ROCm repository automatically.
2) We are planning on adding a rpm repository this week.

I will update this item when the rpm repository becomes available.


---

### 评论 #2 — jedwards-AMD (2016-05-01T20:33:28Z)

The binaries have been posted on the packages.amd.com repository server. Please follow updated instructions for installing.


---
