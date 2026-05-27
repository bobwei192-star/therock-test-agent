# Does it support the following GPU: Sun XT [Radeon HD 8670A/8670M/8690M / R5 M330 / M430 / R7 M520]

> **Issue #528**
> **状态**: closed
> **创建时间**: 2018-09-14T10:29:34Z
> **更新时间**: 2018-09-17T23:25:15Z
> **关闭时间**: 2018-09-14T12:14:22Z
> **作者**: ruc98
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/528

## 描述

*(无描述)*

---

## 评论 (3 条)

### 评论 #1 — ruc98 (2018-09-14T10:36:12Z)

I followed all the steps mentioned in the description.
But while running `rocminfo` command, I got the following error
`hsa api call failure at line 900, file: /home/jenkins/jenkins-root/workspace/compute-rocm-rel-1.8/rocminfo/rocminfo.cc. Call returned 4104`
Any suggestions what to do further?
My target is to use tensorflow with my GPU.
Thanks


---

### 评论 #2 — kentrussell (2018-09-14T12:14:22Z)

Sun XT (Hainan) is GFX6, which is not supported in ROCm, We have experimental support for GFX7, but GFX8+ is the only official support for GPUs (see https://rocm.github.io/ROCmInstall.html for more info). The kernel will work, but the runtime (and rocminfo) doesn't have gfx6 support.

---

### 评论 #3 — JMadgwick (2018-09-14T12:27:42Z)

~~From what I can see your chip (Sun XT) is first Gen GCN (gfx 6xx) and not supported. Unfortunately there is very little info around on it, but it might be second gen GCN (gfx 7xx) if it is then ROCm can be used but Tensorflow cannot.~~

I am sure that sadly you can **NOT** use ROCm Tensorflow. To use Tensorflow you need a [gfx 803, 900 or 906 GPU.](https://github.com/ROCmSoftwarePlatform/tensorflow/blob/rocm-v1/tensorflow/core/common_runtime/gpu/gpu_device.cc#L749) No others are supported and if you use something else then Tensorflow will use the CPU instead.

The supported GPU list is meant to be updated at sometime but nobody has done it yet. Also more GPU support [looks like it will or was going to be added](https://github.com/RadeonOpenCompute/hcc/compare/feature_enable_what_rocm_supports) to HC but it's very unlikely this will ever mean Tensorflow working on gfx7xx Chips.

Edit: posted after already closed as was posted before it was closed

---
