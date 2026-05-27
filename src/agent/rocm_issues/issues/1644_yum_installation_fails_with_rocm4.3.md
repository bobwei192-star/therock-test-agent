# yum installation fails with rocm4.3

> **Issue #1644**
> **状态**: closed
> **创建时间**: 2021-12-18T08:55:00Z
> **更新时间**: 2022-01-25T13:05:25Z
> **关闭时间**: 2022-01-25T13:05:25Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1644

## 描述

after satisfying all requirements, yum installation gives out error aboutsome dependency but  problem  is this happens with is ROCm4.3 installation instruction : 

ROCm                                            202 kB/s | 168 kB     00:00
(try to add '--skip-broken' to skip uninstallable packages or '--nobest' to use not only best candidate packages)
Error:
 Problem: package rocm-dkms-4.2.0.40200-21.el7.x86_64 requires rocm-dev, but none of the providers can be installed
  - package rocm-dev-4.2.0.40200-21.el7.x86_64 requires hip-base, but none of the providers can be installed
  - conflicting requests
  - nothing provides perl-File-BaseDir needed by hip-base-4.2.21155.5900.40200-21.el7.x86_64


---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2022-01-25T13:04:33Z)

Hi @gggh000 
Thanks for reaching out.
Let me check this for you.

---

### 评论 #2 — ROCmSupport (2022-01-25T13:05:25Z)

I have tried with 4.5 and did not see any issues.
Can you please try with the latest 4.5 or 4.5.1 and update. Thank you.

---
