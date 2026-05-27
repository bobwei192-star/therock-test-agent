# Is it a RX580 ERROR? Backward-propagation doesn't work both in tensorflow and pytorch.

> **Issue #724**
> **状态**: closed
> **创建时间**: 2019-03-04T14:43:36Z
> **更新时间**: 2019-03-04T15:24:53Z
> **关闭时间**: 2019-03-04T15:24:52Z
> **作者**: YongyiZhou
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/724

## 描述

Recently I use tensorflow-rocm to train my model, but the result is wrong while the same code work well in another CUDA computer.

https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/337

 And some guys who use pytorch-rocm meet the same problem: his code doesn't work on rx580, but works well in pytorch-rocm developer's gfx900 architecture.

https://github.com/ROCmSoftwarePlatform/pytorch/issues/342


---

## 评论 (1 条)

### 评论 #1 — jlgreathouse (2019-03-04T15:24:52Z)

Closing this since there are open issues both in tensorflow-upstream and our pytorch branch about this.

---
