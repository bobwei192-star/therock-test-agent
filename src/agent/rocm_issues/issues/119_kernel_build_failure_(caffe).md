# kernel build failure (caffe)

> **Issue #119**
> **状态**: closed
> **创建时间**: 2017-05-10T23:36:44Z
> **更新时间**: 2017-07-02T01:40:08Z
> **关闭时间**: 2017-07-02T01:40:08Z
> **作者**: maxlem
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/119

## 描述

Hi, not sure where this belongs but I can't complete caffe's opencl branch's test due to a kernel crash. More details here:

https://github.com/BVLC/caffe/issues/5610


---

## 评论 (1 条)

### 评论 #1 — maxlem (2017-05-13T00:27:52Z)

dmesg had not much to add after all:
`
[  119.943603] clang[2141]: segfault at 1028 ip 00000000016fc8e1 sp 00007fffc99bda08 error 4 in clang[400000+250e000
`

---
