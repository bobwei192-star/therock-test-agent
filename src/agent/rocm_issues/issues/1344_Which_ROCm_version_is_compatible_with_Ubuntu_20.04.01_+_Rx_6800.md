# Which ROCm version is compatible with Ubuntu 20.04.01 + Rx 6800 

> **Issue #1344**
> **状态**: closed
> **创建时间**: 2020-12-19T06:55:08Z
> **更新时间**: 2020-12-19T10:32:16Z
> **关闭时间**: 2020-12-19T10:32:16Z
> **作者**: jhb115
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1344

## 描述

Hi, I would like to know which version of ROCm is compatible with Ubuntu 20.04.01 + Rx 6800.

---

## 评论 (4 条)

### 评论 #1 — jhb115 (2020-12-19T07:25:14Z)

Hmm... I see that Rx 6800 is not one of the gpus officially supported by ROCm. Is there any timeline or schedule when this ROCm will also support on Rx 6800? 

Is there any bypassing/unofficial way to run pytorch on Rx 6800? 

---

### 评论 #2 — lorisgir (2020-12-19T08:56:22Z)

[This](https://github.com/RadeonOpenCompute/ROCm/issues/1180#issuecomment-746164720) is all we know regarding RDNA2 support

---

### 评论 #3 — johnbridgman (2020-12-19T09:18:39Z)

> Hi, I would like to know which version of ROCm is compatible with Ubuntu 20.04.01 + Rx 6800.

None at the moment, unfortunately. 

The 20.45 packaged drivers include an OpenCL implementation based on the lower levels of the ROCm stack (kernel code up through language runtimes) but HIP and library support still require additional work. 

---

### 评论 #4 — jhb115 (2020-12-19T10:32:16Z)

Thank you for the reply. That's quite unfortunate to hear. Really hope ROCm version compatible with the AMD 6000 series gpus comes out in the near future.... 

---
