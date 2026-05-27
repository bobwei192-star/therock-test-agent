# Navi support ready for trial

> **Issue #938**
> **状态**: closed
> **创建时间**: 2019-11-18T19:30:28Z
> **更新时间**: 2023-12-18T16:13:09Z
> **关闭时间**: 2023-12-18T16:13:09Z
> **作者**: smartbitcoin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/938

## 描述

After wait 5 month since navi launch, Rocm still not officially add support for navi. 
I have to spend two weeks to make it navi compatible.
To help developers to try this new hardware,  I create a repo for downloading.

https://github.com/smartbitcoin/MyROCm

![image](https://user-images.githubusercontent.com/5984485/69083260-c25ec780-0a0f-11ea-97d2-9c1a2f884f85.png)

welcome testing and send me feedback.


---

## 评论 (10 条)

### 评论 #1 — linzhanyu (2019-12-16T16:23:05Z)

Can you support Ubuntu 18.04 ?  Thank you !!!

---

### 评论 #2 — stylemistake (2020-01-08T20:28:56Z)

Be careful installing his binary releases. He has provided no build scripts, patches or complete instructions on how to build it yourself.

---

### 评论 #3 — smartbitcoin (2020-01-17T20:16:24Z)

@stylemistake This is just prototype to confirm how far Navi from ROCm.  You should NOT install this binary on any critical system and it's far from product ready also.
Use spare PC , clean format and test it is proper way.  and I am not very sure the quality of this porting ( lots of changes is based on assumption, and NO confirmation from AMD yet).

Now I am trying working on navi for rocm3.0 with tensorflow,  if I able to fully confirm it works.  I 'll upload the patch into git and building docs.

---

### 评论 #4 — smartbitcoin (2020-01-17T20:18:01Z)

> Can you support Ubuntu 18.04 ? Thank you !!!

Fully function Navi need linux kernel > 5.3 , which ubuntu 18.04 missing, that's why I start from ubuntu 19.10.

---

### 评论 #5 — stylemistake (2020-01-18T01:06:12Z)

> Now I am trying working on navi for rocm3.0 with tensorflow, if I able to fully confirm it works. I 'll upload the patch into git and building docs.

That is awesome news! PyTorch has also released recently with an official ROCm support, so I'm even more inclined to try building it myself, but the process is quite hacky. Some docs would be really handy. :ok_hand: 

---

### 评论 #6 — wis (2020-01-30T17:50:48Z)

I'm not downloading sketchy binaries, open source it

---

### 评论 #7 — smartbitcoin (2020-01-30T19:04:39Z)

@wis > I'm not downloading sketchy binaries, open source it

does anybody force you download it ?  if yes,  could you sue them ?  or could you just patch it by yourself? 

If you are here try to help ,  could you please ask AMD add opensource support for Navi?

What make your think that I'll care about what you need when AMD who sold you their NAVI don't care about you at all?   lol 



---

### 评论 #8 — mritunjaymusale (2020-02-22T12:05:09Z)

At this point, I am starting to think, I wasted my money on 5700xt.

---

### 评论 #9 — nartmada (2023-12-13T20:10:13Z)

Hi @smartbitcoin , please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #10 — nartmada (2023-12-18T16:13:09Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
