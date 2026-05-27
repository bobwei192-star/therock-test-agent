# ROCm installation for RX550

> **Issue #1581**
> **状态**: closed
> **创建时间**: 2021-09-28T21:09:10Z
> **更新时间**: 2021-09-30T16:16:37Z
> **关闭时间**: 2021-09-30T16:16:37Z
> **作者**: basileus93
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1581

## 描述

Hi,

I installed ROCm following the instructions here: https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu .
I am using Ubuntu 18.04.5 and I downgraded the kernel to 5.4.0.71 to have the same reported in the instructions.
ROCm 4.3 fails with the problem reported in this issue: https://github.com/RadeonOpenCompute/ROCm/issues/1302
ROCm 4.1 fails with the following error
`ERROR: rocprofiler_iterate_info(), Translate(), ImportMetrics: bad block name 'GRBM', GPU device_id(699f) is not supported`
`/usr/bin/rocprof: line 358:  2582 Aborted                 (core dumped) /opt/rocm-4.1.0/rocprofiler/tool/ctrl`

I am trying to analyze an RX 550.
Could you please report which package versions (Ubuntu, kernel, ROCm, amdgpu) should be used for this GPU?


---

## 评论 (3 条)

### 评论 #1 — xuhuisheng (2021-09-28T21:37:30Z)

Try this:
<https://github.com/boriswinner/RX580-rocM-tensorflow-ubuntu20.4-guide>

---

### 评论 #2 — basileus93 (2021-09-30T08:34:54Z)

I tried that (same ubuntu, kernel and rocm versions). I am still getting: 
`>>> Run: `
`ERROR: rocprofiler_open(), Translate(), ImportMetrics: bad block name 'GRBM', GPU device_id(699f) is not supported`
/`opt/rocm/bin/rocprof: line 275:  4824 Aborted                 (core dumped) "./main.x"`

It seems that the counters are not supported for this GPU. The command `rocprof --stats` works fine.



---

### 评论 #3 — ROCmSupport (2021-09-30T16:16:36Z)

Thanks @basileus93 for reaching out.
We do not support RX550 officially with ROCm and request to look at supported cards @ https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support
Hope this helps.
Thank you.

---
