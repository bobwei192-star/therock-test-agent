# Device::callbackQueue aborting with status: 0x100f

> **Issue #1393**
> **状态**: closed
> **创建时间**: 2021-02-25T21:00:55Z
> **更新时间**: 2021-03-18T00:36:38Z
> **关闭时间**: 2021-03-18T00:36:37Z
> **作者**: zjin-lcf
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1393

## 描述

Can you please explain the meaning of the status ?

:0:rocdevice.cpp            :2303: 768423197593 us: Device::callbackQueue aborting with status: 0x100f

Thanks

---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2021-02-26T06:16:02Z)

Hi @zjin-lcf for reaching out.
Looks like **specific kernel is broken and calculation is aborted**.

Can you please share the exact steps to reproduce the problem for better understanding.

---

### 评论 #2 — ROCmSupport (2021-03-17T06:15:02Z)

Hi @zjin-lcf 
Please update us to move this issue to next level.
Else request you to close this ticket, if you are not seeing/required anymore.
Thank you.


---

### 评论 #3 — zjin-lcf (2021-03-18T00:36:37Z)

Thank you.

---
