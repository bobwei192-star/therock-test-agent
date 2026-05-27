# [Issue]: performance panelty caused by separated HSA queues in HIP and OpenMP implementations

> **Issue #2705**
> **状态**: closed
> **创建时间**: 2023-12-11T22:29:12Z
> **更新时间**: 2024-11-01T15:47:34Z
> **关闭时间**: 2024-11-01T15:47:33Z
> **作者**: ye-luo
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/2705

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

### Problem Description

The two programming models OpenMP and HIP provided by ROCm leverage the same HSA runtime. HIP holds its own pool HSA queues controlled by the `GPU_MAX_HW_QUEUES` environment variable and OpenMP holds its own pool HSA queues controlled by the `LIBOMPTARGET_AMDGPU_NUM_HSA_QUEUES` environment variable.

However, HSA queues are directly related if not one-to-one mapped to hardware queues and over-subscription causes huge performance penalty. I can view this from the application performance regression and kernel log
`amdgpu: Runlist is getting oversubscribed. Expect reduced ROCm performance.`

For applications using both GPU programming models, developers need to take into account how many HSA queues in each programming model runtime to use when figuring out the optimal performance. This is unnecessary complication added for applications. On the contrary, all the CUDA streams (runtime and driver APIs) are virtualized and decoupled from the hardware count. Although concurrent execution is still limited by the hardware queues, users can create any amount of CUDA streams without much penalty.

One possible solution could be HSA making its queues virtualized.
Potentially, one can implement Vulkan APIs on top of HSA and cause further problems if the current design issue retains.


### Operating System

Any Linux

### CPU

Any CPU

### GPU

Any AMD GPUs

### ROCm Version

Throughout 5.x and beyond

### ROCm Component

HIP, OpenMP, HSA

### Steps to Reproduce

_No response_

### Output of /opt/rocm/bin/rocminfo --support
```
ROCk module is loaded
=====================    
HSA System Attributes    
=====================    
Runtime Version:         1.1
System Timestamp Freq.:  1000.000000MHz
Sig. Max Wait Duration:  18446744073709551615 (0xFFFFFFFFFFFFFFFF) (timestamp count)
Machine Model:           LARGE                              
System Endianness:       LITTLE                             
Mwaitx:                  DISABLED
DMAbuf Support:          YES
```

