# Support for Centos 7.9 Kernel version 3.10.0-1160

> **Issue #1615**
> **状态**: closed
> **创建时间**: 2021-11-07T01:14:15Z
> **更新时间**: 2021-11-10T14:21:28Z
> **关闭时间**: 2021-11-10T12:51:05Z
> **作者**: orensg1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1615

## 描述

I have recently upgraded a Centos 7.9 machine to the latest kernel version: 3.10.0-1160
Unfortunately ROCm upgrade has failed.
According to:  https://github.com/RadeonOpenCompute/ROCm 
Only CentOS 7.9 kernel 3.10.0-1127 is supported by ROCm
Are there any plans to support kernel version 3.10.0-1160?
Are there any alternatives to downgrading the kernel version?



---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2021-11-10T12:51:05Z)

Hi @orensg1, Thanks for reaching out.
I certainly understood the problem.
Yes, we validated 3.10.0-1127 with CentOS 7.9 and hence official support is given.
We started validating 3.10.0-1160 with our internal builds and things are pretty good. So next ROCm release will have official 3.10.0-1160 support.
Hope its clear.
Thank you.

---

### 评论 #2 — orensg1 (2021-11-10T14:21:28Z)

Great, thank you.

---
