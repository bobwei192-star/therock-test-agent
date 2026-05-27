# torch.nn.Conv1d calculation is slow

> **Issue #1565**
> **状态**: closed
> **创建时间**: 2021-08-25T08:13:33Z
> **更新时间**: 2021-09-20T11:12:08Z
> **关闭时间**: 2021-09-20T11:12:08Z
> **作者**: Saber-f
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1565

## 描述

ROCm 4.0.1
in_channels = 1, out_channels = 64, kernel_size = 32, stride = 2.
The calculation speed of the forward pass is very slow when out_channels < 16 .
The calculation speed of the backward pass is very slow when out_channels < 32.
When I increase out_channels, the speed increases by about 60 times.
Nvidia does not have this problem.



---

## 评论 (7 条)

### 评论 #1 — ROCmSupport (2021-09-07T11:23:06Z)

Hi @Saber-f 
Thanks for reaching out.
Can you please share the following.
1. Exact steps to reproduce the problem to replicate locally here
2. Details of OS, Asic, any other additional information
3. Output of /opt/rocm/bin/rocminfo and /opt/rocm/opencl/bin/clinfo
4. Can you please try with the latest ROCm 4.3.1 release and share an update on this.

Thank you.

---

### 评论 #2 — Flock1 (2021-09-10T05:20:26Z)

Hi. I wanted to know if RX 6700 is compatible with ROCm. 

---

### 评论 #3 — ROCmSupport (2021-09-13T05:20:57Z)

Hi @Flock1 
This is to inform that RX 6700 is not compatible with ROCm. Thank you.

---

### 评论 #4 — ROCmSupport (2021-09-13T05:21:30Z)

Hi @Saber-f 
Any update on execution steps please, so that we will work as per the steps and provide an update asap.
Thank you.

---

### 评论 #5 — Flock1 (2021-09-13T22:41:20Z)

@ROCmSupport, is there any plan to add RX 6700 to the compatibility list? I have that GPU and I want to use it for deep learning. 

---

### 评论 #6 — ROCmSupport (2021-09-14T04:47:20Z)

Hi @Flock1 
I do not have data at present. Request you to keep checking @ https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support

---

### 评论 #7 — ROCmSupport (2021-09-20T11:12:08Z)

I am closing this as there is no update on execution steps for the last 15 days.
Request to open a new issue, if any, with all steps, for quick resolutions.
Thank you.

---
