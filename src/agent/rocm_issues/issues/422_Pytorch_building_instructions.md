# Pytorch building instructions?

> **Issue #422**
> **状态**: closed
> **创建时间**: 2018-05-17T19:18:11Z
> **更新时间**: 2018-07-27T05:26:46Z
> **关闭时间**: 2018-06-03T14:12:06Z
> **作者**: victor-felicitas
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/422

## 描述

Dear ROCm team, congrats with successful Pytorch integration!
I am eager to try it with my AMD gpu, but could not find any instructions.

In particular, default instruction assumes
_# Add LAPACK support for the GPU
conda install -c pytorch magma-cuda80 # or magma-cuda90 if CUDA 9_

What should I do to install Pytorch with AMD gpu support?

---

## 评论 (2 条)

### 评论 #1 — gstoner (2018-06-03T14:12:06Z)

Facebook will post the instruction on their site how to do install   Currently you have to build from Source. 

---

### 评论 #2 — syoyo (2018-07-27T05:26:46Z)

FYI, there is emerging PR for the documentation of caffe2 ROCm build > https://github.com/ROCmSoftwarePlatform/pytorch/pull/71

---
