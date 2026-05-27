# Enabling xla on tensorflow-rocm with Rocm 5.2.3?

> **Issue #1796**
> **状态**: closed
> **创建时间**: 2022-08-23T18:19:27Z
> **更新时间**: 2023-12-19T01:55:50Z
> **关闭时间**: 2023-12-19T01:55:50Z
> **作者**: ffleader1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1796

## 描述

I have a gfx1030 card l, Rocm 5.2.3 and currently running into xla issues with tensorflow.
My GPU can do pytorch model fine, can do tensorflow fine, without xla. With xla however, I got this error: ````bitcode module not found at ./opencl.bc````

Am I missing something during the install process (because I installed with ````rocm```` usecase).

How to get my device running tensorflow training with xla?
Thank you 

---

## 评论 (7 条)

### 评论 #1 — aoolmay (2022-08-26T09:20:46Z)

Can confirm, error is reproducible on 6800XT and 6950XT.
Fresh installation: ROCm 5.2.3 + tensorflow-rocm 2.9.2 + Linux 5.11.0-27 (as per installation instructions)
Last working setup, ROCm 5.1.3 + tensorflow 2.9.1

Loss of XLA capability results in ~7% performance loss on most tensorflow workloads.

---

### 评论 #2 — Mushoz (2022-12-04T14:14:01Z)

Same issue here. Any idea on when we can expect a fix?

---

### 评论 #3 — Mushoz (2022-12-05T08:54:38Z)

I would have expected this issue to get way more attention if it affected everyone. Maybe it doesn't? A question for you @aoolmay and @ffleader1 : What distro are you guys running? I am using Archlinux myself, which is technically unsupported. I am curious if this also affects people that are running supported distributions.

Lastly, my models currently refuse to run at all. How do I explicitly disable XLA so that it at least works again?

---

### 评论 #4 — macmv (2023-02-28T07:34:48Z)

I've had the same issue (also running arch with a 6800xt), and setting `ROCM_PATH` to `/opt/rocm` fixed it for me.

---

### 评论 #5 — Epliz (2023-03-25T09:26:23Z)

hit the same issue with a MI100 GPU, setting `ROCM_PATH` also helped

---

### 评论 #6 — nartmada (2023-12-18T20:16:52Z)

Hi @ffleader1, please check latest ROCm Documentation and ROCm 6.0.0 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #7 — ffleader1 (2023-12-19T01:55:22Z)

> Hi @ffleader1, please check latest ROCm Documentation and ROCm 6.0.0 to see if your query has been resolved. If resolved, please close the ticket. Thanks.

I am no longer have access to my original PC
But guessing the complaints were not that much anymore, I guess it's fixed.

---
