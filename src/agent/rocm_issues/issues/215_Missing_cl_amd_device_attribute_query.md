# Missing cl_amd_device_attribute_query

> **Issue #215**
> **状态**: closed
> **创建时间**: 2017-09-28T06:39:14Z
> **更新时间**: 2018-04-23T17:38:48Z
> **关闭时间**: 2018-04-23T17:38:48Z
> **作者**: CNugteren
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/215

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

A user of the CLBlast library [reported full output](https://github.com/CNugteren/CLBlast/issues/186#issuecomment-328012892) of running `/opt/rocm/opencl/bin/x86_64/clinfo` on a Fiji device with ROCm 1.6.

However, although it displays a value for  `CL_DEVICE_BOARD_NAME_AMD` which is part of the [AMD extension cl_amd_device_attribute_query](https://www.khronos.org/registry/OpenCL/extensions/amd/cl_amd_device_attribute_query.txt)), it does not list this extension when querying for the supported extensions.

Is `cl_amd_device_attribute_query` not officially supported by ROCm devices? How to reliably query for the `CL_DEVICE_BOARD_NAME_AMD` attribute?

---

## 评论 (5 条)

### 评论 #1 — gstoner (2017-09-29T12:10:54Z)

We have this in a newer version of OpenCL that runs on ROCm,  OpenCL is still in beta testing on ROCm.  We looking to see if can be enabled in the next release it not it be in the  November release 

---

### 评论 #2 — CNugteren (2018-01-29T19:05:20Z)

Any update? Can you confirm whether it is enabled in the 1.7 version?

---

### 评论 #3 — CNugteren (2018-04-22T09:09:38Z)

@gstoner Any update? Can you confirm that this is available in the latest release?

---

### 评论 #4 — gstoner (2018-04-22T16:32:19Z)

It should be in ROCm 1.7 https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/blame/ac32bfefcac66667614ce392d2b196c52ac14beb/runtime/device/rocm/rocsettings.cpp#L106

---

### 评论 #5 — CNugteren (2018-04-23T17:38:48Z)

OK, thanks. I'll ask the users of CLBlast to try ROCm 1.7 or newer.

---
