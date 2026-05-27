# rocm-smi

> **Issue #1144**
> **状态**: closed
> **创建时间**: 2020-06-09T13:38:47Z
> **更新时间**: 2020-07-10T18:18:48Z
> **关闭时间**: 2020-07-10T18:18:48Z
> **作者**: florekem
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1144

## 描述

Can't find it in my system, has it been removed? I used it for controlling gpu fan. Is there another way to do it now?

---

## 评论 (2 条)

### 评论 #1 — ableeker (2020-06-09T18:28:04Z)

If you install rocm-dkms, or rocm-dev, it's definitely included. Otherwise, I see there's a package called rocm-smi-xxx.deb

---

### 评论 #2 — preda (2020-06-11T08:57:00Z)

rocm-smi is basically just a glorified python script, that you can check out from:
https://github.com/RadeonOpenCompute/ROC-smi


---
