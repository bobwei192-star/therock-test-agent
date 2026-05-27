# Why is the AMD Tobago chipset not supports ROCm?

> **Issue #1317**
> **状态**: closed
> **创建时间**: 2020-12-03T05:54:54Z
> **更新时间**: 2025-12-12T23:12:45Z
> **关闭时间**: 2020-12-03T17:32:07Z
> **作者**: burgil
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/1317

## 标签

- **Question** (颜色: #cc317c)

## 描述

I don't even remember what is this about any more

---

## 评论 (4 条)

### 评论 #1 — ROCmSupport (2020-12-03T07:06:22Z)

Hi @orrburgel 
As per the current rocm docs, Hawaii is not fully supported. Am pasting the info here.
We have plans to update the docs about gfx7. Let me talk to docs team to have this change asap.
We are not guaranteed for gfx7 for now, might/might not work.

_The following list of GPUs are enabled in the ROCm software, though full support is not guaranteed:
        GFX7 GPUs
        "Hawaii" chips, such as the AMD Radeon R9 390X and FirePro W9100_


---

### 评论 #2 — jlgreathouse (2020-12-03T17:31:51Z)

Hi @orrburgel 

As my colleague @ROCmSupport mentions, even Hawaii is only experimentally enabled in the ROCm software stack. Hawaii was used by our team to do initial AMD-internal work porting of the ROCm software stack from the integrated GPUs in APUs to discrete GPUs over a PCIe bus. We eventually made some changes public that would (hopefully) allow ROCm to run on Hawaii dGPUs.

Whether GPUs are supported in ROCm can be quite complicated. See the discussion in [this old thread](https://github.com/RadeonOpenCompute/ROCm/issues/451#issuecomment-422836032) for instance. I cannot publicly describe what things may or may not prevent Tobago from running ROCm (e.g., missing hardware support, missing firmware support, missing software support).

At this time, AMD has not announced any public plans to bring up the Tobago GPU on the ROCm software stack. As described in that linked conversation, the amdgpu-pro stack and the ROCm stack are quite different, and use the GPUs in very different ways. Support for a GPU in the amdgpu-pro stack does not imply support for that GPU in ROCm.

---

### 评论 #3 — owlshrimp (2025-12-12T21:30:26Z)

> Hi @orrburgel As per the current rocm docs, Hawaii is not fully supported. Am pasting the info here. We have plans to update the docs about gfx7. Let me talk to docs team to have this change asap. We are not guaranteed for gfx7 for now, might/might not work.
> 
> _The following list of GPUs are enabled in the ROCm software, though full support is not guaranteed: GFX7 GPUs "Hawaii" chips, such as the AMD Radeon R9 390X and FirePro W9100_

It's not just "not fully supported." Hawaii cards like the W9100 have been completely broken since ROCm 2.0 and people have been reporting this since at least 2019: https://github.com/ROCm/ROCm/issues/871

Drop the facade and release an official list of what you have actually tested and verified works with the latest ROCm, and which you also actually intend to support. Include how long you intend to support it. That is the standard of a mature and production-capable compute stack. Without this bare minimum, people will continue to be averse to investing in the AMD ecosystem.

---

### 评论 #4 — owlshrimp (2025-12-12T21:32:47Z)

> Hi @orrburgel
> 
> As my colleague [@ROCmSupport](https://github.com/ROCmSupport) mentions, even Hawaii is only experimentally enabled in the ROCm software stack. Hawaii was used by our team to do initial AMD-internal work porting of the ROCm software stack from the integrated GPUs in APUs to discrete GPUs over a PCIe bus. We eventually made some changes public that would (hopefully) allow ROCm to run on Hawaii dGPUs.

Hawaii has been completely broken in ROCm since ROCm 2.0. See https://github.com/ROCm/ROCm/issues/871 from 2019.

It's dead.

---
