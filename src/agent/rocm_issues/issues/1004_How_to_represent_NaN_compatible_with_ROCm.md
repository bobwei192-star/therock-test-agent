# How to represent NaN compatible with ROCm?

> **Issue #1004**
> **状态**: closed
> **创建时间**: 2020-01-22T13:34:51Z
> **更新时间**: 2020-01-23T17:37:55Z
> **关闭时间**: 2020-01-23T17:37:55Z
> **作者**: pbelevich
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1004

## 负责人

- b-sumner

## 描述

I tried to use std::nan("") and std::nanf("") but got this:

error:  'nan':  no overloaded function has restriction specifiers that are compatible with the ambient context ...

---

## 评论 (3 条)

### 评论 #1 — AlexVlx (2020-01-22T22:46:28Z)

Soft assigning to @b-sumner since this is his area of expertise.

---

### 评论 #2 — b-sumner (2020-01-22T23:19:17Z)

HIP (and Cuda) provide float nanf(const char *) and double nan(const char *) device functions to create NaNs.

---

### 评论 #3 — pbelevich (2020-01-23T17:37:55Z)

thanks!

---
