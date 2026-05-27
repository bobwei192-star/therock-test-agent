# Vega ISA Document: Poor documentation of ds_swizzle_b32

> **Issue #685**
> **状态**: closed
> **创建时间**: 2019-01-23T19:17:06Z
> **更新时间**: 2019-12-13T06:56:04Z
> **关闭时间**: 2019-12-12T21:08:02Z
> **作者**: dragontamer
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/685

## 描述

I don't know where to report documentation issues. But hopefully someone here knows where to forward this issue?

On the 28-July-2017 Vega ISA guide (which exists at https://developer.amd.com/wp-content/resources/Vega_Shader_ISA_28July2017.pdf today), there's virtually no documentation on the ds_swizzle_b32 instruction. Page 161:

```
RETURN_DATA = swizzle(vgpr_data, offset1:offset0).
Dword swizzle, no data is written to LDS memory.
```

Fortunately, the 2016 GCN3 ISA Guide has good documentation for ds_swizzle_b32. Hopefully, the issue can be corrected before the next ISA document is released. Ideally, the Vega ISA guide could be updated as well.

---

## 评论 (6 条)

### 评论 #1 — preda (2019-01-24T11:00:32Z)

CLRX has some great GCN documentation, see e.g.
https://github.com/CLRX/CLRX-mirror/wiki/GcnInstrsDs#ds_swizzle_b32

Some information from there, such as instruction timing information, would be a valuable addition to AMD docs.

---

### 评论 #2 — phani544 (2019-01-31T17:15:44Z)

see if this helps https://gpuopen.com/amd-gcn-assembly-cross-lane-operations/ 

---

### 评论 #3 — dragontamer (2019-01-31T18:56:07Z)

> see if this helps https://gpuopen.com/amd-gcn-assembly-cross-lane-operations/

Oh yeah, that's how I started down this rabbit hole to begin with!

It feels like the ISA document should be the end-all be-all of documentation. Its a thick 250ish page manual. For it to be "missing" information seems to be a mistake.

---

### 评论 #4 — jlgreathouse (2019-03-12T19:02:52Z)

Hi @dragontamer 

I've sent this issue to our team that writes the ISA manuals. The fixes for this should be part of the manuals we release for Vega 20 chips.

---

### 评论 #5 — jlgreathouse (2019-12-12T21:08:02Z)

Hello all. I apologize about the long delay on this. Our team that normally does the ISA manuals was moved around in an organizational shakeup, so getting this released took much longer than we originally hoped. However, the ISA guide for the Vega 7nm has been released. It covers the new instructions in this chip, and has an extended ds_swizzle_b32 description in Section 12.13.1.

https://gpuopen.com/wp-content/uploads/2019/11/Vega_7nm_Shader_ISA_26November2019.pdf

---

### 评论 #6 — preda (2019-12-13T06:56:04Z)

@jlgreathouse thanks for the ISA document, it's welcome. BTW, the links on Contact Information at the end of page3 don't work (404) (maybe an editor could verify all the links just in case)


---
