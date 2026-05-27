# Wavelet calculation support in ROCm

> **Issue #1520**
> **状态**: closed
> **创建时间**: 2021-07-12T10:05:31Z
> **更新时间**: 2021-07-29T15:23:38Z
> **关闭时间**: 2021-07-29T15:23:38Z
> **作者**: sampie
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1520

## 描述

I am wondering if ROCm is a good platform for doing scientific calculations, particularly for wavelet calculations. Does ROCm have a math library for calculating Mexican hat wavelet transforms? I could not find good documentation answering this question. 

---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2021-07-13T03:40:43Z)

Thanks @sampie for reaching out.
I will check this for you and get back asap.
Thank you.

---

### 评论 #2 — malcolmroberts (2021-07-29T15:12:37Z)

Hi, @sampie.  There isn't an official ROCm package for discrete wavelet transform.  For running on AMD GPUs, you can either try an OpenCL DWT, or try using the hipify tool on a CUDA-based DWT library.  This would all be third-party, so you'd have to reach out to the developers of those libraries for support.

---
