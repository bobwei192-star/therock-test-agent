# HIP vs. HC C++ in rocFFT (question)

> **Issue #336**
> **状态**: closed
> **创建时间**: 2018-02-15T08:42:25Z
> **更新时间**: 2018-06-03T14:41:49Z
> **关闭时间**: 2018-06-03T14:41:49Z
> **作者**: preda
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/336

## 标签

- **Question** (颜色: #cc317c)

## 描述

I'd like to know, why rocFFT is implemented in HIP instead of HC C++? is there a reason to prefer one over the other? performance, API maturity?

(I did look here for a discussion of the various ROCm APIs:
http://rocm-documentation.readthedocs.io/en/latest/Programming_Guides/Programming-Guides.html
)


---

## 评论 (2 条)

### 评论 #1 — ekondis (2018-02-15T18:06:31Z)

Good question. After all according to docs one should choose HIP only if he requires compatibility with NVidia hardware otherwise choosing HC is the norm. Please comment if I'm wrong.

---

### 评论 #2 — gstoner (2018-03-02T23:01:52Z)

@ekondis  Can you try this beta http://repo.radeon.com/misc/archive/beta/rocm-1.7.1.beta.4.tar.bz2

---
