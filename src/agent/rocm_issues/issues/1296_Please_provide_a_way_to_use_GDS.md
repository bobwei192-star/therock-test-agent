# Please provide a way to use GDS

> **Issue #1296**
> **状态**: closed
> **创建时间**: 2020-11-18T20:09:33Z
> **更新时间**: 2022-12-07T01:00:17Z
> **关闭时间**: 2020-12-01T03:52:34Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1296

## 描述

This is a copy of #308 which has been closed without resolution.

We still need a way to programatically access this capability of the hardware.


---

## 评论 (11 条)

### 评论 #1 — ROCmSupport (2020-11-19T06:18:55Z)

Thanks @preda for reaching out.
Will try to gather more information and update you.

---

### 评论 #2 — Degerz (2020-11-19T09:15:16Z)

Is it possible to use the HIP API with [inline assembly](https://github.com/ROCm-Developer-Tools/HIP/tree/master/samples/2_Cookbook/10_inline_asm) to directly access the GDS ?

---

### 评论 #3 — ROCmSupport (2020-11-19T12:33:39Z)

Hi @preda 
ROCm does not use GDS for anything currently. So there is no way to enable its use.

You can also check [https://github.com/RadeonOpenCompute/ROCT-Thunk-Interface/issues/64](url)

---

### 评论 #4 — FilipVaverka (2020-11-23T17:11:05Z)

I had GDS working under OpenCL in Windows running back with Fiji GPU. I used [CLRX](https://clrx.nativeboinc.org/wiki) to assemble the GCN kernel binary, which could be loaded by OpenCL. I believe, there were two things that had to be done:

- Size of the GDS segment had to be set in ".config" section of the kernel (".gdssize N").
- M0 register has to be setup properly with offset and size of the GDS segment.

OpenCL driver on windows probably doesn't make use of the GDS just like ROCm, but with that setup I could access GDS using "ds_write_b32 X, X gds" etc. So, I would think that inline assembly would work once GDS size is specified beforehand. In ROCm I'm not sure how/where in the stack is [amd_kernel_code_t](https://rocmdocs.amd.com/en/latest/ROCm_Compiler_SDK/ROCm-Codeobj-format.html?highlight=finalizer#amd-kernel-code-object-amd-kernel-code-t) composed so that "gds_segment_byte_size" could be properly set.

---

### 评论 #5 — jlgreathouse (2020-12-01T03:52:34Z)

Hi @preda 

To add a bit more detail to the answer provided by my colleagues that run the @ROCmSupport account: at this time, no language supported by ROCm includes native support for GDS. There are no OpenCL extensions that really encompass what GDS can do, nor are there any such mechanisms in HIP. While you could use inline assembly to access the ISA instructions that would allow you to speak to the GDS (as suggested by @Degerz, and detailed further by @FilipVaverka ), this will only produce a kernel that attempts to access GDS memory and then fails.

Last year, I submitted [kernel patches](https://www.spinics.net/lists/amd-gfx/msg36318.html) to disable access to the GDS unless a process explicitly requests a GDS allocation. So your compute kernel that tries to use GDS instructions will take a memory fault and crash. This was done for security reasons: previously, we had (incorrectly) allowed every user to access the entire GDS. Any processes could surreptitiously communicate with any other, and anyone trying to use GDS ran the risk of some other process corrupting their GDS values.

Now you need to explicitly [allocate memory in the GDS region](https://static.lwn.net/kerneldoc/gpu/amdgpu.html#memory-domains) to use the instructions. This is possible through some mechanisms I don't want to go into for graphics software, but importantly for this conversation: this is not possible for ROCm compute processes. Even if you properly set the `amd_kernel_code_t` information described above, that is the user-level description of the kernel and does not cause anyone to request GDS space from the kernel-mode driver.

We have no KFD ioctl to request GDS allocations in ROCm, nor do we plan to add one at this time. This would require some significant firmware changes to allow GDS to properly work in the ROCm software stack. At this time, we have chosen to put our development resources into other areas that have more direct uses on existing languages and software. Nevertheless, thank you for the request for this. We will keep in mind for the future.

---

### 评论 #6 — jlgreathouse (2020-12-01T04:06:43Z)

Though I closed this after the last response, I will note that there are a few instructions descrigbed in our ISA manual that say "GDS Only" that _are_ supported, but they are not actually "GDS" instructions:
 - DS_GWS_SEMA_RELEASE_ALL
 - DS_GWS_INIT
 - DS_GWS_SEMA_V
 - DS_GWS_SEMA_BR
 - DS_GWS_SEMA_P
 - DS_GWS_BARRIER

These instructions are actually in the "GWS" unit, not the "GDS" unit. As described in the [memory region information for the driver](https://static.lwn.net/kerneldoc/gpu/amdgpu.html#memory-domains), the GWS is hardware to help with synchornization, rather than the more general scratchpad memory available through GDS.

GWS _is_ supported (depending on your hardware version and the firmware avaialble for it). You can allocate GWS entries to a queue using the KFD ioctl `AMDKFD_IOC_ALLOC_QUEUE_GWS`. This will attempt to allocate a requested number of GWS entries to a queue (up to one queue per process). Any kernel in that queue can then cleanly use the GWS. We use this as part of our [Cooperative Groups](https://github.com/ROCm-Developer-Tools/HIP/blob/rocm-3.10.0/include/hip/hcc_detail/hip_runtime_api.h#L3110) implementation -- the GWS instructions can be accessed using `grid_group.sync()` and `multi_grid_group.sync()` functionality, for example.

I just wanted to add this extra few bits of information for the folks that deeply read our ISA manuals. :)

---

### 评论 #7 — preda (2020-12-12T09:52:04Z)

@jlgreathouse thank you for the informative answer!

I understand that an API for GDS access is not in place right now (either in OpenCL or in ROCm). 

OTOH the hardware does offer this useful capability, and it would be in everyone's interest to expose it and make it available for use. (maybe some extension mechanisms are in place in OpenCL that could be used?)

Thank you again for the answer.


---

### 评论 #8 — misos1 (2022-11-25T21:33:19Z)

@jlgreathouse Any update on this?

> Now you need to explicitly [allocate memory in the GDS region](https://static.lwn.net/kerneldoc/gpu/amdgpu.html#memory-domains) to use the instructions. This is possible through some mechanisms I don't want to go into for graphics software

Could I just send the PM4 packet ALLOC_GDS to allocate it?


---

### 评论 #9 — jlgreathouse (2022-12-06T05:12:42Z)

Hi @misos1 -- No, we currently have no updated plans to support GDS in ROCm. As far as I know, AMD GPUs have not supported the ALLOC_GDS PM4 packet since the gfx6/"Southern Islands" generation. This would not work for enabling GDS on ROCm-enabled GPUs.

---

### 评论 #10 — misos1 (2022-12-06T12:42:03Z)

@jlgreathouse
> As far as I know, AMD GPUs have not supported the ALLOC_GDS PM4 packet since the gfx6/"Southern Islands" generation. This would not work for enabling GDS on ROCm-enabled GPUs.

Nice to know. It just hangs the GPU at 100% usage and needs `amdgpu_gpu_recover`. You mentioned that it is possible through some mechanisms for graphics software (so I thought it could be ALLOC_GDS). Can you provide some more clues, please?


---

### 评论 #11 — jlgreathouse (2022-12-07T01:00:17Z)

I'm sorry to say that I don't know. I'm ignorant about our graphics-specific APIs. You may want to ask on the amd-gfx mailing list on freedesktop.

---
