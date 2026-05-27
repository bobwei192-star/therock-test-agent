# [Question] hipDeviceProp' major/minor for AMD GPUs

> **Issue #1907**
> **状态**: closed
> **创建时间**: 2023-02-13T20:07:39Z
> **更新时间**: 2024-03-31T14:09:40Z
> **关闭时间**: 2024-03-31T14:09:40Z
> **作者**: HardMax71
> **标签**: Documentation
> **URL**: https://github.com/ROCm/ROCm/issues/1907

## 标签

- **Documentation** (颜色: #5319e7)

## 描述

Hi, 

I have 2 GPUs: GTX 1650 (Nvidia, Turing arch) and RX 5500 XT (AMD, gfx1012) + rocm 4.5.0.

If i start the program with Nvidia GPU and populate hipDeviceProp_t, i get major & minor compute capability = 7 and 5 accordingly (in total -> 7.5), and that's completely [fine](https://forums.developer.nvidia.com/t/cuda-enabled-geforce-1650/81010#:~:text=The%20GTX%201650%20is%20based,able%20to%20run%20those%20frameworks.).

if start the same program with Radeon, i get 10 & 1 -> 10.1. 

What do the values of major/minor attributes in hipDeviceProp_t mean for AMD GPUs? 

`RX 5500 XT has compute capability of about 10.1`?


---

## 评论 (2 条)

### 评论 #1 — nartmada (2024-03-17T15:14:43Z)

Hi @HardMax71, apologies for not following up.  Is this ticket still open?  Thanks.

---

### 评论 #2 — nartmada (2024-03-31T14:09:40Z)

Closing the ticket.  @HardMax71, please re-open if your query still not fully answered.  Thanks.

---
