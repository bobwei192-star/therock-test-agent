# Rocm support for Radeon RX 7000 Series (7900XT and 7900XTX)

> **Issue #1874**
> **状态**: closed
> **创建时间**: 2022-12-12T14:47:10Z
> **更新时间**: 2022-12-16T14:23:21Z
> **关闭时间**: 2022-12-16T14:23:21Z
> **作者**: SharoonSaxena
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1874

## 描述

I am done building a Deep learning build except for GPU. I have same thoughts on Nvidia GPUs as Linus Torvalds a decade ago.

I wish to know if ROCm will support the upcoming Radeon RX 7900XTX, or when it is expected to be supported, if at all.

---

## 评论 (4 条)

### 评论 #1 — aoolmay (2022-12-13T15:44:15Z)

Urgently need ETA on RDNA3 inclusion too!

RDNA2 PRO cards came about 6 months after gaming cards and you had to wait another 6 months for driver and software stack update.

Not waiting this time.

---

### 评论 #2 — powderluv (2022-12-15T07:49:33Z)

While you wait for an official ROCM release, if you have specific workloads like stable diffusion it is worth trying http://shark.sd that uses the AMD vulkan path and is available on both linux and windows and supports 100s of models (https://github.com/nod-ai/SHARK/tree/main/tank) . Also in the past I have been able to build / test ROCM on newer hardware  from the public sources. 

---

### 评论 #3 — aoolmay (2022-12-15T08:09:21Z)

I know about some half measures, i bought my first RDNA2 card anticipating support, i waited more than half a year gimping around on PlaidML, OpenCL implementation of Keras , eventually ended up on 4 RDNA2 workstations.

Can't afford to wait this time around, got commercial work cut out for next months and i already have to rent RTXs from the cloud. At this point it's whatever gets the job done faster.

---

### 评论 #4 — SharoonSaxena (2022-12-16T14:23:21Z)

Well, I am not buying a $1000 GPU for gaming, strictly for Science purposes. I guess half-measures are not going to cut it.

---
