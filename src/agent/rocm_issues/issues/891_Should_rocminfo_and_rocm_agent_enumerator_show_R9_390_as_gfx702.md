# Should rocminfo and rocm_agent_enumerator show R9 390 as gfx702?

> **Issue #891**
> **状态**: closed
> **创建时间**: 2019-09-25T08:38:42Z
> **更新时间**: 2023-12-19T15:06:10Z
> **关闭时间**: 2023-12-18T17:08:52Z
> **作者**: Lucretia
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/891

## 描述

I'm asking because according to [LLVM docs](https://llvm.org/docs/AMDGPUUsage.html#processors) my card shows as gfx702. I know HCC is deprecated, but I'm helping with Gentoo ROCm and I have implemented the patches for gfx700, gfx701, gfx702 from https://github.com/RadeonOpenCompute/hcc-clang-upgrade/pull/149 and I now have a compiler using the correct bitcodes.

So, really shouldn't these tools return gfx702 in my case? If so, I can send a patch in.

---

## 评论 (4 条)

### 评论 #1 — fxkamd (2019-10-09T15:44:02Z)

As I understand the definition of gfx701 vs gfx702, the only difference is the 64-bit floating point rate. There are different Hawaii variants available that are fused differently depending on the target market. The driver doesn't currently distinguish the two. If we unconditionally change all Hawaiis from one gfx version to the other, we'll always get it wrong for someone.

---

### 评论 #2 — nartmada (2023-12-12T17:49:07Z)

Please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #3 — nartmada (2023-12-18T17:08:52Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---

### 评论 #4 — Lucretia (2023-12-19T15:03:10Z)

Because AMD just drops users and did with rocm, I bought an NV card so i could use CUDA instead. Fix your stuff properly and stop dropping support for users who have shelled out money on your hardware. I still have numerous AMD gfx cards and another one in another slot for vfio passthrough.

It's not you can blame me given the total lack of support since I opened this ticket 4 (READ IT! 4!!!) years ago. 

You can "close this as completed," but it's far from completed, it's "closed because YOU can't be arsed."

---
