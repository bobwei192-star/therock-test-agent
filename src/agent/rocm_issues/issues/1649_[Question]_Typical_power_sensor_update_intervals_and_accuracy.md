# [Question] Typical power sensor update intervals and accuracy

> **Issue #1649**
> **状态**: closed
> **创建时间**: 2021-12-28T14:09:40Z
> **更新时间**: 2023-03-31T10:16:51Z
> **关闭时间**: 2023-03-31T10:16:50Z
> **作者**: lukalt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1649

## 描述

For a thesis, I am currently evaluating on-board power monitoring facilities of different CPUs and GPUs in the field of scientific computing.
In the documentation of the SMI, I found out that many power and energy metrics as well  as information on the respective accuracy and update interval are exposed through the sysfs interface and can be updated by the GPU during runtime (c.f. https://rocmdocs.amd.com/en/latest/ROCm_System_Managment/ROCm-System-Managment.html). Unfortunately, I do not have a supported GPU available to investigate this.
Are there any further information on details of the power sensors available? Specifically, I am interested in typical values for update_interval, power[1-*]_average_interval, and power[1-*]_accuracy for an exemplary device. Thanks in advance!

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2022-01-25T13:31:30Z)

Thanks for reaching out.
I understood your query. Let me assign to SMI team for help.
Thank you.

---

### 评论 #2 — bill-shuzhou-liu (2023-03-30T19:28:38Z)

The driver can read at 1ms intervals. If multiple calls come within 1ms then previous cached value is returned. 

---

### 评论 #3 — lukalt (2023-03-31T10:16:50Z)

Okay, thank you!

---
