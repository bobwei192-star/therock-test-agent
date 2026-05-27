# Question: how is SQ_INSTS_VALU incremented?

> **Issue #1723**
> **状态**: closed
> **创建时间**: 2022-04-11T22:05:57Z
> **更新时间**: 2024-05-09T15:59:46Z
> **关闭时间**: 2024-05-09T15:59:46Z
> **作者**: vasslavich
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1723

## 描述

Hello, colleagues!
I noticed that SQ_INSTS_VALU is incremented once per warp by an instruction. It's right?
Then to count the total number of executed vector instructions on the grid, I have to multiply this value by the size of a warp?


---

## 评论 (2 条)

### 评论 #1 — ppanchad-amd (2024-05-08T15:02:43Z)

@vasslavich Apologies for the lack of response.  Do you still need assistance? Thanks!

---

### 评论 #2 — vasslavich (2024-05-09T15:59:46Z)

@ppanchad-amd , hello! We've decided to reject this task. Thank you any way. 

---
