# OpenCL clBuildProgram terminates on invalid -save-temps

> **Issue #779**
> **状态**: closed
> **创建时间**: 2019-04-22T06:29:41Z
> **更新时间**: 2019-04-22T16:25:24Z
> **关闭时间**: 2019-04-22T16:25:23Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/779

## 描述

ROCm 2.2 OpenCL:

when clBuildProgram() is invoked with an invalid path in -save-temps , it terminates the process abruptly after displaying the message:
LLVM ERROR: IO failure on output stream: Bad file descriptor

The expected behavior of clBuildProgram is to return an error code != CL_SUCCESS on error, not to terminate the process.


---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-04-22T16:25:23Z)

Please submit this bug to the [ROCm OpenCL project](https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/issues).

---
