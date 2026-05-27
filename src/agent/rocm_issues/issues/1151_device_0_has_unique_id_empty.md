# device 0 has unique_id empty

> **Issue #1151**
> **状态**: closed
> **创建时间**: 2020-06-16T17:49:04Z
> **更新时间**: 2020-06-20T14:39:06Z
> **关闭时间**: 2020-06-19T05:12:01Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1151

## 描述

On all my systems the device 0 has unique_id empty while device 1, 2, etc. show the actual unique_id.


---

## 评论 (6 条)

### 评论 #1 — valeriob01 (2020-06-16T17:50:48Z)

I run Ubuntu Focal on those systems.


---

### 评论 #2 — preda (2020-06-18T23:18:57Z)

Please provide a bit more detail:
- how many GPUs, what GPUs. Does the CPU have an integrated GPU? Maybe provide a listing of /sys/class/drm/ for comparison with the number of GPUs. Also, maybe a comparison of the content of /sys/class/drm/card0/ vs. /sys/class/drm/card1/
I suppose there are no errors reported in dmesg?

What does "rocm-smi --showuniqueid" report?


---

### 评论 #3 — valeriob01 (2020-06-18T23:54:33Z)

No errors in dmesg. 2 GPUs, Radeon VII of course. Details later maybe.

---

### 评论 #4 — valeriob01 (2020-06-19T03:37:06Z)

```
/opt/rocm-3.3.0/bin/rocm-smi --showuniqueid


========================ROCm System Management Interface========================
================================================================================
GPU[1] 		: Unique ID: 592c190172fd5d40
GPU[2] 		: Unique ID: c6f220c172dc76bb
================================================================================
==============================End of ROCm SMI Log ==============================

```

---

### 评论 #5 — valeriob01 (2020-06-19T05:12:01Z)

This is a gpuOwl specific issue.

---

### 评论 #6 — valeriob01 (2020-06-20T14:39:06Z)

https://github.com/preda/gpuowl/pull/170

---
