# ROCm Supported Motherboards with PCIe Atomics

> **Issue #1146**
> **状态**: closed
> **创建时间**: 2020-06-13T17:06:35Z
> **更新时间**: 2024-10-08T15:34:44Z
> **关闭时间**: 2021-01-12T08:59:44Z
> **作者**: onyedikilo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1146

## 描述

Can you guys comment here with the motherboards you are using indicating the number of GPU's and  GPU types. It is really hard to find a motherboard with correct specs, I am having a hard time seeing an indicator for PCIe Atomics support on any of the spec sheets.

Also there is another issue with one of the PCIe slots being capable of Atomics and the rest is not.

So if anyone can write down their systems motherboards, it would help a lot of people I believe.

Or maybe I am missing something like "if its x16 or x8 speed then it would support Atomics" type of thing? Any help is appreciated.

Found these motherboards for a 6x rig but could not verify their Atomics support on every PCIe slot:

EVGA X299 DARK 151-SX-E299-KR 
Asus WS X299 SAGE
SUPER MICRO X11DPi-N
SUPERMICRO X11DAi-N


---

## 评论 (15 条)

### 评论 #1 — briansp2020 (2020-06-13T18:28:43Z)

I'm sure all of them supports PCIe atomic since they support skylake and newer CPUs. Atomic support has more to do with CPU than chipset unless the MB uses PCIe bridge. Do you plan on using multiple GPUs?

But why not use AMD CPUs with PCIe 4 since they are more future proof? Zen2 based Threadripper would be better choice in my opinion.

---

### 评论 #2 — onyedikilo (2020-06-14T10:54:29Z)

@briansp2020 I have a motherboard : Biostart TB250-BTC, ROCm runs fine with a RX580 on main slot, but the other 5 slots don't support Atomics so I can only use one of the cards. As I mentioned before I cannot tell from the motherboards spec sheet that it only supports one slot for Atomics. 

Well the reason I don't want to use PCIe4 is that i have 384 pieces of RX580 and don't want them to go to waste. They were mining Gpu's, now they are sitting there doing nothing.

I am afraid to buy a new motherboard just to see it doesn't work.

---

### 评论 #3 — briansp2020 (2020-06-14T14:47:14Z)

Are you intending to just change the mother board? The motherboard you listed in OP are for HEDT CPUs but you seem to have Skylake LGA 1151 CPUs based on your current MB.

On consumer desktop motherboards, most of the PCIe lanes coming off the chipset do not support PCIe atomic passthrough. Hence, PCIe x1 lanes not working with ROCm with RX580 on your current MB. You need to make sure that the MB sends PCIe lanes coming off CPU to PCIe slots directly. One way to make sure of that is to buy MB that supports NVIDIA SLI. MB supporting NVIDIA SLI tends to be MBs that splits x16 to x8/x8 configuration. I'm not too familiar with Intel motherboards. But on AMD side, X370/X470/X570 supports SLI and should work with 2 AMD graphics cards. B350/B450 boards support AMD CrossFire but uses PCIe lanes coming off chipset for the second GPU and does not work with ROCm when you plug in the GPU to the second PCIe slots.

If you want to use more than 2 GPUs at once, you will need HEDT or server grade MB. I think Threadripper has more PCIe lanes coming off CPUs so you will be able to use more than 2 GPUs on those MBs. Intel HEDT CPUs do not have as many PCIe lanes so they have to use a bridge chip to support more PCIe lanes and I do **not** know whether Intel HEDP MBs can support more than 2 GPUs or not.

AMD uses EPYC servers for their multi GPUs systems. The following threads have people discussing their experience with highend MBs with ROCm

https://github.com/RadeonOpenCompute/ROCm/issues/451
https://github.com/RadeonOpenCompute/ROCm/issues/738

Hope this helps.

---

### 评论 #4 — onyedikilo (2020-06-15T17:05:36Z)

@briansp2020, Brian, thank you for your time, I really appreciate your help. Where did you get the information `B350/B450 boards uses PCIe lanes coming off chipset for the second GPU` ? 

  

---

### 评论 #5 — seesturm (2020-06-15T17:16:11Z)

To my best knowledge only X70 chipset supports so-called "bifurcation" in order to split the CPU 1x16 PCIe lanes into 2x8. So everything below X70 supports additional PCIe slots only via chipset.

There is one board where I have the impression that the CPU lanes for the NVMe slot (x4) can also be used for the 2nd PCIe slot: ASRock AB350 Pro4. In theory this should enable PCIe atomics for both slots. But then you have to live without (PCIe-)NVMe.

---

### 评论 #6 — briansp2020 (2020-06-15T17:55:06Z)

@onyedikilo From personal experience. https://github.com/RadeonOpenCompute/ROCm/issues/46 I had ASUS Z170M-E D3 which supported CrossFire but not SLI and I currently have GigaByte GA-AB350M-D3H (rev. 1.0) which also supports CrossFire but not SLI. Neither worked with ROCm on the second PCIe x16 slot.

Look for motherboard that support x8/x8 configuration (AFAIK, on AMD side, only X_70 chipsets support it. On Intel side, I'm not sure. As I said, I had Z170 but it did not work.) 

---

### 评论 #7 — Q2Learn (2020-07-02T02:50:10Z)

Motherboard ASUS Prime Z270-P only works with one GPU (I have a MSI RX 570 connected) in the main PCIE slot. I am using a Intel Core i5-7500. That motherboard does not have Atomics apparently see [#1168](https://github.com/RadeonOpenCompute/ROCm/issues/1168)

---

### 评论 #8 — dundir (2020-07-19T02:48:58Z)

@onyedikilo I can confirm the ASUS Prime B450-Plus will only work with the first GPU and then only if the APU is also disabled or not functional, and you've also set X to use the second GPU only for display. There may be some stability issues (i.e. kernel hangs sporadically).

---

### 评论 #9 — SomethingGettingWrong (2020-07-23T08:04:48Z)

it would seem in my experience that when  mining riser cards at x1 speed will not allow for pci atomics. I have to use the amdgpupro or the windows driver.

---

### 评论 #10 — ROCmSupport (2021-01-12T08:59:44Z)

Thanks all for the discussion.
I am closing this as its not actually a defect and no ETA required.
Thank you.

---

### 评论 #11 — dundir (2021-01-12T12:29:11Z)

@ROCmSupport, this is a defect, though it appears it is not in rocm but in the hardware/firmware level architecture of the various MB being used. At a bare minimum this should be considered a defect in the documentation for rocm if not a defect in the software (since there are no software tests to determine whether the required hardware support is actually available reliably). 

There are a large number of AMD motherboard brands which simply won't work with consistency, reliability, or repeatability across the same GPU hardware running rocm. Its been years and AMD/rocm hasn't been able to address these challenges in a straight forward way. Hence the discussion, large number or multiple threads, and large amount of time and attention many people have spent on this.

The end result, for people impacted by this class of problem is that rocm is simply being discarded as a viable alternative. Some people with money to burn have tried various chipsets to see if one will work but those are in the minority. Rocm at this point without further action is stuck as more of a gimmick than anything else. Simply because there isn't a test anyone can run that can quickly determine if the necessary hardware/compatibility support is there in all cases across the MB ecosystem. I hated having to drop $1000+ on an Nvidia card/motherboard combo just to be able to do some basic ML research .The hardware is equivalent to the AMD RX series and I would much prefer to use AMD if it were viable.

Instead of closing this difficult problem it should be escalated as this is technically a problem with the MB hardware/firmware not properly supporting your hardware. I can say from experience that the presence of PCI-E Atomics support is not the whole picture, my ASUS B450-Prime Plus when queried shows it has support for PCIE Atomics but runs into the same inconsistent behavior of some motherboards that do not have PCIE-Atomics. The conclusion I've drawn based on months of testing is that ASUS either has issues with their BIOS to support, specifically the Ryzen 5 APU support fix, which may prevent it from working correctly or they use PCI-E lines that show PCI-E atomics support when there is none.

When last I posted on this (~ September or November I think) I was even willing to donate my AMD MB/GPU combo which could repeatedly cause the problem to someone with the necessary low level system architecture expertise to troubleshoot. I never did get any response to that offer and the offer still remains open.

Edit: Updated for Clarity

---

### 评论 #12 — ROCmSupport (2021-01-28T11:35:50Z)

Thanks @dundir for your good feedback. I will work with Documentation team for the changes as requested.
Thank you.

---

### 评论 #13 — DrSensor (2021-02-02T00:22:58Z)

Does motherboard with chipset AMD A320 supported?

---

### 评论 #14 — Plotnus (2021-10-17T22:49:23Z)

I'm gonna have to agree here. We need a way to know which part of our setup is lacking and how to evaluate potential hardware.
For example I don't know if the issue is in my MoBo, CPU, or both. All PCIe slots are v3 compatible.

So, how to evaluate if hardware will suport atomics for _every_ pcie slot prior to purchase?


Looking at [ROCM:Hardware-and-Software-Support](https://github.com/RadeonOpenCompute/ROCm#Hardware-and-Software-Support)
I see "In the default ROCm configuration, GFX8 and GFX9 GPUs require PCI Express 3.0 with PCIe atomics."
Which begs the question, "How do I do a configuration that doesn't require PCIe atomics and deploy it to my system?"




---

### 评论 #15 — T-Shilov (2024-10-08T15:34:42Z)

Hello everyone,

I have read this [topic](https://github.com/ROCm/ROCm/issues/1146) carefully, and I want to buy a [PRIME X370-PRO](https://www.asus.com/supportonly/prime%20x370-pro/helpdesk_cpu/) motherboard.
Do you think it will be able to work with **two** AMD RX580 graphics cards?

---
