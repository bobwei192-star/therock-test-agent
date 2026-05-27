# E: Unable to locate package cxlactivitylogger

> **Issue #1213**
> **状态**: closed
> **创建时间**: 2020-09-05T19:17:15Z
> **更新时间**: 2020-12-16T05:46:19Z
> **关闭时间**: 2020-12-15T13:04:39Z
> **作者**: tugot17
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1213

## 描述

**Platform: Ubuntu 20.04.01 LTS**

**Problem**
I try to install `tensorflow` as described in the official [tutorial](https://rocmdocs.amd.com/en/latest/Deep_learning/Deep-learning.html#amd-rocm-tensorflow-v2-2-0-beta1-release) `Rocm` seems to be installed properly but I have the problem follwing the steps. 

After command `sudo apt install rocm-libs miopen-hip cxlactivitylogger rccl` I get `E: Unable to locate package cxlactivitylogger`.

What may be the reason or how to fix it?



---

## 评论 (2 条)

### 评论 #1 — xuhuisheng (2020-09-05T23:47:47Z)

Please ignore the cxlactivitylogger. I installed tensorflow_rocm success without it.

---

### 评论 #2 — ROCmSupport (2020-12-15T13:04:39Z)

Hi @tugot17 
Thanks for reaching out.
cxlactivitylogger is no more required and we updated the docs accordingly.
Thank you.

---
