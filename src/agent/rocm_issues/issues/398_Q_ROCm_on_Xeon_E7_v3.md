# Q: ROCm on Xeon E7 v3

> **Issue #398**
> **状态**: closed
> **创建时间**: 2018-04-28T21:01:48Z
> **更新时间**: 2018-06-10T11:08:43Z
> **关闭时间**: 2018-05-05T14:55:53Z
> **作者**: Bliss3d
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/398

## 描述

So, 
I'd like to run OpenCL applications with 2 or more Vega 64's on my Supermicro X10QBI, which is part of Intel's mission critical server line up. In the readme it says: 
Current CPUs which support PCIe Gen3 + PCIe Atomics are:

Intel Xeon E5 v3 or newer CPUs;
Intel Xeon E3 v3 or newer CPUs;
Intel Core i7 v4, Core i5 v4, Core i3 v4 or newer CPUs (i.e. Haswell family or newer).
AMD Ryzen CPUs;

So no Xeon E7 v3 or newer CPUs?
However the Xeon E7 v3 is part of the Haswell family

Could someone or Radeon clarify?


---

## 评论 (4 条)

### 评论 #1 — gstoner (2018-04-28T21:04:21Z)

Xeon E7 v3 will work,  we just do not have to many people use this class of system..   We can added to the list.

Greg

On Apr 28, 2018, at 4:01 PM, Bliss3d <notifications@github.com<mailto:notifications@github.com>> wrote:


So,
I'd like to run OpenCL applications with 2 or more Vega 64's on my Supermicro X10QBI, which is part of Intel's mission critical server line up. In the readme it says:
Current CPUs which support PCIe Gen3 + PCIe Atomics are:

Intel Xeon E5 v3 or newer CPUs;
Intel Xeon E3 v3 or newer CPUs;
Intel Core i7 v4, Core i5 v4, Core i3 v4 or newer CPUs (i.e. Haswell family or newer).
AMD Ryzen CPUs;

So no Xeon E7 v3 or newer CPUs?
However the Xeon E7 v3 is part of the Haswell family

Could someone or Radeon clarify?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/398>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuSoEQ6c6zt9H2B0lone0srQ2HxAzks5ttNi9gaJpZM4TrkJ_>.



---

### 评论 #2 — Bliss3d (2018-04-28T21:07:16Z)

Thanks;
Would be nice to see it on the list - for the 3 people it applies to
Best regards

---

### 评论 #3 — gstoner (2018-05-05T14:55:53Z)

It was on the hardware list 
https://github.com/ROCm/ROCm.github.io/blob/master/hardware.md

---

### 评论 #4 — Bliss3d (2018-06-10T11:08:43Z)

Just to add some information - I tested vega 64 & rocm on a Xeon E7-4890V2 and it seems to be work using PCIE 3.0 Atomics

---
