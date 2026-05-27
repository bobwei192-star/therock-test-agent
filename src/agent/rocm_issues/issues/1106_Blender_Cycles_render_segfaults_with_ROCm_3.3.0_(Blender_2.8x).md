# Blender Cycles render segfaults with ROCm 3.3.0 (Blender 2.8x)

> **Issue #1106**
> **状态**: closed
> **创建时间**: 2020-05-09T18:05:18Z
> **更新时间**: 2024-01-18T05:40:33Z
> **关闭时间**: 2023-12-22T13:18:38Z
> **作者**: thima2017
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1106

## 描述

I installed rocm3.3.0 from rocm's repo for Ubuntu (http://repo.radeon.com/rocm/apt/debian/). And I've read an installation guide (https://rocmdocs.amd.com/en/latest/Installation_Guide/Installation-Guide.html#ubuntu).

[ROCm3.3.0+Blender2.82a-logs-infos-strace.zip](https://github.com/RadeonOpenCompute/ROCm/files/4604249/ROCm3.3.0%2BBlender2.82a-logs-infos-strace.zip)


---

## 评论 (20 条)

### 评论 #1 — thima2017 (2020-05-09T18:14:59Z)

Maybe related https://developer.blender.org/T68809

---

### 评论 #2 — ableeker (2020-05-11T18:03:50Z)

I have installed ROCm 3.3.0 on Ubuntu 20.04, and I'm running Blender 2.82a. Blender sees, and recognises my Radeon RX Vega 64. It doesn't segfault on my system, and even renders using the GPU. So, in a sense, it works. Unfortunately, though it's "working" for me, it's pretty useless. I've been trying it out, and either it doesn't seem to do much, it renders exactly as "fast" as CPU only, or it will render MUCH slower... For example, a simple scene will render in a couple of minutes CPU only, but rendering GPU only not only won't render faster, it will render a magnitude slower, or even more.

---

### 评论 #3 — Szalacinski (2020-05-14T02:47:11Z)

Same thing here.  It also causes severe graphical corruptions and slowdowns in Gnome.

Edit: I tried the deb package of Blender instead of the snap package, and instead of graphical corruptions, display updates slow to a halt and all screens go black, making the system unusable.

Ubuntu 20.04
5.4.0-29-generic

---

### 评论 #4 — iszotic (2020-06-01T16:52:36Z)

the workaround is here https://github.com/RadeonOpenCompute/ROCm/issues/402

---

### 评论 #5 — ableeker (2020-06-02T18:38:13Z)

I've tried it, and it seems to work, Blender with OpenCL rendered a bit faster (10%, or maybe 20% faster). But, and this kills this configuration for me, when I reboot the computer with it, it hangs during boot. When I restore the normal ROCM configuration, it boots again.

---

### 评论 #6 — deralmas (2020-06-09T18:43:51Z)

Are there any updates on this whole opencl issue? Is there any planned fix for blender or slow performance, or is this project dead?

---

### 评论 #7 — olFi95 (2020-07-01T20:21:04Z)

> Are there any updates on this whole opencl issue? Is there any planned fix for blender or slow performance, or is this project dead?

I am also very interested in this Feature. 

---

### 评论 #8 — ROCmSupport (2020-12-17T03:33:51Z)

Hi @thima2017 and all,
Thanks for reaching out.
Developer is working on the issues and fixes will be ready and will be part of upcoming releases.
Please stay tuned.

---

### 评论 #9 — CamilleScholtz (2020-12-19T12:43:42Z)

As of 4.0.0 I am still having this issue.

---

### 评论 #10 — ROCmSupport (2020-12-21T06:09:09Z)

Hi @onodera-punpun, we are aware this issue is not fixed yet.
As there are multiple issues with Blender, we are working on them.
The fixes will be part of upcoming releases definitely, but have no specific timelines as of now.
Will share more updates soon.
Thank you.

---

### 评论 #11 — ROCmSupport (2021-03-01T09:02:30Z)

Hi All,

As per the latest information and clarity provided in our Documentation that ROCm does not support GUI applications officially.

Docs also updated accordingly @ https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support

Hardware and Software Support
ROCm is focused on using AMD GPUs to accelerate computational tasks such as machine learning, engineering workloads, and scientific computing. In order to focus our development efforts on these domains of interest, ROCm supports a targeted set of hardware configurations which are detailed further in this section.
Note: The AMD ROCm™ open software platform is a compute stack for headless system deployments. GUI-based software applications are currently not supported.

---

### 评论 #12 — Szalacinski (2021-03-01T16:50:43Z)

There isn't anything fundamentally different between a GUI program using OpenCL, and a CLI program using OpenCL.  Incorrect results and system crashes are still major bugs no matter which way you look at it.  If ROCm can't deliver correct results without crashing the system, regardless of the program being GUI or CLI, then it is functionally useless.  This is basically just rewriting the rules to avoid solving massive problems with your system.  This is really a complete cop-out.  I was hoping that ROCm would improve over time, and that I could go back to using it. If this is the way that the ecosystem is going to go, I can't see myself ever using it again.

Oh, and Blender renders can be run as a CLI command, so this excuse is both wholly incorrect on a rational level, as well as a technical level.

---

### 评论 #13 — johnbridgman (2021-03-01T22:52:37Z)

> There isn't anything fundamentally different between a GUI program using OpenCL, and a CLI program using OpenCL. Incorrect results and system crashes are still major bugs no matter which way you look at it. If ROCm can't deliver correct results without crashing the system, regardless of the program being GUI or CLI, then it is functionally useless. This is basically just rewriting the rules to avoid solving massive problems with your system. This is really a complete cop-out. I was hoping that ROCm would improve over time, and that I could go back to using it. If this is the way that the ecosystem is going to go, I can't see myself ever using it again.

Agree, and apologies for this. The README message was a bit too vague and is being misinterpreted. What it was trying to say was more like "the ROCm stack **releases** do not include userspace graphics components and are not tested for graphics", which has always been the case - you need to combine ROCm userspace compute components with a graphics stack to get a full solution. We currently include a subset of the ROCm stack (up to OpenCL) in our packaged graphics drivers and will be including more over time. 

We did a lot of testing and fixing of the ROCm OpenCL stack as part of the 20.45 release, including a lot of testing/fixing on Blender. Those fixes have not yet made it into a ROCm stack release AFAIK but they should appear shortly. 

---

### 评论 #14 — ROCmSupport (2021-03-09T12:10:11Z)

We are going to rephrase the text about GUI apps in our rocm documentation.
We have come up with some plans to handle GUI apps in a way.
I am reopening it now.
Thank you.

---

### 评论 #15 — tasso (2023-12-19T15:59:32Z)

Is this still an issue?  If not, can we please close it?  Thanks!

---

### 评论 #16 — tasso (2023-12-22T13:18:38Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate.  Thanks

---

### 评论 #17 — ArcticLatent (2023-12-26T22:03:30Z)

This is still an issue. Arch linux user here. Installed hip-runtime-amd-blender package from AUR. I can see my gpu in preferences/system tab but when I try to render Blender just crashes. In Fedora I can use blender with my amd gpu. Whats the problem with rocm and arch linux? Thanks.

---

### 评论 #18 — kuhar (2024-01-08T03:46:25Z)

+1, as of rocm 5.7 / radeon 7900xtx I have issues running rocm examples in a desktop environment alongside unrelated GUI apps. Happy to provide more info / help debugging, just let me know what extra info would be useful.
![image](https://github.com/ROCm/ROCm/assets/4612584/b7d5fe62-4cc5-498f-9283-1a3613e92cb5)

@tasso can we either reopen this or file a new tracking issue?


---

### 评论 #19 — tasso (2024-01-17T15:52:39Z)

@kuhar Let's open up anew ticket.  Thanks!
 @nartmada  Can you please follow up on this?


---

### 评论 #20 — kuhar (2024-01-18T05:40:33Z)

@tasso Filed a new issue here: https://github.com/ROCm/ROCm/issues/2820

---
