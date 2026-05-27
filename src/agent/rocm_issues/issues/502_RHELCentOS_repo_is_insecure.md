# RHEL/CentOS repo is insecure

> **Issue #502**
> **状态**: closed
> **创建时间**: 2018-08-18T16:11:05Z
> **更新时间**: 2021-01-07T08:43:12Z
> **关闭时间**: 2021-01-07T08:43:12Z
> **作者**: sdh4
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/502

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

The installation http://repo.radeon.com/rocm/yum/rpm/ is insecure and vulnerable to man-in-the-middle attacks that could install trojanized software because: 1. It uses http, not https, and 2. gpgcheck is disabled in the .repo file, presumably because the packages are not signed. 


---

## 评论 (2 条)

### 评论 #1 — duckinator (2019-08-29T13:39:54Z)

It's been over a year since this issue was opened. It'd be really nice to _at least_ have it using HTTPS.

---

### 评论 #2 — ROCmSupport (2021-01-07T08:43:12Z)

Hi @sdh4 
The changes are done and modified long back.
Request you to follow: https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#centos-rhel

Thank you.

---
