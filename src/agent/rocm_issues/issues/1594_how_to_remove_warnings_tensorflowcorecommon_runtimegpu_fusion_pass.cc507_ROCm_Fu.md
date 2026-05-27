# how to remove warnings "tensorflow/core/common_runtime/gpu_fusion_pass.cc:507 ROCm Fusion is enabled"

> **Issue #1594**
> **状态**: closed
> **创建时间**: 2021-10-22T06:41:10Z
> **更新时间**: 2023-08-11T14:18:00Z
> **关闭时间**: 2021-11-16T09:13:11Z
> **作者**: neqkir
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1594

## 描述

TF 2.6.0
docker image
CentOs
running a machine learning TF  code

How to tune or hide those warnings ?

![image](https://user-images.githubusercontent.com/89974426/138405238-53c01286-cba3-4ec9-8616-89e910c4f91c.png)


---

## 评论 (5 条)

### 评论 #1 — ROCmSupport (2021-11-02T12:08:57Z)

Thanks @neqkir for reaching out.
Can you please share the exact steps(step-by-step) to reproduce the problem.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-11-02T12:13:27Z)

I recommend to raise this issue in TensorFlow area as I feel issue is due to TensorFlow runtime.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-11-16T09:13:11Z)

I am closing this issue as its mostly TF related, recommend to file in TF space.
Thank you.

---

### 评论 #4 — mpeschel10 (2023-06-02T20:58:11Z)

To suppress the "ROCm Fusion is enabled" warning, set the following environment variable:
```sh
export TF_CPP_MAX_VLOG_LEVEL=-1
```
Works for me on Arch Linux as of June 2, 2023.

As ROCmSupport mentions, this appears to be a tensorflow-upstream issue. I believe the bug appears at [line 508 of core/common_runtime/gpu_fusion_pass.cc](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/blob/18ddd5aa0329993f581bdb433b999b85c15f69e3/tensorflow/core/common_runtime/gpu_fusion_pass.cc#L508):
```cpp
  VLOG(0) << "ROCm Fusion is enabled.";
```
where `VLOG(0)` should probably be `VLOG(kVlogLevel)`.

---

### 评论 #5 — mpeschel10 (2023-08-11T14:17:59Z)

I came back to submit a pull request because it seemed easy to fix. However, it looks like `VLOG(0)` was intentional, and the log spam is caused by a bug somewhere else.

Specifically, the `VLOG(0)` line was introduced in [commit 07a72f230](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/commit/07a72f23034d996c9dc2870d1007af4778045058), "disabling the ROCm Fusion related info messages". According to the commit message, "when fusion is enabled... a single info message will be displayed". I assume, then, that `ROCmFusionPassBase::Run` was only meant to run once, and a later commit made it run many times.

To fix this, either the message should be moved to a function called only once, or it should have a separate log level (maybe `kVlogLevel - 1`?), or it should have a global boolean flag to stop it being printed multiple times, or it should be moved to an if statement in Tensorflow's entry point looking at `TF_ROCM_FUSION_ENBALE`. I don't have enough experience to say which would work better. Fixing this is left as an exercise for the reader.

---
