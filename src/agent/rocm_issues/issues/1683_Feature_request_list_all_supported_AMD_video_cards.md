# Feature request: list all supported AMD video cards.

> **Issue #1683**
> **状态**: closed
> **创建时间**: 2022-02-17T05:57:32Z
> **更新时间**: 2022-02-28T21:31:25Z
> **关闭时间**: 2022-02-28T21:31:25Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1683

## 描述

When I buy any recent NVIDIA video card, I know it supports CUDA.

When I see people open issues here saying their AMD video card can't initialize ROCm stack, the usual response from AMD employees is "we don't support that video card".

I can find mentions of *some* supported AMD video cards in some obscure AMD PDFs on the Internet, but

would've been nice to just have a list of all AMD video cards that are currently supported.

Thanks.

---

## 评论 (13 条)

### 评论 #1 — Umio-Yasuno (2022-02-17T06:29:03Z)

I agree.  
In my opinion, it would be helpful to indicate the support status in some groups: *the software tools (e.g. for debug), the OpenCL/HIP runtime, the HPC libraries, the machine learning libraries*, etc.  
This prevents the issue from focusing on one ROCm repository.
It also makes it easier to provide appropriate support and report problems.

---

### 评论 #2 — nlnjnj (2022-02-18T01:31:16Z)

I agree too.

I only find a list from here:
https://docs.amd.com/bundle/ROCm_Installation_Guidev5.0/page/Prerequisite_Actions.html

But for RDNA GPUs, do 6800xt and 6900xt support by this release?

---

### 评论 #3 — sampie (2022-02-19T09:10:10Z)

I agree. I think it has been clearly stated that ROCM will come with RDNA2 support (https://github.com/RadeonOpenCompute/ROCm/issues/1180). It was also said to happen already in 2021. 6000 series GPUs are RDNA2 right?

---

### 评论 #4 — ghost (2022-02-19T09:23:58Z)

Please stay on topic of this issue, this issue is about an official *list* of *all* supported AMD video cards and feature levels, as was suggested by @Umio-Yasuno, not about some particular video cards you want to know about. Open another issue if you want to know which ones or if all RDNA2 video cards are supported, though this issue is not about that. Thanks! 🙂 

---

### 评论 #5 — FCLC (2022-02-21T02:35:36Z)

I've been attempting to create something analogous to this in #1617 

It's doesnt currently include pre-RDNA cards, but I'd gladly welcome contributions from others to track

A: What cards are supported in the latest version
B: What was the last version of ROCm to support a given card
C: What card has no support in any version whatsoever 

---

### 评论 #6 — ROCmSupport (2022-02-23T07:30:16Z)

Hi @procedural 
Thanks for reaching out.
You are looking for the information of listing each and every card that supports ROCm?
Our docs have this information right? This needs to be matured or do you wish to see the list in a different way?
Please share your thoughts. 

---

### 评论 #7 — ghost (2022-02-23T09:19:21Z)

> You are looking for the information of listing each and every card that supports ROCm?

Yes, a list of all AMD cards AMD officially supports for latest versions of ROCm. Such a list can be updated if support for some AMD cards or ROCm versions is dropped.

> Our docs have this information right? This needs to be matured or do you wish to see the list in a different way?

This repository doesn't have a direct link to such a list, @nlnjnj found one, but it already conflicts with the links from https://docs.amd.com for ROCm v5.0 and ROCm v5.0.1 which point to https://docs.amd.com/bundle/AMD_ROCm_Release_Notes_v4.5/page/Hardware_and_Software_Support.html that doesn't state that RDNA cards are supported, even though https://docs.amd.com/bundle/ROCm_Installation_Guidev5.0/page/Prerequisite_Actions.html states they are.

This is all confusing. Just have a single list of currently supported AMD video cards and link it to this repository's readme. Thanks.

---

### 评论 #8 — kingcrimsontianyu (2022-02-28T04:26:19Z)

Team green has set a great example: https://developer.nvidia.com/cuda-gpus

---

### 评论 #9 — ROCmSupport (2022-02-28T10:27:54Z)

> > You are looking for the information of listing each and every card that supports ROCm?
> 
> Yes, a list of all AMD cards AMD officially supports for latest versions of ROCm. Such a list can be updated if support for some AMD cards or ROCm versions is dropped.
> 
> > Our docs have this information right? This needs to be matured or do you wish to see the list in a different way?
> 
> This repository doesn't have a direct link to such a list, @nlnjnj found one, but it already conflicts with the links from https://docs.amd.com for ROCm v5.0 and ROCm v5.0.1 which point to https://docs.amd.com/bundle/AMD_ROCm_Release_Notes_v4.5/page/Hardware_and_Software_Support.html that doesn't state that RDNA cards are supported, even though https://docs.amd.com/bundle/ROCm_Installation_Guidev5.0/page/Prerequisite_Actions.html states they are.
> 
> This is all confusing. Just have a single list of currently supported AMD video cards and link it to this repository's readme. Thanks.

Hi @procedural 
I personally felt the same. We have different weblinks pointing different information, informed Documentation team already.
Request to wait for sometime.
Thank you.

---

### 评论 #10 — Rmalavally (2022-02-28T20:57:33Z)

Thank you for reaching out, @procedural. This issue is fixed. Could you please access https://docs.amd.com, and click the link in the Support Documentation box. 

As always, we look forward to your feedback for improvement.

Sincerely,
AMD ROCm Documentation Team

---

### 评论 #11 — ghost (2022-02-28T21:16:02Z)

So the new link is
https://docs.amd.com/bundle/Hardware_and_Software_Reference_Guide/page/Hardware_and_Software_Support.html
, correct?

---

### 评论 #12 — Rmalavally (2022-02-28T21:21:12Z)

That is correct. 

---

### 评论 #13 — ghost (2022-02-28T21:31:25Z)

Thanks, the issue can be closed then.

It would also be nice to add the link to this repository's readme directly, to track it if it will change in future.

---
