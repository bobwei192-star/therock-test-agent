# Latest ROCm 4.5, GFX8 support?

> **Issue #1695**
> **状态**: closed
> **创建时间**: 2022-03-02T11:48:52Z
> **更新时间**: 2022-03-04T02:54:06Z
> **关闭时间**: 2022-03-02T12:59:52Z
> **作者**: ramin-raeisi
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1695

## 描述

To whom it may concern,

Is there any GFX8 GPU is supported in ROCm 4.5? Like AMD Radeon RX 580 or any other one?

Actually, I want to have the minimum cost possible for my POC.

Thank you in advance

---

## 评论 (6 条)

### 评论 #1 — ROCmSupport (2022-03-02T12:59:52Z)

Hi @ramin-raeisi 
Thanks for reaching out.
Currently ROCm does not support gfx8 anymore. Hope this helps.
Thank you.

---

### 评论 #2 — ramin-raeisi (2022-03-02T13:13:40Z)

Thanks for getting back to me, even just for HIP?

---

### 评论 #3 — Moading (2022-03-02T14:21:23Z)

@ramin-raeisi I'm interested in this as well. Maybe you should ask "what is the latest known working ROCm for gfx8"
I'm running my gfx803 (Radeon Pro Duo) with ROCm 3.3 under ubuntu 18.4.4 LTS kernel 4.15.0-96, OpenCL works.
If others would post their combinations of ROCm, OS, kernel here, that might answer your question.

---

### 评论 #4 — xuhuisheng (2022-03-02T23:12:28Z)

If you want to run larest rocm on gfx803, you need do some patch. https://github.com/xuhuisheng/rocm-build/tree/master/gfx803

---

### 评论 #5 — Moading (2022-03-03T08:24:17Z)

@xuhuisheng thanks for your work to get gfx803 working again. I have seen your posts before but I never tried to reproduce.
Have you done any verification with hip examples? I am asking because the fact that the GPU shows up in clinfo or rocminfo does not mean it produces correct results.
Could you post the os and kernel you are using?
Thanks again!

@ROCmSupport could you please re-open this issue because the discussion is still ongoing

---

### 评论 #6 — xuhuisheng (2022-03-04T00:36:39Z)

@Moading 
I uploaded some codes on gfx803, including hip, rocblas, miopen. <https://github.com/xuhuisheng/rocm-build/tree/master/check>
And I can run small samples with pytorch and tensorflow on gfx803. basicly, just mnist.

Date: 2022-02-24

|software | description                          |
|------------| -------------------------------------|
|ROCm   | 5.0.0                                    |
|OS         | Ubuntu-20.04.3, kernel-5.11|
|Python   | 3.8.10                                  |
|Tensorflow-rocm | 2.8.0                       |



And cgmb said there are some testcases failed, but I had no enough time to dig recently.

---
