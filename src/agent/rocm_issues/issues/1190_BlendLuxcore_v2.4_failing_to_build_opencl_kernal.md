# BlendLuxcore v2.4 failing to build opencl kernal 

> **Issue #1190**
> **状态**: closed
> **创建时间**: 2020-08-17T03:40:46Z
> **更新时间**: 2021-03-01T08:55:38Z
> **关闭时间**: 2021-03-01T08:55:38Z
> **作者**: Navi-Professor
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1190

## 描述

specs. 2x Vega 56, 3900x, 128gb ram, Ubuntu 20.04.1, rocm 3.5.1. 
in an attempt to diagnose a issue with blendluxcore, i installed rocm and it fails to build the opencl kernals, cycles is able to build kernals and render with my gpus. 
following error the addon spat out. 
OpenCL driver API error (code: -11, file:/home/vsts/work/1/s/LinuxCompile/LuxCore/src/luxrays/utils/ocl.cpp, line: 369): CL_BUILD_PROGRAM_FAILURE
it does build the kernal with the AMD PRO drivers. (however there is a issue with normal maps that i was trying to nail down by installing these drivers)

*UPDATE* Blendluxcore v2.3 doesnt compile either and just instantly crashes out


---

## 评论 (3 条)

### 评论 #1 — ROCmSupport (2020-12-16T10:32:12Z)

Hi @matthewv1998 
Thanks for reaching out.
Can you please share the below outputs.
_/opt/rocm/bin/rocminfo
/opt/rocm/opencl/bin/clinfo_

Can you please try with the latest ROCm 3.10 and update please?

If the issue still exist, please share the exact steps to reproduce the problem.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-01-28T08:39:06Z)

Hi @matthewv1998 
Please share an update, else close this issue if no issues.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-03-01T08:55:38Z)

Closing this ticket as there is no response from user for a long time.
Thank you.

---
