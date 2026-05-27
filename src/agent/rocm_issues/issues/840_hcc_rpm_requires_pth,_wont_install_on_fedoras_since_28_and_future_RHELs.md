# hcc rpm requires pth, wont install on fedoras since 28 and future RHELs

> **Issue #840**
> **状态**: closed
> **创建时间**: 2019-07-10T00:31:05Z
> **更新时间**: 2024-05-07T19:53:50Z
> **关闭时间**: 2024-05-07T19:53:50Z
> **作者**: fatmalama
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/840

## 描述

`pth` is gone in fedora and will be gone on next RHEL releases. the `npth` package is the replacement.

since the hcc rpm has a hard dependency on pth it wont install at all.
`  - nothing provides pth needed by hcc-1.3.19242-1.x86_64`

forcing installation, it does work, as npth is the intended replacement for pth.

[(more details)](https://github.com/RadeonOpenCompute/ROCm/issues/567#issuecomment-430500573)

---

## 评论 (1 条)

### 评论 #1 — fatmalama (2019-07-10T00:31:26Z)

it would be nice if it accepted both.

---
