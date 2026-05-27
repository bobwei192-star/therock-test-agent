# On AMD Ryzen CPU, OpenCL app runs faster when the CPU is not idle

> **Issue #319**
> **状态**: closed
> **创建时间**: 2018-01-31T01:42:52Z
> **更新时间**: 2018-06-03T14:45:40Z
> **关闭时间**: 2018-06-03T14:45:40Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/319

## 描述

System: Ubuntu 17.10, CPU Ryzen 1700x, Rx Vega64, ROCm 1.7.

case 1: the CPU is idle, save for the OpenCL app which is not using much CPU.
case 2: the CPU is busy, used by mprime https://www.mersenne.org/download/ , which runs with nice -20.

In case 2 (CPU busy), the measured performance of the OpenCL app is about 1.5% faster than in case 1 (CPU idle).


---

## 评论 (3 条)

### 评论 #1 — psteinb (2018-01-31T08:53:47Z)

Just seeing this issue. Could the 1.5% be related to noise on the 
system? In other words, did you try repeated measurements (say 20) of 
the app for each case?


---

### 评论 #2 — preda (2018-01-31T10:38:39Z)

Yes the measures are the total time of 100000 kernel runs. The effect is distinct and reproducible, doesn't look like noise.

I guess a possible explanation is that the CPU enters some sleep mode when not active, and takes a tiny bit of time to wake up when the app needs to do something, and this "wakeup" is not needed when the CPU is "hot".

---

### 评论 #3 — gstoner (2018-06-03T14:45:40Z)

We found out why this has to do with how long it takes the CPU to come out of deep sleep,  we finding we even have manage C-state during transfers 

---
