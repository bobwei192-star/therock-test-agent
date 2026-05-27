# ROCm in the news

> **Issue #252**
> **状态**: closed
> **创建时间**: 2017-11-13T13:23:02Z
> **更新时间**: 2017-12-20T19:05:23Z
> **关闭时间**: 2017-12-20T19:05:23Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/252

## 描述

https://www.anandtech.com/show/12032/amd-announces-wider-epyc-availability-and-rocm-17-with-tensorflow-support

---

## 评论 (10 条)

### 评论 #1 — gstoner (2017-11-13T13:56:15Z)

Should have been Tensorflow get MultiGPU support,  ROCm has alway had multigpu support    We working on RCCL.





---

### 评论 #2 — boxerab (2017-11-13T14:08:46Z)

Yes. Usually Anandtech quality is good.  What is RCCL ?
Since they mention 1.7, can you share an ETA for this release ?

---

### 评论 #3 — nevion (2017-11-13T14:21:59Z)

I think anandtech is relatively good to an abysmally bad industry but the homework the benchmark industry puts in doesn't cut it anymore and they're wrong very often... especially on details like this.  Which is to say I don't trust anandtech much on CPUs or especially GPUs anymore either.

RCCL.... is that pronounced rickle?

---

### 评论 #4 — gstoner (2017-11-13T14:40:36Z)

Thanks.

Yes. We did scratch re-write MPI/NCCL like Communication Primitive library.

Big think is three Distro Ubuntu, REHL/CENTOS and SUSE supported by DKMS. 

Greg



---

### 评论 #5 — oscarbg (2017-11-13T21:32:47Z)

So ROCM 1.7 is what brings finally also full OpenCL 2.1 support (SPIR-V included) to AMD GPUs under Linux?
also shipped kernel will be updated from current 4.11?
thanks..
 

---

### 评论 #6 — xyang2013 (2017-11-16T02:11:08Z)

Hi Greg, I think there was a talk by Ben Sander on Tensorflow during SC17. Is it possible to upload the talk on Youtube? I am also interested in the talk by the person from Xilink. Thank you.

---

### 评论 #7 — gstoner (2017-11-21T16:31:31Z)

@oscarbg  This is early access release of 2.1,  last minute we had to pull pipes and Device enqueue the resource for this feature we pulled on a customer project.   Also, there is no SPIR-V  support part of this release, it is an optional spec for 2.1.    2.1 capability will be final in Q1 2018.   

---

### 评论 #8 — mirh (2017-12-10T22:29:00Z)

Last time I [checked](https://www.khronos.org/registry/OpenCL/specs/opencl-2.1.pdf) SPIR-V as an imperative requirement of core opencl 2.1, was all over the place in spec. 

---

### 评论 #9 — oscarbg (2017-12-11T08:33:54Z)

@mirh I was thinking the same but was afarid to say so as I was not sure enough..

---

### 评论 #10 — jimdowling (2017-12-14T18:29:24Z)

@gstoner  - looking forward to this. How different is your implementation to the Baidu Collectives library now in contrib in TensorFlow? And what about NCCL2? Will you support Ring-AllReduce with GPU-aware topology (that is, places devices on the same host adjacent to one another in the Ring so that there is only one input n/w link and one output n/w link in the Ring for each host) ? 

---
