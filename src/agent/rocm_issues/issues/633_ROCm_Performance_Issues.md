# ROCm Performance Issues...

> **Issue #633**
> **状态**: closed
> **创建时间**: 2018-12-13T16:29:15Z
> **更新时间**: 2023-09-20T21:08:41Z
> **关闭时间**: 2023-09-20T21:08:41Z
> **作者**: briansp2020
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/633

## 描述

https://www.phoronix.com/scan.php?page=article&item=rocm19-nvidia415-compute&num=3

I thought the whole idea behind HSA/ROCm was to reduce kernel launch latency overhead. How is it that NVidia has so much lower latency? Is NVidia doing similar thing to HSA for kernel launch? How much more room for improvement in AMD's code is there? Is the bottleneck software? firmware? or something else?

Just curious. I did not expect AMD to lose so badly in latency measure against NVidia... 

---

## 评论 (2 条)

### 评论 #1 — foobar2019 (2019-01-23T03:03:33Z)

ROCm is an optimizing compiler toolchain, bleeding edge llvm as opposed to the poor ancient thing which comes with stock driver. You can get fancy things like int24 and tight control over compiler result, but it can't fix inheherent limits of GCN architecture. Such as the latencies - frequently just GDDR5 NV CU shared bus vs GCN+HBM tightly banked to CUs.

When you strip all the marketing bullshit, AMD boils down to being awesome as an open architecture, but meh choice if the plan is standard throwing hardware, not dev effort at the problem. Because of the openness, it can beat NV by far when you choose to exploit it and work close to the metal - NV being a profound black box compared to that. Yet NV is far more "cpu-like", friendlier to high level, sprawling kernels which can afford to be less aware of the metal itself.

---

### 评论 #2 — briansp2020 (2023-09-20T21:08:41Z)

Closing since this is very old

---
