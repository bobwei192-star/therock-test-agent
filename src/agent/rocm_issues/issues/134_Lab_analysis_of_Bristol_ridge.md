# Lab analysis of Bristol ridge

> **Issue #134**
> **状态**: closed
> **创建时间**: 2017-06-24T03:03:59Z
> **更新时间**: 2017-07-01T21:37:52Z
> **关闭时间**: 2017-07-01T21:37:52Z
> **作者**: trinayan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/134

## 描述

I was wondering if there is any update on the lab testings of HP 15t V1M95AV containing the new bristol ridge APU's. Are there any know issues with the latest rocm drivers for that device? Also is the functionality to control cpu,gpu,memory frequencies exposed to the user on this platform using something like rocm-smi? 

---

## 评论 (1 条)

### 评论 #1 — gstoner (2017-07-01T21:37:40Z)

ROCm SMI does not work on the APUs. currently, it uses different interface then the dGPU's.   

I was just notified by the president of HSA Foundation he has three of these laptop working with ROCm 1.6

---
