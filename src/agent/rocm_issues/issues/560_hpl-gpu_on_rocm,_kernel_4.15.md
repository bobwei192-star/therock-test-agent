# hpl-gpu on rocm, kernel 4.15

> **Issue #560**
> **状态**: closed
> **创建时间**: 2018-09-27T10:44:10Z
> **更新时间**: 2018-09-27T16:04:46Z
> **关闭时间**: 2018-09-27T16:04:45Z
> **作者**: agarkov-a
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/560

## 描述

Hello!
I am trying to run hpl-gpu (https://github.com/davidrohr/hpl-gpu/wiki) on rocm (v 1.9-211) on 4.15.3 linux kernel.  But it says "No CPU OpenCL device found for mapping buffers". I have Intel Xeon E5 v3 series CPU and instinct-mi25 GPU, rocm v1.9-211, rocm-opencl v1.2.0-2018090737
clinfo shows only AMD GPU device, no CPU devices. 
Please, help me to solve the problem

---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2018-09-27T16:04:45Z)

The ROCm OpenCL runtime does not support OpenCL CPU devices as a target. If your particular application of interest *requires* OpenCL CPU devices, then it will not work in ROCm.

That said, a quick search through the [CALDGEMM code](https://github.com/davidrohr/caldgemm/tree/master) that hpl-gpu uses shows me that this CPU requirement [seems to be something that you can disable in its configuration parameters](https://github.com/davidrohr/caldgemm/blob/master/caldgemm_parse_parameters.h#L340). [This line](https://github.com/davidrohr/caldgemm/blob/master/README#L161) in the README may be useful. The error you're seeing is only called [when CALDGEMM is configured to use a CPU](https://github.com/davidrohr/caldgemm/blob/master/caldgemm_opencl.cpp#L393).

Now, I don't know exactly how to reconfigure hpl-gpu to call CALDGEMM without the "use CPU" parameter. I'll leave that to you, as AMD cannot claim to offer support on every possible user application.

---
