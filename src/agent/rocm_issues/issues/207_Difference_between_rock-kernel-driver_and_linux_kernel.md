# Difference between rock-kernel-driver and linux kernel

> **Issue #207**
> **状态**: closed
> **创建时间**: 2017-09-13T08:58:11Z
> **更新时间**: 2018-06-03T14:57:48Z
> **关闭时间**: 2018-06-03T14:57:48Z
> **作者**: lintcoder
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/207

## 标签

- **Question** (颜色: #cc317c)

## 描述

I am trying to build rock-kernel-driver on branch roc-1.6.3, and I want to know if the modification of the rock-kernel-driver bases on linux kernel tree, and all the modified files involved are only in directory drivers/gpu/drm/amd/amdkfd?  @gstoner 

---

## 评论 (1 条)

### 评论 #1 — fxkamd (2017-09-14T15:54:53Z)

There are modifications in other parts of the kernel as well. Mostly in amdgpu (and radeon, though that's just to keep it compiling).

---
