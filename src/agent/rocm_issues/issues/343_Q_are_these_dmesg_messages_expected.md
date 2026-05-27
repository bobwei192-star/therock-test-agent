# Q: are these dmesg messages expected?

> **Issue #343**
> **状态**: closed
> **创建时间**: 2018-02-21T04:14:13Z
> **更新时间**: 2019-08-07T09:40:43Z
> **关闭时间**: 2018-02-21T19:48:22Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/343

## 描述

Ubuntu 17.10, ROCm 1.7, Vega64

When I run my OpenCL app, I see plenty of such entries appearing in dmesg. Are these normal/expected and nothing to worry about, or do they signal some problem?

```
[ 2258.451590] Evicting PASID 1 queues
[ 2258.459225] Restoring PASID 1 queues
[ 2261.663077] Evicting PASID 1 queues
[ 2261.671167] Restoring PASID 1 queues
[ 2270.003068] Evicting PASID 1 queues
[ 2270.011013] Restoring PASID 1 queues
[ 2273.263280] Evicting PASID 1 queues
[ 2273.271263] Restoring PASID 1 queues
[ 2276.529269] Evicting PASID 1 queues
[ 2276.535340] kfd2kgd: update_invalid_user_pages: Failed to get user pages: -14
[ 2276.535357] kfd2kgd: update_invalid_user_pages: Failed to get user pages: -14
[ 2276.535433] Restoring PASID 1 queues
[ 2279.792647] Evicting PASID 1 queues
[ 2279.799514] kfd2kgd: update_invalid_user_pages: Failed to get user pages: -14
[ 2279.799570] Restoring PASID 1 queues
[ 2283.091064] Evicting PASID 1 queues
[ 2283.099425] Restoring PASID 1 queues
```

---

## 评论 (3 条)

### 评论 #1 — fxkamd (2018-02-21T15:58:28Z)

These messages are normal. The evicting/restoring messages are a bit verbose, and we could probably turn them into debug messages that aren't printed in the log by default.

The "Failed to get user pages" happens if userptr memory is freed while it's still mapped for GPU access. This can result from an optimization in the OpenCL runtime that tries to keep user pages mapped to avoid repeatedly mapping and unmapping them unnecessarily. These messages aren't a problem as long as the GPU doesn't try to access this invalid memory mapping. Again, this could probably be turned into debug messages.

---

### 评论 #2 — preda (2018-02-21T19:48:22Z)

Thanks! I was sort of guessing they are benign, because everything seemed to function correctly when they were present. Closing then.


---

### 评论 #3 — Sfinx (2019-08-07T09:40:43Z)

Yep, the AMD driver is too chatty, Ubuntu kernel  5.2.7-050207-lowlatency + rocm-opencl 1.2.0-2019070446. Every time I'm running OpenCL examples I'm getting this in kernel logs:

```
[ 3507.287389] Over-subscription is not allowed for SDMA.
[ 3511.201126] Over-subscription is not allowed for SDMA.
[ 3558.449204] Over-subscription is not allowed for SDMA.
[ 3565.242940] Evicting PASID 32784 queues
[ 3565.244793] Restoring PASID 32784 queues
[ 3565.291636] Over-subscription is not allowed for SDMA.
```

They should present in debug builds

---
