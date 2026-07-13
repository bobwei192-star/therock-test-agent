# [Feature]: NVMe <---> GPU VRAM DMA/RDMA

- **Issue #:** 5837
- **State:** closed
- **Created:** 2026-01-07T10:05:45Z
- **Updated:** 2026-01-10T04:37:14Z
- **Labels:** Feature Request, status: triage
- **Assignees:** schung-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5837

### Suggestion Description

I’d like to propose adding GPU-direct storage support to ROCm - specifically, the ability for storage devices (e.g., NVMe SSDs) to DMA directly into GPU memory (VRAM) without staging data through host memory.

This would be conceptually similar to NVIDIA GPUDirect Storage (GDS), where data can flow:
```
NVMe <---> GPU VRAM
```
instead of:
```
NVMe <---> CPU RAM <---> GPU VRAM
```

Such a capability would significantly reduce CPU overhead, memory bandwidth pressure, and end-to-end latency for data-intensive GPU workloads.

Adding it like a flag will be really awesome, with a fallback to the default old path.

**And willing to work on this one.**

Good reads:
 - https://github.com/NVIDIA/gds-nvidia-fs
 - https://developer.nvidia.com/gpudirect
 - https://forums.developer.nvidia.com/t/example-codes-and-reffrence-for-rdma-gpudirect/284591
 - https://github.com/NVIDIA/gdrcopy
 - https://docs.nvidia.com/gpudirect-storage/

### Operating System

*

### GPU

*

### ROCm Component

*