# Is HCC supported for Kaveri APUs? Kaveri APU are based on GCN 2.0 architecture, so will the HCC and ROCM provide support for these platforms 

> **Issue #85**
> **状态**: closed
> **创建时间**: 2017-02-02T04:24:19Z
> **更新时间**: 2018-01-29T11:53:02Z
> **关闭时间**: 2017-07-02T17:23:07Z
> **作者**: VishwasRao17
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/85

## 描述

*(无描述)*

---

## 评论 (3 条)

### 评论 #1 — jedwards-AMD (2017-02-22T15:45:25Z)

THe HCC compiler will not be supported on Kaveri APUs, just as ROCm is not supported on Kaveri APUs. Please see the main ROCm page for a list of supported APUs, CPUs and ASICS.

---

### 评论 #2 — VishwasRao17 (2017-02-23T08:05:48Z)

•We also do not support AMD Carrizo and Kaveri APU as host for compliant dGPU attachments. But it is mentioned that test platform used for testing ROCm drivers is AMD7850K . We are not using discrete GPU, we are using the APU only which has integrated GPU in it. Correct me if I am wrong please.

---

### 评论 #3 — mirh (2018-01-29T11:38:03Z)

> THe HCC compiler will not be supported on Kaveri APUs, just as ROCm is not supported on Kaveri APUs.

Are you sure? According to [one of your colleagues](https://lists.freedesktop.org/archives/amd-gfx/2017-September/013609.html) Kaveri should be supported. 
Of course not with dedicated gpus (since the cpus even lack PCIe Atomics, afaik), but still. 

EDIT: also [here](https://github.com/RadeonOpenCompute/hcc/wiki#platform-requirements) EDIT2: but it's missing [here](https://github.com/RadeonOpenCompute/ROCm_Documentation/blob/master/ROCm_Compiler_SDK/ROCm-Native-ISA.rst#processors)

---
