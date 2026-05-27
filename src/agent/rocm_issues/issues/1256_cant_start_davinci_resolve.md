# cant start davinci resolve 

> **Issue #1256**
> **状态**: closed
> **创建时间**: 2020-10-08T12:42:50Z
> **更新时间**: 2021-03-09T12:09:30Z
> **关闭时间**: 2021-03-01T08:32:10Z
> **作者**: AtulPremNarayan
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1256

## 描述

![Screenshot from 2020-10-08 18-04-55](https://user-images.githubusercontent.com/72484130/95459863-d0a03400-0991-11eb-830e-03bcfce058f0.png)

showing this

---

## 评论 (24 条)

### 评论 #1 — rkothako (2020-10-09T09:45:05Z)

Hi @AtulPremNarayan 
Can you please share more information on this.

Is application not loading on rocm platform or something else?
Please share clear steps to reproduce the problem.

---

### 评论 #2 — rkothako (2020-11-02T11:00:27Z)

Hi @AtulPremNarayan 
Can you please reply if you are still facing the problem.
Request you to close the issue, if not reproduced.
Thank you.

---

### 评论 #3 — beatboxa (2020-11-14T01:54:30Z)

@rkothako there have been a number of issues with Davinci Resolve, and some have not yet been responded to yet at all by the ROCm development team.  This is actually the first thread where I've seen any response.

For example, these issue are still open from 18 months ago, still active the past few days, and nobody responding:
https://github.com/RadeonOpenCompute/ROCm/issues/768
https://github.com/RadeonOpenCompute/ROCm/issues/1281
https://github.com/RadeonOpenCompute/ROCm/issues/1030

@AtulPremNarayan the support for Davinci Resolve from AMD has generally been very poor over the past few years:  only 2 specific versions of ROCm work:
- version 2.2
- version 3.3
Every version in-between these or newer than these (including the current version) is broken, with no response from AMD.  Also, Davinci Resolve 17.x doesn't work at all (even with ROCm 3.3); so you are stuck with Resolve 16.x.  You can see the multiple responses and reactions from users in the threads above over the past few years.

In the case of this current thread, the screenshot shown does not offer any information.  This is where the storage drives are configured.  The "Memory & GPU" above it are where you would see anything regarding GPU & drivers.

---

### 评论 #4 — rkothako (2020-12-03T12:45:42Z)

Sorry @beatboxa for the delayed reply.
Recently ROCmSupport has been created and the team will take care of responding these tickets.

---

### 评论 #5 — ROCmSupport (2020-12-03T12:50:10Z)

Hi @beatboxa 
Due to the current resources we have, we were not able to validate all of the issues at present, mainly like GUI based applications like Blender, Davinci and Luxmark. 
We will respond slowly.

---

### 评论 #6 — major-mayer (2020-12-09T23:59:36Z)

Seems like finally somebody from AMD is taking care of this issues. 
At least something after all these months :) 

---

### 评论 #7 — beatboxa (2020-12-10T07:39:51Z)

@major-mayer

I would not celebrate.  We have not seen anything yet, other than a comment that they might begin to start looking into these issues slowly, after they skipped so many other issues.

For example, they have still not commented on my original issue (#768), which I opened in April 2019, when Rocm 2.3 broke Davinci Resolve, didn't get fixed until 3.3, and then was immediately broken again in the next point release (3.5).  It has been broken since.

I've literally been trying to use my Vega 64 for years without progress.  To me, it sounds like ROCm is a mess, with issues just now starting to be looked into, with a newly formed support team that is too small and moving too slowly.  Doesn't appear that AMD is investing the revenue we've given them by buying their products or taking GPU-acceleration seriously.  From what it sounds like, rocm is probably several years away from being usable (if ever) for davinci resolve, by which point the hardware will be obsolete.

So I'm not celebrating quite yet.  Instead, I'm annoyed that I spent money on an expensive AMD gpu that is barely usable because of years of poor AMD drivers, with no progress, and AMD just now telling us for the first time after several years that there will be no resolution in the foreseeable future.

---

### 评论 #8 — major-mayer (2020-12-10T07:59:56Z)

I've just switched from windows to manjaro with my Vega 56 and am pretty surprised how good everything works (despite computing) , so this issue might not be as frustrating for me as it is for you.

I agree with you on the point that there seems to be little interest and too few resources available on providing a good open-source opencl driver. 
But then I think at least they have something and if you really need computing capabilities you still have the proprietary drivers (which I haven't tried yet but I heard they work with DaVinci). 
I mean the status quo leaves definitely room for improvement, but if you look on the green side, we can be happy that AMD seems interested in building open source drivers at all. 

Hopefully the Rocm support team gets this driver usable in the near future... 

---

### 评论 #9 — beatboxa (2020-12-10T14:01:13Z)

Unfortunately, the proprietary drivers do **not** work for DaVinci either:
https://github.com/RadeonOpenCompute/ROCm/issues/1281

There is a certain combination of older os / linux kernel, older rocm/driver version, and older davinci resolve that works currently.  The most stable combination appears to be what I am running:
-  Ubuntu 18.04
- rocm 3.3
- davinci resolve 16.2

The current versions of the above are:
- Ubuntu 20.04 (2 years newer)
- rocm 3.10 (8 months newer)
- davinci resolve 17b4 (9 months newer)

(As a reminder, there was 1 year between the previous version of rocm that worked & rocm 3.3, with all releases in-between breaking support, starting with 2.3).

To my earlier point, this means keeping the entire system bottlenecked and being unable to actually use software and features until long after they are released--and sometimes building and maintaining workarounds.  For example, on my system, because of rocm, I have to manually mark certain packages to not update (while others are automatically marked as being unable to update), which causes all sorts of dependency issues, warnings, and other messes.

---

### 评论 #10 — major-mayer (2020-12-10T14:42:50Z)

Hmm I didn't know about that. Using such old software is definitely not an option for me.
That's pretty sad then. Please AMD get your Linux OpenCL Drivers to the same conditions as your OpenGL / Vulkan drivers are :+1: 

---

### 评论 #11 — KristijanZic (2020-12-15T07:09:34Z)

They won't fix anything I guarantee you that. They just announced 4.0. While the driver is in the worst state ever they decided to announce and are days from releasing a major version...

I think we all should have bought Nvidia GPUs and hope that they release open drivers. At least we'd have a working proprietary driver while we wait for them to give a **** about FOSS.

This way we have nothing, no driver, can't do my work, no nothing.
I have a very expensive PCB in a metal case that I can use to hold my door open, as a paper weight or as an art piece to remind me how I got played.

---

### 评论 #12 — unexploredtest (2020-12-15T07:47:59Z)

> They won't fix anything I guarantee you that. They just announced 4.0. While the driver is in the worst state ever they decided to announce and are days from releasing a major version...
> 
> I think we all should have bought Nvidia GPUs and hope that they release open drivers. At least we'd have a working proprietary driver while we wait for them to give a **** about FOSS.
> 
> This way we have nothing, no driver, can't do my work, no nothing.

Yeah, I'm in the same boat. I also bought an AMD GPU because of FOSS and better support on Linux, now I regret it, should have bought an Nvidia GPU.

---

### 评论 #13 — beatboxa (2020-12-15T21:01:17Z)

Same.  I regret buying my AMD Vega 64 for video editing.  I should have bought an Nvidia instead.

One of the most frustrating parts is that after years, it sounds like AMD is just now **starting** to build a team around this; and that the team is not big enough, and that the use case is not important enough.  It took 1.5 years for AMD to provide their first comment on the topic of DaVinci Resolve, and their comment was:
> Due to the current resources we have, we were not able to validate all of the issues at present, mainly like GUI based applications like Blender, Davinci and Luxmark.
> We will respond slowly.

Not exactly confidence inspiring; but at least it is consistent in how poor it is.

---

### 评论 #14 — b-sumner (2020-12-15T22:30:58Z)

I'm not in a position to be of much help, but I was wondering if/how blackmagicdesign is involved.  I was unable to find a specific list of supported configurations on their site.  Do they have such a list, and if so, is it correct?  Are they offering any support, and if so, what do they say about these issues?

---

### 评论 #15 — beatboxa (2020-12-16T01:51:53Z)

I don't think blackmagic is directly involved, but they do have an active forum.  Their forum is relatively restricted though.

This isn't a davinci problem only per se; it affects multiple GUI-based rendering software.

But blackmagic has stated that davinci resolve was always primarily designed around Nvidia cards (& CUDA).  OpenCL is extending the functionality for additional hardware configurations.

With all that said, at the end of the day, this is a driver issue, and the device designer (AMD in this case) should be the primary point of contact as far as I'm concerned.  If OpenCL and related drivers work as they should, this would be a non issue.  One point backing this up:  the things that so far have broken support for resolve have been when ROCm gets updated--ie. the same versiom of resolve will break with different versions of ROCm; and the ROCm project itself seems to be spawned from a need for more GPU-driven applications, in order for AMD to compete better with Nvidia.  This means commercial applications like ML will generally take priority--and as someone in that industry, I'll say that Nvidia currently has a sizeable lead and dominance in everything from partnerships to use cases in commercial applications of GPU-acceleration.

I hope AMD succeeds, but I am frankly astounded by a combination of how far behind they are right now + my direct observations of lack of support & development over the past few years.  It's disappointing and extremely frustrating to say the least; and if I were building a new system today (and I will be very soon), I would purchase Nvidia GPUs instead until AMD gets closer to responding to my needs.  This sentiment appears to be shared by several users--and it might be related to the terrible support of popular applications like DaVinci Resolve, where only ROCm versions 2.2 & 3.3 worked, and all the versions in-between had huge rearchitectures and broke support.  It generally seems to me that AMD has been targeting CPU (and has frankly done a very good job there vs Intel); but there are multiple battle fronts.  CPU (which appears to be starting to move toward ARM architectures) + GPU (where AMD is obviously an underdog relative to Nvidia).  And given the number of ROCm rearchitectures, it seems to me that AMD is rushing a poor & rushed base architecture with a team and investment that's too small.  ie. learning as they go.

Sorry for the rant--I needed it after such a poor experience over such a long period of time. I really hope AMD recognizes and fixes these problems quickly, because I fear that by the time they do, the hardware I bought from them will be obsolete and a waste of money.

---

### 评论 #16 — b-sumner (2020-12-16T21:00:35Z)

@beatboxa many thanks for your comments.  And I think AMD has clearly gotten the message about the frustration it has imposed on its customers.  I expect to see things improving.

I do have one comment about the software though.  Many other ISV's take responsibility for the quality of their software and want to be the first to hear of customer issues.  Only once they determine that the fault is not theirs then they look to the lower levels.  So it surprises me to see that they do not prominently publish which configurations they test and support.  I think anyone purchasing their products should be able to easily check on whether the product is expected to work on their own current or planned configurations and should have a clear route to report issues when the product doesn't work as described.  Without that, I would personally classify the product as "use at your own risk".

---

### 评论 #17 — beatboxa (2020-12-16T21:43:09Z)

This is what BlackMagic has published:
https://forum.blackmagicdesign.com/viewtopic.php?f=21&t=90190#13

That seems consistent with the level of requirements I've seen for similar types of software.  They have also have documentation per version as part of the installation packages, and they have utilities to check and gather system configurations.

I have never seen software take responsibility to post specific versions of drivers for specific hardware, like "AMD ROCm 3.3, but not 3.5, 3.6, 3.7, 3.8, 3.9, 3.10"

---

### 评论 #18 — KristijanZic (2020-12-17T02:19:36Z)

> I think AMD has clearly gotten the message about the frustration it has imposed on its customers.

They didn't even acknowledge our frustration let alone got the message. I'm tired of them ignoring us. And if they ignore us like this, they are ignoring other issues too.

They only said in this thread that they don't have the resources to support their own hardware and quoted DaVinci Resolve an Blender, which are both FREE! What resources do they need?? Do they want a Resolve Studio license, I'll freaking buy one for them if a multi billion dollar company can't afford it.

What are we to do?? Make a Kickstarter to pay AMD to support the hardware we bought? Has everyone lost their minds here?

While you read their response as that they have gotten the message (because they finally came up with a one liner response to us), we who have been dealing with this for Y E A R S already read it as they finally telling us to go **** ourselves as they "d o n ' t     h a v e     t h e     r e s o u r c e s" to support their own hardware. Then what the **** do I have? I've spent my resources buying this GPU. What do I have now? A glorified paper weight?

I'm sorry for the rant and strong words, but at this point I just need a vent. I mean this is ridiculous, how low do we have to fall... I'm ashamed of myself for the level of discourse I had to fall to, like some primitive. But this is what I get for my money, support and years of patience. YEARS of patience! I get a multi billion dollar company telling me they don't have the resources to debug the software they sold me against a free application. What a world we live in, throw a brick at my head right now and absolve me of this misery XDDD

---

### 评论 #19 — major-mayer (2020-12-17T08:28:06Z)

You have a fair point, but please calm a bit down. This thread is already salty enough.
I don't think it will help much if 5 guys are ranting about Amd over and over again 😅

---

### 评论 #20 — KristijanZic (2020-12-17T08:51:29Z)

Yeah, I know... I'm sorry. I started writing and got caught up in the moment... Will do better 😅😇

---

### 评论 #21 — beatboxa (2020-12-18T04:27:36Z)

I'll just point out that the reason you are seeing so much ranting about AMD in this thread is:

- This has been an issue for years, with no progress.  In fact, we've had regressions rather than forward progress.
- This is the first time (after years) we've even seen any sort of acknowledgement from AMD
- This is the first thread (of several) where we've even seen any sort of acknowledgement from AMD

You'll note that above, all of the comments were directing at helping others who have this issue; but also setting proper expectations as a reaction, only after people get overly optimistic.  Because we who have been dealing with this for years have seen no reason to be optimistic so far.  To reiterate:  this is quite literally the first response from AMD we've seen, and even this (AMD's response) is not optimistic.

To be clear, this first response from AMD says:
- AMD has just recently formed a support team
- This recently formed support team is understaffed
- GUI applications are low priority and will be looked into very slowly

This collectively sounds like being late to the airport & trying to catch the flight by running after the plane, after it has already started to accelerate down the runway

---

### 评论 #22 — KristijanZic (2021-01-29T18:53:52Z)

> Due to the current resources we have, we were not able to validate all of the issues at present, mainly like GUI based applications like Blender, Davinci

Guys, let me tell you something! The only reason you are developing that dhriver is for purpose of third party applications to take advantage of it for for users to buy your hardware on that basis. WHAT IS THE POINT OF HAVING THIS DRIVER IF IT'S BROKEN AND THIRD PARTY APPLICATIONS CAN'T USE IT???!!! It is your sole responsibility to first ensure that the driver works and for it's intended purpose and that's enabling third part apps to work better! Everything else is secondary! DO YOU UNDERSTAND THAT?! YOU CAN'T PUSH A BROKEN RELEASE AND A MAJOR VERSION??! But you did, and we the users are paying for it.

---

### 评论 #23 — ROCmSupport (2021-03-01T08:32:10Z)

Hi All,

As per the latest information and clarity provided in our Documentation that ROCm does not support GUI applications officially.

Docs also updated accordingly @ https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support

Hardware and Software Support
ROCm is focused on using AMD GPUs to accelerate computational tasks such as machine learning, engineering workloads, and scientific computing. In order to focus our development efforts on these domains of interest, ROCm supports a targeted set of hardware configurations which are detailed further in this section.
Note: The AMD ROCm™ open software platform is a compute stack for headless system deployments. GUI-based software applications are currently not supported.

---

### 评论 #24 — ROCmSupport (2021-03-09T12:09:30Z)

We are going to rephrase the text about GUI apps in our rocm documentation.
We have come up with some plans to handle GUI apps in a way.
But I am marking this as duplicate of #1345 and hence not reopening for now.
All progress can be seen at #1345 
Thank you.

---
