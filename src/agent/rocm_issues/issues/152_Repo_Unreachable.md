# Repo Unreachable

> **Issue #152**
> **状态**: closed
> **创建时间**: 2017-07-06T14:56:45Z
> **更新时间**: 2017-07-06T21:17:17Z
> **关闭时间**: 2017-07-06T16:04:26Z
> **作者**: raxbits
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/152

## 描述

Hi, 

http://repo.radeon.com/rocm  ---> Unreachable 

Fails:
wget -qO - http://repo.radeon.com/rocm/apt/debian/rocm.gpg.key | sudo apt-key add - 

Is it under maintenance by any chance? 

Thanks

---

## 评论 (3 条)

### 评论 #1 — jedwards-AMD (2017-07-06T15:33:56Z)

The repo.radeon.com URL is not accessible inside the AMD corporate network. If you are an AMD employee, you need to use the internal alias.

---

### 评论 #2 — nevion (2017-07-06T18:03:00Z)

@raxbits does this mean you're working for AMD/interning or some other academic based deal?

---

### 评论 #3 — raxbits (2017-07-06T21:17:02Z)

@nevion Transitioning  

---
