# For an unknown Proprietary application - OpenCL - ROCm LLVM Compiler is spilling registers to  scratch registers where the PAL drivers did not with large performance hit.

> **Issue #553**
> **状态**: closed
> **创建时间**: 2018-09-21T09:56:10Z
> **更新时间**: 2018-09-21T13:14:59Z
> **关闭时间**: 2018-09-21T13:14:58Z
> **作者**: liwoog
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/553

## 描述

The PAL drivers used 114 VGPRs. 82 + 2 x 16 (two arrays of 16 floats).

The ROCm 1.9 driver uses scratch space instead and is ~60% slower.
                enable_sgpr_flat_scratch_init = 1
                workitem_vgpr_count = 82
 


---

## 评论 (9 条)

### 评论 #1 — gstoner (2018-09-21T12:05:17Z)

On what workload, I have zero idea where this is happing if we do not know the application you talking about.  Also, we need to understand which Driver version you are using with AMDGPUpro and ROCm. 

We need to quantify the performance issue. 

---

### 评论 #2 — liwoog (2018-09-21T12:08:41Z)

ROCm 1.9 vs AMDGPU 18.30

---

### 评论 #3 — liwoog (2018-09-21T12:09:15Z)

Proprietary app

---

### 评论 #4 — gstoner (2018-09-21T12:14:04Z)

Are you doing aggressive inlining is so that would be why you see scratch memory being used, you are spilling your registers.  It is hard to address the issue when there is Zero information about the application.   

If we can not get more info I will have to close this issue 

---

### 评论 #5 — gstoner (2018-09-21T12:15:18Z)

I  am saying we need  reproducible to help sold you problem 

---

### 评论 #6 — liwoog (2018-09-21T12:39:07Z)

I understand the  difficulty. There is no inlining, I cannot post the code here. Please close the issue.

---

### 评论 #7 — liwoog (2018-09-21T12:46:54Z)

Still begs the question why scratch space is used when enough VGPRs are available.

---

### 评论 #8 — liwoog (2018-09-21T12:48:55Z)

workitem_private_segment_byte_size = 136

---

### 评论 #9 — gstoner (2018-09-21T13:14:58Z)

We need to work with you directly and profile the application,  you can just contact me at my email address at amd.  greg "."  stoner 

---
