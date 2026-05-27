# Texture objects?

> **Issue #81**
> **状态**: closed
> **创建时间**: 2017-01-21T15:00:42Z
> **更新时间**: 2017-02-22T19:12:21Z
> **关闭时间**: 2017-02-22T19:12:21Z
> **作者**: szellmann
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/81

## 描述

Hi, I'd like to ask if support for texture objects like those introduced with CUDA 6.5 is planned - dedicated access to the HW linear texture filtering routines, and variable texture object count accessible from within kernels. I could findno such thing in the docs, is this somewhere on the roadmap?

---

## 评论 (10 条)

### 评论 #1 — boxerab (2017-01-23T14:33:12Z)

I believe these are known as images in opencl land. Images are not supported yet.

---

### 评论 #2 — jedwards-AMD (2017-02-22T17:26:55Z)

Image support is being planned for the OpenCL LC implementation. Are you referring to OpenCL image support or support in another programming model?

---

### 评论 #3 — boxerab (2017-02-22T17:54:17Z)

Thanks. What is "OpenCL LC", may I ask ?

---

### 评论 #4 — jedwards-AMD (2017-02-22T18:00:48Z)

OpenCL LC is AMDs OpenCL implementation that uses what is known as the lightning compiler. It is the only implementation of OpenCL that is supported on ROCm.

---

### 评论 #5 — boxerab (2017-02-22T18:02:12Z)

Cool. Where can I learn more about this compiler?  Can you comment on stability and performance?

---

### 评论 #6 — jedwards-AMD (2017-02-22T18:06:49Z)

The compiler is actually distributed as HCC. The OpenCL implementation uses parts of HCC to enable kernel compilation.

---

### 评论 #7 — jedwards-AMD (2017-02-22T18:07:56Z)

The LC compiler is actually a part of HCC. Please look at this link for details: https://github.com/RadeonOpenCompute/hcc

---

### 评论 #8 — boxerab (2017-02-22T18:09:00Z)

Great. Thanks for the info.  I have an application that makes heavy use of opencl images, so really looking forward for this to arrive for ROCm.

---

### 评论 #9 — szellmann (2017-02-22T18:35:01Z)

Ah sorry, I would maybe better have placed this in the hcc issue tracker. I'm interested in using images with hcc.

CUDA originally had support for textures (their analog to images in OCL), and they were directly related to texture units, i.e. you had to have a static amount of textures. They relaxed this later (I think wirh CUDA 6)  so that you could use texture objects and wouldn't need to (e.g.) pack a dynamic number of images into an atlas. So texture objects (or whatever one would call them in the ROCm world) rather than mere images are what I'm interested in.

> On Feb 22, 2017, at 6:26 PM, James Edwards <notifications@github.com> wrote:
> 
> Image support is being planned for the OpenCL LC implementation. Are you referring to OpenCL image support or support in another programming model?
> 
> —
> You are receiving this because you authored the thread.
> Reply to this email directly, view it on GitHub, or mute the thread.
> 


---

### 评论 #10 — scchan (2017-02-22T19:12:21Z)

We are planning to provide image support in a future version of hcc.  Please open a new issue under hcc if you are interested in tracking it.  Thanks,

---
