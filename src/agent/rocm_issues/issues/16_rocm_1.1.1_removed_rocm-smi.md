# rocm 1.1.1 removed rocm-smi

> **Issue #16**
> **状态**: closed
> **创建时间**: 2016-06-08T12:33:48Z
> **更新时间**: 2016-06-09T05:54:43Z
> **关闭时间**: 2016-06-08T14:25:45Z
> **作者**: psteinb
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/16

## 描述

I recently updated to rocm 1.1.1 under ubuntu 14.04.x. I saw that rocm-smi was remove during the update. I saw that I can install it via aptitude but I get a version that carries 1.0.0 in it's name. 

I was wondering how to proceed? Further, I love nvidia-smi in order to see if a process really runs on the dGPU, AFAIK I cannot do this with rocm-smi. What other methods are there to monitor app execution on the dGPU?


---

## 评论 (6 条)

### 评论 #1 — jedwards-AMD (2016-06-08T14:25:45Z)

The rocm-smi 1.0.0 version is the latest smi version, so you have the latest installed. It should be part of the default installation; the dependency list will be modified to includes it.


---

### 评论 #2 — psteinb (2016-06-08T14:55:23Z)

Thanks for your reply, @jedwards-AMD. What about my other question in the original issue post?


---

### 评论 #3 — ghost (2016-06-08T18:46:06Z)

Hey @psteinb 

Do you mean the feature to list <pid> <process> name for all processes that have a gpu context allocated?


---

### 评论 #4 — psteinb (2016-06-08T18:52:14Z)

well, in principle yes. I just need a command line tool where I see which processes use the device. of course, some more statistics like GPU occupancy and memory use would help as well. 


---

### 评论 #5 — ghost (2016-06-08T21:17:56Z)

These features are part of the plan. It should be available in one of the future ROCm releases.


---

### 评论 #6 — psteinb (2016-06-09T05:54:43Z)

thanks @arodrigx7 for the update. I'd wish that these kind of things would be visible in a roadmap file in this repo, with this it would be easier for stakeholders to judge where rocm is potentially evolving. just as an idea.

other projects do something along those lines as well: https://github.com/tensorflow/tensorflow/blob/master/tensorflow/g3doc/resources/roadmap.md


---
