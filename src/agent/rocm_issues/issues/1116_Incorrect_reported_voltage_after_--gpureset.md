# Incorrect reported voltage after --gpureset

> **Issue #1116**
> **状态**: closed
> **创建时间**: 2020-05-23T16:40:59Z
> **更新时间**: 2021-08-04T10:09:50Z
> **关闭时间**: 2021-08-04T10:09:49Z
> **作者**: izixxxc
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1116

## 描述

ROCm v3.3.0
Ubuntu 18.04
Radeon VII

:~$ rocm-smi --showvoltage

GPU[0] 		: Voltage (mV): 737

:~$ rocm-smi -d0 --gpureset

GPU[0] 		: GPU reset was successful

:~$ rocm-smi --showvoltage

GPU[0] 		: Voltage (mV): 1550

Power consumption is also misreported. Any quick fix?

---

## 评论 (5 条)

### 评论 #1 — ROCmSupport (2021-03-03T05:55:42Z)

Thanks @izixxxc for reaching out.
I will check this for you.

---

### 评论 #2 — ROCmSupport (2021-03-03T09:20:33Z)

Hi @izixxxc 
I am able to reproduce this issue with the latest ROCm 4.0 also.
Looks like SMI is showing wrong result. let me debug more and get back to you on this.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-06-02T12:22:46Z)

Hi @izixxxc 
Got update.
I debugged it and found that issue is not with SMI.
Actual problem is with kernel. Without SMI also, issue is observed.
And the issue is specific to Radeon7 only.

---

### 评论 #4 — ROCmSupport (2021-06-02T12:23:47Z)

Assigned to dev and fix ready, which is good news.
Most likely it will be part of ROCm 4.4, please stay tuned.
Thank you.

---

### 评论 #5 — ROCmSupport (2021-08-04T10:09:49Z)

Good news.
Issue is fixed with 4.3.
I just verified with 4.3 and issue is not observed anymore.

======================= ROCm System Management Interface =======================
=============================== Current voltage ================================
GPU[0]          : Voltage (mV): 737
GPU[1]          : Voltage (mV): 737
================================================================================
============================= End of ROCm SMI Log ==============================
taccuser@taccuser-SYS-4028GR-TR2:/usr/bin$ /opt/rocm/bin/roci -d0 --gpureset
-bash: /opt/rocm/bin/roci: No such file or directory
taccuser@taccuser-SYS-4028GR-TR2:/usr/bin$ /opt/rocm/bin/rocm-smi -d0 --gpureset
[sudo] password for taccuser:


======================= ROCm System Management Interface =======================
================================== Reset GPU ===================================
GPU[0]          : Successfully reset GPU 0
================================================================================
taccuser@taccuser-SYS-4028GR-TR2:/usr/bin$ /opt/rocm/bin/rocm-smi --showvoltage


======================= ROCm System Management Interface =======================
=============================== Current voltage ================================
GPU[0]          : Voltage (mV): 737
GPU[1]          : Voltage (mV): 737
================================================================================
============================= End of ROCm SMI Log ==============================


---
