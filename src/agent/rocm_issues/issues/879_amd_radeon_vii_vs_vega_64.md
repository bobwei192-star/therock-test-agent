# amd radeon vii vs vega 64

> **Issue #879**
> **状态**: closed
> **创建时间**: 2019-08-28T13:09:41Z
> **更新时间**: 2023-12-18T22:25:31Z
> **关闭时间**: 2023-12-18T22:25:31Z
> **作者**: SlimRG
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/879

## 描述

Sorry, If I shouldn't ask here... 
I want to buy GPU only for ROCm PyTorch
So I don't know - what will give me more speed in pytorch

---

## 评论 (5 条)

### 评论 #1 — himanshugoel2797 (2019-08-28T13:59:03Z)

The VII is hands down the faster card, plus the larger HBM memory is useful if you're working with large matrices. But, the 64 is much cheaper so it's up to you if you're willing to spend nearly double for around 20-30% more perf.

---

### 评论 #2 — kinred (2019-08-30T11:17:28Z)

@himanshugoel2797 the Radeon VII performance increase to a Vega 64, from my experience, is more like 50%.

Also the Radeon VII has useable fp16 support which can further increase the performance, at least for interference jobs.

For example for Resnet 50 training:

Vega 64 fp32:  202 images/s
Vega 64 fp16:  186 images/s ?!?
Radeon VII fp32:  315 images/s
Radeon VII fp16:  455 images/s

(These numbers are with Tensorflow 1.14 though)

So if there is the budget, I would definitely go for a Radeon VII.

---

### 评论 #3 — twuebi (2019-09-02T10:33:15Z)

No experience with PyTorch, but with TF:

Be aware of these unresolved issues with the VII, Vega and ROCm:

1. https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/325:
 Networks randomly crash because at least two ops (`tf.transpose`, `tf.dynamic_stitch`) produce garbage integer outputs. Reported in February, confirmed on 5 nodes (3x Radeon VII, 1x Vega FE, 1x unknown), it took 3 months to set up a reproducer and another 3 months to arrive at the conclusion that the problem is most likely somewhere on a "lower level of the stack"

2. https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/534:
BERT, a standard residual FF network in NLP, crashes with a memory access fault. Reported two months ago, confirmed on 3 Radeon VII, the "workaround" is to use the official docker image which means 20% decrease in throughput.

For both errors, there is no fix in sight and no indication of active work or progress on the issue.

---

### 评论 #4 — tasso (2023-12-12T22:56:29Z)

Is this issue still reproducible?  if not, can we please close it?  Thanks!

---

### 评论 #5 — tasso (2023-12-18T22:25:31Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request.  If this is still an issue, please file a new ticket and we will happy to investigate it.  Thanks!

---
