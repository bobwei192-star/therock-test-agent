# Compile-away get_local_size() when workgroup size is known at compile time.

> **Issue #321**
> **状态**: closed
> **创建时间**: 2018-02-01T21:23:18Z
> **更新时间**: 2018-06-03T15:34:14Z
> **关闭时间**: 2018-06-03T15:34:14Z
> **作者**: preda
> **标签**: Compiler Functional Bug
> **URL**: https://github.com/ROCm/ROCm/issues/321

## 标签

- **Compiler Functional Bug** (颜色: #d847b6)

## 描述

(OpenCL, ROCm 1.7)

The workgroup size can be fixed at compile-time using: ```__attribute__((reqd_work_group_size(x, y, z)))```

The workgroup size can be queried at runtime using get_local_size().

Expected: for a kernel with compile-time fixed workgroup size, the get_local_size() should be compiled-away to the compile-time constant.

Observed: get_local_size() is kept, reading the size from SGPR values passed to the kernel at runtime.


---

## 评论 (1 条)

### 评论 #1 — arsenm (2018-05-19T06:59:55Z)

llvm r332771 implements this. It will be completely eliminated for CL1.2. For CL2.0 you also must specify -cl-uniform-work-group-size, or else only some of the loads will be eliminated.

---
