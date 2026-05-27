# In-memory compilation roadmap?

> **Issue #469**
> **状态**: closed
> **创建时间**: 2018-07-26T08:11:04Z
> **更新时间**: 2023-12-08T18:17:30Z
> **关闭时间**: 2023-12-08T18:17:18Z
> **作者**: blueberry
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/469

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

I'm currently using the old catalyst and waiting for a few OpenCL things to land in the new drivers.

One of those is in-memory compilation. My programs simply have to generate and compile kernels during the runtime so I don't have a way around it.

Is there any rough estimate on when I could expect any of the new OpenCL implementations (I admit that I am confused by different amd libraries by now: ROCm, AMDGPU(PRO) etc. when it comes to OpenCL) to have support for in-memory compilation on newer hardware (VEGA 64 in my case)?

For the time being, I do net even insist on open-source. Any way to use this functionality would be acceptable.

---

## 评论 (9 条)

### 评论 #1 — preda (2018-07-26T11:20:05Z)

Unless I misunderstand your question, dynamic (runtime) compilation of OpenCL kernels by the driver is, has always, been supported by both amdgpu-pro and ROCm.

Now that I think of this, this is required by OpenCL.

---

### 评论 #2 — blueberry (2018-07-26T11:47:39Z)

Thank you. I was confused by various statements on different RadeonOpenCompute pages.

Now that you confirmed, I found that https://rocm.github.io/QuickStartOCL.html states that it *is* available, but previously most places related to this project mentioned that it is *not* available.
For example, https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime explicitly states that

> Supports offline ahead of time compilation today; during the Beta phase we will add in-process/in-memory compilation.

Maybe there are different outdated informations floating on dispersed wiki pages related to this project. Maybe it would be a good idea to update them, or at least to mark them obsolete.

---

### 评论 #3 — b-sumner (2018-07-26T14:40:03Z)

The OpenCL runtime for ROCm makes use of the LLVM compiler libraries.  LLVM and certain tools were first updated to allow the OpenCL runtime to perform on-line compilation without forking.  However, the next step, updating LLVM and certain tools,. to run entirely in memory instead of using file I/O, has not yet been carried out.   It's feature under development for a future date when the ROCm OpenCL runtime will have fully in-memory compilation. 

---

### 评论 #4 — ROCmSupport (2021-01-07T06:58:29Z)

Hi @b-sumner 
Do we have any updates on this. Please move this to next step or towards closure.
Thank you.

---

### 评论 #5 — b-sumner (2021-01-07T15:48:27Z)

We are working on this.  It is a large project that requires buy-in by the LLVM community.  There is no current ETA.

---

### 评论 #6 — yxsamliu (2021-02-09T15:43:45Z)

If you just need to generate and compile kernels during the runtime, normal OpenCL compilation is sufficient. You only need in-memory compilation if /tmp is not writable, which is a rare situation for Linux.

Can you clarify? Thanks.

---

### 评论 #7 — tasso (2023-12-08T17:07:10Z)

Is this still an issue?  If not; can we please close it?

---

### 评论 #8 — blueberry (2023-12-08T18:12:10Z)

I don't know. I had to switch to Nvidia GPUs on newer machines due to better (OK, arugably) software support, so I can't try it any more.

---

### 评论 #9 — tasso (2023-12-08T18:17:29Z)

Sorry to hear this.  I hope you consider us again in the future.  I will close the issue

---
