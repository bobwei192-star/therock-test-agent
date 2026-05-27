# HIP_VISIBLE_DEVICES not working properly in ROCm 3.5

> **Issue #1170**
> **状态**: closed
> **创建时间**: 2020-06-30T08:39:19Z
> **更新时间**: 2022-10-18T23:23:35Z
> **关闭时间**: 2020-12-01T04:22:37Z
> **作者**: MarcelSimon
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/1170

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

It seems that neither HIP_VISIBLE_DEVICES nor ROCR_VISIBLE_DEVICE is working properly anymore in ROCm 3.5 and newer. When running a program with 

```
HIP_VISIBLE_DEVICES= python training.py
```

all GPUs are used. The expected behavior is that all GPUs are hidden.

I tested this with Tensorflow version 2.2.

OS: Ubuntu 18.04.4
ROCm version: 3.5.1, using the rocm-dkms package

---

## 评论 (5 条)

### 评论 #1 — jlgreathouse (2020-12-01T04:22:37Z)

Thanks for the report on this. I just tested this on a ROCm 3.7 system I have sitting around, and I believe this is fixed as of at least ROCm 3.7 (maybe 3.6 as well).

---

### 评论 #2 — jedbrown (2022-10-18T23:16:37Z)

It looks like this is back. Testing on rocm-5.2, I observe that `HIP_VISIBLE_DEVICES= ./app` behaves the same as when the variable is unset, so using all devices. `ROCR_VISIBLE_DEVICES= ./app` finds no device as intended.

---

### 评论 #3 — saadrahim (2022-10-18T23:18:19Z)

Can you file a new ticket?

---

### 评论 #4 — Jacobfaib (2022-10-18T23:22:13Z)

I created one over in the HIP repo a few days ago: https://github.com/ROCm-Developer-Tools/HIP/issues/3001

---

### 评论 #5 — saadrahim (2022-10-18T23:23:35Z)

Thanks, I triaged your issue.

---
