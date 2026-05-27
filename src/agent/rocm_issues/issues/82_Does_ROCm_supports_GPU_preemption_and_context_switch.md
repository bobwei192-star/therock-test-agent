# Does ROCm supports GPU preemption and context switch?

> **Issue #82**
> **状态**: closed
> **创建时间**: 2017-01-24T05:52:27Z
> **更新时间**: 2017-07-02T17:21:44Z
> **关闭时间**: 2017-07-02T17:21:44Z
> **作者**: FalconBsp
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/82

## 负责人

- hthangirala

## 描述

Most of the HSA docs says it supports GPU preemption and context switch. Can you please give us more details how it is supporting? 

---

## 评论 (1 条)

### 评论 #1 — gstoner (2017-07-02T17:21:44Z)

ROCm support  Pre-emption and Context Switching as described in HSA specification,  now you need to be care using it since there is lot of state in GPU. 

---
