# Question: Does TensorFlow ROCm support an OpenCL backend (miopen-opencl)?

> **Issue #703**
> **状态**: closed
> **创建时间**: 2019-02-11T21:19:03Z
> **更新时间**: 2019-02-15T16:47:02Z
> **关闭时间**: 2019-02-15T16:47:02Z
> **作者**: bpsegal
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/703

## 标签

- **Question** (颜色: #cc317c)

## 描述

First, apologies if I'm posting these questions to the incorrect place.  Let me know if there's a forum where I should post instead.

My understanding is that the TensorFlow ROCm version requires both miopen-hip and rocm-opencl rocm-opencl-dev, along with miopengemm.  My confusion is that miopen-hip doesn't exploit OpenCL, right? But if that's the case, why do we need to install rocm-opencl?  To exploit particular toolchains as part of the OpenCL packaging?  Are there particular tensorflow routines that use OpenCL directly?  And conversely, since rocm-opencl already is an installation requirement, is miopen-opencl functionally supported with TensorFlow ROCm, rather than miopen-hip?  If miopen is meant to provide an abstraction layer for deep learning, from a functional (and not performance) perspective, why does the backend matter?  Is there more support for hip-ified kernels for tensorflow at this point, and that's the main reason?

Thanks for any clarification you might be able to provide.

---

## 评论 (3 条)

### 评论 #1 — jlgreathouse (2019-02-12T03:16:30Z)

This is probably better asked in the [ROCm TensorFlow repository](https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues) or [MIOpen repository](https://github.com/ROCmSoftwarePlatform/MIOpen/issues). They're the experts at the internals of our TF and MIOpen implementations, and not all of them watch this general repository closely.

Here is my understanding: Both `miopen-hip` and `miopen-opencl` make use of kernels written in OpenCL and compiled by our ROCm OpenCL compiler. This is to write high-performance device-side functions. You can see this in MIOpenGEMM, which creates kernels from OpenCL C code. However, the major difference between `miopen-hip` and `miopen-opencl` is the host-side functions that are used to interface the library with higher-level runtimes.

So there are particular TensorFlow routines that, when they are launched to the GPU, use kernels that are compiled from OpenCL C. However, that does not mean that our TensorFlow implementation uses *host-side* OpenCL code. Instead, `miopen-hip` uses HIP host-side APIs so that it is easier to integrate it into runtimes (like TensorFlow) that use CUDA APIs. Because the version of TensorFlow that we have running on ROCm does not use OpenCL host side APIs, that means no, `miopen-opencl` functionality is not supported within TF.

---

### 评论 #2 — bpsegal (2019-02-12T18:11:52Z)

Thanks @jlgreathouse .  Your comments cleared up most of my confusion.  I thought that miopen, itself, provided the *host-side* abstraction, but now I see that it provides interfaces for either HIP or OpenCL.  Since TF was originally written with CUDA APIs, a natural direction was to use (host-side) HIP as its overall runtime, tied into MIOpen, which itself, is capable of using kernels built from OpenCL C or GCN assembly kernels.  Hopefully, I got most of that right.  I'll continue to dig into the code.  Thanks again.

---

### 评论 #3 — daniellowell (2019-02-15T16:42:19Z)

@bpsegal MIOpen supports both OpenCL backend and HIP backend, but not at the same time. For TF specifically the HIP backend is only supported. In MIOpen you will see kernels written in OpenCL, but what is really going on the HIP backend side is that the OpenCL kernels are compiled into code objects when are then pulled back into MIOpen and executed using the HIP runtime.

---
