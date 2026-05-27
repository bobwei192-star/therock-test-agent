# Will rocm repo accept a pull request for adding Navi support for HCC & HIP?

> **Issue #1003**
> **状态**: closed
> **创建时间**: 2020-01-22T02:59:09Z
> **更新时间**: 2021-04-19T12:58:24Z
> **关闭时间**: 2021-04-19T12:58:24Z
> **作者**: smartbitcoin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1003

## 负责人

- b-sumner

## 描述

HI dear official rocm team:
There are long time since Navi launched and ROCm still missing Navi support yet.  There are lots of improvement in rocm 3.0 codebase for Navi to functional well.  Meanwhile, MyROCm porting to navi for hcc and hip component, seems stable now. So I would like contribute this patch to rocm git, but I am not sure if AMD have the any decision on Navi support from rocm yet.   
Would AMD treat Navi as a consumer grade card excluding from ROCm or it will soon add the support ?
Would the contribution for Navi to Rocm welcome or it will against some AMD's policy ?

Can't wait for a clear guidance from AMD and the plan for Navi with ROCm.

Good new:
linux kernel 5.4+'s golden register patch improve Navi performance by 20%+ after myrocm's benchmark. that's really amazing patch. 

If any interest to review myrocm navi build , you can find binary download url here:
https://github.com/smartbitcoin/MyROCm/releases/download/3.0_navi10/myrocm.3.0.tar.bz2

---

## 评论 (7 条)

### 评论 #1 — AlexVlx (2020-01-22T22:47:16Z)

Soft assigning to @b-sumner since he might have more insight.

---

### 评论 #2 — omerferhatt (2020-01-23T16:56:58Z)

For fun fact, committing AMD's repo with NVIDIA Geforce RTX profile photo. Made me smile

---

### 评论 #3 — ddobreff (2020-01-24T12:01:40Z)

Its opensource project? Why would AMD block your PRs? Just submit for review.

---

### 评论 #4 — mritunjaymusale (2020-01-26T20:34:53Z)

Can you tell how to install your binary ? I have a 5700xt I would like to test it for pytorch.



---

### 评论 #5 — smartbitcoin (2020-01-30T17:47:43Z)

@mritunjaymusale    > Can you tell how to install your binary ? I have a 5700xt I would like to test it for pytorch.
MyRocm for navi only provide hcc and hip support for gfx1010, which is a compiler.
For pytorch support,  it also need MIOpen, rocBlas, rocRand component. I once tried to compile rocBlas, but this lib use tons of asm. Even it also have a default hip implementation , I still failed to build a working lib as it need some some opencl dependencies somewhere.


---

### 评论 #6 — smartbitcoin (2020-01-30T17:54:35Z)

@ddobreff > Its opensource project? Why would AMD block your PRs? Just submit for review.

Opensource project have community driven or corporate driven. For community driven project, you can just PR and wait the response.   For company driven project,  it have certain policies, like product support range, functionality required etc.

ROCm is a AMD leading project, if your PR not align with their roadmap, it won't work.

Since it's opensource, you definitely can just fork and improve.  But maintenance a project like ROCm need huge resource, it's just not for individual developers.

The best hope is AMD leading it by adding support for Navi,  and community helping testing and contributing.


---

### 评论 #7 — ROCmSupport (2021-04-19T12:58:24Z)

Hi @smartbitcoin 
Thanks for reaching out.
Navi is in internal testing phase.
Once complete work is done, it will be added officially.
Thank you.

---
