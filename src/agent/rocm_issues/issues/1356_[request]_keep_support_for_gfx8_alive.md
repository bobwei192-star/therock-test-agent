# [request] keep support for gfx8 alive

> **Issue #1356**
> **状态**: closed
> **创建时间**: 2021-01-05T11:43:31Z
> **更新时间**: 2021-01-09T12:45:10Z
> **关闭时间**: 2021-01-06T04:28:00Z
> **作者**: Moading
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1356

## 描述

Dear ROCm developers,
I am asking you to keep the support for gfx8 devices in ROCm. I know resources are rare and it it inevitable to drop support for any given GPU at some point in time. However, there seems to be a rather large user group using these GPUs. Even if these GPUs are not manufactured anymore, they are still available for purchase. Excluding the users of these GPUs from latest developments is unwise because many developers make their first steps on workstations before using more professional hardware in a GPU cluster. Here are a few reasons for keeping support for gfx alive:

- gfx8 GPUs are still sold and advertised as OpenCL 2.0 devices
- gfx8 GPUs allow beginners to make first steps in GPU computing before using more powerful hardware
- latest GPUs are only slowly added to ROCm and the availability in stores is bad, prices for new hardware are high
- no graduate student can afford a 5.000+$ GPU

People, please comment here if you would like to see continued support for gfx8. For me, I would like to see support for gfx803.

---

## 评论 (8 条)

### 评论 #1 — valeriob01 (2021-01-05T12:03:21Z)

I support this request.


---

### 评论 #2 — xuhuisheng (2021-01-06T02:27:27Z)

In my opinion, we cannot ask something live forever.

Actually, gfx803 had been broken seems ROCm-3.7, in the mid of August, 2020. 
But I suppose these issues maybe only affect Polaris, because of  polaris has only 36 cu, which fiji has 64 cu. If someone had r9nano or fury could have a try.

I think we should create a community edition for supporting these old cards. Since AMD wont add new features on old cards, at least we can try to prevent these old cards broken on AI computing.

---

### 评论 #3 — ROCmSupport (2021-01-06T04:28:00Z)

Hi @Moading and all
Thanks for your support and suggestions.
Due to the addition of new hardware, os etc and increased coverage, we can not support old devices.
We are adding new hardware slowly and so supporting & working on fixing issues specific to old hardware is not possible.
This is the part of the process and request you to understand and align with us.
Thank you.

---

### 评论 #4 — Moading (2021-01-06T08:49:40Z)

Closing the ticket after about 17 hours, killing a discussion before it generates too much trouble - nice culture.
Please make sure that the rate of added hardware is comparable to the rate of deprecated hardware.

---

### 评论 #5 — ROCmSupport (2021-01-06T09:10:37Z)

Thanks @Moading for understanding and sharing your suggestions.
Thank you.

---

### 评论 #6 — selroc (2021-01-06T20:46:18Z)

> Hi @Moading and all
> Thanks for your support and suggestions.
> Due to the addition of new hardware, os etc and increased coverage, we can not support old devices.
> We are adding new hardware slowly and so supporting & working on fixing issues specific to old hardware is not possible.
> This is the part of the process and request you to understand and align with us.

and throw away our old cards!
do you understand that for some of us it is a financial disaster ?



---

### 评论 #7 — umeshu (2021-01-08T05:14:07Z)

@selroc 

Apparently, they don't. 

The problems of the peasants are of no concern to the olympian gods who drink honey with their golden cups.  

---

### 评论 #8 — umeshu (2021-01-09T12:44:36Z)

> In my opinion, we cannot ask something live forever.
> 
> Actually, gfx803 had been broken seems ROCm-3.7, in the mid of August, 2020.
> But I suppose these issues maybe only affect Polaris, because of polaris has only 36 cu, which fiji has 64 cu. If someone had r9nano or fury could have a try.
> 
> I think we should create a community edition for supporting these old cards. Since AMD wont add new features on old cards, at least we can try to prevent these old cards broken on AI computing.

@xuhuisheng It would be great to have a community edition of ROCm for old cards. Although I'm not a qualified ROCm developer by any means, just a regular joe who wants to use the card for my research in AI, I can help in other things, like testing, documentation, etc. 

---
