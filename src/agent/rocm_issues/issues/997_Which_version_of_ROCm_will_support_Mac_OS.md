# Which version of ROCm will support Mac OS?

> **Issue #997**
> **状态**: closed
> **创建时间**: 2020-01-08T05:49:54Z
> **更新时间**: 2020-11-25T01:31:57Z
> **关闭时间**: 2020-01-12T23:34:20Z
> **作者**: mk2016a
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/997

## 描述

Apple is the biggest company buying amd's graphics card. 
Why amd can not provide ROCm or hip on Mac?
Even Nvidia which not selling card to Apple support cuda on Mac OS. 
Why amd's software support is so much worse than nvidia?

---

## 评论 (14 条)

### 评论 #1 — Radddder (2020-01-08T14:12:16Z)

I guess it's not about the video card. This is mainly related to system adaptation. 

---

### 评论 #2 — mk2016a (2020-01-09T09:12:02Z)

> I guess it's not about the video card. This is mainly related to system adaptation.

Well, the truth is old cuda, nvidia 1080ti, and tensorflow gpu works pretty well on el capitan or high sierra, but the new one doesn't even have a driver.
How could a company making so much profit from Mac users provide such worse software support than the one which not profitting at all.
Although Nvidia put cuda on Mac system must for a large mount of profit. But how could AMD whose graphics cards mostly selling to Mac not do so?
I mean AMD now have HIP, ROCm and so on. Why none of them support the biggest buyer mac?
Just because they very unstable and not good for use like what they are on linux?
I don't think so.
I think the AMD management just need a lesson. They need to know why customers are important. 
And I hope there will be no more crashes no matter Linux or ROCm. And now we can just live with LVM or directly passthrough virtual machine because they all have snapshot to backup.

---

### 评论 #3 — Degerz (2020-01-09T23:07:03Z)

How about you start blaming Apple instead ? 

The reason why AMD software support is "so much worse" than Nvidia is solely down to Apple's own incompetence ... 

You want to know why any Nvidia GPU after Kepler doesn't work on macOS Mojave or later ? It's because Apple doesn't want to approve their web drivers or want anyone using CUDA on their platforms! 

Troll AMD all you want for having "worse support" despite getting official driver support from Apple while Nvidia's web drivers don't work for macOS Mojave and have subsequently [deprecated](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#cuda-general-new-features) CUDA support on macOS since 10.2 ... 

Also why would Apple want ROCm/HIP on their platforms if it's vendor locked to AMD hardware which is essentially just CUDA designed for AMD hardware instead ? 

---

### 评论 #4 — mk2016a (2020-01-10T10:39:41Z)

> How about you start blaming Apple instead ?
> 
> The reason why AMD software support is "so much worse" than Nvidia is solely down to Apple's own incompetence ...
> 
> You want to know why any Nvidia GPU after Kepler doesn't work on macOS Mojave or later ? It's because Apple doesn't want to approve their web drivers or want anyone using CUDA on their platforms!
> 
> Troll AMD all you want for having "worse support" despite getting official driver support from Apple while Nvidia's web drivers don't work for macOS Mojave and have subsequently [deprecated](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#cuda-general-new-features) CUDA support on macOS since 10.2 ...
> 
> Also why would Apple want ROCm/HIP on their platforms if it's vendor locked to AMD hardware which is essentially just CUDA designed for AMD hardware instead ?

Maybe get some points.
You mean they can not support Windows while cuda on win for so many years because of the same reason, that Microsoft does not allow them to build their version of hip or rocm?

Linux is a good choice because of its efficiency but it is still not stable enough and not easy to repair the errors of the system or the software.

Mac OS is some kind of open system, the darwin system. While I using Mac os for so many years, the only thing I need to restore backups is unnecessary upgrade. 

On linux actually it became much better than the old version which even get crashed after update or install some system patches. I can totally understand why European governments give up using Linux system. But there is still some errors or problems occuring from time to time. And now it support lvm system and can quickly restore the system from an early snapshot, it became easier to fix its problem.

But don't you think the Mac OS would be a much better choice almost in everywhere except computer efficiency or resources. As a mac user, we need amd which provides graphic cards to us to do a better job, or just tell your superior to give more resources to Mac OS software support. You can do and should do much better.

---

### 评论 #5 — Degerz (2020-01-11T00:34:33Z)

Maybe fix your ignorance first ? 

Windows is a red herring BTW so CUDA on Windows =/= CUDA on Linux ... 

With Windows, Nvidia has to work around the limitations of WDDM so CUDA has comparatively more limitations on Windows compared to Linux. Those same limitations in WDDM prevent AMD from being able to port their HSA kernel driver thus by extension ROCm as well since Microsoft isn't cooperative enough to change this for them ... 

Linux is the only viable choice since it gives the hardware vendors more control over their compute stack. Mac OS is a big joke and so are Apple since they don't want to support industry standards like Vulkan or SYCL ... (at least with Windows, hardware vendors can have ICDs which allow for APIs other than D3D)

Also you seem to have this misconception that just because Mac OS was initially based on an open source project that it would also feature an open compute/graphics stack but this is absolutely not true as Apple have [shown](https://www.macrumors.com/2018/11/01/nvidia-comment-on-macos-mojave-drivers/) clearly time and time again that it only they who call the shots ... 

Even Intel finds it [impossible](https://software.intel.com/en-us/articles/intel-dpc-compatibility-tool-system-requirements) to cooperate with Apple on oneAPI/DPC++ ... 

You singling out AMD is purely trolling on your part when others (Intel) not just including Nvidia are all unable to support custom compute APIs so how about you start holding the source (Apple) accountable for their own incompetence ? 

---

### 评论 #6 — mk2016a (2020-01-11T09:56:40Z)

> Maybe fix your ignorance first ?
> 
> Windows is a red herring BTW so CUDA on Windows =/= CUDA on Linux ...
> 
> With Windows, Nvidia has to work around the limitations of WDDM so CUDA has comparatively more limitations on Windows compared to Linux. Those same limitations in WDDM prevent AMD from being able to port their HSA kernel driver thus by extension ROCm as well since Microsoft isn't cooperative enough to change this for them ...
> 
> Linux is the only viable choice since it gives the hardware vendors more control over their compute stack. Mac OS is a big joke and so are Apple since they don't want to support industry standards like Vulkan or SYCL ... (at least with Windows, hardware vendors can have ICDs which allow for APIs other than D3D)
> 
> Also you seem to have this misconception that just because Mac OS was initially based on an open source project that it would also feature an open compute/graphics stack but this is absolutely not true as Apple have [shown](https://www.macrumors.com/2018/11/01/nvidia-comment-on-macos-mojave-drivers/) clearly time and time again that it only they who call the shots ...
> 
> Even Intel finds it [impossible](https://software.intel.com/en-us/articles/intel-dpc-compatibility-tool-system-requirements) to cooperate with Apple on oneAPI/DPC++ ...
> 
> You singling out AMD is purely trolling on your part when others (Intel) not just including Nvidia are all unable to support custom compute APIs so how about you start holding the source (Apple) accountable for their own incompetence ?

You mean there will never be a ROCm on Mac? But why Cuda support the old Mac OS?

---

### 评论 #7 — Degerz (2020-01-11T10:52:26Z)

> You mean there will never be a ROCm on Mac? But why Cuda support the old Mac OS?

I already told you why, it's Nvidia who makes the drivers for Mac OS but it's **_Apple's decision_** to approve them and they don't want to anymore ... 

Apple does not even allow either AMD or Intel to make their own drivers for Mac OS but it's Apple who solely provides driver support for their hardware ... 

That's why even Intel thinks supporting oneAPI/DPC++ (another CUDA competitor) on Mac OS is a waste of time for the same reasons AMD came to that conclusion as well with ROCm/HIP ... 

If Apple are going to take full control of the compute/graphics stack then you must hold them fully responsible too ... 

The lack of CUDA/DPC++/HIP on Mac OS isn't AMD/Intel/Nvidia's problem anymore, it's now Apple's problem ...

---

### 评论 #8 — mk2016a (2020-01-12T23:33:52Z)

> > You mean there will never be a ROCm on Mac? But why Cuda support the old Mac OS?
> 
> I already told you why, it's Nvidia who makes the drivers for Mac OS but it's **_Apple's decision_** to approve them and they don't want to anymore ...
> 
> Apple does not even allow either AMD or Intel to make their own drivers for Mac OS but it's Apple who solely provides driver support for their hardware ...
> 
> That's why even Intel thinks supporting oneAPI/DPC++ (another CUDA competitor) on Mac OS is a waste of time for the same reasons AMD came to that conclusion as well with ROCm/HIP ...
> 
> If Apple are going to take full control of the compute/graphics stack then you must hold them fully responsible too ...
> 
> The lack of CUDA/DPC++/HIP on Mac OS isn't AMD/Intel/Nvidia's problem anymore, it's now Apple's problem ...

This is really bad for apple. By the way, will there be a verson for windows developing now?

---

### 评论 #9 — Degerz (2020-01-13T03:14:40Z)

Don't expect HIP on Windows this year and possibly next year as well ... 

Without cooperation from Microsoft to do some invasive changes to the Windows graphics kernel, it'll hold up HIP support on Windows for quite a while ... 

This is why Linux is the uncompromising future for GPGPU compute. CUDA has limitations on Windows and does not support a Mac OS anymore. HIP relies on several components of the HSA kernel drivers which have yet to see ground work on Windows and AMD does not make drivers for Mac OS so they never made any promises about ROCm or HIP appearing over there ... 

Linux is the ideal platform for hardware vendors because neither Apple nor Microsoft can dictate or limit AMD/Intel/Nvidia ... 

---

### 评论 #10 — Crear12 (2020-07-07T03:19:08Z)

> How about you start blaming Apple instead ?
> 
> The reason why AMD software support is "so much worse" than Nvidia is solely down to Apple's own incompetence ...
> 
> You want to know why any Nvidia GPU after Kepler doesn't work on macOS Mojave or later ? It's because Apple doesn't want to approve their web drivers or want anyone using CUDA on their platforms!
> 
> Troll AMD all you want for having "worse support" despite getting official driver support from Apple while Nvidia's web drivers don't work for macOS Mojave and have subsequently [deprecated](https://docs.nvidia.com/cuda/cuda-toolkit-release-notes/index.html#cuda-general-new-features) CUDA support on macOS since 10.2 ...
> 
> Also why would Apple want ROCm/HIP on their platforms if it's vendor locked to AMD hardware which is essentially just CUDA designed for AMD hardware instead ?

Yes, if Apple approved Nvidia web drivers, cuda will also be supported on Mac OS. Then, I won't even consider buying a RX 580 egpu (which I have done), I will consider to buy the 1080 or 2070 one instead.

---

### 评论 #11 — Degerz (2020-07-07T03:49:02Z)

> Yes, if Apple approved Nvidia web drivers, cuda will also be supported on Mac OS. Then, I won't even consider buying a RX 580 egpu (which I have done), I will consider to buy the 1080 or 2070 one instead.

Never going to happen and Apple are going to eventually remove support for AMD/Intel GPUs too so you'll be stuck with even worse in-house Apple designed GPUs that won't even have comparable tools to CUDA, oneAPI, OpenMP, ROCm/HIP ... 

You can also kiss goodbye to the idea of having a single machine that supports both macOS and high-end compute solutions as well so you'll have to buy another device solely dedicated to compute or machine learning ... 

---

### 评论 #12 — ZhouXiaolin (2020-07-27T02:42:28Z)

maybe Apple has Metal , so ...

---

### 评论 #13 — qixiang109 (2020-11-19T07:18:14Z)

good news!  tensorflow has just announced a folk that support MacOS (through Apple ML-Compute framework) , seems that CPUs, AMD GPUs, and the new M1 chips are all supported.

 https://blog.tensorflow.org/2020/11/accelerating-tensorflow-performance-on-mac.html 

---

### 评论 #14 — Crear12 (2020-11-19T08:30:27Z)

I knew that Tensorflow had support for Metal before, but it was for iOS/iPad OS only. This time, seriously? Support for Mac OS with AMD? That’s surprising!

> On Nov 19, 2020, at 02:18, qixiang109 <notifications@github.com> wrote:
> 
> 
> good news! tensorflow has just announced a folk that support MacOS (through Apple ML-Compute framework) , sees that CPUs, AMD GPUs, and the new M1 chips are all supported.
> 
> https://blog.tensorflow.org/2020/11/accelerating-tensorflow-performance-on-mac.html <https://blog.tensorflow.org/2020/11/accelerating-tensorflow-performance-on-mac.html>
> —
> You are receiving this because you commented.
> Reply to this email directly, view it on GitHub <https://github.com/RadeonOpenCompute/ROCm/issues/997#issuecomment-730180660>, or unsubscribe <https://github.com/notifications/unsubscribe-auth/AJKZHZ657VUN5VYICDYOOVLSQTBEJANCNFSM4KEDFTGQ>.
> 



---
