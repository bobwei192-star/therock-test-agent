# The speed of predict is so slow! 

> **Issue #1564**
> **状态**: closed
> **创建时间**: 2021-08-24T09:20:41Z
> **更新时间**: 2021-12-13T05:30:24Z
> **关闭时间**: 2021-12-13T05:30:24Z
> **作者**: Joevaen
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1564

## 描述

Hi, everyone. I am meeting a really confusing question!
I use the Super Computing Center in China to accelerate my training process, which deploys the DCU Card and installs the pytorch ROCm whose version is 4.2(beta). 
But I encountered a srange issue:
![image](https://user-images.githubusercontent.com/46133615/130589787-5b55809f-f4d2-481f-a299-e5d57bdd9e58.png)
As the picture above shows, The value in left circle  is time of `out = model(in)` , and the valu in right circle is time of `backward()`.
In NVIDIA's 960, the two value above are both 0.0x. I think this is so weired. The input that was feed to network is an array whose shape is (2500, 12). 
Another, I test on two different Super Compute Center in China. They all have the same problem.
Actually, I know that maybe I have to make some optimization if I want to move from cuda to dcu. But I can't find the solution and I wanna know why.
Thanks vvvvvvery much!!!!!!

---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-08-24T09:45:24Z)

Thanks @Joevaen for reaching out.
Can you please share the exact steps you followed to reproduce the problem so that I will try the same and update.
Thank you.

---

### 评论 #2 — Joevaen (2021-08-25T10:01:30Z)

[https://github.com/RadeonOpenCompute/ROCm/issues/1565](url) is the same question. We have dealt with this issue via modify network architecture. Maybe you can make a test and I think it is an urgently needed bug.

---

### 评论 #3 — ROCmSupport (2021-11-16T09:56:14Z)

Hi @Joevaen 
Can you please validate with the latest ROCm 4.5 and update.
Thank you.

---

### 评论 #4 — ROCmSupport (2021-12-13T05:30:24Z)

I am closing this as there is no response from user for the last 4 weeks.
Request to open a new ticket, if any, with all details steps, for quick resolution. Thank you.

---
