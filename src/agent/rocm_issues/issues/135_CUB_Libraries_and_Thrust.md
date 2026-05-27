# CUB Libraries and Thrust

> **Issue #135**
> **状态**: closed
> **创建时间**: 2017-06-26T23:32:19Z
> **更新时间**: 2017-07-02T01:33:01Z
> **关闭时间**: 2017-07-01T21:33:39Z
> **作者**: acyeh
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/135

## 描述

I was wondering if there were equivalents for the CUB/Thrust Libraries available for ROCm?

Namely, I'm searching for alternative methods for:

1. cub::DeviceReduce::ArgMax
2. cub::DeviceReduce::ArgMin
3. cub::DeviceReduce::Max
4. cub::DeviceReduce::Sum
5. cub::DeviceRadixSort::SortKeys
6. cub::DeviceScan::InclusiveSum

---

## 评论 (4 条)

### 评论 #1 — nevion (2017-07-01T07:51:18Z)

I don't think they're on the drawing board yet.  Keep pressure on and maybe they'll eventually figure it out.  Libraries like this are required for researchers to be productive.

CUB under the covers is definitely nastier than on the top and would probably be difficult to support upstream, but since it's FOSS... maybe they can work it out.

---

### 评论 #2 — gstoner (2017-07-01T21:33:39Z)

CUB and Thurst Ports are under development. We have seen some nice progress on them.   Remember we young project and we have competing priorities, capped capacity for man/engineering hours.    We are also working on PSTL based libraries for HCC. 

---

### 评论 #3 — nevion (2017-07-01T23:54:55Z)

just FYI - I think CUB is generally more useful than most of thrust/PSTL after a point.  What I've seen is most people tend only use the stl like libraries for any of sort (including key variants), scatter, gather, and reduction.  Not too much else as complicated stuff always finds itself in new kernels for huge relative speedups.  Point being that it's easy to hit diminishing returns after just a few functions in those libraries.

---

### 评论 #4 — gstoner (2017-07-02T01:33:01Z)

We still keep running into Thurst in our Ports so we decided to knock it out.   CUB is more interested we agree. 

---
