# Is 5900HX iGPU is supported by ROCm now ?

> **Issue #1799**
> **状态**: closed
> **创建时间**: 2022-08-25T08:07:37Z
> **更新时间**: 2024-02-16T16:06:29Z
> **关闭时间**: 2024-02-16T16:06:28Z
> **作者**: timiil
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1799

## 描述

hi , as the title, i have brought a board which 5900 HX cpu,  i am looking to install an Ubuntu 20.04, and use ROCm to predict some PyTorch pretrainned mode (using TorchServe)

any idea ?

---

## 评论 (6 条)

### 评论 #1 — langyuxf (2022-08-26T02:17:26Z)

It is a gfx90c iGPU, not officially supported. But there is a hack, just run like this.

```
$ HSA_OVERRIDE_GFX_VERSION=9.0.0 python3
>>> import torch
>>> torch.cuda.is_available()
True
>>>
```


---

### 评论 #2 — timiil (2022-08-26T03:02:06Z)

thanks a lot , i will make a try and post the result here , thanks again :)

---

### 评论 #3 — MatPoliquin (2022-09-29T00:30:31Z)

@xfyucg Did it work?

---

### 评论 #4 — nartmada (2023-12-18T20:09:52Z)

Hi @timiil, please check latest ROCm Documentation and ROCm 6.0.0 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #5 — nartmada (2023-12-22T19:43:13Z)

Hi @timiil, any luck with using xfyucg's work-around?  Thanks.

$ HSA_OVERRIDE_GFX_VERSION=9.0.0 python3
>>> import torch
>>> torch.cuda.is_available()
True
>>>

---

### 评论 #6 — nartmada (2024-02-16T16:06:28Z)

Closing this ticket as no response from @timiil.  Please re-open if you are not able to work-around the issue.  Thanks.

---
