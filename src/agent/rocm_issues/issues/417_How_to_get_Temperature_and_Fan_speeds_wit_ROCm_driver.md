# How to get Temperature and Fan speeds wit ROCm driver

> **Issue #417**
> **状态**: closed
> **创建时间**: 2018-05-14T22:23:52Z
> **更新时间**: 2018-06-03T14:14:41Z
> **关闭时间**: 2018-06-03T14:14:41Z
> **作者**: minzak
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/417

## 描述

Modern GPU cards has a lot control point for temperature and several fan speed.
Maybe it is possible to control fan speed, and LED activity?
And native sensors/lm-sensors - very primitive.
Thanks.

---

## 评论 (2 条)

### 评论 #1 — gstoner (2018-05-14T22:35:48Z)

We are working on new System Management API, to update this it what the Linux driver team promoted to access the critical registers 

---

### 评论 #2 — gstoner (2018-06-03T14:14:41Z)

This is where the new library will be placed it has monitoring feature now 
https://github.com/RadeonOpenCompute/rocm_smi_lib

---
