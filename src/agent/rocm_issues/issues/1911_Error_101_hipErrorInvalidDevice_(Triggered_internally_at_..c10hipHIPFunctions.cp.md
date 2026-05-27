# Error 101: hipErrorInvalidDevice (Triggered internally at ../c10/hip/HIPFunctions.cpp:110.)

> **Issue #1911**
> **状态**: closed
> **创建时间**: 2023-02-23T15:04:43Z
> **更新时间**: 2024-04-26T05:38:03Z
> **关闭时间**: 2024-02-06T18:14:29Z
> **作者**: arch-user-france1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1911

## 描述

```
>>> import torch
>>> torch.cuda.is_available()
/home/rocm-user/.local/lib/python3.8/site-packages/torch/cuda/__init__.py:88: UserWarning: HIP initialization: Unexpected error from hipGetDeviceCount(). Did you run some cuda functions before calling NumHipDevices() that might have already set an error? Error 101: hipErrorInvalidDevice (Triggered internally at ../c10/hip/HIPFunctions.cpp:110.)
  return torch._C._cuda_getDeviceCount() > 0
False
>>>
```

Using your docker image with the AMD RADEON RX 7900 XT.
According to your documentation, the RDNA architecture is supported.

---

## 评论 (3 条)

### 评论 #1 — nartmada (2024-02-02T23:09:05Z)

Hi @arch-user-france1, please check latest ROCm 6.0.2 if your issue has been fixed.  If fixed, please close the ticket.  Thanks.

---

### 评论 #2 — arch-user-france1 (2024-02-06T18:14:29Z)

fixed

---

### 评论 #3 — Youth4688 (2024-04-26T05:38:01Z)

Hello, how did you solve it? I also had the same problem.

---
