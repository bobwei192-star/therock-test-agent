# OpenCL support in ROCm

> **Issue #30**
> **状态**: closed
> **创建时间**: 2016-09-05T12:09:06Z
> **更新时间**: 2016-12-02T21:11:19Z
> **关闭时间**: 2016-09-06T13:50:25Z
> **作者**: nevion
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/30

## 描述

I see #12 - but this topic did not lay out OpenCL support - Ben Sander in comments @ http://gpuopen.com/rocm-do-you-speaka-my-language/ says OpenCL is soon, but this was May 5th (4 months ago from this issue).

I think it's pretty ironic/funny/sad OpenCL is the last thing to come out of the treasure trove of HSA that's been going on.  I see CLOC but it's useless against complex applications that use the OpenCL runtime.

Where are we with OpenCL kernel + runtime support in ROCm?


---

## 评论 (25 条)

### 评论 #1 — gstoner (2016-09-05T23:49:31Z)

First  ROCm while it leverage capabilities form HSA Runtime Specification, we are moving beyond what HSA is capable off to better meet the need of HPC and Deep learning market.  We have  focused on other programing model first, HCC & HIP  since we had some key customer drive our direction.  Also since we have shipping drivers with OpenCL support today this is not as critical as you make it out.

Where we are on OpenCL on ROCm,  we had a version that running internally  via the old LLVM to HSAIL, HSAIL Finalizer to SC compiler (SC is our last big binary blob we are removing in ROCm 1.3).  Instead of releasing this we going to release OpenCL on ROCm only on the new Native GCN ISA Code generator based on LLVM.

The team is busy working on this and  the first release will be post ROCm 1.3

Please keep your comment professional on this site.

On Sep 5, 2016, at 7:09 AM, nevion <notifications@github.com<mailto:notifications@github.com>> wrote:

I see #12https://github.com/RadeonOpenCompute/ROCm/issues/12 - but this topic did not lay out OpenCL support - Ben Sander in comments @ http://gpuopen.com/rocm-do-you-speaka-my-language/ says OpenCL is soon, but this was May 5th (4 months ago from this issue).

I think it's pretty ironic/funny/sad OpenCL is the last thing to come out of the treasure trove of HSA that's been going on. I see CLOC but it's useless against complex applications that use the OpenCL runtime.

Where are we with OpenCL kernel + runtime support in ROCm?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/30, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuShfZiyRdcTTcF_y-iHNA3MQHBgiks5qnAZjgaJpZM4J1Azo.


---

### 评论 #2 — nevion (2016-09-06T09:30:58Z)

@gstoner I am being professional and here to help as well as meet my own needs (which should also benefit AMD)

The OpenCL implementation on catalyst doesn't function on the polaris arch, and doesn't _really_ have multi-GPU support (bugs where it hurts performance greatly and generates incorrect results, not even talking about p2p dma) - cryptominers found that out first but I've acked it in my own work. Further, it's not exactly the best driver around, and in the interim (really for 1 year +) it seems to be a dead driver/stack, understandably so with AMD GPUPRO and ROCm.  I guess there may be OpenCL support on GPUPRO which is mutually exclusive for now with ROCm...hm - I believe I had some trouble trying that out the other day with some unsupported pcie ids, will update on that but it's definitely a post to the new amd ML on freedesktop.

I do think it's pretty critical to get OpenCL here, all the people who wanted to keep things portable and didn't use CUDA wrote in OpenCL... so it's these same people you are not yet [currently] supporting but are a large part of your target audience - I know many of these types professionally and they're going to collectively wtf when they learn the current state of ROCm (which along with HSA took quite some time to understand).  It is truth that CLOC is useless for applications using the OpenCL runtime - no ifs, ands, or buts about it - I can't use or rebase on it in any modest OpenCL using application.  I can see why the big money from your customer went to making something close to CUDA work immediately but I know several small and large companies who either have OpenCL investments or choose to go that path already or in future that this presents a a problem to, and the money should still be pretty serious business as well as a gateway to getting AMD parts where NVidia parts used to be used - unfortunately many of the OpenCL projects I know of still are on top of team green's hardware, despite their level of OpenCL support.

Post 1.3 sounds like maybe 1.4 at best which sounds like well into 2017 - is there no re-prioritization that can be done at this point?  Perhaps the internal library in the interm that still leans on the HSAIL/SC compiler ontop of current or old LLVM?  I take it this is what the AMD GPUPRO stack is doing?

And related - how's progress doing on 1.3 - is that something that we should be seeing in Sept/October or in 2016?

-Jason


---

### 评论 #3 — gstoner (2016-09-06T13:15:03Z)

The current driver which support OpenCL which is not catalyst based that also supports RX480  that support Linux  this is 16.30.  This currently only supports Ubuntu 16.04, and 14.04 http://support.amd.com/en-us/kb-articles/Pages/AMD-Radeon-GPU-PRO-Linux-Beta-Driver–Release-Notes.aspxhttp://support.amd.com/en-us/kb-articles/Pages/AMD-Radeon-GPU-PRO-Linux-Beta-Driver%E2%80%93Release-Notes.aspx   Note this driver uses the same base AMDGPU kernel driver as ROCm ( We also use KFD beyond this)  with the HSAIL/SC compiler for OpenCL compilation.   Again it is not Catalyst based.

CLOC was developed by AMD Research,  honestly for those who take the time it very powerful tool on APU.  But it is not for those who want to leverage the OpenCL Runtime API for Host Code integration since you have to learn a new API interface.  We have number of customer who used it in the past for specialized code and had some nice performance wins since it give you more control over HSA runtime api.  But it not for you who need to be 100% aligned with OpenCL Runtime API in your coding practice.

ROCm 1.3 is currently scheduled in  late Oct to Early November, as I stated before this is when we see RX480 support as well, aka Polaris.   The OpenCL team has dependencies on OpenCL 1.3 so it needs to come out first,  First Release of OpenCL on ROCm will be before Christmas 2016.

Patience we working on this diligently,  we just want you to have solid experience with it when it comes out.

Software development of this class is not trivial, remember for OpenCL we have to run through Khronos Group conformance process as well if you want it to be conferment version you can use.

Greg

On Sep 6, 2016, at 4:30 AM, nevion <notifications@github.com<mailto:notifications@github.com>> wrote:

@gstonerhttps://github.com/gstoner I am being professional and here to help as well as meet my own needs (which should also benefit AMD)

The OpenCL implementation on catalyst doesn't function on the polaris arch, and doesn't support multi-GPU support (or at least has bugs where it hurts performance greatly) - cryptominers found that out first but I've acked it in my own work. Further, it's not exactly the best driver around, and in the interim (really for 1 year +) it seems to be a dead driver.

I do think it's pretty critical to get OpenCL here, all the people who wanted to keep things portable and didn't use CUDA wrote in OpenCL... so it's these same people you are not yet [currently] supporting but are a large part of your target audience - I know many of these types professionally and they're going to collectively wtf when they learn the current state of ROCm. It is truth that CLOC is useless for applications using the OpenCL runtime - no ifs, ands, or buts about it - I can't use or rebase on it in any modest OpenCL application.

Post 1.3 sounds like maybe 1.4 at best which sounds like well into 2017 - is there no re-prioritization that can be done at this point? Perhaps the internal library in the interm that still leans on the HSAIL/SC compiler ontop of current or old LLVM?

And related - how's progress doing on 1.3 - is that something that we should be seeing in Sept/October or in 2016?

-Jason

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/30#issuecomment-244898719, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuZjW8Sf8pWm0u9CvblKr9YhUJVNgks5qnTLSgaJpZM4J1Azo.


---

### 评论 #4 — nevion (2016-09-06T17:10:09Z)

@gstoner 

FYI I edit my messages quite a bit so it is best you reply on github or at least reply to the post there so you see changes prior to reply.  I touched or clarified on a few of the topics you replied with.

You've restated CLOC and what it does but realize I never said it was a bad tool - just as you restarted, it doesn't work for OpenCL runtime using code... which is basically all code other than CUDA, at least in industry - it's only in that context I challenged it's applicability. For APUs it looks pretty nice but the HSA runtime or OpenCL runtime looks like a necessity for effective memory transfers to GPUs - at least this seems to be the case if you use SNACK.

Learning another API is not necessarily the issue, it's existing code/investments.  And I also want to track rocm's performance publicly, along with gpupro and team green's CUDA/OpenCL implementations - but I've got no way to do that now from what I can tell - unless arrayfire will support HSA/HIP - also a pretty big undertaking beyond what I can invest currently.  Said tests would be at Phoronix to help developers see the true (or truer) performance differences between the hardwares and driver stacks in-line with their capabilities - I've not come across other efforts to show this kind of data.

As for conformance tests, since you are doing this FOSSY, I'd rather see functional pieces starting in the near term so we can catch issues on it and iterate, rather than the big semi-annual release done previously.  Basically like POCL, beignet etc - you're allowed to iterate now and don't have to start being a perfectly polished conforming piece.  There may be parts I/others could contribute to in that process as long as they didn't cross into the closed source portion.

Remember I'm extremely happy you provide me/the public with information - this isn't available elsewhere - I won't hold you to it with a knife to dates but remember we've had patience with OpenCL support as a technology in general since it's inception - and it's frustrating to see all the disparate parts working... just not together, with no clear outline of current state or milestones that lead to expectations.  Maybe since you guys are trying to do this as a FOSS project - post public feature matrix of what can be done and milestones/release schedule so we can track along?


---

### 评论 #5 — gstoner (2016-09-06T21:38:03Z)

I want to thank you for your inputs,  your request for OpenCL on ROCm has been registered.   Since we have a base of commercial customer who want better then the current open source OpenCL distributions quality and capability for our  first release,  we need to balance level of quality, performance  and conformance on the first release.  We will be releasing it  before GA.

I recommend you to look at for benchmark so you can track performance with the three benchmarks  They Support OpenCL, CUDA and HIP.

https://github.com/ekondis/mixbench
https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP-Examples/tree/master/GPU-STREAM
https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP-Examples/tree/master/rodinia_3.0

On Sep 6, 2016, at 12:10 PM, nevion <notifications@github.com<mailto:notifications@github.com>> wrote:

@gstonerhttps://github.com/gstoner

FYI I edit my messages quite a bit so it is best you reply on github or at least reply to the post there so you see changes prior to reply. I touched or clarified on a few of the topics you replied with.

You've restated CLOC and what it does but realize I never said it was a bad tool - just as you restarted, it doesn't work for OpenCL runtime using code... which is basically all code other than CUDA, at least in industry - it's only in that context I challenged it's applicability. For APUs it looks pretty nice but the HSA runtime or OpenCL runtime looks like a necessity for effective memory transfers to GPUs - at least this seems to be the case if you use SNACK.

Learning another API is not necessarily the issue, it's existing code/investments. And I also want to track rocm's performance publicly, along with gpupro and team green's CUDA/OpenCL implementations - but I've got no way to do that now from what I can tell - unless arrayfire will support HSA/HIP - also a pretty big undertaking beyond what I can invest currently. Said tests would be at Phoronix to help developers see the true (or truer) performance differences between the hardwares and driver stacks in-line with their capabilities - I've not come across other efforts to show this kind of data.

As for conformance tests, since you are doing this FOSSY, I'd rather see functional pieces starting in the near term so we can catch issues on it and iterate, rather than the big semi-annual release done previously. Basically like POCL, beignet etc - you're allowed to iterate now and don't have to start being a perfectly polished conforming piece. There may be parts I/others could contribute to in that process as long as they didn't cross into the closed source portion.

Remember I'm extremely happy you provide me/the public with information - this isn't available elsewhere - I won't hold you to it with a knife to dates but remember we've had patience with OpenCL support as a technology in general since it's inception - and it's frustrating to see all the disparate parts working... just not together, with no clear outline of current state or milestones that lead to expectations. Maybe since you guys are trying to do this as a FOSS project - post public feature matrix of what can be done and milestones/release schedule so we can track along?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/30#issuecomment-245020384, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuaeLcutQHlcTUn7qQY50PBLUDNVaks5qnZ5ygaJpZM4J1Azo.


---

### 评论 #6 — nevion (2016-09-06T22:23:38Z)

@gstoner  What does releasing before general availability  mean? I wasn't able to understand

Also, after initial release - do you mean to imply that things will be a bit more open on development?  E.g. I submit a pull-request and you merge it and have it where you guys are doing development?

Thanks for the links to the benchmarks - I might add additional benchmarks for that after I get my initial release of the arrayfire CUDA/OpenCL tests working - still getting slowed down with Ubuntu support only there since I dont' have enough machines (my desktop runs OpenSUSE and I'm not willing to dual boot or keep switching GPUs on it since.. it's my everyday environment)   Anyway, I looked over each the tests of them just now.

With arrayfire based tests I'll be running something like 60 different tests across 32 and 64 bit floating point and integer types, perhaps also 16bit floats/ints.  I'm trying to not leave any stone unturned in the typical/atypical GPU engineers toolbox - there will be many opportunities for an implementation (hw + sw) to shine and falter on simple individual tests - and the code+work parameters are already very highly optimized and put in production. Where applicable we'll see a comparison  libraries like CUBLAS vs clBlas too since arrayfire builds on these.  So the testing is to be exhaustive over a large domain, high performance with real high-performance production code with "fair" comparisons being a goal as well, not just a stress testing code.


---

### 评论 #7 — gstoner (2016-09-07T03:07:25Z)

GA is old term when we see the product is no longer Beta Quality but ready for general release to customers to go into production.

Do you work for Arrayfire,  Since we working with them via the libraries team that works for me.

greg

On Sep 6, 2016, at 6:23 PM, nevion <notifications@github.com<mailto:notifications@github.com>> wrote:

@gstonerhttps://github.com/gstoner What does releasing before general availability mean? I wasn't able to understand

Also, after initial release - do you mean to imply that things will be a bit more open on development? E.g. I submit a pull-request and you merge it and have it where you guys are doing development?

Thanks for the links to the benchmarks - I might add additional benchmarks for that after I get my initial release of the arrayfire CUDA/OpenCL tests working - still getting slowed down with Ubuntu support only there since I dont' have enough machines (my desktop runs OpenSUSE and I'm not willing to dual boot or keep switching GPUs on it since.. it's my everyday environment) Anyway, I looked over each the tests of them just now.

With arrayfire based tests I'll be running something like 60 different tests across 32 and 64 bit floating point and integer types, perhaps also 16bit floats/ints. I'm trying to not leave any stone unturned in the typical/atypical GPU engineers toolbox - there will be many opportunities for an implementation (hw + sw) to shine and falter on simple individual tests - and the code+work parameters are already very highly optimized and put in production. Where applicable we'll see a comparison libraries like CUBLAS vs clBlas too since arrayfire builds on these. So the testing is to be exhaustive over a large domain, high performance with real high-performance production code with "fair" comparisons being a goal as well, not just a stress testing code.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/30#issuecomment-245114954, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuWQ9hQqKhlQ9Azgxj3-w4_fDLxIkks5qnefqgaJpZM4J1Azo.


---

### 评论 #8 — nevion (2016-09-07T03:37:41Z)

@gstoner still lost on what the means for releasing before GA - does this mean you're releasing to your customer before GA or Releasing source on github before GA?

I don't work for or have any affiliation with Arrayfire, though I've talked with them about doing this testing a few months ago and patching up some of their existing stuff towards my goals.


---

### 评论 #9 — gstoner (2016-09-07T04:09:33Z)

When you do production software, there is number of development milestone 

Developer Preview, ALPHA, BETA, Release Candidate,  General Availability.   Each release goes rigorous Q/A process , all of these milestones we pass through to a GA release branch, especially on pre 1.0 products. 

First drop of OpenCL will be a  Developer Preview and will be OpenSource 

Here is good overview Software release cycles https://en.wikipedia.org/wiki/Software_release_life_cycle  


---

### 评论 #10 — oscarbg (2016-10-05T08:25:10Z)

Just some  questions seems from notes that GPUPRO Linux Polaris driver supports only OpenCL1.2?
Any roadmap on supporting OpenCL 2.0 on Polaris on Linux?
it's sad now that even Intel has a OpenCL 2.0 Linux driver for Skylake iGPUs..
Also Intel has a OpenCL 2.1 preview driver since June and from gfxbench report seems drivers are in beta form for Kabylake iGPUs having 2.1..
Any beta info on OpenCL 2.1 drivers on AMD GPUs? some release on 2016?
mainly interested on using SPIR-V for OpenCL..
also hope that AMD Vega GPU release (heard rumors..) comes with ROCM support and OpenCL 2.x on Linux from day 1..


---

### 评论 #11 — gstoner (2016-10-05T14:13:36Z)

What do you need in OpenCL 2.0 that is so compelling?     Does Intel have OpenCL 2.0 on Xeon E5 v3 Hawell and Xeon E5 v4 Broadwell.   How about Xeon Phi, Night Landing?

Is SPIR_V for Compiler, if so you have much better path now we upstream our compiler in LLVM and built standardized loader and ABI for compiler.

On Oct 5, 2016, at 3:25 AM, Oscar Barenys <notifications@github.com<mailto:notifications@github.com>> wrote:

Just some questions seems from notes that GPUPRO Linux Polaris driver supports only OpenCL1.2?
Any roadmap on supporting OpenCL 2.0 on Polaris on Linux?
it's sad now that even Intel has a OpenCL 2.0 Linux driver for Skylake iGPUs..
Also Intel has a OpenCL 2.1 preview driver since June and from gfxbench report seems drivers are in beta form for Kabylake iGPUs having 2.1..
Any beta info on OpenCL 2.1 drivers on AMD GPUs? some release on 2016?
mainly interested on using SPIR-V for OpenCL..
also hope that AMD Vega GPU release (heard rumors..) comes with ROCM support and OpenCL 2.x on Linux from day 1..

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/30#issuecomment-251612847, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuWifc-TEfiqPonIhmzNh_fdSNWPgks5qw17ngaJpZM4J1Azo.


---

### 评论 #12 — nevion (2016-10-05T17:35:45Z)

To clarify the first part of @gstoner 's message: http://registrationcenter-download.intel.com/akdlm/irc_nas/9418/intel-opencl-r2.0-release-notes-external.pdf

Looks like they got 2.1 with SPIR-V on windows though (see section 2.2).  No telling when linux will be so blessed from them, even for CPU only target, as is their tradition.

I'm more for 2.1 than 2.0 (for C++ support chiefly) - we definitely have a better path forward with AMD/ROCm's tool chain - there's no question, but critically it's still vaporware until it's not - an OpenCL long time tradition.  One can't yet plan or execute a project around the future support.

There's alot of things to be sad of in the state of things and especially confusion towards @oscarbg 's post, but @gstoner you seem to be frustrated in your replies as well.  Take some relief in that once you lay the golden egg, all us frustrated OCL developers will finally have a release to the stifling confusion we're in as well. Maybe that'll start a chain reaction of getting everyone's act together too; but at least there will be a platform that did it right.


---

### 评论 #13 — gstoner (2016-10-05T19:36:48Z)

Guys, we have been shipping OpenCL 2.0 on Windows for while now.  Honestly we have very few people really using it.  A bulk of our user are still using OpenCl 1.2 so they can support Mac OS X, NVIDIA, Intel and our hardware with there application.  Through in FPGA that support 1.0 and 1.1 and  when you build that matrix of Hardware and OS support it interesting view world of OpenCL.

When I look at OpenCL 2.0, here are the good features
- C11 Atomics
- Global Address Spaces
- Shared Virtual Memory
- Images - improved support

These are features that need more baking in CL group
- clCreateCommandQueueWithProperties obuscating clCreateCommandQueue
- PIPES, which need spec overhaul
- Dynamic Parallelism need more time to bake as feature

We were building SPIR 1.2 in our driver Windows and Linux for last few years,  only  3 companies ever used it.   AMD, Codeplay and Continuum IO.

We also had C++ kernel language in our driver since 2012 which was hardly used.  http://developer.amd.com/community/blog/2012/05/21/opencl-1-2-and-c-static-kernel-language-now-available/

Greg

On Oct 5, 2016, at 12:35 PM, nevion <notifications@github.com<mailto:notifications@github.com>> wrote:

To clarify the first part of @gstonerhttps://github.com/gstoner 's message: http://registrationcenter-download.intel.com/akdlm/irc_nas/9418/intel-opencl-r2.0-release-notes-external.pdf

Looks like they got 2.1 with SPIR-V on windows though (see section 2.2). No telling when linux will be so blessed from them, even for CPU only target, as is their tradition.

I'm more for 2.1 than 2.0 (for C++ support chiefly) - we definitely have a better path forward with AMD/ROCm's tool chain - there's no question, but critically it's still vaporware until it's not - an OpenCL long time tradition. One can't yet plan or execute a project around the future support.

There's alot of things to be sad of in the state of things and especially confusion towards @oscarbghttps://github.com/oscarbg 's post, but @gstonerhttps://github.com/gstoner you seem to be frustrated in your replies as well. Take some relief in that once you lay the golden egg, all us frustrated OCL developers will finally have a release to the stifling confusion we're in as well. Maybe that'll start a chain reaction of getting everyone's act together too; but at least there will be a platform that did it right.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/30#issuecomment-251744150, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8Due__viXdMPvQagvQAi1JKoqPb7oLks5qw9_ygaJpZM4J1Azo.


---

### 评论 #14 — nevion (2016-10-05T20:30:14Z)

@gstoner yes, I used the C++ kernel language, professionally, a few times.  It solved some problems but had a bunch of other issues too -namely around memory spaces for pointer passing leading to copy paste definitions to handle variations on input.  Worth noting it never got 2.0 support.  I'll take 2.1 proper-er C++ support over that but AMD was very early showing it could be done / had it working.  I suspect there are more users of (early) SPIR than you know of because it's used to prevent issues in distributing source, but it only works in limited platforms - I know a few more people who've tried or used these things.

Surprised pipes are in need of overhaul - seemed to basically unify Altera and Xillin'x channels, but maybe I missed something as I've not used any of the 3.  Also looking forward to more atomic operations and unified memory spaces (no combinatoric tagging of pointers in subroutines).  Images have been a mixed bag for speed, as an image processing/matrix processing person.

I'm sure you know but the OpenCL BoF conferences show a matrix of all the vendors and where they are at - confusion city, couldn't be in more disarray if they tried, even per vendor (like intel).


---

### 评论 #15 — gstoner (2016-10-05T21:22:45Z)

OpenCL 1.2 crippled C++ kernel language.

greg
On Oct 5, 2016, at 3:30 PM, nevion <notifications@github.com<mailto:notifications@github.com>> wrote:

@gstonerhttps://github.com/gstoner yes, I used the kernel language, professionally a few times. It solved some problems but had a bunch of other issues too -namely around memory spaces for pointer passing leading to copy paste definitions to handle variations on input. Worth noting it never got 2.0 support. I'll take 2.1 proper-er C++ support over that but AMD was very early showing it could be done / had it working. I suspect there are more users of SPIR than you know of because it's used to prevent issues in distributing source, but it only works in limited platforms - I know a few more people who've tried or used these things.

Surprised pipes are in need of overhaul - seemed to basically unify Altera and Xillin'x channels, but maybe I missed something as I've not used any of the 3. Also looking forward to more atomic operations and unified memory spaces (no combinatoric tagging of pointers in subroutines). Images have been a mixed bag for speed, as an image processing/matrix processing person.

I'm sure you know but the OpenCL BoF conferences show a matrix of all the vendors and where they are at - confusion city, couldn't be in more disarray if they tried, even per vendor (like intel).

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/30#issuecomment-251790294, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuVAuJoK7I9DItjVIs4-20afeI0JOks5qxAjWgaJpZM4J1Azo.


---

### 评论 #16 — VincentSC (2016-10-17T12:03:28Z)

At StreamComputing we made a OpenCL 1.2 to 1.1 wrapper to cope with NVidia's 1.1 in both the host-code and the kernels. We could extend that project for making 2.0 projects to be backwards compatible with 1.1/1.2.


---

### 评论 #17 — jstefanop (2016-12-01T20:46:00Z)

@gstoner So where are we with OpenCL support on ROCm now that 1.3 is out? Trying to get a test system up, but don't want to waste time if my Polaris hardware can't run OpenCL apps on ROCm in its current form. 

---

### 评论 #18 — jedwards-AMD (2016-12-01T20:57:47Z)

OpenCL on ROCm is not supported on 1.3. A developer preview should be released later this year.

---

### 评论 #19 — jstefanop (2016-12-01T21:27:21Z)

@jedwards-AMD In terms of porting OpenCL kernels to run on ROCm...what kind of endeavor would this entail? Would there even be any advantage to doing this? I know nvidia has a tool to port over CUDA code to their "version" of ROCm...is there something similar for ROCm for OpenCL code?

---

### 评论 #20 — nevion (2016-12-01T22:13:57Z)

sorry for the wandering discussion but @jstefanop , what is NVidia's "version" of ROCm - and they need to port CUDA to run on it...?

Also, I think once the OpenCL runtime is in place, besides the kernel compiler, there shouldn't be any porting going on.  There's an inbetween state without the runtime and I believe that's where we're at and have been for a while, but I could be wrong.

---

### 评论 #21 — jedwards-AMD (2016-12-01T22:39:13Z)

You can take a look at CLOC if you want to do 'porting' to the HSA runtime. This is the link to it: https://github.com/HSAFoundation/CLOC
.
We actually distribute the CLOC tools from the rocm repository; you can install them with 'sudo apt-get install amdcloc'. However, if you want to use OpenCL on ROCm directly porting shouldn't be required.

---

### 评论 #22 — jstefanop (2016-12-02T17:25:40Z)

>However, if you want to use OpenCL on ROCm directly porting shouldn't be required.

Wait I thought you just said OpenCL is not supported on ROCm yet. Or do you mean ROCm will automatically compile and run OpenCL based code without needing OpenCL libraries etc?

---

### 评论 #23 — nevion (2016-12-02T18:12:20Z)

@jstefanop That's in the future, _not_ _now_ - you may be able to test without code modifications (that is, the OpenCL runtime...) something before the end of the year though December being December, I suspect it's right at the end (christmas/new years present) or slips into January.  If you use the HSA runtime, you can compile OpenCL kernels _now_, but you need to use HSA runtime rather than OpenCL runtime to invoke them.

Also, again - what is NVidia's "version" of ROCm - and they need to port CUDA to run on it...?

---

### 评论 #24 — jstefanop (2016-12-02T18:58:39Z)

@nevion Ok, so in other words use the CLOC tool to convert OpenCL kernels to HSA code object file, and then use the HSA runtime to run the program? Would the HSA runtime offer any speedup over running the kernel via normal OpenCL APIs/drivers?

And I mean the CUDA HIP tools where you can port CUDA to HIP and then run on either HCVV or NVCC

---

### 评论 #25 — nevion (2016-12-02T21:09:43Z)

@jstefanop it _could_ - OpenCL doesn't allow you to persist memory, it's not in the execution model - HSA I believe does.  Now how to practically get at that, IDK.  I've looked at the API with an OpenCL lens and it looks familiar but, especially in terms of OpenCL CLOC compiler, I'm not sure at all how you'd exploit something like that.  Other than persisting of memory to remove global memory transfers or local memory configurations, I don't think there could be any performance bumps than that.  And that's just theory, we have nothing to benchmark/see the performance of right now in terms of comparisons.

HIP kernels can run on nvcc / hcvv - but the CUDA runtime and the HIP runtime have alot of regexes at the very least - believe me, NVidia doesn't want something like HIP existing and it's not an effort they bless is my bet.

---
