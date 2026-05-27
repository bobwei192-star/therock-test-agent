# GPU not working with rocm-5.2.1

> **Issue #1812**
> **状态**: closed
> **创建时间**: 2022-09-23T18:21:21Z
> **更新时间**: 2023-12-27T17:17:54Z
> **关闭时间**: 2023-12-27T17:17:54Z
> **作者**: srinivasans74
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1812

## 描述

I have setup the MI 100 on ubuntu 20.04.5 with kernel version with 5.13.0-35-generic. I installed the rocm-5.2.1 version. But there was something strange which I observed.  The GPU is detected (I used rocm-smi) to check that

But there was another issue. 

1. The hip sample programs are getting compiled but when I am executing them, There GPU is not executing them. I was getting issues that the GPU was not detected. 
2. The code skips the section which has to be executed by the gpu. 

 

Hoping to hear from you soon

---

## 评论 (4 条)

### 评论 #1 — saadrahim (2022-10-13T21:43:05Z)

Perhaps you can share the terminal output of your GPU not detected issue? Backtrace would be helpful to see. 

Is the GPU detectable with rocminfo? It is another binary executable located in the same folder as rocm-smi.

It is possible your MI100 GPU needs a VBIOS update. You may have to contact your system provider for access to VBIOS updates.

---

### 评论 #2 — nartmada (2023-12-18T19:23:25Z)

Hi @srinivasans74, please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #3 — nartmada (2023-12-23T05:01:18Z)

Hi @srinivasans74, please try ROCm 6.0.0 to see if your issue has been fixed.  If the issue is still there, as suggested by saadrahim, please provide a backtrace.  Also please run rocminfo to check if the GPU is detected.  Thanks.

---

### 评论 #4 — nartmada (2023-12-27T17:17:54Z)

Closing the ticket as there was no response from the ticket reporter.  @srinivasans74, please re-open the ticket if your issue still exists with ROCm 6.0.0.  Thank you.

---
