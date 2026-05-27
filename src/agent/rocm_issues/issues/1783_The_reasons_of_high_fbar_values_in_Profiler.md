# The reasons of high fbar values in Profiler

> **Issue #1783**
> **状态**: closed
> **创建时间**: 2022-08-09T06:56:25Z
> **更新时间**: 2024-05-09T15:53:36Z
> **关闭时间**: 2024-05-09T15:53:35Z
> **作者**: vasslavich
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1783

## 描述

Hello, dear colleagues!
I have two kernels which implement the same algorithm, but the first kernel does its work in the LDS, and the second kernel distributes the data between the LDS and registers in half. The performance of the second kernel is ~2.5 times low as the first kernel. I've found that the **fbar** counter of the second kernel is more _higher_. 
Please, if anybody knows, how can I understand _the reasons_ for the higher value of **fbar**?
Thanks!

---

## 评论 (2 条)

### 评论 #1 — ppanchad-amd (2024-05-09T15:24:42Z)

@vasslavich Sorry for the lack of response.  Do you still need assistance with this ticket? Thanks

---

### 评论 #2 — vasslavich (2024-05-09T15:53:35Z)


@ppanchad-amd, hi! No, thank you, it has already dismissed. 


---
