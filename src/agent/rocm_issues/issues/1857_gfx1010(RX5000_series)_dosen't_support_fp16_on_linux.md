# gfx1010(RX5000 series) dosen't support fp16 on linux

> **Issue #1857**
> **状态**: closed
> **创建时间**: 2022-11-12T17:36:14Z
> **更新时间**: 2024-11-14T18:08:41Z
> **关闭时间**: 2024-11-14T18:08:40Z
> **作者**: AiPs1717
> **标签**: Under Investigation
> **URL**: https://github.com/ROCm/ROCm/issues/1857

## 标签

- **Under Investigation** (颜色: #0052cc)

## 描述

currently using gfx1010.
In the latest version of ROCm, 5.3.2, gfx1010 cannot use fp16 calculations.
An attempt was made to calculate fp16 in the pytorch environment, but it did not work.
Is there a way to force the fp16 calculation in the gfx1010 series?

---

## 评论 (5 条)

### 评论 #1 — zjin-lcf (2023-02-09T13:43:57Z)

Could you run the HIP programs without errors in https://github.com/CHIP-SPV/chip-spv/blob/main/samples/fp16 ?

---

### 评论 #2 — Yougoshatenshi (2023-05-14T06:23:11Z)

> Could you run the HIP programs without errors in https://github.com/CHIP-SPV/chip-spv/blob/main/samples/fp16 ?

Ran all 3 cpp files in hipcc without any errors, but also have the problem that i cant use FP16 in pytorch with ROCm on my 5700XT.
In directml on windows its working fine too, although almost as slow as FP32 in pytorch under linux.

---

### 评论 #3 — abhimeda (2024-01-30T04:04:17Z)

@AiPs1717  Hi, is this resolved on the latest ROCm? If so can we close this ticket?

---

### 评论 #4 — Zakhrov (2024-04-24T09:17:03Z)

> @AiPs1717 Hi, is this resolved on the latest ROCm? If so can we close this ticket?

It has been partially, see [https://github.com/ROCm/ROCm/issues/2527#issuecomment-2074468176](https://github.com/ROCm/ROCm/issues/2527#issuecomment-2074468176)

---

### 评论 #5 — jamesxu2 (2024-11-14T18:08:41Z)

Hi @AiPs1717 , let's consolidate the discussion in the thread @Zakhrov mentioned. 

Also, thank you for your efforts in documenting your process in enabling PyTorch for the community @Zakhrov.

---
