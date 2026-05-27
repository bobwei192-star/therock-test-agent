# ispc compiler on ROCm + Ryzen

> **Issue #393**
> **状态**: closed
> **创建时间**: 2018-04-25T11:09:32Z
> **更新时间**: 2018-04-25T17:26:03Z
> **关闭时间**: 2018-04-25T17:26:03Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/393

## 描述

Not really a ROCm issue, but not sure where else to post this.
Are there plans to customize the ispc compiler for Ryzen/EPIC chips?
I've heard great things about speedup potential for SPMD on ispc.

https://github.com/ispc/ispc

---

## 评论 (3 条)

### 评论 #1 — boberfly (2018-04-25T17:14:00Z)

@boxerab hmm doesn't it just target AVX2 already? Ryzen should support those wide vectors already, embree seems to function fine for instance, maybe I'm mistaken.

---

### 评论 #2 — gstoner (2018-04-25T17:16:40Z)

Yes it should work via AVX2 path. 

---

### 评论 #3 — boxerab (2018-04-25T17:26:03Z)

cool. thanks guys.

---
