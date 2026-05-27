# ROCm dose not detect my GPU ( AMD Radeon R7 M265)

> **Issue #1492**
> **状态**: closed
> **创建时间**: 2021-06-10T04:00:05Z
> **更新时间**: 2021-06-10T07:50:24Z
> **关闭时间**: 2021-06-10T07:50:23Z
> **作者**: BahramianArmin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1492

## 描述

enter in terminal 'rocm-smi' and says No AMD GPUs specified
-->rocm-smi

======================= ROCm System Management Interface =======================
WARNING: No AMD GPUs specified
================================= Concise Info =================================
GPU  Temp  AvgPwr  SCLK  MCLK  Fan  Perf  PwrCap  VRAM%  GPU%  
================================================================================
============================= End of ROCm SMI Log ==============================





so what should i do ???
thanks for your OPPONION!

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-06-10T07:37:45Z)

Thanks @BahramianArmin for reaching us out.
Can you please share the output of "lspci -nn | grep AMD/ATI" command.
Thank you.

---

### 评论 #2 — BahramianArmin (2021-06-10T07:40:34Z)

lspci -nn | grep AMD/ATI
05:00.0 Display controller [0380]: Advanced Micro Devices, Inc. [AMD/ATI] Opal XT [Radeon R7 M265/M365X/M465] [1002:6604]



---

### 评论 #3 — ROCmSupport (2021-06-10T07:50:23Z)

Thanks @BahramianArmin 
Opal XT is not a ROCm supported card and so ROCm does not work with specific hardware.
Thank you.

---
