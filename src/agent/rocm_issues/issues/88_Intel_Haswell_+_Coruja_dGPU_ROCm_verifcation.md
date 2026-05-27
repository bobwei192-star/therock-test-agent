# Intel Haswell + Coruja dGPU  ROCm verifcation

> **Issue #88**
> **状态**: closed
> **创建时间**: 2017-02-22T12:12:23Z
> **更新时间**: 2017-07-02T01:47:02Z
> **关闭时间**: 2017-07-02T01:47:02Z
> **作者**: FalconBsp
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/88

## 描述

Hi, 
I try to run ROCm vector_copy on Intel Haswell + Coruja dGPU combination. Vector_copy works fine. But i am suspecting with Virtual CRAT table creation .

Do we need separate BIOS to support CRAT table for Intel Haswell ?


[    4.691934] AMD IOMMUv2 driver by Joerg Roedel <jroedel@suse.de>
[    4.718973] AMD IOMMUv2 functionality not available on this system
[    4.747848] CRAT table not found
[    4.774840] Virtual CRAT table created for CPU
[    4.932931] Parsing CRAT table with 1 nodes
[    4.958942] Creating topology SYSFS entries
[    4.985162] Topology: Add CPU node
[    5.011497] Finished initializing topology
[    5.039518] kfd kfd: Initialized module

---

## 评论 (2 条)

### 评论 #1 — FalconBsp (2017-02-22T12:27:38Z)

Does Intel also contain CRAT table or only AMD APU's support CRAT table?

If no CRAT table support in Intel , How the performance impact with Virtual CRAT table ?

---

### 评论 #2 — jedwards-AMD (2017-02-22T15:39:35Z)

Only AMD APU's require a CRAT table. What makes you suspect that a virtual CRAT was created? Also, if a virtual CRAT table is created it would have no impact on the performance of a Intel CPU/dGPU combination. 

---
