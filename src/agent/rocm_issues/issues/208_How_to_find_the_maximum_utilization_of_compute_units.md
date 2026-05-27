# How to find the maximum utilization of compute units

> **Issue #208**
> **状态**: closed
> **创建时间**: 2017-09-13T13:47:49Z
> **更新时间**: 2017-09-28T01:11:06Z
> **关闭时间**: 2017-09-28T01:11:06Z
> **作者**: FalconBsp
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/208

## 描述

While running a application how to find the u percentage of compute power is getting utilized?
How many compute units are loaded ? 


---

## 评论 (2 条)

### 评论 #1 — nevion (2017-09-13T18:37:10Z)

profilers or performance counters.  rocm-smi may also be good enough. but definitely way undersamples if is a direct analog of nvidia-smi.

---

### 评论 #2 — gstoner (2017-09-24T14:14:27Z)

@FalconBsp ROCm-SMI samples the power from the GPU not total board level power aka TGP  

---
