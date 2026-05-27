# Impact of OpenCL constant vs. global mem space on code generation.

> **Issue #203**
> **状态**: closed
> **创建时间**: 2017-09-12T12:36:46Z
> **更新时间**: 2018-05-24T04:28:22Z
> **关闭时间**: 2018-05-24T04:28:22Z
> **作者**: preda
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/203

## 标签

- **Question** (颜色: #cc317c)

## 描述

This is a request for information, not a bug.

Using OpenCL with AMDGPU-pro 17.30 with RX Vega 64 on Linux (thus, with the ROCm compiler),
I see that the compiled code has different performance and different VGPR usage depending on a kernel argument being "constant" or "const global" pointer.

Maybe somebody could explain the reason for the difference, and what exactly is the difference.

(from my POV, if I only read from a buffer in the kernel I can mark it as either constant or global at my choice. Why wouldn't the compiler make the "better" choice instead of my trial-and-error? What is the impact on the compiler of marking the buffer constant. Thanks!)

---

## 评论 (2 条)

### 评论 #1 — jgoldsAMD (2017-09-12T21:51:17Z)

The difference is aliasing, and that ought to be it. Example:
_kernel void foo(constant float* in, global float* out) { }_
Here, _in_ and _out_ cannot alias because they are in different memory spaces (constant vs. global). Thus, the compiler may optimize more aggressively, particularly with respect to _in_.
_kernel void foo(global const float* in, global float* out) { }_
Here, _in_ and _out_ may alias because the "restrict" keyword is not used. Thus, the compiler may be pessimistic.
_kernel void foo(global const float* restrict in, global float* restrict out) { }_
Here, _in_ and _out_ may not alias thus the compiler can be more aggressive with optimization, particularly with respect to _in_.

The constant address space can be limited: We recently raised the constant buffer limit on newer GPU devices to match the global buffer limit, but some devices have a much smaller limit on constant buffers (64KB being the minimum the spec allows for non-embedded platforms). However, using "global const T* restrict ptrname" ought to give the same performance as "constant T* ptrname" without size restrictions (if you are using an older driver release that does not have the increased constant buffer size).

Also note that using "global const T* restrict ptrname" will also result in very efficient code if the addresses are uniform across a wavefront/workgroup: The compiler will be able to leverage the constant cache and issue a single fetch (or group of fetches if a large data structure) for a whole wavefront at a time.

These comments only apply to AMD's newer GPU devices, other devices may have other restrictions. Using clinfo (provided in the AMD APP SDK) can show you the maximum constant buffer size or you can query the device directly in your application.

---

### 评论 #2 — preda (2017-09-13T08:48:46Z)

Thank you for the thorough answer! (could be turned into a useful blog post IMO)


---
