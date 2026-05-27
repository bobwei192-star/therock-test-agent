# Key expired error from ROCm debian repo

> **Issue #496**
> **状态**: closed
> **创建时间**: 2018-08-10T06:41:26Z
> **更新时间**: 2018-08-10T07:12:18Z
> **关闭时间**: 2018-08-10T07:12:18Z
> **作者**: schwarzschild-radius
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/496

## 描述

I am getting the following error while doing `apt update`
        W: An error occurred during the signature verification. The repository is not updated and the previous 
        index files will be used. GPG error: http://repo.radeon.com/rocm/apt/debian xenial InRelease: The             following signatures were invalid: KEYEXPIRED [key]  KEYEXPIRED [key]      KEYEXPIRED [key]
        W: Failed to fetch http://repo.radeon.com/rocm/apt/debian/dists/xenial/InRelease  The following     signatures were invalid: KEYEXPIRED [key]  KEYEXPIRED [key]  KEYEXPIRED [key]

Is there any solution to that?

---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2018-08-10T06:50:13Z)

Yes, please try [adding the new GPG keys](https://github.com/RadeonOpenCompute/ROCm#add-the-rocm-apt-repository).

---

### 评论 #2 — schwarzschild-radius (2018-08-10T07:12:15Z)

Okay. That worked. Thank you

---
