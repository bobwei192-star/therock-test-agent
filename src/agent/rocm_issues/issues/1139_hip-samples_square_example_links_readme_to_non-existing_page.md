# hip-samples square example links readme to non-existing page

> **Issue #1139**
> **状态**: closed
> **创建时间**: 2020-06-06T19:21:24Z
> **更新时间**: 2021-08-04T09:48:45Z
> **关闭时间**: 2021-08-04T09:48:45Z
> **作者**: baryluk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1139

## 描述

`/opt/rocm-3.5.0/hip/samples/0_Intro/square/README.md`

links to http://gpuopen.com/hip-to-be-squared-an-introductory-hip-tutorial

which doesn't exist.

So this example is impossible to use or understand really.

This is the first example and sample, and already can't progress further, because it doesn't work.

Please include all the relevant information in the README.md without external dependencies, or in the source code comments.



---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2021-01-12T09:24:29Z)

Thanks @baryluk for reaching us out.
I am able to reproduce this issue.
I will work with HIP developer and update the status asap.
Thank you.

---

### 评论 #2 — ROCmSupport (2021-02-15T08:48:58Z)

Latest update on this:
Changes are ready and will be pushed very soon.
Thank you.

---

### 评论 #3 — ROCmSupport (2021-06-03T08:40:14Z)

Latest update:
Changes will be part of ROCm 4.3.
Thank you.

---

### 评论 #4 — ROCmSupport (2021-08-04T09:48:45Z)

Verified this issue with ROCm 4.3(4.3-52) and issue is no more observed.


---
