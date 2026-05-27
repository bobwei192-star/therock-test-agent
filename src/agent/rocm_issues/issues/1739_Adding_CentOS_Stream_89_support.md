# Adding CentOS Stream 8/9 support

> **Issue #1739**
> **状态**: closed
> **创建时间**: 2022-05-19T12:09:15Z
> **更新时间**: 2024-01-26T05:24:14Z
> **关闭时间**: 2024-01-26T05:24:14Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1739

## 描述

Currently amdgpu-install rpm failed to detect the version of CentOS Stream series as CentOS Stream versioning only use one number (8 or 9) which differs from RHEL's dual number.
As CentOS Stream has different updating model than RHEL it may be tricky to maintain upstream with amdgpu-dkms but rocm repo seems to work fine.
Please add support for CentOS Stream.

---

## 评论 (1 条)

### 评论 #1 — swinzy (2022-09-29T03:58:36Z)

It seems like currently there's still no RHEL 9 support? #1646

---
