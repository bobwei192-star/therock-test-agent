# Freezing during OpenCL kernel compilation (ROCm 1.7)

> **Issue #352**
> **状态**: closed
> **创建时间**: 2018-03-03T16:13:18Z
> **更新时间**: 2018-06-06T12:34:26Z
> **关闭时间**: 2018-06-06T12:34:26Z
> **作者**: ekondis
> **标签**: Under Investigation, Compiler Functional Bug
> **URL**: https://github.com/ROCm/ROCm/issues/352

## 标签

- **Under Investigation** (颜色: #0052cc)
- **Compiler Functional Bug** (颜色: #d847b6)

## 描述

I'm maintaining a μ-benchmark suite for GPU memories using OpenCL dubbed _gpumembench_. A particular benchmark (_shmembench-ocl_) freezes during compilation when using _int4_ data type. This even happens with ROCm v1.7.1 beta 4. It seems that the problem is triggered by using an unroll directive before the core loop:

```
#pragma unroll 32
for(...)
```

Removing the directive resolves the problem but there has to be a better solution.

The full source code is provided on [gpumembench page on github](https://github.com/ekondis/gpumembench)

---

## 评论 (3 条)

### 评论 #1 — gstoner (2018-03-03T18:02:05Z)

Thank you, we will start looking at this 

greg

---

### 评论 #2 — ghost (2018-03-15T07:03:26Z)

Ran into this I ended up disabling the watchdog in the kernel.


---

### 评论 #3 — gstoner (2018-06-06T12:34:26Z)

Fixed in 1.8 and now part of regression suite 

---
