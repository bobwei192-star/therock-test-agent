# Is BFloat16 supported on radeon7 (non MI-5/60)?

> **Issue #855**
> **状态**: closed
> **创建时间**: 2019-08-02T20:49:00Z
> **更新时间**: 2020-01-09T16:21:06Z
> **关闭时间**: 2020-01-09T16:20:43Z
> **作者**: witeko
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/855

## 描述

Is BFloat16 supported on radeon7 (non MI-5/60)?
Can I use mixed precision in rocm-tensorflow?

---

## 评论 (4 条)

### 评论 #1 — ekuznetsov139 (2019-08-03T03:58:23Z)

As far as I can tell, the native fp16 format used by all modern GPUs (including Radeon 7) is float16, *not* bfloat16. The only ones natively accelerating bfloat16 are ASICs like Google Cloud TPU.

The stuff about support of bfloat16 in their docs is mostly about being able to load existing bfloat16 models (they even say that the arithmetic is going to be done in fp32).

If that is what you need, I can't help you. If you want to use mixed precision and for it to be faster than straight up fp32, you need to use tf.float16. Which is supposed to be supported within rocm ( see https://community.amd.com/thread/222479 ).

---

### 评论 #2 — witeko (2019-08-03T15:18:37Z)

@ekuznetsov139 ok, thanks for the answer. :)

---

### 评论 #3 — IIIBlueberry (2019-08-09T05:47:57Z)

hmn? but Miopen 2.0.0 just included support for bfloat16? https://github.com/ROCmSoftwarePlatform/MIOpen/releases

---

### 评论 #4 — dagamayank (2020-01-09T16:20:43Z)

MIOpen supports `bfloat16` on Radeon VII using software emulation for functional correctness. As correctly stated by @ekuznetsov139 Radeon VII does not have native HW acceleration for `bfloat16`.

@witeko  @IIIBlueberry please try out this feature and report any issues you encounter on our TensorFlow [repo](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream).

---
