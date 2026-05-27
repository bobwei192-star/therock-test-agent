# Q: does ROCm work on Ubuntu 18.04?

> **Issue #397**
> **状态**: closed
> **创建时间**: 2018-04-26T22:51:01Z
> **更新时间**: 2018-08-22T14:24:00Z
> **关闭时间**: 2018-06-03T12:48:20Z
> **作者**: preda
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/397

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

I would like to ask whether ROCm works on Ubuntu 18.04 (which was released recently).


---

## 评论 (41 条)

### 评论 #1 — extraymond (2018-04-26T23:09:05Z)

It woks with kernel 4.13, I'm living with it for the moment.

---

### 评论 #2 — preda (2018-04-26T23:19:29Z)

Thanks. Does it work with Linux kernel 4.15 (which is the default in 18.04) as well?

---

### 评论 #3 — extraymond (2018-04-26T23:22:08Z)

I tried and nah. I've heard that someone tried to patch the kernel and worked, you can try if it fits your appetite.

BTW, you can use [ukuu](https://github.com/teejee2008/ukuu) to install kernels from [ubuntu.kernel](http://kernel.ubuntu.com/~kernel-ppa/mainline/), it's really handy for managing kernels. Just remember to set it in grub as default.

---

### 评论 #4 — preda (2018-04-27T07:40:05Z)

Thanks again. Well Ubuntu 18.04 is LTS (Long Term Support), so there's my hope that AMD would like ROCm to work on stock Ubuntu 18.04 eventually.

In the meantime, tentative answer: NO ?!

---

### 评论 #5 — gstoner (2018-04-27T12:34:34Z)

It coming we just need base bits from Linux driver team 

---

### 评论 #6 — 3D-360 (2018-04-29T21:18:29Z)

ROCm on 18.04 would be FANTASTIC.
ROCm on 18.04 with mobile Ryzen/Vega APU would be even better.  
I am working on an embedded vision system with Deep Learning DNN, and ROCm with MIOpen is VERY fast.  Is there any way that I can speed up the 18.04 Ryzen/Vega APU roll-out?

---

### 评论 #7 — odellus (2018-05-07T01:34:16Z)

Big huge :+1: on this request from my end.
I'm playing around with ROCm in 18.04 right now. Ubuntu I downloaded came with Linux 4.15.0-20-generic kernel installed by default. Can confirm not working with the 4.15 kernel at this time.

System: 
AMD® Ryzen 3 1300x quad-core processor × 4 
Radeon RX 580 Series (POLARIS10 / DRM 3.23.0 / 4.15.0-20-generic, LLVM 6.0.0)

Running `rocminfo` yields:
```
hsa api call failure at line 900, file: /rocmdata/jedwards/git/compute/rocrinfo/rocminfo.cc. Call returned 4104
```

And `clinfo` can't find a useable device either:
```
Number of platforms                               0
```

Calling `dmesg | grep kfd` returns:
```
[    0.978522] kfd kfd: Initialized module
[    1.725905] amdgpu 0000:09:00.0: kfd not supported on this ASIC
```

---

### 评论 #8 — gstoner (2018-05-07T02:31:29Z)

Your kfd did not load so none of the stack will work.  You may have device I’d issue.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Tomas Wood <notifications@github.com>
Sent: Sunday, May 6, 2018 8:34:18 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Comment
Subject: Re: [RadeonOpenCompute/ROCm] Q: does ROCm work on Ubuntu 18.04? (#397)


Big huge 👍 on this request from my end.
I'm playing around with ROCm in 18.04 right now. Ubuntu I downloaded came with Linux 4.15.0-20-generic kernel installed by default. Can confirm not working with the 4.15 kernel at this time.

System:
AMD® Ryzen 3 1300x quad-core processor × 4
Radeon RX 580 Series (POLARIS10 / DRM 3.23.0 / 4.15.0-20-generic, LLVM 6.0.0)

Running rocminfo yields:

hsa api call failure at line 900, file: /rocmdata/jedwards/git/compute/rocrinfo/rocminfo.cc. Call returned 4104


And clinfo can't find a useable device either:

Number of platforms                               0


Calling dmesg | grep kfd returns:

[    0.978522] kfd kfd: Initialized module
[    1.725905] amdgpu 0000:09:00.0: kfd not supported on this ASIC


—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/397#issuecomment-386934222>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuetpDkRdQgdvZJfp2LMvP9QVf-paks5tv6SagaJpZM4Tolni>.


---

### 评论 #9 — odellus (2018-05-07T03:07:18Z)

Sounds about right. Interested in contributing to support for 18.04, but falling back to 16.04 for now.

---

### 评论 #10 — 3D-360 (2018-05-07T15:49:47Z)

gstoner,
If the "kfd" loads, then ROCm will work?
How do I learn about "kfd"?  It looks like it is related to the amdgpu driver in the kernel.

The following link suggests that the 4.18 kernel will support kfd on the RavenRidge APU.

https://www.phoronix.com/scan.php?page=news_item&px=AMDKFD-GFX9-Vega-Patches

Should I sit back and wait for the kernel, or is it worth trying to patch the 4.17 kernel so that ROCm can work on Raven Ridge?

---

### 评论 #11 — Johnreidsilver (2018-05-10T09:46:03Z)

Does ROCm work only with KFD's OpenCL "glue" or can it work with AMDGPU-PRO OpenCL "glue" too?
There's an early preview of AMDGPU-PRO out now for Ubuntu 18.04:
https://support.amd.com/en-us/kb-articles/Pages/Radeon-Software-for-Linux-18.20-Early-Preview-Release-Notes.aspx

Sorry if this is off topic or outside the scope of this git.

---

### 评论 #12 — stalkerg (2018-05-11T10:01:47Z)

I think you can install newer kernel to Ubuntu, it's easy, and build ROCm form source. 

---

### 评论 #13 — dcheng0 (2018-05-14T20:35:01Z)

Worth noting, if you feel more comfortable with more up to date OS, but still wish to run ROCm, you can always run ROCm in KVM. I run ROCm in KVM with PCIE passthrough with a Fedora 28 Host and an Ubuntu 16.04 guest. 
Edit: It also runs with binary support on Centos 7.4 now :) thank you ROCm devs!

---

### 评论 #14 — preda (2018-05-16T06:18:31Z)

FYI, AMDGPU-Pro 18.20 (beta) for Ubuntu 18.04; includes OpenCL based on ROCm 1.6:

https://support.amd.com/en-us/kb-articles/Pages/Radeon-Software-for-Linux-18.20-Early-Preview-Release-Notes.aspx


---

### 评论 #15 — preda (2018-05-23T13:45:54Z)

ping? -- still no ROCm for Ubuntu 18.04?
As seen above apparently amdgpu-pro did put out a version for 18.04, with OpenCL, and based on ROCm no less.

---

### 评论 #16 — gstoner (2018-05-23T14:59:45Z)

@ preda it will be in ROCm 1.9.  

---

### 评论 #17 — eriklindahl (2018-05-25T09:46:39Z)

Hi Greg!

Is there *any* way we can try to hack it for now? While I'm sure we all appreciate AMD's (and your) efforts with limited resources, there was a ~6 month span between 1.7 & 1.8, and if there's a similar time until 1.9 it would mean that AMD doesn't support the long-term-stability release of the most widely installed Linux distribution for ~6 months after the release. At least for my team, that would be a pretty worrying signal.


---

### 评论 #18 — gstoner (2018-05-25T12:11:34Z)

@eriklindahl   I understand your desire for Day 1 support for Ubuntu. 18.04.  But our focus for  1.8 RHEL/CENTOS support which was critical for a large number of our customers. This is what took longer to get 1.8 out the door.   We even have a number customers who still want Centos 7.2.    

Remeber inside the 5 months ( not 6) to release 1.8 we have 1.7.1 and 1.7.2 release 

Also, we are on LTS release 16.04 which is still support out until 2021, 18.04 is targeted not 6 months but for an August release.  3months post 18.04 release. In the scheme of LTS this not as bad as you make it out

But yes we opensource the driver source so you can work on it.   the issue is DKMS KCL interface the portion of the base Linux driver my team is responsible for will work, this is about getting base driver operation aka AMDGPU ( KGD, KFD, Thunk) they userland will work once this is in place. 

---

### 评论 #19 — eriklindahl (2018-05-25T12:26:52Z)

Thanks @gstoner; I do see how it makes sense to prioritize large customers.

Rewriting kernel interfaces might take a little too much time to learn, but I'm at least chipping in by porting the AMD kubernetes device plugins to k8s v1.10 - I just can't test them without reinstalling a machine right now ;-)

---

### 评论 #20 — gstoner (2018-05-25T12:34:51Z)

@eriklindahl  That is fantastic your helping out on K8 support.  this area we putting lot more energy into as you can see.    I am asking what we can do about 18.04 support. 

One thing Dekken did a fix for 4.16 kernel recently so we getting guys in the community who can do this class of work.  Which is great to see.   

---

### 评论 #21 — gstoner (2018-05-25T13:13:55Z)


Looking at it 18.4.1 is the target for July/Aug, which is good timing since we can pick up the version that clean up the launch issue of 18.04  I work with the team to align with this first patch 

---

### 评论 #22 — Bengt (2018-06-02T15:02:47Z)

@gstoner, what launch issue are you talking about? The release notes of Ubuntu 18.04 do not explain to me, why one would hold back on using it for GPU computing: https://wiki.ubuntu.com/BionicBeaver/ReleaseNotes#Known_issues

---

### 评论 #23 — preda (2018-06-03T00:07:49Z)

According to Ubuntu 18.04 ReleaseSchedule, https://wiki.ubuntu.com/BionicBeaver/ReleaseSchedule ,
18.04 Beta1 was released on March 8, and 18.04 Final Beta was released on April 5. It looks like all the "launch issues" had plenty of time to be addressed before the 18.04 release on April 27.

I think the community tried to point out, before the 18.04 release, that it is coming out soon and that maybe AMD should get ready for that. But well I guess it's a question of priorities with limited resources..


---

### 评论 #24 — gstoner (2018-06-03T12:48:20Z)

@preda @Bengt 

I am closing this thread since it no longer productive,   We have a formal release coming with 18.04 support for those who need the binary image 

If you want it today you need to either bootleg the kernel or use Denken patch for DKMS/KCL ( kernel compatibility layer)  ROCM 1.8 Userland and components work on Ubuntu 18.04 on top of the bootleg kernel driver.  We tested it on a  monolith kernel replacement in our team.  We also have run ROCm 1.8 Userland in 18.04 in Docker package. 

The issue we have to wait on is getting from AMDGPU Linux team DKMS KCL + KFD based driver that has been updated to support 18.04.   ROCm enabled driver has a number of configuration that different then AMDGPUpro around the amount of memory you can allocate on the GPU, we also have optimization for LargeBAR that have to be enabled, They develop AMDGPU support first since AMGPUpro DKMS KCL package.   So we waiting on the Linux driver team.   I have asked if we can do .x release to support it.  Prior to 1.9.   Right, it is 1.9 

---

### 评论 #25 — oleid (2018-06-07T18:15:37Z)

FYI: The dkms-module of 1.8 seems to work on ArchLinux using Linux 4.16, when applying this patch: https://github.com/oleid/amdgpu-dkms/commit/7d11254249da86c987601b7d8a1860e12efabefa

---

### 评论 #26 — rhlug (2018-06-07T20:50:31Z)

But wont compile against 4.17 because vga_switcheroo_set_dynamic_switch() was provided by drivers/gpu/vga/vga_switcheroo.c in 4.16, but not in 4.17.x.

---

### 评论 #27 — rhlug (2018-06-07T22:16:10Z)

So wiping out some switcheroo calls, it builds fine on 4.17rc2.

```
# grep VERSION /etc/os-release 
VERSION="18.04 LTS (Bionic Beaver)"

# clinfo | egrep -e "Driver Version|Board"
  Driver Version                                  2617.0 (HSA1.1,LC)
  Device Board Name (AMD)                         Vega [Radeon RX Vega]
  Driver Version                                  2617.0 (HSA1.1,LC)
  Device Board Name (AMD)                         Vega [Radeon RX Vega]

```

But the powerplay problems that are fixed by running 4.17rc2, still exists in rocm, and by using dkms, it overloads those fixes...

```
# cat /sys/class/drm/card0/device/pp_dpm_sclk 
0: 852Mhz *
1: 991Mhz 
2: 1138Mhz 
3: 1269Mhz 
4: 1312Mhz 
5: 1474Mhz 
6: 1538Mhz 
7: 1590Mhz 

# cat pp_table.1403.953.890mv > /sys/class/drm/card0/device/pp_table 

# cat /sys/class/drm/card0/device/pp_dpm_sclk 
Killed

# dmesg
[  750.848937] amdgpu: [powerplay] Failed to register high thermal interrupt!
[  750.848938] amdgpu: [powerplay] amdgpu: powerplay initialization failed
[  753.310724] CPU: 0 PID: 1904 Comm: cat Tainted: G           OE     4.17.0-rc2-180424-fkxamd #1
[  753.311166] RIP: 0010:vega10_print_clock_levels+0x10b/0x240 [amdgpu]
[  753.312481]  pp_dpm_print_clock_levels+0x82/0xd0 [amdgpu]
[  753.312650]  amdgpu_get_pp_dpm_sclk+0x32/0x50 [amdgpu]
[  753.364102] RIP: vega10_print_clock_levels+0x10b/0x240 [amdgpu] RSP: ffffbb6642dc7c90

```

So you end up with same fate ("RIP: vega10_print_clock_levels") as I report on Issue #429 against the 4.13 stock kernel.   



---

### 评论 #28 — stalkerg (2018-06-08T05:28:20Z)

@rhlug I think you should just use 4.18

---

### 评论 #29 — rhlug (2018-06-08T17:56:12Z)

@stalkerg  and rocm 1.8.1 userland without dkms?

---

### 评论 #30 — preda (2018-06-08T20:57:57Z)

(on my Vega and Fury GPUs, I use Ubuntu 18.04 with kernel 4.17 and amdgpu-pro 18.20 userland, and opencl works nicely).

If ROCm 1.8.1 userland works with 4.18 on Ubuntu 18.04, I would be thankful for instructions on how to install it (i.e., ROCm 1.8.1 userland, specifically).


---

### 评论 #31 — rhlug (2018-06-09T20:28:08Z)

@preda I agree, 4.17rc2 and beyond are good with the pro 18.20 drivers.  I dont have amdgpu-dkms installed, and I have a working opencl.     I tried drm-next-4.18-wip with rocm-1.8-151, but no working opencl without rocm-dkms.


---

### 评论 #32 — KeironO (2018-07-19T09:34:57Z)

@preda, what exactly do you mean by ```amdgpu-pro 18.20 userland```?

---

### 评论 #33 — preda (2018-07-19T10:06:47Z)

@KeironO: on linux kernel 4.17, installing amdgpu-pro 18.20 produces an error related to dkms compilation (or similar), i.e. the kernel part of amdgpu-pro is not installed. Nevertheless, opencl works nicely. OpenCL comes from amdgpu-pro 18.20, but the kernel part is the standard 4.17 unchanged.


---

### 评论 #34 — preda (2018-07-27T10:52:33Z)

I can install ROCm 1.8.2 on Ubuntu 18.04 with kernel 4.15, so I consider this issue fixed now.

---

### 评论 #35 — valeriob01 (2018-08-20T20:51:34Z)

Hello, I have installed ubuntu server 18.04 and ROCm 1.8.192 from the ROCm repository, installed clang and rocm-opencl but when running the program I get an error -1001: platform not found.



---

### 评论 #36 — preda (2018-08-20T23:01:38Z)

You may try this for OpenCL:
sudo apt install rock-dkms rocm-opencl-dev

did you get any errors during install?


---

### 评论 #37 — valeriob01 (2018-08-21T04:36:51Z)

I did this already as per the instructions and one error said it is incompatible with current kernel 18.04

I have downloaded rocm 1.8.192, unable to find 1.8.2 .


---

### 评论 #38 — valeriob01 (2018-08-21T07:37:33Z)

@preda I have installed amdgpu-pro 18.20 on kernel 4.17.0, it works, barring some timeout error. Today when I have time I will try ubuntu 16 and ROCm. It seems that the ROCm repositories are made for Ubuntu 16.

---

### 评论 #39 — valeriob01 (2018-08-22T06:01:41Z)

I have attempted, following the documentation scrupulously, to install ROCm on Debian 9 and on Ubuntu 16 and 18, each time it says No Platform found. Please update the documentation.

---

### 评论 #40 — jlgreathouse (2018-08-22T14:13:31Z)

I suspect that your hardware is either incorrectly configured or not supported on ROCm. Please create a new issue so that I can help try to debug this for you. I would prefer not to piggyback on this issue.

---

### 评论 #41 — eriklindahl (2018-08-22T14:24:00Z)

For reference, after updating to rocm 1.8.192, rocminfo works just fine for me with Ubuntu-18.04 on a machine with dual Radeon 560s, with both devices visible.

---
