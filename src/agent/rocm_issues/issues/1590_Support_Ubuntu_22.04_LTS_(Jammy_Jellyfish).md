# Support Ubuntu 22.04 LTS (Jammy Jellyfish)

> **Issue #1590**
> **状态**: closed
> **创建时间**: 2021-10-12T14:54:31Z
> **更新时间**: 2024-02-02T06:23:58Z
> **关闭时间**: 2024-02-01T20:03:22Z
> **作者**: Bengt
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1590

## 描述

The next version of Ubuntu with long-term support, called 22.04 (JJ), will be released on April 21st, 2022. This version will be the first Ubuntu version to be supported by AMD ROCm for 2 years, which is significant for anybody look to modernize their Ubuntu-based ROCm installation. Please make sure this Ubuntu release is supported from day one on and keep us posted about the progress towards that all-important goal.

---

## 评论 (43 条)

### 评论 #1 — Bengt (2021-10-12T14:54:34Z)

From a consumer perspective, this Ubuntu version will be critical in determining ROCm's presence and future. Reason being, that Intel will bring competition to the currently supply-driven GPU market in early 2022. Nvidia is already preparing GPUs to counter the Intel ARC products, aiming at the 3070-ish level of performance. AMD also has competitive hardware in this performance bracket, namely the 6700 XT, 6800, and 6800 XT cards.

However, the software support of these products is vastly different. Nvidia dominates the software support for deep learning with their practically ubiquitous and largely flawless support of CUDA, which is but closed-source software. Intel has positioned themselves multiple times as a proponent of open-source software, but whether that translates to their deep learning offering on GPUs remains to be seen. In any case, the Ubuntu 22.04 release marks a possible turning point, if Intel and Nvidia offer day-one deep learning support for their GPUs, while AMD doesn't. 

---

### 评论 #2 — aoolmay (2021-10-12T17:00:26Z)

Yup, bought 6800XT, not even OpenCL works reliably so i'm limping with old WXs. I don't game so this NAVI is practically trash to me.
Over the last years promises regarding NAVI inclusion into ROCm stack have devolved from "soon" through "tenatively next releases" to basically avoiding specific answers.
Got 3060 for trials and it just works, i'd blame myself over my not doing it earlier only if i wasn't mislead.

---

### 评论 #3 — Bengt (2021-10-12T17:30:13Z)

@aoolmay, I get your sentiment. Thanks for weighing in.

[ROCm Support promised to deliver ROCm for RDNA2 within 2021](https://github.com/RadeonOpenCompute/ROCm/issues/1180#issuecomment-746164720). If they deliver on this promise, RDNA2 support could arrive right on time for Ubuntu 22.04 and the Intel competition. However, I am burned enough to not buy on promises, but on delivery. That seems to be the only sensible way to handle ROCm compatibility.

Personally, my Vega 64 (GFX900) is also due for an upgrade. I am considering a 3060 Ti at least, but I am hoping for competition at the 3070 performance level to bring prices down somewhat. I would still prefer buying AMD, but at the moment (and this moment has been a long one), AMD simply has nothing for me to buy in their retail portfolio. Alternatively, I could go for a used Vega VII, but they seem to die like flies, so that would not be economical.

---

### 评论 #4 — xuhuisheng (2021-10-12T23:13:12Z)

The ubuntu-22.04 does not even start.
We don't know if they will use kernel-5.13 or higher, cannot do any test now.
But ubuntu-22.04 is LTS, so it will be supported, in some day of future.

BTW, ROCm-4.3.1 may already support RX6800. Someone who had this card could have a try.

---

### 评论 #5 — ROCmSupport (2021-10-13T09:10:27Z)

Hi @Bengt 
Thanks for reaching out.
Thanks for explaining things in a good way and also helping AMD in different ways.
Regarding Ubuntu 22.04 support, yes, we will definitely have plans to support in future once it lands in the market.
Thank you.

---

### 评论 #6 — Bengt (2021-10-13T12:48:58Z)

@xuhuisheng Thanks for your response.

- Yes, I am a little early with requesting support or 22.04. However, the 22.04 release cycle starts with the release of 21.10., which is due to be released tomorrow.
- The kernel freeze will probably happen in February or March next year, which is when more concrete testing could be conducted.
- Yes, Ubuntu 22.04 is an LTS version and should be supported, which is why I am asking for support in this issue.
- Maybe some RDNA2 cards already work for some use cases. However, I am asking for OS support, which can only be given once all supported cards work for all supported use cases.

@ ROCmSupport Thanks for your response and appreciation.

- Planning support once this Ubuntu version is released seems a bit late to me. I am specifically asking for it at this early point time, so that day-one support can be worked towards.
- Thank you for confirming that the next LTS release of Ubuntu shall be supported. Why though are you closing this issue now? I am requesting official support for this Ubuntu release, which is not yet achieved. So please, let's keep this issue open to track progress towards that goal.

---

### 评论 #7 — ROCmSupport (2021-10-13T13:02:41Z)

Hi @Bengt 
Thank you much for understanding.
We can not keep issues related to future supported OSes.
As per ROCm's OS support strategy, we keep supporting LTS versions of Ubuntu always.
So we will definitely support the latest LTS version, when it lands. Until then we can not keep it open as its not fair.
If we do not support/someone is facing issues though its officially supported/if ROCm support is delayed/not enabled with it, I recommend to open tickets that time and we will keep them open until issues are resolved.
Hope this helps.
Thank you.

---

### 评论 #8 — Bengt (2021-10-13T17:12:37Z)

@ROCmSupport  Thanks for explaining your policy to me. I did not know that and find it interesting to learn. I am happy to know, that closing this issue was not a mistake but is in fact in line with said policy. Please consider, that this frankly makes no sense from my perspective: Since this upcoming release will be supported anyway, there is no additional engineering effort required for fulfilling this issue. On the other hand, the community could organize their testing efforts here, helping AMD in fulfilling its goal of a smooth support. Maybe this would prevent quite real problems (like the one about GFX900 in 4.3.0) next time. I see some lost potential for leveraging the oftentimes very engaged user base to increase release quality and avoiding crunch time for AMD's engineers after avoidable mishaps.

---

### 评论 #9 — erkinalp (2022-03-24T05:22:58Z)

> The kernel freeze will probably happen in February or March next year, which is when more concrete testing could be conducted.

4 April 2022 is Ubuntu 22.04's kernel freeze.

> Since this upcoming release will be supported anyway, there is no additional engineering effort required for fulfilling this issue. 

Also to mention, people could make community ports of ROCm to short term support releases to allow for further testing.

---

### 评论 #10 — erkinalp (2022-04-15T19:39:21Z)

> its not fair.

Why? Due to releasing it earlier than CUDA?

---

### 评论 #11 — keryell (2022-04-16T02:43:53Z)

@ROCmSupport can you reopen this?

---

### 评论 #12 — Bengt (2022-04-19T22:07:29Z)

Ubuntu 22.04 is scheduled for release the day after tomorrow. So, I guess I will take the opportunity to one last time lament about missing support ahead of time. I hope that there is a release of ROCm in the works which adds targets for the 22.04 version of Ubuntu to the PPA. Otherwise, these remaining days might be the last ones for a while on which ROCm supported the current LTS version of Ubuntu.

---

### 评论 #13 — xuhuisheng (2022-04-20T01:33:38Z)

Here is dependency errors when intall rocm-lib on ubuntu:22.04 in docker.
The version of ubuntu:22.04 is gcc-11.

```
work@7cead9071756:/var/spool/apt-mirror/mirror$ sudo apt install -y rocm-dev
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
Some packages could not be installed. This may mean that you have
requested an impossible situation or if you are using the unstable
distribution that some required packages have not yet been created
or been moved out of Incoming.
The following information may help to resolve the situation:

The following packages have unmet dependencies:
 openmp-extras : Depends: libstdc++-5-dev but it is not installable or
                          libstdc++-7-dev but it is not installable
                 Depends: libgcc-5-dev but it is not installable or
                          libgcc-7-dev but it is not installable
                 Recommends: gcc but it is not going to be installed
                 Recommends: g++ but it is not going to be installed
 rocm-gdb : Depends: libpython3.8 but it is not installable
 rocm-llvm : Depends: python but it is not installable
             Depends: libstdc++-5-dev but it is not installable or
                      libstdc++-7-dev but it is not installable
             Depends: libgcc-5-dev but it is not installable or
                      libgcc-7-dev but it is not installable
             Recommends: gcc but it is not going to be installed
             Recommends: g++ but it is not going to be installed
             Recommends: gcc-multilib but it is not going to be installed
             Recommends: g++-multilib but it is not going to be installed
E: Unable to correct problems, you have held broken packages.
```

---

### 评论 #14 — erkinalp (2022-04-20T14:35:56Z)

@xuhuisheng That is tracked separately, in #1713.

---

### 评论 #15 — Bengt (2022-04-22T21:03:07Z)

Ubuntu 22.04 LTS was released yesterday: https://ubuntu.com/blog/ubuntu-22-04-lts-released

---

### 评论 #16 — Laitaps (2022-05-23T17:00:36Z)

> Hi @Bengt Thanks for reaching out. Thanks for explaining things in a good way and also helping AMD in different ways. Regarding Ubuntu 22.04 support, yes, we will definitely have plans to support in future once it lands in the market. Thank you.

Not doing very well with this fellas.  Now, I must say, I understood what I was doing when I decided on AMD hardware.  I knew it would not make my life easier.  But damn, you guys are really not helping yourselves.

---

### 评论 #17 — phibonacci85 (2022-05-25T19:23:53Z)

I prefer AMD but I'm a linux user. :(

---

### 评论 #18 — wxianxin (2022-05-29T16:19:41Z)

come on guys. Try harder and try again. Now Nvidia is getting into open source. 

---

### 评论 #19 — JudeDavis1 (2022-06-22T11:29:30Z)

Is this issue still not fixed? I know for a fact that if this was open sourced, you would get far more AMD customers. The development time is far too slow. Please consider open sourcing the software. 

---

### 评论 #20 — Bengt (2022-06-22T11:36:12Z)

@JudeDavis1, technically, ROCm is open-source software. However, developing it requires knowledge and manpower, that only AMD has and not the community. Since AMD's open source strategy is to release new source code only with new releases, there is no continuous engagement with the community. Therefore, porting efforts are currently running internally at AMD and in parallel in the public. I hope that AMD can learn for the community's findings, but the other way around is hindered by confidentiality restrictions. This is why we are largely dependent on AMD releasing a version that is compatible with Ubuntu 22.04 although ROCm is open source.

---

### 评论 #21 — Bengt (2022-06-22T11:39:58Z)

It has been three months, or a full quarter of a year, since the release of Ubuntu 22.04 and ROCm is still lacking support.

This is really not a good look and makes day-1 support seem a distant goal.

---

### 评论 #22 — JudeDavis1 (2022-06-22T15:37:50Z)

@Bengt Ah that makes sense now. Still though, I think AMD should put more effort into this. I don't mean to needlessly pressure developers but at least keep in communication with us as to where you guys are at. 

---

### 评论 #23 — wxianxin (2022-06-22T16:10:24Z)

The fact that I can run my algorithms using my NVIDIA cards on latest Ubuntu release instead of AMD nowadays make me wonder should I just get NVIDIA products instead in the future.

---

### 评论 #24 — Laitaps (2022-06-22T16:34:51Z)

> The fact that I can run my algorithms using my NVIDIA cards on latest Ubuntu release instead of AMD nowadays make me wonder should I just get NVIDIA products instead in the future.

Everyone has a different use case, with different requirements.  As a result, they need to make their own choices based on those requirements and I would not be in a position to tell anyone what to do.

I do machine learning work where it is already easier to use NVIDIA.  Despite this, I went with AMD hardware for my workstation in the hopes that it would be better supported in the future.  This appears not to be the case, which is unfortunate as I would like to see more competition.  Hopefully, support will improve by the time I build my next workstation.

---

### 评论 #25 — dpospisil (2022-06-24T06:32:41Z)

I bought RX6800 more than year ago. Since than I am always waiting for a next driver to fix a critical issue or introduce missing feature. Reminds me early Linux days some 20 years ago. I have lost all the trust in AMD.

---

### 评论 #26 — erkinalp (2022-06-24T06:33:53Z)

@ROCmSupport Any timeline to full 22.04 support?

---

### 评论 #27 — dpospisil (2022-06-27T14:32:11Z)

@ROCmSupport just wondering, is it fair to have this issue open now?

---

### 评论 #28 — saadrahim (2022-06-27T17:07:53Z)

Ubuntu 22.04 support is planned by AMD. Launch support for Ubuntu 22.04's release is not planned.

---

### 评论 #29 — Bengt (2022-06-29T09:07:29Z)

Hi, @saadrahim! Thanks for the information. I opened an issue requesting launch day support in a more general manner.

---

### 评论 #30 — My1 (2022-07-14T13:35:34Z)

> Ubuntu 22.04 support is planned by AMD. Launch support for Ubuntu 22.04's release is not planned.

we are WAY beyond that already.
I wonder tho how hard it would have been to do some efforts back in the prep stage when this issue was made and how much would have been left to do at the time of release.

---

### 评论 #31 — directrix1 (2022-08-21T10:54:08Z)

Any updates on this?

---

### 评论 #32 — Laitaps (2022-08-21T12:25:00Z)

> 

I never wanted to say this, but buy NVIDIA.

---

### 评论 #33 — directrix1 (2022-08-22T04:17:42Z)

If Nvidia would open up their compute platform then that would be an option.

---

### 评论 #34 — AbelVM (2022-09-10T10:43:51Z)

Wow,  I just set up my brand new Ryzen laptop with preinstalled Ubuntu 22.04 and, surprise! There is no installable GPU stack for this 4-months-old LTS Ubuntu release. No OpenCL for me! 

Should I go back to my old i7 backed laptop?


---

### 评论 #35 — JudeDavis1 (2022-09-10T10:50:36Z)

> Wow,  I just set up my brand new Ryzen laptop with preinstalled Ubuntu 22.04 and, surprise! There is no installable GPU stack for this 4-months-old LTS Ubuntu release. No OpenCL for me! 
> 
> 
> 
> Should I go back to my old i7 backed laptop?
> 
> 

And what's worse is that they aren't communicating any details, so we're left in the dark. That's the part I find really pathetic and irritating. 

---

### 评论 #36 — Laitaps (2022-09-10T14:00:20Z)

> > Wow,  I just set up my brand new Ryzen laptop with preinstalled Ubuntu 22.04 and, surprise! There is no installable GPU stack for this 4-months-old LTS Ubuntu release. No OpenCL for me!
> > Should I go back to my old i7 backed laptop?
> 
> And what's worse is that they aren't communicating any details, so we're left in the dark. That's the part I find really pathetic and irritating.

Yup.  This lack of support is almost forcing me to move off of AMD with this next generation of GPU.  My next workstation is most likely going to be powered by NVIDIA.  This is something I had hoped to avoid, but I do need to get work done and they provide better support.

---

### 评论 #37 — abhimeda (2024-01-02T15:46:24Z)

Is this still reproducible with the latest ROCm?  If not, can we please close it?  Thanks

---

### 评论 #38 — cgmb (2024-02-01T20:03:22Z)

Support for Ubuntu 22.04 was added in ROCm 5.3.

---

### 评论 #39 — keryell (2024-02-02T01:17:04Z)

I hope the full team is ready for Ubuntu 24.04. :-)

---

### 评论 #40 — My1 (2024-02-02T01:26:38Z)

I opened a discussion about this whole issue for the future, sadly no responses yet

---

### 评论 #41 — keryell (2024-02-02T01:30:13Z)

> I opened a discussion about this whole issue for the future, sadly no responses yet

Could you put the link to your discussion here too so we can follow?

---

### 评论 #42 — My1 (2024-02-02T01:41:00Z)

https://github.com/ROCm/ROCm/discussions/2760
dammit forgot to press the paste hotkey lol

---

### 评论 #43 — cgmb (2024-02-02T06:22:14Z)

> I hope the full team is ready for Ubuntu 24.04. :-)

Ubuntu 24.04 will ship with most of the math libraries from ROCm 5.7 in the OS repositories, so regardless of whether AMD supports 24.04 at launch or not, there will at least be hip, rocblas, hipblas, rocsparse, hipsparse, rocsolver, hipsolver, rocrand, hiprand, rocfft, hipfft, rocprim, rocthrust, and rccl on day one.

I was hoping to have miopen and pytorch-rocm in the OS repos in time for Ubuntu 24.04, but pytorch-rocm is not going to be ready in time and even miopen is unlikely. The cutoff for new packages is the end of the month, and the review process usually takes a couple weeks, so for MIOpen to have a good chance of getting into the Ubuntu 24.04 OS repos, somebody would have to package it and submit a request for sponsorship to the Debian AI mailing list within the next week or so.

I'm busy trying to ensure that we have RDNA 3 support in the OS repos for the 24.04 launch, so I don't have time to put together the MIOpen package...

---
