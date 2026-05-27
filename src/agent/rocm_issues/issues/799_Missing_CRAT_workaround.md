# Missing CRAT workaround

> **Issue #799**
> **状态**: closed
> **创建时间**: 2019-05-16T13:35:08Z
> **更新时间**: 2023-12-14T20:40:51Z
> **关闭时间**: 2023-12-14T20:40:51Z
> **作者**: joshchngs
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/799

## 描述

Is there a workaround possible for APUs where the OEM/ODM has failed to include the correct CRAT table entries? For instance, I have an IBase MI988, which I know has a V1807B. Are the missing CRAT entries specific to the MI988 implementation, or will it be the same across all V1807B devices?

If the OEM can't update the BIOS with a corrected CRAT, can I find the appropriate values and hardcode them into the parsing code? Where would I find those values for this board?

Snipped from #435:

I should also point out that, even with code in ROCK to enable particular APUs, you may have difficulty getting `amdkfd` to come up on such devices. When trying to come up on an APU, the `amdkfd` driver expects your system BIOS to make a CRAT (component resource affinity table) available that describes the layout of the hardware (and the GPU in particular).

We have found that OEMs and ODMs that sold machines built using AMD APUs often did not make this table available in their system BIOS. As such, in the past we found that users were often unable to properly use APUs because of hardware settings outside of our control.

I don't know if this situation has improved with Raven Ridge, but it's something to keep in mind if you try to go off the "supported systems" path. :)

_Originally posted by @jlgreathouse in https://github.com/RadeonOpenCompute/ROCm/issues/435#issuecomment-421821479_

---

## 评论 (4 条)

### 评论 #1 — AGenchev (2021-06-19T12:40:09Z)

I also read about this BIOS dependency and I wonder why even when GPU is **physically** inside the CPU, the motherboard manufacturer still can mess up things like "where physically the GPU is" ? 
It is important in these days of GPU shortages and also because we expect more capable APUs to come out from AMD (with the bigger 3D stacked cache tech announced and DDR5 system memory). Won't these be enabled for ROCm ?
Also how this is solved with the discrete (Vega64) GPUs - how does the driver get their location, provided that the MB manufacturer doesn't have idea where the user will put it ?!
Also, provided that in the common case the manufacturer does not have this knowledge and relies on few AMD reference designs, doesn't AMD provide reference BIOSes with correctly set-up CRAT tables ? Because these unsolved relations AMD-Manufacturers reflect on the end users / customers. 
I wonder where a customer can get a list of compatible motherboards with Component Resource Attribute Table set the right way to enable ROCm on AMD APU. Probably we need "ROCm enabled" logo for the MB manufacturers ?!


---

### 评论 #2 — tasso (2023-12-12T20:05:04Z)

Is this still an issue?  If not, can we please close it?  Thanks!

---

### 评论 #3 — AGenchev (2023-12-14T17:30:41Z)

It is selfish to talk only for my case, but my main board works. PyTorch 2 ran successfully on my APU 5700G so AMD kind of did it. Let hope for even more powerful APUs in the future. But Josh started the thread.

---

### 评论 #4 — joshchngs (2023-12-14T20:40:51Z)

It is not longer relevant for **me**, because I ditched the platform – for this reason among others. I don't know if it's still a problem for anybody else, but I guess if it was they either gave up also, or found a workaround.

---
