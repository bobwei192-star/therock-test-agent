# ROCm on IBM Power8: PCIe atomics?

> **Issue #800**
> **状态**: closed
> **创建时间**: 2019-05-18T16:53:09Z
> **更新时间**: 2024-01-19T04:16:06Z
> **关闭时间**: 2024-01-19T04:16:05Z
> **作者**: illuhad
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/800

## 描述

Hi,

I'm aware that Power8 is not officially supported for ROCm 2.4, but it seems to have been supported previously (mentioned in issue #157 and [here](https://www.anandtech.com/show/10831/amd-sc16-rocm-13-released-boltzmann-realized)), so I wanted to give it a try and see if I could get current ROCm working with my system (Tyan TN71-BP012 with Power8 CPU, Radeon Pro WX2100, Ubuntu 19.04).

I got to the point where I managed to get `rock-dkms` compile (with a couple of minor changes), but `amdkfd` prints the infamous error `kfd: skipped device [...], PCI rejects atomics`.  The GPU is in a PCIe slot directly attached to the CPU, without switches in between.

This [stackoverflow](https://stackoverflow.com/a/44509852) post indicates that Power8 doesn't implement atomics.

This make me wonder, if Power8 really doesn't support atomics as a hardware limitation, how come that it supposedly worked previously? Is there some magic kernel/driver parameter that needs to be used? Or was there perhaps a special codepath for Power8, possibly using CAPI instead of regular PCIe atomics? Is there anything I can do to get it working?

---

## 评论 (10 条)

### 评论 #1 — madscientist159 (2019-08-28T21:16:24Z)

Newer versions of ROCm don't require atomics, so they should be able to work on POWER8 and POWER9 systems.  What do we need to get builds going, preferably with some QA on AMD's side to make things work properly?

EDIT: If anyone wants to work on this I do have the ability to allow remote access to a bare metal POWER9 machine with a Vega installed.  The Vega series is supposed to work without atomics with ROCm, so it should be possible to work through any issues on a platform like that.

---

### 评论 #2 — illuhad (2019-08-28T21:25:25Z)

Newer versions still need PCIe atomics, this has only been relaxed for gfx9 (Vega) cards. My Radeon Pro WX2100 is still gfx8.
Most of the changes I had to make were on the build system level (mostly, remove `-msse` and `-march=` etc).
I would be willing to give it a try, but without a use case for me (without a Power machine that can fit a Vega - my Power8 box doesn't have enough physical space) the amount of time I could invest is very limited.

For solid ROCm support on ppc64le, I think that CI testing of some sort is a must. My experience with ROCm compilers and the stack in general is that it can be quite brittle due to fast development speed, little documentation and a lot of interacting components.

---

### 评论 #3 — madscientist159 (2019-08-28T21:30:04Z)

@illuhad If you could get it working we'd probably give you a few months free use of the Vega enabled system for whatever you wanted -- even mining if you were so inclined.  For physical space issues, we've run flexible cables before from the PCIe slot to the GPU; perhaps that would work in your situation?

EDIT: We can also provide the CI system, as this support is important to us.  Let's see if it first works, then we can figure out CI.

---

### 评论 #4 — illuhad (2019-08-28T21:45:44Z)

hm, I work with GPU clusters for my day job, so access to GPUs is not really something that I lack ;) I've also already had the pleasure of playing with some big P9+Tesla V100+NVlink systems, and I'm not really a miner, so for me it's mostly about the curiosity then ;)
What might be interesting for me is a Power system where I can run performance regression tests on (I lead the [hipSYCL](https://github.com/illuhad/hipSYCL) project which implements the Khronos SYCL programming model for AMD/NVIDIA GPUs), but of course for that I would need some non-temporary machine.

As I've said I would be interested in giving it a shot, but I don't want to make any promises. ROCm is a huge stack with lots of error sources and even compiling it for x86 so that it actually works bug-free can be difficult..

I don't think that flexible cables would work for me, unless I find a way to put the GPU outside of the chassis (it's a 2u box without any risers), and then I would also have to solve the issue of power delivery to the GPU which this system is not really made for.

---

### 评论 #5 — madscientist159 (2019-08-28T23:40:06Z)

@illuhad We're flexible, if you wanted to at least look into the ROCm sources and could make it work I'm sure we could figure out a way to get you non-transient access to a system for your regression tests.  Does that sound reasonable enough?

---

### 评论 #6 — darkbasic (2023-02-17T13:58:18Z)

@illuhad any news on this?

---

### 评论 #7 — tasso (2023-12-12T20:04:21Z)

Is this still an issue?  If not, can we please close it?  Thanks!

---

### 评论 #8 — darkbasic (2023-12-12T20:35:15Z)

I don't know about PCIe atomics but ROCm doesn't work at all on anything but x86: https://github.com/RadeonOpenCompute/ROCm-OpenCL-Runtime/issues/158

---

### 评论 #9 — tasso (2023-12-12T23:08:24Z)

Does this document help?  Thanks!

https://rocm.docs.amd.com/en/latest/understand/More-about-how-ROCm-uses-PCIe-Atomics.html



---

### 评论 #10 — nartmada (2024-01-19T04:16:05Z)

Please refer to this link "How ROCm uses PCIe atomics".
https://rocm.docs.amd.com/en/latest/conceptual/More-about-how-ROCm-uses-PCIe-Atomics.html

Closing this ticket.  @illuhad, please re-open if your original query is still not answered.  Thanks.


---
