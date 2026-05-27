# rocm installation issue in my pc

> **Issue #930**
> **状态**: closed
> **创建时间**: 2019-11-07T13:34:14Z
> **更新时间**: 2023-12-18T16:25:07Z
> **关闭时间**: 2023-12-18T16:25:07Z
> **作者**: kabish01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/930

## 描述

hsa api call failure at: /data/jenkins_workspace/compute-rocm-rel-2.9/rocminfo/rocminfo.cc:1102
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

---

## 评论 (6 条)

### 评论 #1 — Burstaholic (2019-11-22T18:03:13Z)

What hardware are you using? This happens to me on my Vega M laptop (i7-8705G).

---

### 评论 #2 — kabish01 (2019-11-23T10:27:38Z)

I am using Ryzen 5 3550h CPU with Vega 8 integrated graphics and Radeon RX560X dedicated GPU.

---

### 评论 #3 — bugparty (2021-03-06T12:10:51Z)

amd 1800x + amd470 and centos8.3 failed too

---

### 评论 #4 — Shreyashwaghe (2021-04-30T21:09:10Z)

Any luck with the recent rocm 4.1 or 4.0 with your rx560x card, i am facing few problems too

---

### 评论 #5 — nartmada (2023-12-13T15:07:18Z)

Hi @kabish01, please check latest ROCm Documentation and ROCm 5.7.1 to see if your issue has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #6 — nartmada (2023-12-18T16:25:07Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
