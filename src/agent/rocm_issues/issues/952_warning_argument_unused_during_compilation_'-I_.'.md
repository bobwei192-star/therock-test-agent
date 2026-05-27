# warning: argument unused during compilation: '-I .'

> **Issue #952**
> **状态**: closed
> **创建时间**: 2019-11-26T14:07:41Z
> **更新时间**: 2023-12-18T16:10:44Z
> **关闭时间**: 2023-12-18T16:10:44Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/952

## 描述

```
1 warning generated.
2019-11-26 06:06:12 warning: argument unused during compilation: '-I .'
```

This happens with the gpuowl program. ROCm 2.10


---

## 评论 (5 条)

### 评论 #1 — boxerab (2019-11-29T01:55:35Z)

This just means that it is no longer necessary to add the current compile directory as an include directory when compiling opencl kernels to binary format. To fix, simply remove this from the opencl compile settings.

---

### 评论 #2 — preda (2019-12-09T11:37:56Z)

I understand what it means, but I can't simply remove it, because with other OpenCL backends would not work anymore. That's one of the points of OpenCL, being portable to more than just ROCm.

---

### 评论 #3 — boxerab (2020-01-05T18:35:31Z)

What is odd is that if this build parameter is removed, then ROCm will not find include files in the same directory. So, it is needed, and there should not be a warning.

---

### 评论 #4 — nartmada (2023-12-13T21:16:43Z)

Hi @valeriob01, please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #5 — nartmada (2023-12-18T16:10:44Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---
