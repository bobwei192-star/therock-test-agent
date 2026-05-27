# Is Caffe the only ML framework that currently supports AMD GPUs ?

> **Issue #349**
> **状态**: closed
> **创建时间**: 2018-03-01T13:20:02Z
> **更新时间**: 2018-03-05T08:17:07Z
> **关闭时间**: 2018-03-03T17:08:25Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/349

## 描述

*(无描述)*

---

## 评论 (7 条)

### 评论 #1 — gstoner (2018-03-01T13:35:46Z)

No we have Tensorflow 1.0 out refresh is happing soon.

On Mar 1, 2018, at 7:20 AM, Aaron Boxer <notifications@github.com<mailto:notifications@github.com>> wrote:


—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/349>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuVWb6BLO5kfEnXIQejXRi0YWL90Vks5tZ_WDgaJpZM4SYSyZ>.



---

### 评论 #2 — boxerab (2018-03-01T13:40:08Z)

Great. Can't wait! Can you comment on PyTorch ? 

---

### 评论 #3 — psteinb (2018-03-01T13:43:18Z)

How about mxnet as hinted at 
[here](https://github.com/RadeonOpenCompute/hcc/issues/397#issuecomment-358262001)?


---

### 评论 #4 — gstoner (2018-03-02T22:58:59Z)

@boxerab  @psteinb @perhaad http://repo.radeon.com/misc/archive/beta/rocm-1.7.1.beta.4.tar.bz2

Can you test this release 

g

---

### 评论 #5 — boxerab (2018-03-03T16:47:46Z)

Thanks, I am testing it now. Question: how can I test that I have the latest opencl driver from the beta?
When I run `/opt/rocm/opencl/bin/x86_64/clinfo`, it says that driver version is `2576`.  Is this the correct version?  

---

### 评论 #6 — gstoner (2018-03-03T17:09:18Z)

@psteinb MxNet is getting real close 

---

### 评论 #7 — psteinb (2018-03-05T08:17:07Z)

Very cool. Am at a [hackathon 
now](https://gcoe-dresden.de/the-hack-is-on-in-2018/) and will upgrade 
and test it right after. If anyone can share experiences, please do so.


---
