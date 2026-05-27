# ROCm equivalent of GDS cuFile API

> **Issue #1854**
> **状态**: closed
> **创建时间**: 2022-11-08T06:08:09Z
> **更新时间**: 2026-03-10T15:24:48Z
> **关闭时间**: 2024-02-19T03:12:51Z
> **作者**: Mark1626
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1854

## 描述

Hi,

I understand that P2P communication is available in ROCm through ROCmRDMA

https://rocmdocs.amd.com/en/latest/Remote_Device_Programming/Remote-Device-Programming.html

Is there an equivalent of the cuFile API in the ROCm universe?


---

## 评论 (4 条)

### 评论 #1 — abhimeda (2024-01-30T04:03:53Z)

@Mark1626  Hi, were you able to figure this out? If so can we close this ticket?

---

### 评论 #2 — Mark1626 (2024-01-30T04:23:51Z)

Can you provide an answer to my question? Is there an equivalent of GDS cuFile API planned for ROCm?

---

### 评论 #3 — nartmada (2024-02-16T22:05:25Z)

Thanks @kentrussell for the internal reply.  

@Mark1626, there is currently no cuFile equivalent in ROCm.  

---

### 评论 #4 — brockhargreaves-amd (2026-03-10T15:24:48Z)

@Mark1626 In case you haven't stumbled across it yet, hipFile is rocm's equivalent to cuFile. It landed in the public github last October and is early access preview/development: https://github.com/ROCm/hipFile 

---
