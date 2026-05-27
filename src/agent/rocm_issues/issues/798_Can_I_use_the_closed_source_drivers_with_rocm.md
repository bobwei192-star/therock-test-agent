# Can I use the closed source drivers with rocm?

> **Issue #798**
> **状态**: closed
> **创建时间**: 2019-05-16T13:27:29Z
> **更新时间**: 2023-12-12T21:03:31Z
> **关闭时间**: 2023-12-12T21:03:31Z
> **作者**: EricTheMagician
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/798

## 描述

Hi,

I need opengl rendering for the application that I am developing.
Can I use the closed source drivers from AMD with rocm or do I need to use Mesa?

---

## 评论 (3 条)

### 评论 #1 — kentrussell (2019-05-22T15:23:04Z)

You can always try, but there's no guarantee about compatibility. There are some shared features, and our code is pretty close, but there's no guarantee that it will work. It's always worth a try though.

---

### 评论 #2 — tasso (2023-12-12T20:05:43Z)

Is this still an issue? If not, can we please close it? Thanks!

---

### 评论 #3 — EricTheMagician (2023-12-12T21:03:31Z)

It ended up not really working well, but it was years ago at this point. I haven't tried since.

---
