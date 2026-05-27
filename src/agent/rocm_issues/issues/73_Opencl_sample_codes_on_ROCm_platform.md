# Opencl sample codes on ROCm platform ? 

> **Issue #73**
> **状态**: closed
> **创建时间**: 2017-01-10T11:47:31Z
> **更新时间**: 2017-02-22T15:54:06Z
> **关闭时间**: 2017-02-22T15:54:06Z
> **作者**: VishwasRao17
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/73

## 描述

Do we have a sample codes in openCL language on ROCm platform. 
Any other sample codes which will offload job to gpu ? in any language HIP / OpenCL / HCC . 
This will help me in understanding the flow of instructions ? 

---

## 评论 (4 条)

### 评论 #1 — jedwards-AMD (2017-01-10T15:48:56Z)

There are samples for HIP in the /opt/rocm/hip/samples directory. For OpenCL, you should be able to use many of the available OpenCL applications. There are some features of OpenCL not supported on the ROCm OpenCL runtime (the biggest being images), but basic OpenCL functionality should be the same.

---

### 评论 #2 — VishwasRao17 (2017-01-11T03:33:15Z)

@jedwards-AMD Thank you. I will go through the HCC samples available over the same directory. It says the source codes of runtime apis are available. This might help me. Also a quick question, does the wrapper src code which binds opencl apis to rocm are available ? 

---

### 评论 #3 — nevion (2017-01-12T23:14:27Z)

@VishwasRao17 pet-peev - please say source code, not and preferably never use codes; at the very least for near universal consistency with the web.

 I can't understand what your question is but you don't have to do anything special to get OpenCL to run on ROCm provided you're loading their libOpenCL.so.   Go read up on an existing OpenCL application such as clinfo (there are many variants available on github) rather than file an issue here.  This question does not seem to be ROCm specific...

---

### 评论 #4 — jedwards-AMD (2017-01-12T23:28:36Z)

The OpenCL on ROCm source code is not yet available. I assume this is what you meant with the term "wrapper src code".

---
