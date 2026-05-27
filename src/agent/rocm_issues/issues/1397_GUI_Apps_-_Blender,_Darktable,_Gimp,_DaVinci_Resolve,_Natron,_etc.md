# GUI Apps - Blender, Darktable, Gimp, DaVinci Resolve, Natron, etc.

> **Issue #1397**
> **状态**: closed
> **创建时间**: 2021-03-01T17:03:56Z
> **更新时间**: 2024-08-15T14:19:49Z
> **关闭时间**: 2024-08-15T14:19:49Z
> **作者**: beatboxa
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1397

## 描述

Earlier, several issues that have been open and worked on for some time were closed by @ROCmSupport.  The justification for closing the tickets was that **ROCm is now not supporting any GUI applications**, and will now only support headless applications.  For example, see this post:
- https://github.com/RadeonOpenCompute/ROCm/issues/1345#issuecomment-787750471

The purpose of creating this thread is to:

1. Ensure users & prospective buyers to be aware that **AMD ROCm is not suitable for any GUI applications**, such as Blender, Darktable, Gimp, DaVinci Resolve, Natron, etc.

2. Mark that the fact AMD ROCm does not support any GUI applications as being an issue for ML.  For example, some machine learning cases require some form of GUI, including machine vision (eg. facial or object recognition); or interactive cases (eg. geospatial: 5G tower placement for optimizing signal strength)

3.  Request that AMD ROCm consider supporting these types of graphical OpenCL applications with their graphics cards.  There is no word yet from AMD on whether or not ROCm will be supported in headless mode for these applications (example: parallel-GPU-compute render farm for blender).

For these cases specifically, it seems that nvidia CUDA (https://developer.nvidia.com/cuda-zone) is a better system, and AMD ROCm cannot be considered to be in parity or a potential point for transition.

---

## 评论 (31 条)

### 评论 #1 — KristijanZic (2021-03-01T18:51:27Z)

This issue should be pinned as this is huge 180° change in direction and makes AMD graphics hardware unusable for most users on Linux that require OpenCL or do any serious graphics work including but not limited to machine learning, engineering workloads, and scientific computing.

Does AMDGPU-PRO deprecating PAL in favor of ROCr mean that AMDGPU-PRO also doesn't support GUI interfaces with OpenCL now?

---

### 评论 #2 — Szalacinski (2021-03-01T19:57:00Z)

Same with #1106. The fact that AMD is supposed to be launching supercomputers soon, and seem to be effectively giving up on the ROCm stack, is bizarre.  I see no particular technical rationale whatsoever for limiting ROCm to headless applications.  You still haven't fixed the underlying computational issues, regardless of whether they are headless or not.  They already know how to do it with their closed drivers, so I don't see why this is difficult.  Blender hasn't worked properly at least since 2019, and the only real update that we've gotten is that the issue is somehow out-of-scope because it links with graphical libraries.  If you don't feel like working on this project anymore, or it isn't in your budget, just tell us.  But don't feed nonsense to us, because we'll see right through it.

I'm hoping that this was just some intern misinterpreting something.

---

### 评论 #3 — chippey (2021-03-01T20:35:31Z)

It might be wise to add more applications to the list as unsupported:
Autodesk Maya
SideFX Houdini
Foundry Nuke
and many more in the same realm.

---

### 评论 #4 — johnbridgman (2021-03-01T22:54:34Z)

> This issue should be pinned as this is huge 180° change in direction and makes AMD graphics hardware unusable for most users on Linux that require OpenCL or do any serious graphics work including but not limited to machine learning, engineering workloads, and scientific computing.
> 
> Does AMDGPU-PRO deprecating PAL in favor of ROCr mean that AMDGPU-PRO also doesn't support GUI interfaces with OpenCL now?

Absolutely not a change in direction... this is just a too-vague message being misinterpreted both inside and outside AMD. 

Apologies for the confusion - I'm trying to get this fixed up internally.

---

### 评论 #5 — Szalacinski (2021-03-01T23:03:01Z)

> Absolutely not a change in direction... this is just a too-vague message being misinterpreted both inside and outside AMD.
> 
> Apologies for the confusion - I'm trying to get this fixed up internally.

Thanks for the update on this.  Looks like it may have been a misunderstanding then by someone on the team.  Mistakes happen.
If you, or someone on your team is able to re-open those tickets, that would be great!


---

### 评论 #6 — johnbridgman (2021-03-01T23:08:03Z)

Yep - I want to make sure we are aligned internally before I reopen them so they don't just get closed again, but yes we will get them re-opened. 

---

### 评论 #7 — da-phil (2021-03-13T17:03:17Z)

> Earlier, several issues that have been open and worked on for some time were closed by @ROCmSupport. The justification for closing the tickets was that **ROCm is now not supporting any GUI applications**, and will now only support headless applications. For example, see this post:
> 
>     * [#1345 (comment)](https://github.com/RadeonOpenCompute/ROCm/issues/1345#issuecomment-787750471)
> 
> 
> The purpose of creating this thread is to:
> 
>     1. Ensure users & prospective buyers to be aware that **AMD ROCm is not suitable for any GUI applications**, such as Blender, Darktable, Gimp, DaVinci Resolve, Natron, etc.

Wow, after using ROCm (now at version 4.0.0) on my RX 5700XT for the past 5 months everything (GUI apps) except machine learning frameworks have been working for me, namely gimp and darktable with OpenCL acceleration turned on and considerable speed boost.

Only yesterday I noticed that using OpenCL with both gimp and darktable started to freeze my PC immediately and sometimes I see weird graphics artifacts. I'm using Ubuntu 20.04.2 and just upgraded my kernel to 5.4.0-67-generic, I'm was quite sure that it has been working with 5.4.0-65-generic.

Now I'm with AMDGPU-PRO 20.45 and all OpenCL apps work as they have been before with ROCm.

@KristijanZic I remember seeing your name with darktable issues. Have you had those issues also recently with OpenCL apps such as darktable? Which ubuntu / kernel / ROCm version are you using?

---

### 评论 #8 — KristijanZic (2021-07-18T20:57:24Z)

@da-phil I don't know. I haven't tested it lately. Although I can report that the latest AMDGPU-PRO 21.20 --opencl=rocr is broken. Clinfo gives out normal output but none of the apps that require opencl actually work. DaVinci Resolve doesn't even start and Blender doesn't render. Darktable crashes because it can see opencl but can't use it.

---

### 评论 #9 — BloodyIron (2021-07-30T16:11:22Z)

So what's the current state of all this? I'm still stuck on Resolve 16.x, with my RX 580, and it's looking like upgrading to an RDNA 2 GPU would break OpenCL operations, upgrading to Resolve 17.x would also break, and/or upgrading to ROCm v4.1 or v4.2 would also break. I'm still stuck on my old version of ROCm with my old GPU (again, RX 580) just so Resolve can actually work, and it's been over a year now.

Or am I perhaps misunderstanding the current state of affairs? I saw in another GitHub issue that the "solution" is targeted by "end of 2021" which... really is a long time...

---

### 评论 #10 — da-phil (2021-07-30T19:06:36Z)

> @da-phil I don't know. I haven't tested it lately. Although I can report that the latest AMDGPU-PRO 21.20 --opencl=rocr is broken. Clinfo gives out normal output but none of the apps that require opencl actually work. DaVinci Resolve doesn't even start and Blender doesn't render. Darktable crashes because it can see opencl but can't use it.

@KristijanZic as already mentioned, for me using recent versions of AMDGPU-PRO with ROCr fixed the issue, but I haven't used my desktop machine for the past weeks as it is still in a box after a move, so can't tell you which version I'm using. I try to update the comment once my desktop machine is up and running again.

---

### 评论 #11 — da-phil (2021-10-10T21:58:00Z)

> > @da-phil I don't know. I haven't tested it lately. Although I can report that the latest AMDGPU-PRO 21.20 --opencl=rocr is broken. Clinfo gives out normal output but none of the apps that require opencl actually work. DaVinci Resolve doesn't even start and Blender doesn't render. Darktable crashes because it can see opencl but can't use it.
> 
> @KristijanZic as already mentioned, for me using recent versions of AMDGPU-PRO with ROCr fixed the issue, but I haven't used my desktop machine for the past weeks as it is still in a box after a move, so can't tell you which version I'm using. I try to update the comment once my desktop machine is up and running again.

Getting back to you @KristijanZic after I'm back at my machine and doing all the necessary updates...
It turns out that `amdgpu_21.30` behaves exactly as you described it, it makes the whole system unstable when applications make use of OpenCL, so darktable is ununable with it :(

Did you find any way how to make use of OpenCL acceleration in your tools of trade with the AMD GPU? Or did you finally turn AMD your back and finally got a well supported NVIDIA card? I'm contemplating too these days...

---

### 评论 #12 — da-phil (2021-10-23T12:08:15Z)

> > > @da-phil I don't know. I haven't tested it lately. Although I can report that the latest AMDGPU-PRO 21.20 --opencl=rocr is broken. Clinfo gives out normal output but none of the apps that require opencl actually work. DaVinci Resolve doesn't even start and Blender doesn't render. Darktable crashes because it can see opencl but can't use it.
> > 
> > 
> > @KristijanZic as already mentioned, for me using recent versions of AMDGPU-PRO with ROCr fixed the issue, but I haven't used my desktop machine for the past weeks as it is still in a box after a move, so can't tell you which version I'm using. I try to update the comment once my desktop machine is up and running again.
> 
> Getting back to you @KristijanZic after I'm back at my machine and doing all the necessary updates... It turns out that `amdgpu_21.30` behaves exactly as you described it, it makes the whole system unstable when applications make use of OpenCL, so darktable is ununable with it :(
> 
> Did you find any way how to make use of OpenCL acceleration in your tools of trade with the AMD GPU? Or did you finally turn AMD your back and finally got a well supported NVIDIA card? I'm contemplating too these days...

@KristijanZic so it looks like I didn't pay enough attention on what was going on on my system.
I failed to miss that the kernel headers of a new kernel (currently `5.11.0-38-generic` on Ubuntu 20.4.3) were not automatically downloaded during the last upgrade and hence the AMDGPU-PRO installer couldn't build the DKMS module.
Once I installed the missing kernel header and re-run the installer (`./amdgpu-install -y --opencl=rocr `) the DKMS module was build successfully and since then OpenCL seems to be working again, but I can only tell for darktable, I haven't tested other OpenCL accelerated programs.

So at least the AMDGPU-PRO driver is working again.

Did you make sure that the respective DKMS kernel module was built and installed correctly on your machine?


---

### 评论 #13 — Mhowser (2021-10-23T17:34:20Z)

@da-phil can you test Blender 2.93 cycles rendering, please?

---

### 评论 #14 — da-phil (2021-11-01T19:04:18Z)

> @da-phil can you test Blender 2.93 cycles rendering, please?

I've no experience with blender, can you please give me concrete instructions on what to do?
I suspect you want me to run benchmark program within blender?

---

### 评论 #15 — Mhowser (2021-11-02T17:35:10Z)

No, it is as simple as opening Blender, there should be a default scene with a cube, camera and light source, all you would need to do is select cycles in the rendering section.

---

### 评论 #16 — da-phil (2021-11-03T22:07:42Z)

Okay, just downloaded blender and tested the "cycles" renderer with feature set "supported" and both "CPU" and "GPU Compute" as devices while starting animation rendering.  CPU based rendering took around 8.5s per frame and  "GPU Compute" was slightly slower at 8.8s.
My hardware:
* CPU: AMD Ryzen 7 1700 (8 cores)
* GPU: AMD Radeon RX 5700 XT (with silent BIOS setting turned on)

I assume the GPU rendering is quite slow, it should be superior to CPU rendering, eh?

---

### 评论 #17 — Mhowser (2021-11-04T03:55:31Z)

Yes, it should be *substantially* faster than rendering with the CPU. When I tried rendering with my RX 580 GPU, the object does not render at all, just appears black.

---

### 评论 #18 — da-phil (2021-11-04T20:10:57Z)

Maybe something is wrong with the OpenGL driver setup.
The only GPU intensive app I'm currently using is darktable, which is accelerated by OpenCL, and this works pretty well with the AMDGPU-PRO driver.

---

### 评论 #19 — Mhowser (2021-11-05T02:41:56Z)

@da-phil what kernel version are you running?

---

### 评论 #20 — da-phil (2021-11-06T12:03:40Z)

> @da-phil what kernel version are you running?

 5.11.0-38-generic, as written in a previous post. 

---

### 评论 #21 — da-phil (2021-11-16T14:32:00Z)

> Yes, it should be _substantially_ faster than rendering with the CPU. When I tried rendering with my RX 580 GPU, the object does not render at all, just appears black.

I just read that the new blender version (using Cycles X) will abolish OpenCL support in favor of AMDs HIP API.
Let's see how that goes...


---

### 评论 #22 — Mhowser (2021-11-16T18:19:05Z)

Considering how "intimate" Blender and Nvidia are, the future for AMD hardware looks bleak.

---

### 评论 #23 — kaerumy (2022-10-18T05:13:11Z)

As of Ubuntu 22.04, RX 5500 XT (gfx1012) with stock open source drivers, and rocm 5.3 the following desktop apps are working for me, out of the box without any special configuration, environment variables or command line options

- Blender 3.3.1 Cycles rendering with HIP
- Darktable 4.0.1 OpenCL
- Davinci Resolve 18.04 OpenCL (preview, import/export DNxHD format video)

---

### 评论 #24 — da-phil (2022-10-31T11:18:35Z)

> As of Ubuntu 22.04, RX 5500 XT (gfx1012) with stock open source drivers, and rocm 5.3 the following desktop apps are working for me, out of the box without any special configuration, environment variables or command line options
> 
>     * Blender 3.3.1 Cycles rendering with HIP
> 
>     * Darktable 4.0.1 OpenCL
> 
>     * Davinci Resolve 18.04 OpenCL (preview, import/export DNxHD format video)

Sounds good, finally!
Did you use the proprietary drivers (amdgpu-pro) before and did you do a brief performance comparison?


---

### 评论 #25 — xuhuisheng (2022-10-31T11:41:47Z)

@kaerumy 
BTW, Blender3 rewrite cycles HIP parts, so it can support vega and navi1, navi2 cards. Blender3 just drop OpenCL.

But community said there is a hang issue on navi2 when there is heavy computing.

And I try compile the HIP kernel part of blender3 cycles on gfx803, fortunately, it passed. Seems there is not many peoples used gfx803 with blender3, I haven't get callbacks yet.

---

### 评论 #26 — kaerumy (2022-11-03T09:33:02Z)

> > As of Ubuntu 22.04, RX 5500 XT (gfx1012) with stock open source drivers, and rocm 5.3 the following desktop apps are working for me, out of the box without any special configuration, environment variables or command line options
> > ```
> > * Blender 3.3.1 Cycles rendering with HIP
> > 
> > * Darktable 4.0.1 OpenCL
> > 
> > * Davinci Resolve 18.04 OpenCL (preview, import/export DNxHD format video)
> > ```
> 
> Sounds good, finally! Did you use the proprietary drivers (amdgpu-pro) before and did you do a brief performance comparison?

No I didn't use AMD-Pro or do benchmarks. It just looked too convoluted to get DaVinci running.  I just want something that worked out of the box on well supported mainstream distribution like Fedora or Ubuntu, with the default open source stack + rocm.

Have not tested Davinci extensively other than basic import, editing and export. But others now should be able to test it more, knowing that you can now install it on standard Ubuntu with rocm, without doing any complicated configuration.




---

### 评论 #27 — abhimeda (2024-01-22T22:35:15Z)

Hi @beatboxa, is this issue still persisting on the latest version of ROCm? If not can we close this ticket?

---

### 评论 #28 — beatboxa (2024-05-14T20:53:19Z)

I will check, but it may take me a bit of time.
Related:  https://github.com/ROCm/ROCm/issues/768

**I'm not sure why this ticket was already closed however**, seemingly at the same time you asked me if the issue is still persisting and if you can cloase the ticket.  You just posted that comment last week and you also closed this ticket last week.  Giving yourselves 3 years to work on it and giving us just hours to reply, closing it without testing or verifying a solution.

This ticket seems to have been closed prematurely, without actually offering a chance to validate that it has been resolved.

I suppose marking this "completed" must mean "AMD has completely transitioned to not supporting GUI apps" and I have completed my transition by purchasing an **nvidia RTX 4070 ti Super**.

---

### 评论 #29 — ppanchad-amd (2024-06-17T17:29:58Z)

@beatboxa Sorry for closing the ticket.  Will leave it in the open state until it's validated. Thanks!

---

### 评论 #30 — harkgill-amd (2024-07-09T18:59:44Z)

Hi @beatboxa, DaVinci Resolve, Blender and other GUI based apps are working in the latest 6.1.3 ROCm release. 

Please follow the steps [here](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-radeon.html) to install it and make sure to specify the workstation usecase as done below.

`amdgpu-install -y --usecase=workstation,rocm`

---

### 评论 #31 — harkgill-amd (2024-08-15T14:19:49Z)

@beatboxa, as mentioned in my previous comment, these GUI based apps are working with the 6.1.3 release of ROCm. If you do encounter any issues with these applications after following the installation steps above, please create a new GitHub issue. This will help maintain clarity and allow us to more easily investigate the issue. Thanks! 

---
