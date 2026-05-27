# Compatibility of opencl binaries with Windows open CL AMD drivers.

> **Issue #332**
> **状态**: closed
> **创建时间**: 2018-02-12T13:27:52Z
> **更新时间**: 2018-06-03T14:42:34Z
> **关闭时间**: 2018-06-03T14:42:34Z
> **作者**: Enoch72
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/332

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

It's not clear if a compiled, then exported OpenCL binary in ROCm enviroment  is compatible with the latest OpenCL AMD Windows drivers. (the windows OpenCl program will load it using the OPenCL clCreateProgramWithBinary function).

---

## 评论 (2 条)

### 评论 #1 — preda (2018-02-12T17:17:45Z)

Not a definitive answer, but I'd suspect that if the driver accepts the binary, then it's all good.

I did explore binary compatibility between ROCm 1.6 and 1.7 (both on Linux), and there the compiled binary is not accepted.

---

### 评论 #2 — Enoch72 (2018-02-19T08:27:23Z)

Good.

---
