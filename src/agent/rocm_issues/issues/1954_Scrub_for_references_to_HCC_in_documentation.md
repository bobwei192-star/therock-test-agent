# Scrub for references to HCC in documentation

> **Issue #1954**
> **状态**: closed
> **创建时间**: 2023-03-16T14:00:48Z
> **更新时间**: 2025-05-30T15:38:59Z
> **关闭时间**: 2025-05-30T15:38:59Z
> **作者**: skyreflectedinmirrors
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1954

## 标签

- **Documentation** (颜色: #5319e7)

## 描述

> on HCC hipMemcpyAsync does not support overlapped H2D and D2H copies. For hipMemcpy, the copy is always performed by the device associated with the specified stream.

https://github.com/ROCm-Developer-Tools/HIP/blob/develop/include/hip/hip_runtime_api.h#L3754

My read is that there is already on-going efforts to remove, but just a heads-up.

cc: @saadrahim 

---

## 评论 (2 条)

### 评论 #1 — ppanchad-amd (2024-05-10T18:17:46Z)

@skyreflectedinmirrors Internal ticket has been created to fix documentation. Thanks!

---

### 评论 #2 — harkgill-amd (2025-05-30T15:38:59Z)

Hi @skyreflectedinmirrors, the references to `hcc` have been replaced with `HIP-Clang` in `hip_runtime_api.h`. These changes have been merged into our internal branch of the hip repo and will make their way into the public docs shortly. Thanks!


---
