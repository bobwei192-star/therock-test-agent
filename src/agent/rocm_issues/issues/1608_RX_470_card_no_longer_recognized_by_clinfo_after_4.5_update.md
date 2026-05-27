# RX 470 card no longer recognized by clinfo after 4.5 update

> **Issue #1608**
> **状态**: closed
> **创建时间**: 2021-11-03T14:39:27Z
> **更新时间**: 2022-09-17T04:29:33Z
> **关闭时间**: 2021-11-10T10:04:24Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1608

## 描述

Card was working fine with 4.3.

I uninstalled my previous version (4.3) and installed 4.5.

output from `/opt/rocm/opencl/bin/clinfo` :

```
Number of platforms:				 1
  Platform Profile:				 FULL_PROFILE
  Platform Version:				 OpenCL 2.2 AMD-APP (3361.0)
  Platform Name:				 AMD Accelerated Parallel Processing
  Platform Vendor:				 Advanced Micro Devices, Inc.
  Platform Extensions:				 cl_khr_icd cl_amd_event_callback 


  Platform Name:				 AMD Accelerated Parallel Processing
Number of devices:				 0
```

output from `rocminfo`

```
hsa api call failure at: /long_pathname_so_that_rpms_can_package_the_debug_info/src/rocminfo/rocminfo.cc:1143
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.
```

output from `rocm-smi`

```
======================= ROCm System Management Interface =======================
================================= Concise Info =================================
GPU  Temp   AvgPwr   SCLK     MCLK    Fan     Perf  PwrCap  VRAM%  GPU%  
0    47.0c  23.116W  1169Mhz  300Mhz  19.22%  auto  92.0W    16%   0%    
================================================================================
============================= End of ROCm SMI Log ==============================
```

---

## 评论 (30 条)

### 评论 #1 — proailurus (2021-11-04T18:19:20Z)

RX 570 here.
`clinfo` shows the same output here with "Number of devices: 0"
However, `rocminfo` shows the correct (I think) output and no error message.
`rocm-smi` shows the same output as yours as well.


I just installed 4.3.1 again to cross-check and it works without issue.

---

### 评论 #2 — boxerab (2021-11-04T23:54:20Z)

@clavinet did you try`/opt/rocm/opencl/bin/clinfo` ? 
I should add that I am running on Ubuntu 20.04

---

### 评论 #3 — proailurus (2021-11-05T00:26:17Z)

I tried both the bundled clinfo that comes with ROCm, as well as the system clinfo.
My distro is openSUSE Tumbleweed 20211102 .

---

### 评论 #4 — boxerab (2021-11-06T20:48:58Z)

After re-install, I can now get rocminfo to show what looks like correct output.
However, I can't run an opencl program - no device is recognized.
Come on, AMD !

---

### 评论 #5 — boxerab (2021-11-06T20:49:43Z)

@clavinet how do I re-install the older 4.3 version ?

---

### 评论 #6 — boxerab (2021-11-06T22:45:51Z)

never mind - I've gone back to 4.3.1. Now recognizing 470 as cl device.

---

### 评论 #7 — proailurus (2021-11-08T17:46:51Z)

@boxerab isn't it too early to close this?
The issue still persists with 4.5.

---

### 评论 #8 — boxerab (2021-11-08T19:51:08Z)

@clavinet right you are.

---

### 评论 #9 — proailurus (2021-11-08T20:46:07Z)

Compiling this beast is daunting even for people experienced in building software (not me), so I can't say if it's an issue with the binaries or the rocm source...

Would be great to know if this issue also happens with self-compiled builds.

---

### 评论 #10 — ROCmSupport (2021-11-10T10:04:24Z)

Thanks @boxerab for reaching out.
RX 470 is not supported anymore and so things might not work.
For supported hardware, please check @ [https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url)
Thank you.

---

### 评论 #11 — boxerab (2021-11-10T13:26:53Z)

Thanks, @ROCmSupport . So, support for Polaris 10 was dropped for 4.5.
Was this mentioned explicitly in the release notes for version 4.5 ? 

---

### 评论 #12 — proailurus (2021-11-10T20:47:27Z)

There's a difference between "not supported" as in "we don't provide support", and "not supported" as in "we don't enable that feature in our binaries".

I had hoped that "not supported" in ROCm meant the first case, similar to ECC RAM on consumer Ryzen platforms which recieves no support as in help and assistance from AMD, yet it works at your own risk.

It's sad to see those Polaris cards now apparently being dropped from ROCm binary releases.

@ROCmSupport Can't there be a policy similar to Ryzen and ECC, in that you don't provide assistance for that feature, but don't actively prevent it from running either?

---

### 评论 #13 — boxerab (2021-11-10T20:55:05Z)

@clavinet on the one hand there are a ton of Polaris cards out there, on the other hand 5 years is a reasonable time to support this card. Is there any reason why you need 4.5 instead of 4.3.1 ?

---

### 评论 #14 — proailurus (2021-11-10T22:45:35Z)

>Is there any reason why you need 4.5 instead of 4.3.1?

Not really. It's just that it's usually better to run newer rather than older software, and nobody knows how long 4.3.1 will keep working on modern systems.

---

### 评论 #15 — johnbridgman (2021-11-11T00:13:41Z)

> Thanks @boxerab for reaching out. RX 470 is not supported anymore and so things might not work. For supported hardware, please check @ [https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support](url) Thank you.

Same question as others are asking - my understanding was that we had stopped testing on Polaris but were not disabling Polaris in the code paths... but it looks like maybe we disabled in the code ? 

---

### 评论 #16 — ROCmSupport (2021-11-11T09:49:22Z)

I am not sure about the gfx8 code whether its disabled or not. AFAIK, we might not have removed any code intentionally. but maybe something changed in the stack and we dont validate gfx8, so it might not be working anymore.

---

### 评论 #17 — boxerab (2021-11-11T13:18:23Z)

@ROCmSupport @johnbridgman Polaris 10 cards have worked fine with ROCM since the library was launched in 2016.
It would be a shame, in my opinion, to disable these cards at this stage, unless there's a good reason for doing so.

---

### 评论 #18 — johnbridgman (2021-11-12T18:57:57Z)

Agreed - I checked with our OpenCL management and they are not aware of any action to disable Polaris - seems most likely that this is a bug resulting from all the build/packaging/install changes we made in 4.5 as part of unifying the ROCm and AMDGPU-PRO stacks. 

---

### 评论 #19 — boxerab (2021-11-12T20:23:23Z)

Thanks for looking into this issue - hopefully this can be addressed easily and we can start using the latest ROCm version with our cards.

---

### 评论 #20 — boxerab (2021-11-13T00:44:21Z)

As this appears to be an unintentional bug, can this issue please be re-opened

cc @ROCmSupport 

---

### 评论 #21 — boxerab (2021-11-26T15:51:06Z)

@ROCmSupport @johnbridgman any updates on this issue ? Also, can we re-open until this is resolved ?

---

### 评论 #22 — boxerab (2021-12-13T21:32:52Z)

@johnbridgman do you know if this issue is fixed in 4.5.2 release ?

---

### 评论 #23 — vladtcvs (2022-01-22T11:32:02Z)

I have rx570, problem also exists - no devices on rocm 4.5, while rocminfo shows it. rocm 4.3.1 work fine


---

### 评论 #24 — boxerab (2022-01-22T13:26:15Z)

@vladtcvs don't hold your breath for a fix - AMD has been studiously ignoring this issue.

---

### 评论 #25 — ROCmSupport (2022-01-28T13:21:28Z)

AFAIK, we have not removed any code intentionally. But maybe something changed in the stack and we don't validate gfx8 on ROCm, so it might not be working anymore.
One thing from support point of view, each card has some duration of support. We can not continue supporting cards for more number of years as per business standards. As new cards coming into the  market, we keep adding the new ones into the supported list and keep dropping the old ones after certain amount of time, which is the process.
Thank you.

---

### 评论 #26 — Atemu (2022-01-28T13:42:30Z)

Where can we these business standards for software support duration of AMD cards? 

---

### 评论 #27 — boxerab (2022-01-28T13:56:00Z)

@ROCmSupport absolutely, all cards have an EOL, but 6 years is not very long IMHO. 

---

### 评论 #28 — John-Gee (2022-01-29T01:15:12Z)

> @ROCmSupport absolutely, all cards have an EOL, but 6 years is not very long IMHO.

The 590 is not even 4 years old yet I believe.

---

### 评论 #29 — boxerab (2022-01-29T01:18:13Z)

I've opened a new issue for this situation 

https://github.com/RadeonOpenCompute/ROCm/issues/1659

---

### 评论 #30 — rajhlinux (2022-09-17T04:29:33Z)

I have the RX-580 GPU... this is also a Polaris 10 card and only 5 years since release. Anyways, its best to learn AMD's open source documents of their GPU ISA and OpenCL programming so you do not need to worry about situations like this, it's somewhat complicated to learn but provides you freedom in not relying on anyone and possibilities to get better performance.

---
