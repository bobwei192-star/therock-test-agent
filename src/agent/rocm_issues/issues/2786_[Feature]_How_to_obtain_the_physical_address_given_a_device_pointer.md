# [Feature]: How to obtain the physical address given a device pointer?

> **Issue #2786**
> **状态**: closed
> **创建时间**: 2024-01-09T14:35:22Z
> **更新时间**: 2024-09-10T14:54:32Z
> **关闭时间**: 2024-09-10T14:54:31Z
> **作者**: xuantengh
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/2786

## 描述

### Suggestion Description

NVIDIA provides a mechanism for developers to obtain the physical address of a allocated pointer [via their driver API](https://docs.nvidia.com/cuda/gpudirect-rdma/index.html). In AMD GPU and ROCm, is there any similar approach to achieve this, i.e., given a virtual address returned by `hipMalloc`, query the underlying phyiscal address corresponding to it.

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_
