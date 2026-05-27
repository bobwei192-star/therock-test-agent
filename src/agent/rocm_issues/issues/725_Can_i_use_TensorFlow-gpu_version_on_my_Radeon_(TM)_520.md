# Can i use TensorFlow-gpu version on my Radeon (TM) 520 ?

> **Issue #725**
> **状态**: closed
> **创建时间**: 2019-03-06T14:54:58Z
> **更新时间**: 2019-03-06T17:44:41Z
> **关闭时间**: 2019-03-06T17:44:41Z
> **作者**: Maryem-Bouhadda
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/725

## 标签

- **Question** (颜色: #cc317c)

## 描述

*(无描述)*

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-03-06T17:44:41Z)

Hi @mariem1bouhadda 

Your Radeon 520 is not supporte din ROCm. It is a "Hainan" chip, part of the Sea Islands generation (gfx601) that is [not supported in ROCm](https://rocm.github.io/hardware.html).

---
