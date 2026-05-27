# rocm-smi reporting a non-existant GPU 0?

> **Issue #561**
> **状态**: closed
> **创建时间**: 2018-09-27T13:14:01Z
> **更新时间**: 2019-03-11T16:26:04Z
> **关闭时间**: 2019-03-11T16:26:03Z
> **作者**: seibert
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/561

## 描述

On my system with ROCm 1.9, I see the following output from `rocm-smi`:
```
====================    ROCm System Management Interface    ====================
================================================================================
 GPU  Temp    AvgPwr   SCLK     MCLK     Fan      Perf    SCLK OD    MCLK OD
  0   N/A     N/A      N/A      N/A      0%       N/A       N/A        N/A
  1   55c     15.0W    852Mhz   167Mhz   10.98%   auto      0%         0%
================================================================================
====================           End of ROCm SMI Log          ====================
```

Is the non-existent GPU 0 an artifact of the CPU being enumerated as an HSA agent?  Might be less confusing to filter it out of rocm-smi output.

---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2018-09-27T14:10:15Z)

`rocm-smi` walks through all of the GPUs in the system shown in, for example, `/sys/class/drm/#/`. The DRM system can include non-AMD GPUs. For example, do you have an integrated GPU in your laptop or server motherboard?

---

### 评论 #2 — kentrussell (2018-10-03T12:32:55Z)

Thanks @jlgreathouse , that's exactly what we do. I have been working forever on trying to only report GPUs that actually matter and have topology loaded, but it hasn't been done yet. For now, we just go through /sys/class/drm/cardX , and X is the GPU that we use. So in your case, it would be an integrated graphics card, or some other non-AMD display device, I would assume.

---

### 评论 #3 — kentrussell (2019-03-11T16:26:03Z)

Fixed in 2.2

---
