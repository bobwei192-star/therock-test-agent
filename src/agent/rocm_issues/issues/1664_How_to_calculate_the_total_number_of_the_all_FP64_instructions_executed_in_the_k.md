# How to calculate the total number of the all FP64 instructions executed in the kernel?

> **Issue #1664**
> **状态**: closed
> **创建时间**: 2022-02-03T08:43:18Z
> **更新时间**: 2024-03-22T23:32:53Z
> **关闭时间**: 2024-03-22T23:32:53Z
> **作者**: vasslavich
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1664

## 描述

Hello!
I analyzing the performance of a several scientific libraries. And, I'd like to understand an actual arithmetic complexity of each. Which metrics of rocproof  I should use for this goal? 

I guess SQ_INSTS_VALU, then _the total number_ will be equal: 
`CU_NUM * SIMD_NUM * SQ_INSTS_VALU`.  Where, for AI100: `CU_NUM` is 120 CU, `SIMD_NUM` is 4. It's correct?

Thanks!

---

## 评论 (6 条)

### 评论 #1 — Maxzor (2022-02-05T04:15:18Z)

First, isn't `SIMD_NUM` 16, not 4 even on your CDNA MI100?
Then I would be surprised if `SQ_INSTS_VALU` was only FP64 instructions!

---

### 评论 #2 — ROCmSupport (2022-02-07T11:29:21Z)

Hi @vasslavich 
Thanks for reaching out.
Let me assign to one of the developers to help you. Thank you.

---

### 评论 #3 — vasslavich (2022-02-07T12:08:14Z)

Hi, 
A note, actually I'd like to know the total number FP64 for to calculate/comparision FLOPS of these specific kernels. It can be very interesting.

---

### 评论 #4 — rwnorth (2023-12-13T20:35:26Z)

Hi @vasslavich, we have a metric for this on MI200 but not MI100. Is this still needed?

rocprofiler/src/core/counters/metrics/derived_counters.xml
The metric is called TOTAL_64_OPS

---

### 评论 #5 — nartmada (2024-02-01T01:43:55Z)

Hi @vasslavich, do you still need help from AMD on this ticket?  If not, please close the ticket.  Thanks.

---

### 评论 #6 — nartmada (2024-03-22T23:32:53Z)

Closing this ticket as there is no response from @vasslavich.  Please re-open if you are still looking for total number of all FP64 instructions executed in the kernel.

---
