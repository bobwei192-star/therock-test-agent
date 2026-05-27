# Incomplete installation downgrading rocm from 4 to 3.9.1?

> **Issue #1409**
> **状态**: closed
> **创建时间**: 2021-03-19T14:49:45Z
> **更新时间**: 2021-03-22T04:07:36Z
> **关闭时间**: 2021-03-19T16:01:23Z
> **作者**: staticdev
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1409

## 描述

I tried deleting the folder /opt/rocm-4.0.1 and then installing rocm-3.9.1 (since I realized it does not support Radeon RX580 anymore). But when I try to run tensorflow I get:

```
ImportError: libamdhip64.so.4: cannot open shared object file: No such file or directory
```

Is there a way to fix that?


---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-03-22T04:07:36Z)

Hi @staticdev 
Hope your issue resolved.
Thank you.

---
