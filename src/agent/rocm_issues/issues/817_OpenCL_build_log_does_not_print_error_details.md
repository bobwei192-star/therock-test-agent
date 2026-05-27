# OpenCL build log does not print error details

> **Issue #817**
> **状态**: closed
> **创建时间**: 2019-06-09T12:11:10Z
> **更新时间**: 2023-12-21T14:33:20Z
> **关闭时间**: 2023-12-21T14:33:20Z
> **作者**: blueberry
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/817

## 描述

Hi,

I'm using ROCm 2.4 on linux.
When I compile a kernel with an error, the build log is always the same:
"Error: Failed to compile opencl source (from CL to LLVM IR)." 

Earlier, when I was using old proprietary AMD's OpenCL 2.0 driver provided by catalyst, the build log displayed the offending source in a usable compilation report.

Is there a way to get that sort of report with ROCm OpenCL?

---

## 评论 (2 条)

### 评论 #1 — tasso (2023-12-18T19:04:33Z)

Is this still reproducible?  If not, can we please close it?  Thanks!

---

### 评论 #2 — tasso (2023-12-21T14:33:20Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request.  If this is still an issue, please file a new ticket and we will happy to investigate it.  Thanks!

---
