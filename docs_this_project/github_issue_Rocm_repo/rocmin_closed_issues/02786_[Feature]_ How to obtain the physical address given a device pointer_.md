# [Feature]: How to obtain the physical address given a device pointer?

- **Issue #:** 2786
- **State:** closed
- **Created:** 2024-01-09T14:35:22Z
- **Updated:** 2024-09-10T14:54:32Z
- **URL:** https://github.com/ROCm/ROCm/issues/2786

### Suggestion Description

NVIDIA provides a mechanism for developers to obtain the physical address of a allocated pointer [via their driver API](https://docs.nvidia.com/cuda/gpudirect-rdma/index.html). In AMD GPU and ROCm, is there any similar approach to achieve this, i.e., given a virtual address returned by `hipMalloc`, query the underlying phyiscal address corresponding to it.

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

_No response_