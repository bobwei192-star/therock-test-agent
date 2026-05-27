# vega 11 support status? (Ryzen 5 3400G)

> **Issue #949**
> **状态**: closed
> **创建时间**: 2019-11-26T06:42:32Z
> **更新时间**: 2023-12-18T22:26:37Z
> **关闭时间**: 2023-12-18T22:26:37Z
> **作者**: linas
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/949

## 描述

So - Ryzen 5 3400G is an entry-level 4core cpu plus "Vega 11 graphics".  Introduced summer 2019. it gets enthusiastic reviews on the interwebs...

This page: https://rocm.github.io/hardware.html makes no mention of it, one way or another.

Given that ROCm is aimed at "HPC and Ultrascale computing", I am not surprised by the overall silence on 3400G ... It's just that I bought one by mistake :-p and am now wondering what I can do with it... 

---

## 评论 (8 条)

### 评论 #1 — smartbitcoin (2019-11-28T01:22:17Z)

when I got navi , I have same expectation as you have for ryzen APU.  later I realize I have to do it by myself as ROCM is oss.
what you really want from apu?  hip compiling stack or tensoflow,   if it's only hip compiler maybe I can help you get a working binary in one week.

---

### 评论 #2 — linas (2019-11-28T05:06:03Z)

Short answer: "Ability to compile & run plain-old opencl2.0 code".  Question:: what's missing for vega11 support?  A compiler backend (hcc or clang)? Can I assume the existing compilers work (because otherwise "hip in a week" would not be possible, right?) 

So I assume that what's missing is dkms or runtime shims to initialize vega11, to load/start/stop apps running on vega11? If that's whats missing, then it sounds like maybe 20 different 10-line tweaks to 6 different packages? 

---

### 评论 #3 — smartbitcoin (2019-11-28T14:12:02Z)

@linas   you are right in most part.   from my experience to turn on navi ( https://github.com/smartbitcoin/MyROCm ),   the linux kernel 5.4 are pretty good for Ryzen APU ,  the llvm also should be ok , if just turn on xnack.  ( for navi , llvm 10 have few bugs which bring unstable issue ).

the component need change is the rocr runtime,  hip and hcc compiler .

for your case , if you only need run opencl, you can use proprietary linux driver for APU, which already support it long time ago.

---

### 评论 #4 — luyatshimbalanga (2019-12-09T05:37:03Z)

@smartbitcoin The catch with amdpgu pro open-cl is the reading of the GPU part of APU as "unknown AMD GPU". It would be great both internal AMD team and ROCm properly coordinate their effort to get out the current mess.

---

### 评论 #5 — Alfcyber (2019-12-21T14:55:33Z)

(edit) @linas 
It looks like there is no PICASSO entry in runtime ...
(maybe you can use the vega binary blobs?)
(less runtime/device/rocm/rocdefs.hpp)

on my laptop (tinkpad e485 (Marketing Name: AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx)) 
(only open source driver, and nearly the latest kernel 5.4.1)
I have a working clinfo and rocminfo, however, I see Pool Info:
    Pool 1
      Segment: GROUP
      Size: 64 (0x40) KB
      _Allocatable: FALSE_
      Alloc Granule: 0KB
      Alloc Alignment: 0KB
      Acessible by all: FALSE

However, it is still possible to compile simple kernel on the gpu, but it has no advantage over a single cpu thread
There is still the possibility to use compute shader with opengl. But programs like blender don't seem to support this.
I think it's good that AMD and the associated teams have disclosed the drivers and software so far.
I hope that the opencl support for this apu will improve in the future, I would be happy to support this somehow, especially since the mesa gallium drivers do not seem to work either


---

### 评论 #6 — eapenfold (2020-07-31T19:29:03Z)

Is there any update on this? I would like to know if it can be used as a GPU for tensorflow in Linux.

---

### 评论 #7 — nartmada (2023-12-13T21:15:37Z)

Hi @linas, please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #8 — linas (2023-12-13T22:06:29Z)

Closing. This is four years old & stale.

---
