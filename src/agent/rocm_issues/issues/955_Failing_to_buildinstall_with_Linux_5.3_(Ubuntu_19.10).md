# Failing to build/install with Linux 5.3 (Ubuntu 19.10)

> **Issue #955**
> **状态**: closed
> **创建时间**: 2019-12-01T18:29:34Z
> **更新时间**: 2023-12-29T19:25:55Z
> **关闭时间**: 2023-12-18T16:09:32Z
> **作者**: BloodyIron
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/955

## 描述

So 2.10 will not build for me on my Linux Kernel 5.3 (which comes with Ubuntu 19.10). Can we please get Linux Kernel 5.3 support added in? And also have the same support in-place for when Ubuntu 20.04 LTS drops?

Currently kinda breaking my package manager, just so I can get acceleration in DaVinci Resolve :(

---

## 评论 (12 条)

### 评论 #1 — BloodyIron (2020-02-17T18:54:45Z)

Anyone? It's February and Ubuntu 20.04 is just around the bend. Really don't want to wait 2 years to keep up with features, that's just way tooooo slow.

---

### 评论 #2 — BloodyIron (2020-02-17T18:55:18Z)

Hmm, re-enabled the repo for "xenial" and seems to build fine, now to reboot and see if my computer explodes.

---

### 评论 #3 — BloodyIron (2020-02-17T19:15:13Z)

Yeah still getting errors

`Building initial module for 5.3.0-40-generic
Error! Bad return status for module build on kernel: 5.3.0-40-generic (x86_64)
Consult /var/lib/dkms/amdgpu/3.0-6/build/make.log for more information.
dpkg: error processing package rock-dkms (--configure):
 installed rock-dkms package post-installation script subprocess returned error exit status 10
dpkg: dependency problems prevent configuration of rocm-dkms:
 rocm-dkms depends on rock-dkms; however:
  Package rock-dkms is not configured yet.

dpkg: error processing package rocm-dkms (--configure):
 dependency problems - leaving unconfigured
No apport report written because the error message indicates its a followup error from a previous failure.
                                                                                                          Errors were encountered while processing:
 rock-dkms
 rocm-dkms
E: Sub-process /usr/bin/dpkg returned an error code (1)
`

Now openCL is completely broken on my system. I'm on Ubuntu 19.10 with Linux Kernel 5.3.0-40-generic. And AFAIK Ubuntu 18.04.4 now has 5.3, so why is this failing? :(

---

### 评论 #4 — BloodyIron (2020-02-18T16:47:22Z)

I tried switching to ROCM 2.9 (method https://github.com/RadeonOpenCompute/ROCm/issues/284#issuecomment-539095892 ) and the building of the rocm-dkms module still fails.

I really wish that we would get some sort of actual response here. I'm on 5.3 and this should work with ROCM 3, and I'm really not sure why 2.9 is failing now as I had it working before. Now I don't have any openCL with AMDGPU, completely broke my setup thinking the 3.0 release would be a proper setup :(

---

### 评论 #5 — LambisElef (2020-02-22T10:18:26Z)

I'm also having the same issues with Ubuntu 19.10 Kernel 5.3. I didn't try with ROCm 2.9. Please reply.

---

### 评论 #6 — nikAizuddin (2020-02-22T10:32:22Z)

I haven't tried rock-dkms on Ubuntu 18.04. But using upstream kernel driver with Linux kernel 5.2.0-rc1 works for me on Ubuntu 18.04.

Update: I'm using ROCm 3.0

---

### 评论 #7 — keryell (2022-04-05T21:03:28Z)

I guess this can be closed since this OS is no longer supported for 2 years.

---

### 评论 #8 — nartmada (2023-12-13T21:25:43Z)

Hi @BloodyIron, please check latest ROCm Documentation and ROCm 5.7.1 to see if your query has been resolved.  If resolved, please close the ticket.  Thanks.

---

### 评论 #9 — nartmada (2023-12-18T16:09:32Z)

Original ticket is more than a year old and the person that opened the ticket has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks!

---

### 评论 #10 — BloodyIron (2023-12-29T18:58:05Z)

@nartmada I appreciate you engaging me, and I apologise for not responding. The frank truth is I have actually switched to nVidia for my GPUs in the last few years. Namely because after talking to the head of the ROCm division directly, and other discussions on this github/elsewhere, it seemed to me that AMD really could not be relied upon for ROCm to work on consumer GPUs. This is a combination of (and this may have changed since I last looked at it) a) lack of ROCm documentation even talking about consumer GPUs that are supported by ROCm, to any degree b) inconsistent experience with different ROCm versions in the past, I had to lock to very specific versions in the past just to get OpenCL at all and c) lack of communication from ROCm devs or those involved (apart from this dialogue in particular).

So, if AMD actually cares about ROCm (or more specifically OpenCL) working for Consumer GPUs in such a way that _DOES NOT_ reduce gaming performance, then the documentation needs to explicitly state Consumer GPUs are supposed, which ones, and which versions of ROCm to expect them to work with.

As I may have mentioned previously, I care about gaming AND GPU offload (namely for video editing, but other stuff too). And that is using the Mesa "AMDGPU" driver for gaming, and in the past (RX 580) using ROCm for OpenCL for DaVinci Resolve. The thing is countless examples tell to use "AMDGPU-Pro" to get OpenCL (I forget if that is in-tandem with ROCm or not). But the problem with that is the "AMDGPU-Pro" driver has substantially reduced gaming performance.

In-contrast, the drivers from nVidia out of the box provide GPU offload via CUDA and I think a few other APIs. Frankly the drivers for AMD GPUs on Linux (Consumer or otherwise) should _already out of the box_ expose all APIs (such as OpenCL) the card(s) are capable of.

I'm sharing these insights with you in the hopes that the GPU offload state for AMD Consumer GPUs on Linux is improved (or already actually good and I don't realise it). I know a lot of work probably goes into ROCm, but I also still can't fathom why there's so much fragmentation in the driver ecosystem for AMD GPUs, or even why ROCm is separate (by default) from the "AMDGPU" driver.

Now I feel like I'm rambling, sorry. Hope this helps! Again thanks for engaging me after so long! Sorry for the delay :(

---

### 评论 #11 — nartmada (2023-12-29T19:12:20Z)

Hi @BloodyIron, Happy Holidays!  Thanks for your reply and no need to apologize.  This is the type of candid and insightful feedback that I can forward to upper management.  Hopefully the ROCm end-user experience will be more pleasant going forward.

---

### 评论 #12 — BloodyIron (2023-12-29T19:25:55Z)

@nartmada hey thanks for hearing me out! Honestly apart from the ROCm aspect, I quite liked my AMD Consumer GPU experience on Linux (Ubuntu in my case). The AMDGPU driver coming included and taking really no work is lovely. So I really hope ROCm can come along for the ride (or something doing the same thing that isn't ROCm). Hopefully it turns into a nice direction! :D Have a nice weekend please :) I really do appreciate you passing this up along the chain. And I can't remember the fellow's name, but if it's the same person who was heading ROCm about 3-4ish years ago, say hi from me and thanks for them hearing me out those years past. Not every day you get to engage someone in a position like that ;)

Ack rambling more. XD

---
