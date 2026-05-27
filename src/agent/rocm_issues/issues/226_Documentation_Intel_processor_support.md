# Documentation: Intel processor support

> **Issue #226**
> **状态**: closed
> **创建时间**: 2017-10-14T22:42:27Z
> **更新时间**: 2020-09-13T16:28:48Z
> **关闭时间**: 2017-10-15T14:59:39Z
> **作者**: GreatEmerald
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/226

## 描述

At the moment the readme states:

> Intel Core i7 v3, Core i5 v3, Core i3 v3 or newer CPUs (i.e. Haswell family or newer).

However, if I'm interpreting "v3" correctly (Intel Core i* 3***), that's Ivy Bridge, not Haswell, which is 4***. So is Ivy Bridge supported? Or is it in theory supportable but not tested? Because Ivy Bridge does have PCIe 3.0 support (see Intel Ark). I'm not sure about the atomics in particular, but I'd assume that it's part of the 3.0 spec.

Is the experimental way of figuring out whether atomics is supported by using `lspci -vvvv` and looking for `AtomicOpsCap` in the root ports and the GPU? In my case the root port does say `AtomicOpsCap: 32bit- 64bit- 128bitCAS-`, which seems to suggest that atomics are not supported (and same on the GPU, but it's not a supported Radeon card, so that's expected).

---

## 评论 (11 条)

### 评论 #1 — gstoner (2017-10-15T03:06:05Z)

We use the v”#” for the Xeon series not Core I”#”  products,   We need Haswell or newer for  Atomics Completer support  Aka PCIe atomics    Here some more info on it https://rocm.github.io/ROCmPCIeFeatures.html

Here how we are tracking version
E5 v3  Haswell
https://ark.intel.com/products/series/78583/Intel-Xeon-Processor-E5-v3-Family

E5 v4  Broadwell
https://ark.intel.com/products/series/91287/Intel-Xeon-Processor-E5-v4-Family

E5 v5 now rebranded

On Oct 14, 2017, at 5:42 PM, Dainius Masiliūnas <notifications@github.com<mailto:notifications@github.com>> wrote:


At the moment the readme states:

Intel Core i7 v3, Core i5 v3, Core i3 v3 or newer CPUs (i.e. Haswell family or newer).

However, if I'm interpreting "v3" correctly (Intel Core i* 3***), that's Ivy Bridge, not Haswell, which is 4***. So is Ivy Bridge supported? Or is it in theory supportable but not tested? Because Ivy Bridge does have PCIe 3.0 support (see Intel Ark). I'm not sure about the atomics in particular, but I'd assume that it's part of the 3.0 spec.

Is the experimental way of figuring out whether atomics is supported by using lspci -vvvv and looking for AtomicOpsCap in the root ports and the GPU? In my case the root port does say AtomicOpsCap: 32bit- 64bit- 128bitCAS-, which seems to suggest that atomics are not supported (and same on the GPU, but it's not a supported Radeon card, so that's expected).

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/226>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuZbmpXuoUYYxyExoUXecB-XeQOHBks5ssTjVgaJpZM4P5jfg>.



---

### 评论 #2 — GreatEmerald (2017-10-15T05:35:12Z)

Oh, I see. Would be nice if the readme actually mentioned the actual names or the codenames to prevent confusion, since the Xeon naming convention does not apply to the Core series.

I found https://github.com/RadeonOpenCompute/ROCm/issues/157 where it seems that Ivy Bridge may or may not have the needed support, depending on the motherboard. So is `AtomicOpsCap` indicative of that?

---

### 评论 #3 — gstoner (2017-10-15T14:59:22Z)

When I look at Ivybridge it has PCIe Gen 3 it was hard to see if has Atomic Completor support.  

---

### 评论 #4 — gstoner (2017-10-15T14:59:31Z)

Also we retune the documentation 

---

### 评论 #5 — gstoner (2017-10-15T15:23:12Z)

Fixed

---

### 评论 #6 — spkvfx (2018-01-14T01:31:24Z)

I can confirm that, as far as I can tell, ROCm does install without problem on E5-2630v2 on a Dell T5610 (Ivy Bridge with PCIe 3), and Intel does specify that e5-2600v2 does support atomicOps (see link below). 

I am able to verify my ROCm install using the Hello World program, though heavy lifting in Houdini causes power interruption. I assume this is a result of not having the PSU neccesary to power the Radeon FE. 

I've ordered an auxiliary PSU and can report further once I have the card properly powered.

See this technical overview sheet:
https://software.intel.com/en-us/articles/intel-xeon-processor-e5-2600-v2-product-family-technical-overview

---

### 评论 #7 — xiamaz (2018-02-02T15:57:07Z)

Were you able to run the card with the ivy bridge system?

---

### 评论 #8 — spkvfx (2018-02-03T06:14:02Z)

Yes. Once I got enough power to the card it has been running fine under ROCm 1.7. Keep in mind though that this is an E5 Xeon with a PCIe 3.0 compliant motherboard. Houdini is reporting Atomics in it's system info. I do not know if it would matter or not, I also have both processor slots occupied. 

I do not know if this will work the same for Ivy Bridge Core or E3-series processors, and it appears that it would not. But E5-2600v2 (Ivy Bridge) does appear to work. I would venture to guess that Ivy Bridge E7 would as well.

---

### 评论 #9 — xiamaz (2018-02-03T10:20:15Z)

This is great to hear. I have also got a Xeon v2 CPU with a PCIe 3 board. So I will test ROCm too.

---

### 评论 #10 — spkvfx (2018-02-03T18:39:36Z)

Just be sure you're using an E5 or possibly E7. I've read elsewhere E3 v2 "workstation" processors do not work.

On a special note about Houdini, FLIP does not seem to be working with ROCm 1.7. I do not know if this is an issue with Houdini or ROCm OCL Runtime. I have a bug report with SideFX.

---

### 评论 #11 — cmal (2020-09-13T16:23:25Z)

I have an Intel Core i7 3770K, which is Intel Core v3 and ivy birdge,
$ lspci -vvvv|grep AtomicOpsCap
get nothing.
Does that mean PCIe AtomicOps are not supported on my CPU?

---
