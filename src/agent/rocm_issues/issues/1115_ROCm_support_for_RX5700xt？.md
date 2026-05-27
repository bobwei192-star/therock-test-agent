# ROCm support for RX5700xt？

> **Issue #1115**
> **状态**: closed
> **创建时间**: 2020-05-23T15:13:56Z
> **更新时间**: 2021-03-03T09:22:54Z
> **关闭时间**: 2021-03-03T09:22:54Z
> **作者**: sqlmap3
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1115

## 描述

*(无描述)*

---

## 评论 (14 条)

### 评论 #1 — ppolych (2020-05-23T15:31:19Z)

Not yet. I hope ROCm 3.4 will support Navi10. Check here: https://github.com/RadeonOpenCompute/ROCm/issues/887

---

### 评论 #2 — sqlmap3 (2020-05-25T03:58:27Z)

> Not yet. I hope ROCm 3.4 will support Navi10. Check here: #887

Do you have any more precise information? 

---

### 评论 #3 — ppolych (2020-05-28T00:33:03Z)

If you check the code there are some lines referring to gfx1010 (which is Navi10) but there is no support yet. There are no other informations about it.  

---

### 评论 #4 — sqlmap3 (2020-05-28T06:25:43Z)

ROCm 3.4 maybe support     

---

### 评论 #5 — x32349501 (2020-05-29T07:40:49Z)

Are you sure? I think it's a trend!

---

### 评论 #6 — ridvan5005 (2020-05-31T12:20:04Z)

I guess AMD doesn't want to invest the money he earns in the software. This is how I interpret that it does not offer Navi 10 support in the new update. Because the Navi 10 is a powerful chip and doesn't support it. 
I think we will have to request ROCm's Navi 10 support from NVIDIA. :)

---

### 评论 #7 — ppolych (2020-06-03T20:39:53Z)

ROCm 3.5 released without Navi support... pitty...  :(

---

### 评论 #8 — soutzis (2020-07-12T08:24:33Z)

I doubt we should expect any Navi10 support anytime before late 2021 - early 2022. I had to buy an Nvidia card instead

---

### 评论 #9 — ekondis (2020-07-12T20:56:46Z)

I have to report that I'm experimenting with an RX-5500 (gfx1012) card, on rocm 3.5.1 and it seems to work, not only for OpenCL apps but for HIP as well.

---

### 评论 #10 — sqlmap3 (2020-07-20T12:30:31Z)

Elias <notifications@github.com> 于2020年7月13日周一 上午4:56写道：

> I have to report that I'm experimenting with an RX-5500 (gfx1012) card, on
> rocm 3.5.1 and it seems to work, not only for OpenCL apps but for HIP as
> well.
>
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1115#issuecomment-657273968>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AETMW3KYCFCSKLVC5UYC7B3R3IPRVANCNFSM4NIPPQJA>
> .
>


---

### 评论 #11 — jli113 (2020-09-16T00:04:18Z)

I deeply regret buying this RX5700XT card. 

---

### 评论 #12 — soutzis (2020-09-16T00:13:07Z)

> 
> 
> I deeply regret buying this RX5700XT card.

Returning it and getting an rtx2070 super was the best decision I ever made.

---

### 评论 #13 — xuhuisheng (2020-09-16T02:20:54Z)

Here are more disscusions about RX 5700XT supporting.
https://github.com/RadeonOpenCompute/ROCm/issues/887

---

### 评论 #14 — ROCmSupport (2021-03-03T09:22:54Z)

Hi All,
As I mentioned in other threads, we will come up with the support of Navi cards soon, but I can not comment on specific series of cards right now.
I hope you understand my point.
We request you to wait for few more days for official support and keep watching our documentation.
Thank you.

---
