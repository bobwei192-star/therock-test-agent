# Use of mainline kernel

> **Issue #118**
> **状态**: closed
> **创建时间**: 2017-05-05T12:19:58Z
> **更新时间**: 2017-08-08T00:00:51Z
> **关闭时间**: 2017-07-02T01:39:54Z
> **作者**: almson
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/118

## 描述

Is any release of ROCm compatible with any mainline release of the Linux kernel? E.g., can I use ROCm 1.5 with kernel 4.11? If not, what are the plans for ROCm to be mainlined?

---

## 评论 (19 条)

### 评论 #1 — gstoner (2017-05-06T16:37:56Z)

1.5 uses the 4.9 kernel,  we are in the process of upstreaming all the key components.   With 1.6 we finally have full DKMS support.  We full engineering team dedicated to ROCm maintaining it.
On May 5, 2017, at 7:19 AM, almson <notifications@github.com<mailto:notifications@github.com>> wro


Is any release of ROCm compatible with any mainline release of the Linux kernel? E.g., can I use ROCm 1.5 with kernel 4.11? If not, what are the plans for ROCm to be mainlined?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/118>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DucR9tNmZEwADy3WatIMIsuxlQ_0sks5r2xPvgaJpZM4NR19l>.



---

### 评论 #2 — grmat (2017-05-10T21:03:39Z)

@gstoner thanks for the info. So you don't plan going upstream with ROCK for 4.12?

---

### 评论 #3 — gstoner (2017-05-22T17:17:29Z)

Merge windows for Linux kernel are delicate balance,  we are working on getting all the code where applicable up streamed 

---

### 评论 #4 — reanimastudios (2017-05-27T19:23:50Z)

In short, wait until the 1.6 release and verification that the mainline kernel has full support for it. Got it.

---

### 评论 #5 — ernstp (2017-06-02T10:59:37Z)

Although you have Ryzen support, Ryzen processors really like a 4.10 kernel. So this will be good for Ryzen users too...

---

### 评论 #6 — gstoner (2017-06-02T11:28:21Z)

It in the plans.

Get Outlook for iOS<https://aka.ms/o0ukef>



On Fri, Jun 2, 2017 at 11:59 AM +0100, "Ernst Sjöstrand" <notifications@github.com<mailto:notifications@github.com>> wrote:


Although you have Ryzen support, Ryzen processors really like a 4.10 kernel. So this will be good for Ryzen users too...

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/118#issuecomment-305756045>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuR_pmdz31h6EWfggLNxXxIsTRYNqks5r_-sbgaJpZM4NR19l>.


---

### 评论 #7 — iavael (2017-07-02T16:52:20Z)

What version of mainline kernel is required to run rocm?

---

### 评论 #8 — gstoner (2017-07-02T17:12:13Z)

It best to load Ubuntu 16.04 and follow the install instruction,  we have new instruction at 
https://rocm.github.io/ROCmInstall.html   Currently ROCm uses the 4.9 Linux kernel.   Note for Ubuntu, it best to use our kernel.     We have base 4.11 Kernel update in our internal mainline, it under test now.  

We are working with the community to upstream the extra driver components we need. 


---

### 评论 #9 — iavael (2017-07-02T20:00:09Z)

@gstoner I thought, that this issue was closed, because all needed patches were upstreamed to mainline. So support of mainline kernel is not ready yet? If it's so, can you reopen this issue, please?

---

### 评论 #10 — reanimastudios (2017-07-02T20:21:31Z)

Mainline kernel support hasn't been updated or it wouldn't be necessary 
for the custom 4.9 kernel and I could just run dkms directly via Debian 
and have it hooked into Debian Sid.

I sure am looking forward to the OpenCL stack from ROCm and Mesa since 
the OpenGL track and later Vulkan support [another interesting topic 
that will come up when AMD is ready with their Vulkan stack vs. RADV] 
since that is the direction AMD has committed to achieving relies on the 
OpenCL stack from ROCm, and not Gallium.

However, I sure as hell am never going to use Ubuntu proper so the only 
full stack that AMD offers in deb format off AMD is out of reach for me. 
I'm a happy AMD investor in stock and hardware but an irritated Linux 
user. I am fully aware of software release schedules in my career.

My other systems are OS X and as an ex-NeXT/Apple engineer I understand 
the need to satisfy the Enterprise markets first and legacy professional 
markets.

With the increased visibility and growth in this upcoming Q10 I urge AMD 
to double the size of their staff for this endeavor. It's paramount that 
the ROCm initiative be mature, across Windows and Linux, and wise if 
they extend their business relationship with Apple to do everything 
possible for the iMac Pro, Mac Pro and future potential Zen systems to 
achieve a long term stable corporation.

- Marc J. Driftmeyer


On 07/02/2017 01:00 PM, Iavael wrote:
>
> @gstoner <https://github.com/gstoner> I thought, that this issue was 
> closed, because all needed patches were upstreamed to mainline. So 
> support of mainline kernel is not ready yet? If it's so, can you 
> reopen this issue, please?
>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub 
> <https://github.com/RadeonOpenCompute/ROCm/issues/118#issuecomment-312513590>, 
> or mute the thread 
> <https://github.com/notifications/unsubscribe-auth/APhR6gNBG2tWsztIFws2vJ95I7Ms8gyvks5sJ_bKgaJpZM4NR19l>.
>


---

### 评论 #11 — gstoner (2017-07-02T21:01:47Z)

Guys I wish we could service all the flavor of Linux, but we can not currently. Marc hit the nail on the head engineering and testing staff is critical to broadening our support.  Remember we balancing supporting new silicon ( Vega10, EPYC, Threadripper, Ryzen, Power, ARM AArch64 etc)  new capabilities, new libraries, new application, improving the software we have already put in place.  All on moving target the Linux Kernel.    

Now it would have been fun to have NextOS and what we doing with ROCm today, plus that engineering team help exploit what we can do with EPYC   Naples is game changer and it  Have 4 Vega10 GPU's on Single socket with 32 cores 64 threads and 8 channel of 4TB memory up  200-250 GB/s bandwidth. 

I give you a preview for 1.7  release  REHL/Centos 7.3, Ubuntu, Fedora via DKMS.  Once we have base DKMS in place we can look at qualifying other Linux Distro. This is the last 1.x series to satisfy this requirement by late mid-summer,  then we focused on 2.0 release for the fall.   

Here is a list of all the packages we rolled out with ROcm 1.6, https://github.com/ROCm/ROCm.github.io/blob/master/ROCmLinuxpackages.md  

---

### 评论 #12 — iavael (2017-07-02T21:08:27Z)

@gstoner  I just wanted to have some place to keep track on effort to run rocm on distro/mainline/custom kernel (in-tree, dkms or any other way). And I thought that this issue is such place. If it's not, then could you tell me where to look?

---

### 评论 #13 — gstoner (2017-07-02T22:04:25Z)

I will build something on ROCm.github.io to talk about how to build custom kernels.  I have been talking to the Linux team about not just dropping a single kernel but breaking out the major components of ROCm kernel driver as separate projects so it easier to understand what is really changing in the kernel.  Also, make it easier to port this to other OS.     Short of this, I set aside some time documentation on the website describing the kernel changes and changes Kernel graphics driver.   

I have been looking at this anyone since I want to work with eBPF with PERF on a EPIC system with Vega10. 

---

### 评论 #14 — almson (2017-07-18T20:33:00Z)

@gstoner The way GitHub works, is that if there is a feature request, then it exists as an open issue until the feature request is implemented. There are multiple reasons for this, including the notification mechanism that GitHub has.

So, reopen this issue.

---

### 评论 #15 — marmistrz (2017-08-07T16:24:50Z)

Yeah, keeping the issue closed suggests it's a wontfix and, as far as I understand, it's the opposite - on the roadmap.

---

### 评论 #16 — gstoner (2017-08-07T16:37:48Z)

We are working on DKMS solution,  for the stack so no it not that we not going to do this, Patience we doing a lot of work with a small team.   We also have REHL/CENTOS and SUSE support on the Roadmap,  REHL/CENTOS is coming first. 

@almson  I know you have strong opinion, but moderation is how GitHub works, this tread has been moderated 

---

### 评论 #17 — marmistrz (2017-08-07T16:47:58Z)

@gstoner I read the whole thread so I perfectly know this. I'm just signaling that the issue being closed miscommunicates:

* open = just reported / todo / assigned / in progress / awaiting merge / ...
* closed = fixed / wontfix / invalid / duplicate / obsolete / notabug

This issue clearly should be open, since you're working on it.

---

### 评论 #18 — gstoner (2017-08-07T16:50:08Z)

We already have a solution,  Base Linux kernel the same for AMDGPU and AMDGPUpro the later use DKMS and Kernel Compatibility layer.   Also, we are upstreaming all the core foundation update for ROCm into the Linux kernel so it will be maintained in each update. 

The issue is closed 

---

### 评论 #19 — reanimastudios (2017-08-08T00:00:50Z)

I have a simple request: Close this after this is upstreamed and mainlined into the Linux Kernel. At the rate AMDGPU and OpenCL is evolving we might be ready for Navi.

- Marc

Marc Jeffrey Driftmeyer
Founder & CEO of Reanimality Studios LLC
Cell: (509) 435-5212
url: https://www.reanimastudios.com <https://www.reanimastudios.com/>
url: https://www.holoworlds.net <https://www.holoworlds.net/>
email: mjd@reanimality.com <mailto:mjd@reanimality.com>
email: mjd@holoworlds.net <mailto:mjd@holoworlds.net>





> On Aug 7, 2017, at 9:50 AM, Gregory Stoner <notifications@github.com> wrote:
> 
> We already have a solution, Base Linux kernel the same for AMDGPU and AMDGPUpro the later use DKMS and Kernel Compatibility layer. Also, we are upstreaming all the core foundation update for ROCm into the Linux kernel so it will be maintained in each update.
> 
> The issue is closed
> 
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub <https://github.com/RadeonOpenCompute/ROCm/issues/118#issuecomment-320717926>, or mute the thread <https://github.com/notifications/unsubscribe-auth/APhR6n2_rHbfdp1FnK83sNXs0BqfOV4dks5sV0BCgaJpZM4NR19l>.
> 



---
