# Document functional hardware status

> **Issue #844**
> **状态**: closed
> **创建时间**: 2019-07-13T13:26:58Z
> **更新时间**: 2024-01-11T04:42:47Z
> **关闭时间**: 2024-01-11T04:42:46Z
> **作者**: Bengt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/844

## 描述

The section "Hardware Support" of ROCm's README lists the status of various GPUs:

https://github.com/RadeonOpenCompute/ROCm/blob/master/README.md#hardware-support
https://rocm.github.io/hardware.html

* The documentation lists some GFX7 GPUs as working, while not being supported.
* The documentation states that GFX8 GPUs are supported, while they do not actually work.[1]
* The documentation lists GFX9 GPUs that are supported, but does not make a statement about whether or not they actually work.

1: ROCm 2.0 broke TF-ROCm: https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/479

There should be a clear statement on whether or not which GPUs work with ROCm. This statement should be reevaluated and updated with at least each minor (1.9, 2.0, 2.1 ...) release.

A more thorough solution would be to add the actual build status to the documentation as badges, like TensorFlow does:

https://github.com/tensorflow/tensorflow#continuous-build-status

However, there are not even resources to add GFX8 gpus to CI in the first place:

https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/479#issuecomment-500099977

---

## 评论 (6 条)

### 评论 #1 — Bengt (2019-07-13T13:30:58Z)

People are frustrated with "supported" not meaning "working" and switching away from AMD GPUs:

* https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/479#issuecomment-499141229
* https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/479#issuecomment-499173264
* https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/479#issuecomment-510304467

---

### 评论 #2 — Bengt (2019-07-13T13:37:10Z)

Given that the cards work properly, many of their users will never need support at all. So the functional hardware status might be the more relevant information for many users.

---

### 评论 #3 — JMadgwick (2019-07-14T07:48:48Z)

>     The documentation lists some GFX7 GPUs as working, while not being supported.

When I last tested it GFX7 is was **not in any way supported by Tensorflow** and I don't think it is working at all now. Last time I had it working was with ROCm 1.9 and it wasn't working in ROCm 2.0, might be fixed now.
Ideally there would be a table stating the gfx numbers and giving examples of GPUs and saying what their status was with TF and other important parts of the ROCm project.

---

### 评论 #4 — sos-michael (2019-07-14T19:47:06Z)

This really is frustrating stuff and I'm glad I'm not alone in wondering when this going to get fixed + how clear the documentation is. 

I realize rocm is still young and. as such, don't mind the performance not being that great, but going out of my way to get a board that support the PCIe atomics and having it still  not be functional was really a pain point that AMD needs to address. 

---

### 评论 #5 — Bengt (2019-07-27T23:46:27Z)

Here is a recent example of a very nice beginner level article about using and GPUs with Keras:

https://towardsdatascience.com/train-neural-networks-using-amd-gpus-and-keras-37189c453878

In the comments, people are inspecting the results and noticing all kinds of weirdnesses run to run and when comparing to Nvidia cards. When this the first experience one makes with ROCm, why buy AMD cards for compute?

---

### 评论 #6 — nartmada (2024-01-11T04:42:46Z)

Thank @Bengt, @JMadgwick, and @sos-michael for your inputs.  Closing this ticket as it has gone stale.  Please check latest ROCm6.0.0 and open a new ticket if you still have concerns.   

---
