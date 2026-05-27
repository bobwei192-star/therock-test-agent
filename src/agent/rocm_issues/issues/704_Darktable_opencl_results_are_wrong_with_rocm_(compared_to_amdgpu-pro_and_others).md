# Darktable opencl results are wrong with rocm (compared to amdgpu-pro and others)

> **Issue #704**
> **状态**: closed
> **创建时间**: 2019-02-12T22:15:17Z
> **更新时间**: 2023-12-11T23:57:54Z
> **关闭时间**: 2023-12-11T23:03:00Z
> **作者**: RvRijsselt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/704

## 描述

The Local Contrast module in Darktable uses an OpenCL kernel for applying a local laplacian filter. As far as I know the OpenCL version always resulted in the same output as a cpu based algorithm. This is also the case with the amdgpu-pro drivers which gives very nice results. With Rocm however the results are, to put it mildly, very ugly.

[Bug 12423 @ Darktable](https://redmine.darktable.org/issues/12423)

So far we have localized the issue to somewhere in the [laplacian_assemble kernel](https://github.com/darktable-org/darktable/blob/6ed9ce3cfbd4089c70d14b820f2afc4a431d10ea/data/kernels/locallaplacian.cl#L159). 
Note that this kernel is run a number of times with different sizes of the same image and the results are merged into one final output. This means that any error will quickly propagate to a big artifact on the end result. With rocm the results already look different from amdpro on the smallest image scale (8x6 pixels). This was tested by dumping all the inputs and outputs and comparing the results from both opencl drivers. 

The compiler option used in Darktable is -cl-fast-relaxed-math. Removing it has no effect. I have tested also a couple of different settings but no changes in the results: -cl-denorms-are-zero -cl-no-signed-zeros. 

I have run out of ideas on how to check why the results are different. It looks more like an issue in the compiled binary than in the kernel itself.

Package: rocm-libs version: 2.1.96
Package: rocm-dkms version: 2.1.96
Package: rocm-opencl version: 1.2.0-2019020110

The issue has been reported also with different gpus: AMD RX-560, RX-570, Vega 56.

---

## 评论 (6 条)

### 评论 #1 — arigit (2019-03-14T22:21:26Z)

+1 affected by this issue.

The current rocm-opencl ubuntu 18.10 package (as of 20190314) is impacted by this issue.
Using opencl from amdgpu with the same kernel (cl code) produces correct results, consistently. When using rocm-opencl, there is some evident loss of precision/saturation/banding.

Also the same .cl code used in nvidia opencl works fine. The issue only happens with rocm-opencl. 




---

### 评论 #2 — arigit (2019-12-16T18:37:35Z)

@RvRijsselt if you get a chance, can you look into the discussion at https://github.com/darktable-org/darktable/issues/3756
Aurelien proposed testing a locallaplacian patch, but I'm having problems getting darktable to build in my environment. If you could confirm there whether the patch works or not that would help

---

### 评论 #3 — arigit (2020-01-27T18:35:30Z)

@RvRijsselt hi again - when you get a chance would you be able to take a look at the following discussion:

https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/issues/103

One of the ROCM devs is asking for specific tests with the problematic ocl kernel that you may have done already during your extensive tests and analysis. Thanks again!

---

### 评论 #4 — tasso (2023-12-08T18:19:47Z)

Have you verified the discussion link provided above?  Is this still an issue?  If not; can we please close the issue?  Thanks!

---

### 评论 #5 — RvRijsselt (2023-12-11T23:03:00Z)

I could not reproduce the issue with a test project and:
  Device: gfx900:xnack-
  Hardware version: OpenCL 2.0
  Software version: 3513.0 (HSA1.1,LC)
The issue can be closed.

---

### 评论 #6 — tasso (2023-12-11T23:57:52Z)

Thank You! 

---
