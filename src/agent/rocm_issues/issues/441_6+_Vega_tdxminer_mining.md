# 6+ Vega tdxminer mining

> **Issue #441**
> **状态**: closed
> **创建时间**: 2018-06-26T10:30:51Z
> **更新时间**: 2018-06-27T11:17:02Z
> **关闭时间**: 2018-06-27T11:17:02Z
> **作者**: xenofobia
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/441

## 描述

Hello. Is there any way to run more than 6 Vegas with rocm? I spent last 48 hours trying to run more by using different kernels etc. and still no result.

---

## 评论 (1 条)

### 评论 #1 — gstoner (2018-06-27T11:17:02Z)

We run 12 GPU on servers today.  The issue is your ussing consumer motherboard with out PLX PCIe Gen3  Swtich on x16 or x8 PCIe lane to support Polaris based GPU.   Only. Vega10 today supports abilty to use PCIe Gen2 in x1 lane if you shut off SDMA in 1.8.1 ( this is tempory for this release, future release it just work with SDMA on)  Also we working on getting Firmware addressed to support GFX 8 parts 

---
