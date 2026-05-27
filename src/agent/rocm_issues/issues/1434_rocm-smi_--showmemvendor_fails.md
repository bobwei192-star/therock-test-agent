# rocm-smi --showmemvendor fails

> **Issue #1434**
> **状态**: closed
> **创建时间**: 2021-03-30T18:43:51Z
> **更新时间**: 2021-03-31T06:47:07Z
> **关闭时间**: 2021-03-31T06:47:07Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1434

## 描述

On both my computers it shows "Unable to get GPU memory vendor." ...



---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-03-31T05:03:13Z)

Hi @valeriob01 
Thanks for reaching out.
Can you please share the details of asic, os, kernel and all other information for better understanding.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-03-31T05:03:40Z)

I tried on 3 different machines with different cards like MI25, Vega20 and Vega10 card and not seeing the problem anywhere.

======================= ROCm System Management Interface =======================

================================ Memory Vendor =================================

GPU[0]          : GPU memory vendor: samsung

================================================================================

============================= End of ROCm SMI Log ==============================


---

### 评论 #3 — valeriob01 (2021-03-31T05:34:37Z)

This is Radeon VII, Ubuntu 20.04, kernel 5.4.0-70-generic, ROCm version 3.3.0
https://github.com/preda/gpuowl/discussions/221


---

### 评论 #4 — ROCmSupport (2021-03-31T06:21:28Z)

Looks like you are using very very old ROCm version.
We are currently with ROCm 4.1 and issue is not reproduced anymore.
Recommend to try with the latest ROCm 4.1.
Thank you.

---
