# ASUS A88XM-A (BIOS: 3001) + A10-7850K Xorg screen corruption/hang with Ubuntu 16.04 + ROCm 1.4

> **Issue #66**
> **状态**: closed
> **创建时间**: 2017-01-01T15:14:26Z
> **更新时间**: 2017-01-04T03:19:11Z
> **关闭时间**: 2017-01-04T03:19:11Z
> **作者**: zpodlovics
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/66

## 描述

Hi,

Recently I tried to upgrade my system (HW: ASUS A88XM-A BIOS: 3001, IOMMUv2 enabled + A10-7850K, the DVI display is used with a ATEN Advance Tech Inc. CS-64U KVM) to Ubuntu 16.04 from Ubuntu 14.04, however I ran into some issue. The system right now works perfectly (Xorg + HSA) with an earlier ROCm version.

```
ii  linux-headers-4.4.0-kfd-compute-rocm-rel-1.1.1-10                4.4.0-kfd-compute-rocm-rel-1.1.1-10-1                  amd64        Linux kernel headers for 4.4.0-kfd-compute-rocm-rel-1.1.1-10 on amd64
ii  linux-image-4.4.0-kfd-compute-rocm-rel-1.1.1-10                  4.4.0-kfd-compute-rocm-rel-1.1.1-10-1                  amd64        Linux kernel, version 4.4.0-kfd-compute-rocm-rel-1.1.1-10
ii  rocm                                                             1.1.2                                                  amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-dev                                                         1.1.2                                                  amd64        Radeon Open Compute (ROCm) Runtime software stack
ii  rocm-kernel                                                      1.1.1                                                  amd64        Radeon Open Compute (ROCm) drivers
ii  rocm-smi                                                         1.0.0                                                  amd64        System Management Interface for ROCm
```

However the same system with a new Ubuntu 16.04 + ROCm 1.4 installation is not working correctly. The HSA example (vectory_copy) seems to works correctly without errors, but the screen show some kind of corrupted image (please see the attachment). The strace showed that the Xorg process is waiting on select syscall. The system will hang on the "service lightdm restart" command. I have attached both the dmesg both the Xorg log and a screenshot about the screen corruption/hang.

![2017101154457](https://cloud.githubusercontent.com/assets/8523206/21581667/d6595c48-d03b-11e6-96c8-2ebe29953cbb.png)
[dmesg.txt](https://github.com/RadeonOpenCompute/ROCm/files/680041/dmesg.txt)

[Xorg.0.log.txt](https://github.com/RadeonOpenCompute/ROCm/files/680044/Xorg.0.log.txt)

Any idea how to fix the screen corruption/hang?

Thanks for your help,
Best Regards,
Zoltan


---

## 评论 (5 条)

### 评论 #1 — jedwards-AMD (2017-01-03T18:58:32Z)

The A10-7850K is a Kaveri chipset, and is not supported on the ROCm stack after version 1.1. Specifically, there are known bugs in the compute-firmware package for the Kaveri chipset which may not be fixed. I would suggest staying on the 1.1 version of ROCm if you want continued Kaveri support.

---

### 评论 #2 — zpodlovics (2017-01-03T20:03:23Z)

Is this some kind of bad joke? I bought this machine for HSA (possible high level compiler) development ( eg.: https://github.com/kp-tech/fshsa ), and I expect it to work correctly for this purpose in addition as a development desktop.

According to the documentation:
https://github.com/HSAFoundation/HSA-Drivers-Linux-AMD

"**These drivers have been superseded** by ROCm Platform now hosted at Radeon Open Compute GitHub Repo https://github.com/RadeonOpenCompute"

Since when it's "normal" to just drop support without notice to a recent (APU) hardware because nobody want's to fix their own (eg.: firmware) bugs at AMD/HSAFoundation/etc? I am sorry, but this is just unacceptable. Why should the any developer invest their and money on something that suddenly become unsupported and no longer works with the newer version of operating system and drivers? Why should the customer choose something that suddenly become unsupported?

---

### 评论 #3 — briansp2020 (2017-01-03T21:23:57Z)

@zpodlovics 
I'm not an AMD insider. So, I can't speak for them. But, I think AMD was clear that Kaveri was not fully HSA compliant. So, though it's unfortunate, it's understandable that they decided not to continue supporting it when problems were found with the platform. AMD is supporting their hardware as long as they possibly can (just see FreeSync 2 announcement) But sometimes, it just does not make financial sense to continue supporting old platform, especially when the hardware is not fully capable of standard to begin with.
Just my 2 cents.

---

### 评论 #4 — zpodlovics (2017-01-03T22:54:34Z)

@briansp2020 
Do you really expect that anybody will accept that an existing and perfectly working functionality suddenly dropped, without any notice and without any migration path? How about providing a working, stable and polished platform and proper development experience (with proper SDK with tools) and support it for several years, and after that provide support for migration to a new version/platform? How about providing a working, stable and polished display driver?

Sometimes just does not make financial sense wasting time and money on platforms that randomly and without notice and migration path discontinue support for existing products. Would you risks your own money on a commercial product (as end user or developer of the product) that plan to use a platform with this kind of risks and history?

---

### 评论 #5 — gstoner (2017-01-04T03:07:27Z)

Zoltan @zpodlovics 

 I remember when you started the F# project. I know your one of the earliest  HSA developers.   I want to respect your early work here.  

I am sorry for your inconvenience on this issue.  If I can contact you l like to talk about path forward beyond Kaveri. 



---
