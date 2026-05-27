# In the future,the platform will run on Windows?

> **Issue #60**
> **状态**: closed
> **创建时间**: 2016-12-23T03:20:22Z
> **更新时间**: 2017-01-04T14:06:09Z
> **关闭时间**: 2017-01-03T22:39:02Z
> **作者**: GhostChild
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/60

## 描述

I use AMD GPU, And have interesting with deep learning.
more and more deep learning project run like caffe and other platform.
but it's not friendly for AMD GPU.
more people use windows system. 
I also want more people can use my program.


---

## 评论 (2 条)

### 评论 #1 — jedwards-AMD (2017-01-03T22:39:02Z)

Currently there are no plans to support of ROCm on Windows platforms.

---

### 评论 #2 — gstoner (2017-01-04T14:06:09Z)

@GhostChild We will bring the ROCm tools to Windows,  HCC, HIP, you already have OpenCL.  So you will be able to support the same program on both systems.  We have lot request for this, but right know we focused on getting performant, stable tools on a single platform initially, but have been working on a new foundation for GPU computing on Windows as well with make it easier to support these tools and other tools in the future.  

---
