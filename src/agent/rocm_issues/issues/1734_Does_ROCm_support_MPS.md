# Does ROCm support MPS?

> **Issue #1734**
> **状态**: closed
> **创建时间**: 2022-05-02T05:55:31Z
> **更新时间**: 2024-02-01T13:42:22Z
> **关闭时间**: 2024-02-01T13:42:22Z
> **作者**: yulingao
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1734

## 描述

MPS takes work (e.g. CUDA kernel launches) that is issued from separate processes, and runs them on the device as if they emanated from a single process. As if they are running in a single context. 

I want 2 processes(parent and son process) to share a context. Can ROCm or a AMD GPU have this MPS-like feature?

---

## 评论 (3 条)

### 评论 #1 — ipe-zhangyz (2023-01-10T02:51:35Z)

https://github.com/RadeonOpenCompute/ROCm-docker/issues/62

---

### 评论 #2 — abhimeda (2024-01-26T05:22:09Z)

@yulingao  Hi, is your issue resolved on the latest ROCm? If so can we close this ticket?

---

### 评论 #3 — yulingao (2024-02-01T13:42:22Z)

Yes, please close it. I've been focusing on other research areas lately, and I might be able to address this when I revisit it in the future.

> @yulingao Hi, is your issue resolved on the latest ROCm? If so can we close this ticket?



---
