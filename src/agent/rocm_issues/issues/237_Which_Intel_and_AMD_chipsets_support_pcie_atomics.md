# Which Intel and AMD chipsets support pcie atomics?

> **Issue #237**
> **状态**: closed
> **创建时间**: 2017-10-26T21:57:37Z
> **更新时间**: 2018-06-03T15:14:33Z
> **关闭时间**: 2018-06-03T15:14:33Z
> **作者**: avfedorov
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/237

## 标签

- **Question** (颜色: #cc317c)

## 描述

Is there any information about pcie atomics support in Intel and AMD chipsets?
I have Intel B250 based motherboard with 2 pcie 3.0 slots.
But only 1 Vega card is usable for rocm.
One pcie slot is OK, but second is routed via chipset and rejects atomics. 

In dmesg:
[    6.087732] kfd kfd: added device 1002:687f
[    8.190144] kfd kfd: skipped device 1002:687f, PCI rejects atomics

I need to search for motherboard with all pcie slots connected to CPU or there are known chipsets with atomics support?
Have you information about atomics support in Intel Z270, H270, X299, AMD X370?

---

## 评论 (5 条)

### 评论 #1 — gstoner (2017-10-27T01:05:57Z)

Haswell or newer CPU's from Intel  
All Ryzen, Threadripper and EPYC CPU's 

---

### 评论 #2 — avfedorov (2017-10-27T08:42:23Z)

My question not about CPU's. 
My question about chipset Southbridge PCIe controler.
Latest chipsets have PCIe 3.0 support, but I see that atomics is rejected on my B250 Kaby Lake chipset Southbridge PCIe.

---

### 评论 #3 — gstoner (2017-10-27T13:29:13Z)

Putting a GPU on Southbridge is not use case we focus on with ROCm since this really for HPC market and Deep learning which you put PCIe switch in a system before you use Southbridge PCIe.  Honestly other for development,  we deploy on servers.   Generally, you do not want to introduce hops to memory which Southbridge does.    Also, most were using PCIe Gen2 in the past.    You have to look at the databook if they support PCIe Atomics aka Atomic Completors. 

---

### 评论 #4 — kruftindustries (2017-10-29T04:19:13Z)

Something I've found out on my system, and I think @gstoner has mentioned this somewhere in the past too, Ivy bridge I.E. Xeon E5-26xx V2 also supports atomics though the only official mention of it is in some Intel off-the-cuff marketing-type spec sheet. I ended up swapping the sandy bridge out for them in a couple supermicro boxes on a leap of faith to find out for sure. When in doubt try it! but don't expect anything unless it's fairly new.

---

### 评论 #5 — wrt54gl (2018-03-22T14:32:56Z)

I am able to run 2 vega 56 cards on rocm with a Prime Z370A motherboard and a i3-8100 cpu. Using kernel 4.13 and installing rocm like this https://rocm.github.io/ROCmInstall.html

---
