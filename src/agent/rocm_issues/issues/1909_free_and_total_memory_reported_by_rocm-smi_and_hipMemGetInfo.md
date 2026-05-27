# free and total memory reported by rocm-smi and hipMemGetInfo

> **Issue #1909**
> **状态**: closed
> **创建时间**: 2023-02-16T14:33:41Z
> **更新时间**: 2024-02-05T17:53:41Z
> **关闭时间**: 2024-02-05T17:53:41Z
> **作者**: zjin-lcf
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1909

## 描述

The free value reported by rocm-smi is different from that reported by the HIP API. Thanks.


$ rocm-smi --showmeminfo vram

```
======================= ROCm System Management Interface =======================
============================= Memory Usage (Bytes) =============================
GPU[0]          : VRAM Total Memory (B): 4278190080
GPU[0]          : VRAM Total Used Memory (B): 108814336
================================================================================
============================= End of ROCm SMI Log ==============================
```

However, hipMemGetInfo(&free, &total) also returns 4278190080 for both

---

## 评论 (3 条)

### 评论 #1 — nartmada (2024-02-02T23:07:39Z)

Hi @zjin-lcf, please close the ticket if the issue has been fixed.  Thanks.

---

### 评论 #2 — zjin-lcf (2024-02-03T03:01:04Z)

Can  you please point out any difference between "VRAM used memory in bytes" and (total - free) ? 

---

### 评论 #3 — kentrussell (2024-02-05T14:34:23Z)

There is never a point where there is zero used memory on a booted system. SMI reports memory from the kernel's memory manager via amdgpu+amdkfd (see (https://github.com/ROCm/ROCK-Kernel-Driver/blob/master/drivers/gpu/drm/amd/amdgpu/amdgpu_vram_mgr.c#L117) . There is a chance that they might not align perfectly if memory is being used at the time, but having 100% total memory available in HIP is inaccurate from a kernel perspective. It may mean something different to HIP however.

---
