# How to get GPU utilization in C++ code

> **Issue #1046**
> **状态**: closed
> **创建时间**: 2020-03-16T14:58:06Z
> **更新时间**: 2024-10-10T15:36:57Z
> **关闭时间**: 2020-12-02T03:42:35Z
> **作者**: zhangheng408
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1046

## 描述

except by read `/sys/class/drm/card0//device/gpu_busy_percent`.
I wonder whether rocm provided a library like nvml.


---

## 评论 (4 条)

### 评论 #1 — valeriob01 (2020-03-22T07:59:52Z)

There is the performance API: https://github.com/GPUOpen-Tools/gpu_performance_api


---

### 评论 #2 — eshcherb (2020-06-27T06:47:35Z)

You can use profiler https://github.com/ROCm-Developer-Tools/rocprofiler
There are a number of derived metrics:
https://github.com/ROCm-Developer-Tools/rocprofiler/blob/amd-master/test/tool/metrics.xml#L76

---

### 评论 #3 — jlgreathouse (2020-12-02T03:42:35Z)

Hi @zhangheng408 

Thank you for the question, and I apologize for the long delay in getting back to you. Yes, we have an NVML-style library, [rocm-smi-lib](https://github.com/RadeonOpenCompute/rocm_smi_lib).

In particular, if you want to get the `gpu_busy_percent` value, you can use the function [rsmi_dev_busy_percent_get](https://github.com/RadeonOpenCompute/rocm_smi_lib/blob/rocm-3.10.0/include/rocm_smi/rocm_smi.h#L1913).

Thanks!

---

### 评论 #4 — williamfgc (2024-10-10T15:36:56Z)

As of 2024 [amdsmi](https://github.com/ROCm/amdsmi):

```
Note: This project is a successor to [rocm_smi_lib](https://github.com/RadeonOpenCompute/rocm_smi_lib)

and [esmi_ib_library](https://github.com/amd/esmi_ib_library)
```

---
