# Sharing of texture/buffer data between OpenGL--HSA ??

> **Issue #1175**
> **状态**: closed
> **创建时间**: 2020-07-08T13:37:52Z
> **更新时间**: 2021-01-28T10:49:42Z
> **关闭时间**: 2021-01-28T10:49:42Z
> **作者**: wsphillips
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/1175

## 标签

- **Question** (颜色: #cc317c)

## 描述

Is there (even low level) functionality to share memory objects between the HSA runtime and OpenGL? e.g. a way to convert a pointer (to an HSA-allocated buffer) into an OpenGL texture?

In other words, if it doesn't _already_ exist, where could one poke around to experiment/build something equivalent to OpenCL's `clCreateFromGLTexture` ?? 

---

## 评论 (2 条)

### 评论 #1 — ROCmSupport (2020-12-17T04:01:38Z)

Hi @wsphillips 
Thanks for reaching out.
I will check with HSA team and get an update on this.
Thank you.

---

### 评论 #2 — skeelyamd (2021-01-12T06:04:40Z)

Hi @wsphillips,

OpenCL's GL interop is actually mostly built on top of ROCr and Mesa interfaces.  Mesa exposes a set of interfaces to export the low level buffer object which backs one of it's resources along with that resource's metadata.  ROCr then imports this resource via some interop map/unmap APIs.  The bit that is OCL specific is in manipulating the imported resources metadata to select specific components of the imported resource.  For instance since OCL doesn't directly support cube maps OCL can't properly import a full cube map (there's no representation of this object in an OCL kernel for instance).  Instead it contains definitions that allow the user to select out a face of the cube map and import that face as a 2D texture, something it can handle.

Currently HSA lacks the definitions needed to perform that kind of component selection for complex GL/EGL objects.

Some possibly helpful pointer:
https://github.com/mesa3d/mesa/blob/8427e5606721019b0885af5b986a875e7d562643/include/GL/mesa
_glinterop.h
https://github.com/RadeonOpenCompute/ROCR-Runtime/blob/master/src/inc/hsa_ext_amd.h#L1409-L1514

---
