# Which devices are even supported? (HIP/ROCm)

> **Issue #1714**
> **状态**: closed
> **创建时间**: 2022-03-25T00:51:42Z
> **更新时间**: 2024-02-13T19:20:22Z
> **关闭时间**: 2024-02-13T19:20:22Z
> **作者**: samuelpmish
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1714

## 描述

I'm a long-time CUDA developer looking to explore ROCm and HIP development, but finding out which hardware even supports these tools is harder than it needs to be. 

Let's see... this repo's readme has a section on "Supported GPUs":

![Screenshot from 2022-03-24 17-23-25](https://user-images.githubusercontent.com/16393433/160030961-ffbcab77-76db-4194-97eb-6360219db7e5.png)

Okay, "extends" implies it supports other GPUs too-- which ones? Maybe the FAQ has more info:

![Screenshot from 2022-03-24 17-26-48](https://user-images.githubusercontent.com/16393433/160031097-ad6ec8d7-7830-4f66-86c3-3f6607bd3a9d.png)

Nope, it'll tell me all of the NVIDIA cards that work, but none of the AMD ones apparently. Okay, I guess I'll look at their HIP Programming Guide pdf. Skimming the table of contents, no indication of "supported GPUs"-- it's a 100 page document, surely they don't expect a user to read all of that to just see if a card works or not? Let's try searching instead:

CTRL+F "supported GPU": zero results
CTRL+F "supported platform": zero results
CTRL+F "supported device": zero results

okay..

CTRL+F "supported": 87 results, great. Going through them one by one, I guess. First 76 results unrelated, 77 is the closest thing I can find:

![Screenshot from 2022-03-24 17-35-47](https://user-images.githubusercontent.com/16393433/160031853-cd0a49a9-eda4-47b0-94f9-9890ee60cb5f.png)

This sounds sort of related to what I'm looking for, although it's deprecated, so the options for `gpu_arch` are probably out of date. I would like to know what HIP _currently_ supports, let's look at the option `--offload-arch=<target>` documentation:

![Screenshot from 2022-03-24 17-39-49](https://user-images.githubusercontent.com/16393433/160032193-0e1ce844-85e5-455d-87da-3206c017bc55.png)

Okay, the documentation doesn't actually explain anything at all, it just links to something. I might have wasted a lot of my time getting here, but finally, a link with an answer to my simple question:

https://clang.llvm.org/docs/ClangOffloadBundlerFileFormat.html#target-id

Ah, of course-- the link is also broken. Maybe try:

https://clang.llvm.org/docs/ClangOffloadBundlerFileFormat.html

No, also broken.

Forgive the sarcastic tone of this issue, but am I an idiot or is this documentation just abysmal?

If I want to know which NVIDIA GPUs support CUDA, and which features, all of that information is readily available in many places, e.g. 

https://developer.nvidia.com/cuda-gpus

I've been looking for an hour and found nothing official about the AMD support for HIP, so I quit. Hopefully creating a github issue will lead to an answer to this trivial question.

---

## 评论 (82 条)

### 评论 #1 — Rmalavally (2022-03-25T01:00:38Z)

@samuelpmish We are sorry you were unable to find the information you need on the documentation portal. Please refer to the ROCm Installation Guide and the latest version of the ROCm Release Notes (v5.0), and let us know if they were helpful. 

If there's specific information you need, please let me know, and I am happy to help. 

AMD ROCm Documentation Team

---

### 评论 #2 — samuelpmish (2022-03-25T02:34:26Z)

> Please refer to the ROCm Installation Guide ...

https://docs.amd.com/bundle/ROCm_Installation_Guidev5.0/page/Overview_of_ROCm_Installation_Methods.html

this does not contain any information about which devices support ROCm or HIP.

> and the latest version of the ROCm Release Notes (v5.0)

https://docs.amd.com/bundle/ROCm_Release_Notes_v5.0/page/About_This_Document.html

Thank you, this document _does_ indicate that there are seven GPUs that support ROCm: Instinct (MI50, MI60, MI100, MI200) and Pro (VII, W6800, V620). 

Does this imply that all other AMD GPUs do not support ROCm? All of the products indicated above have multi-thousand-dollar price tags and/or are not even being manufactured.

> If there's specific information you need, please let me know, and I am happy to help.

The original question was specific: which AMD GPUs support ROCm and/or HIP?

---

### 评论 #3 — ffleader1 (2022-03-25T19:30:06Z)

> > Please refer to the ROCm Installation Guide ...
> 
> https://docs.amd.com/bundle/ROCm_Installation_Guidev5.0/page/Overview_of_ROCm_Installation_Methods.html
> 
> this does not contain any information about which devices support ROCm or HIP.
> 
> > and the latest version of the ROCm Release Notes (v5.0)
> 
> https://docs.amd.com/bundle/ROCm_Release_Notes_v5.0/page/About_This_Document.html
> 
> Thank you, this document _does_ indicate that there are seven GPUs that support ROCm: Instinct (MI50, MI60, MI100, MI200) and Pro (VII, W6800, V620).
> 
> Does this imply that all other AMD GPUs do not support ROCm? All of the products indicated above have multi-thousand-dollar price tags and/or are not even being manufactured.
> 
> > If there's specific information you need, please let me know, and I am happy to help.
> 
> The original question was specific: which AMD GPUs support ROCm and/or HIP?

I tried AMD Vega 64 and it works so at least there is that. I do want to figure out if Navi 21 is supported, then what prevents Navi 22 from getting supported? Does something like 6700 XT get supported, even unofficially?

---

### 评论 #4 — mark-decker (2022-03-28T02:54:19Z)

The list of supported GPUs is also found [here](https://docs.amd.com/bundle/ROCm_Installation_Guidev5.0/page/Prerequisite_Actions.html) in the prerequisite actions document.  Even here though it does not specify if other GPUs based on the same architecture are supported.

---

### 评论 #5 — ffleader1 (2022-03-28T03:07:43Z)

> The list of supported GPUs is also found [here](https://docs.amd.com/bundle/ROCm_Installation_Guidev5.0/page/Prerequisite_Actions.html) in the prerequisite actions document. Even here though it does not specify if other GPUs based on the same architecture are supported.

It does not even list all supported GPU. I have a Vega 64 and I can confirm it works 

---

### 评论 #6 — bernharl (2022-03-28T07:07:31Z)

It works on my RX 6800 XT now. AMD should really add a "unsupported but works" category to their list of supported devices.

---

### 评论 #7 — ffleader1 (2022-03-28T07:09:28Z)

> It works on my RX 6800 XT now. AMD should really add a "unsupported but works" category to their list of supported devices.

Yeah I think so too. The point of a document is to make thing clear. It seems AMD is trying so hard to do the exact opposite. It seems the company really do not want "casual" radeon users to know that their card can work for some reason.

Anyway, does that mean a 6800 non XT should work to, cuz I am thinking of getting one.

---

### 评论 #8 — ye-luo (2022-03-28T13:19:30Z)

Here is my understanding. ROCm is a software suite with compilers, runtime libraries, accelerated numerical libraries, AI related libraries and more. "Support" simply means given hardware are validated at AMD with the whole ROCm stack.

a) Technically the compiler likely works for all the GPUs being listed https://llvm.org/docs/AMDGPUUsage.html. This means compiling/linking not necessarily running the code.
b) The runtime library depends on the GPU driver and hardware compatibility.
c) accelerated numerical libraries, AI related libraries depend on if binaries shipped by ROCm contains the needed GPU architecture. It is very likely nothing beyond the "support" list works but you are still free to compile from source code to the needed architecture.

Users may just need a subset of the stack for their purpose. That is why some ROCm "unsupported" hardware works in limited scopes. Since the scope is on per-user basis, this is not meaningful to list "unsupported but works".

---

### 评论 #9 — samuelpmish (2022-03-28T20:30:08Z)

Thanks to @mark-decker and @ye-luo for linking some relevant documentation to shed light on this issue.

I still wish someone official would weigh in, rather than having us speculate about the reality of what works and what doesn't. I agree that "unsupported but works" is sort of a meaningless idea, perhaps "untested" would be more accurate. If it is the case that  some of the libraries in the stack do not support certain cards, then AMD should at least communicate that, rather than being ambiguous about it. 

e.g. (NOTE: this table is for illustration only, _it does not reflect what actually works and what doesn't_)

| GPU | hipSparse | hipSolver | rocFFT | rocBLAS | rocThrust |
| - | - | - | - | - | - |
| gfx801 |:heavy_check_mark:  | :x: | :heavy_check_mark: |:x:  | :x: | 
| gfx802 |:x:  |:x:  | :grey_question: | :heavy_check_mark: | :x: | 
| gfx803 | :grey_question: | :grey_question: |:heavy_check_mark:  |:grey_question:  |:x:  | 
| gfx1010 | :heavy_check_mark: | :heavy_check_mark: |:grey_question:  |:grey_question:  | :heavy_check_mark: | 
| gfx1030 | :x: | :grey_question: |:heavy_check_mark:  |:grey_question:  | :heavy_check_mark: | 

:heavy_check_mark: : confirmed to work
:grey_question: : untested
:x: : not working

Something like the above needs to be front and center on the documentation, if it is the case that the library support is so limited.

---

### 评论 #10 — ffleader1 (2022-03-28T20:40:46Z)

> Thanks to @mark-decker and @ye-luo for linking some relevant documentation to shed light on this issue.
> 
> I still wish someone official would weigh in, rather than having us speculate about the reality of what works and what doesn't. I agree that "unsupported but works" is sort of a meaningless idea, perhaps "untested" would be more accurate. If it is the case that some of the libraries in the stack do not support certain cards, then AMD should at least communicate that, rather than being ambiguous about it.
> 
> e.g. (NOTE: this table is for illustration only, _it does not reflect what actually works and what doesn't_)
> 
> GPU	hipSparse	hipSolver	rocFFT	rocBLAS	rocThrust
> gfx801	✔️	❌	✔️	❌	❌
> gfx802	❌	❌	❔	✔️	❌
> gfx803	❔	❔	✔️	❔	❌
> gfx1010	✔️	✔️	❔	❔	✔️
> gfx1030	❌	❔	✔️	❔	✔️
> ✔️ : confirmed to work ❔ : untested ❌ : not working
> 
> Something like the above needs to be front and center on the documentation, if it is the case that the library support is so limited.

What more interesting to me is why gfx1030 works, but gfx 1031 does not? It was not the case with Polars. It was not the case with Vega. The cut down version works just fine.

It seems to me that AMD is trying so hard to limit Rocm tool for high-end/professional grade product. Meanwhile Nvidia has a 3060 with 12GB VRAM, bringing ML to everyone.

It is a shame really.

---

### 评论 #11 — Bengt (2022-03-29T00:34:28Z)

I think there is a distinction to be made between "working" and "supported". That is, a GPU might seemingly work, but has subtle bugs (e.g. correctness). AMD might choose not to be bothered with bug reports about older cards with this state (e.g. gfx803). I would suggest considering these cards working with known issues, yet being unsupported. On the other hand, as a prospective buyer I want to know, to which AMD commits some amount of attention. For example, the W6800 is currently supported, so if one buys that card today, one should reasonably expect to find any reported issues with it being honored on this issue tracker within its useful lifetime.

This consideration necessitates a fourth category:

||||
| -- | -- | -- |
| :heavy_check_mark:  | supported | issues being honored |
| :gear: | working | maybe with known issues |
| :grey_question: | untested | ... or not tested rigorously |
| :no_entry: | dysfunctional | tested and found broken |


---

### 评论 #12 — Bengt (2022-03-29T00:42:26Z)

Adding to the list of unhelpful information, there is also this two-year-old - ehm - gem of an outdated document to add confusion:

<https://github.com/ROCm/ROCm.github.io/blob/master/hardware.md>

---

### 评论 #13 — FCLC (2022-03-31T16:07:03Z)

> 

It's unfortunate, but official replies can be hard to come by at times, especially regarding support for hardware. 

A *small* subset of issues that received either vague or no official answers is  #1706 #1694 #1683 #1676  #1617 #1623 #1631 #1595 #1592 #1544 #1547 #1539  

When timelines have been given/set, they've been missed every time that I'm aware of. 

RDNA1 is nearly 3 years in market (launch was July 7 2019) but the workstation card still had no support in the stack. 

With the Frontier super computer now behind schedule with it's software stack, I'm expecting engineering resources that would be allocated to RDNA1-2 support to be redirected towards improving CDNA2. 

See https://insidehpc.com/2022/03/oak-ridge-frontier-exascale-to-deliver-full-user-operations-on-jan-1-2023-crusher-test-system-now-running-code/ for more information on the Frontier delay. 

---

### 评论 #14 — 642258387b (2022-04-01T01:13:02Z)

My graphics card is 6800xt and I tried to install rocm5.1 and pytorch, pytorch displays CUDA.is_ Available is true, but an error about HIP will be reported when running. However,there is no problem when I run the training in the packaged image in docker,. I don't know how to solve the problem and how to configure the pytorch in my local environment.

---

### 评论 #15 — ffleader1 (2022-04-01T02:22:31Z)

> My graphics card is 6800xt and I tried to install rocm5.1 and pytorch, pytorch displays CUDA.is_ Available is true, but an error about HIP will be reported when running. However,there is no problem when I run the training in the packaged image in docker,. I don't know how to solve the problem and how to configure the pytorch in my local environment.

What is the error? Nothing was shown to you?

---

### 评论 #16 — littlewu2508 (2022-04-01T04:28:06Z)

Actually the hip/clang compiler support many GPUs. When ROCm-4.3 released, I added `gfx1031` to source code of Tensile,  rocBLAS, rocFFT, MIOpen, etc. Although there are test failures, especially rocPRIM cannot compile the test suite, pytorch and tensorflow successfully run on RX 6700 XT. So I suggests the support range is actually not restricted to the officially supported chips.

With [help](https://github.com/ROCmSoftwarePlatform/Tensile/issues/1410) from ROCm developers, [navi22 enabled  rocBLAS](https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=f1dcb1e8ba4936959138ccf747400d0d54d87b26) is distributed on gentoo, and I expect gfx1031 on other packages can be more easily enabled.

---

### 评论 #17 — ffleader1 (2022-04-01T05:42:14Z)

> Actually the hip/clang compiler support many GPUs. When ROCm-4.3 released, I added `gfx1031` to source code of Tensile, rocBLAS, rocFFT, MIOpen, etc. Although there are test failures, especially rocPRIM cannot compile the test suite, pytorch and tensorflow successfully run on RX 6700 XT. So I suggests the support range is actually not restricted to the officially supported chips.
> 
> With [help](https://github.com/ROCmSoftwarePlatform/Tensile/issues/1410) from ROCm developers, [navi22 enabled rocBLAS](https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=f1dcb1e8ba4936959138ccf747400d0d54d87b26) is distributed on gentoo, and I expect gfx1031 on other packages can be more easily enabled.

Well yes but the problem is the amount of tinkering required to make, say 6700 XT, works maybe a lot. Assuming I am a casual student who do gaming on Windows, but want to dabble in to ML. Not only I have to install a completely new OS, I need to figure out the many tricks of Ubuntu/Linux to install 6700 XT and make it run pytorch... Or I can just get a Nvidia card, and it "just works" on Windows. Now if you think about it, Rocm user-friendliness is like 10 steps behind Nvidia.

Is there any "it just work" guide for installing rocm to run tf/pytorch on 6700 XT? If not, that is a huge problem.

---

### 评论 #18 — wsippel (2022-04-03T11:45:31Z)

Yeah, ROCm absolutely needs a proper support matrix and a strong public commitment from AMD to get as many GPUs supported as possible, as quickly as possible.. According to two AMD engineers, ROCm actually supports pretty much every GPU since Polaris to varying degrees. rocm-opencl for example should work on everything since Vega, while HIP should work on every GPU since Polaris (but has apparently seen very little testing on older chips). It's also a chicken-and-egg problem, there's really not much software to test with in the first place, and the limited official support makes ROCm not very attractive to developers. Looking at the seven officially supported cards would do little to convince most devs to target ROCm.

---

### 评论 #19 — ffleader1 (2022-04-03T19:50:06Z)

> Yeah, ROCm absolutely needs a proper support matrix and a strong public commitment from AMD to get as many GPUs supported as possible, as quickly as possible.. According to two AMD engineers, ROCm actually supports pretty much every GPU since Polaris to varying degrees. rocm-opencl for example should work on everything since Vega, while HIP should work on every GPU since Polaris (but has apparently seen very little testing on older chips). It's also a chicken-and-egg problem, there's really not much software to test with in the first place, and the limited official support makes ROCm not very attractive to developers. Looking at the seven officially supported cards would do little to convince most devs to target ROCm.

Well if someone has to take a bet, it has to be AMD. Can't win a war if you do not burn some money. As a programmer myself, I would say AMD is hesitant to burn more R&D budget on Rocm that they has already did, thus creating this unfinished product called Rocm that works with every card, but 50% of the cards, and every time, but 50% of the time.

Goes big or goes home does apply here, and I believe Intel is very much willing to chew away this market from Nvidia also.

My opinion means shit of course, but maybe expanding their budgets on Rocm, both technical and marketing. Hide more programmers, sure, but also gives out free/discounted AMD GPUs to academy institutions, create competitions like BETA ML with AMD or something to both hunt bugs and make progress with Rocm. More people in, more data for dev to work with GPUs, more polished product and so on... And also please freaking make Rocm works on Windows. Treat Rocm becomes a product, not a tool.

Well, just my two cents of BSing. I do want to support AMD/Rocm, but I would love not to pay scalper money to get a lack luster ML GPU that does not event "officially" supported on paper.

---

### 评论 #20 — Niko-1118 (2022-04-08T01:40:27Z)

> > My graphics card is 6800xt and I tried to install rocm5.1 and pytorch, pytorch displays CUDA.is_ Available is true, but an error about HIP will be reported when running. However,there is no problem when I run the training in the packaged image in docker,. I don't know how to solve the problem and how to configure the pytorch in my local environment.
> 
> What is the error? Nothing was shown to you?

After exploring for a few days, I think I know the reason. According to the official website documentation, I know i need to download the source code of torch and compile a version of torch suitable for my hardware in my local environment. I failed this step because I am a linux novice, but It doesn't matter, it's more convenient to use docker images, and local deployment is just because of my obsessive-compulsive disorder.finally thank you。

---

### 评论 #21 — dbenedb (2022-04-24T13:31:15Z)

> (hardware/software table)
> 
> Something like the above needs to be front and center on the documentation, if it is the case that the library support is so limited.

Couldn't agree more. Also: clear categories for HPC, workstation/prosumer and consumer hardware.

---

### 评论 #22 — emirkmo (2022-05-06T08:21:14Z)

> It works on my RX 6800 XT now. AMD should really add a "unsupported but works" category to their list of supported devices.

The box of RX 6800XT literally advertises something that’s not officially supported. Why is there no word about whether it’s officially supported?

---

### 评论 #23 — saadrahim (2022-05-17T02:13:58Z)

Navi1x GPU support will not be available in ROCm. My apologies for the delays in confirming this.

AMD GPU support is based on ISA architectures. We officially support two Navi21 GPUs that use the gfx1030 architecture. These two GPUs are Radeon Pro V620 and Radeon Pro W6800. However, if you look at https://github.com/ROCmSoftwarePlatform/rocBLAS/blob/be030feb91fff8d6d2b4409153fe549b81237580/CMakeLists.txt#L113-L118, our code only incorporates GPU support based on the ISA architecture. The model name only impacts official support. As a result, you can be confident that Radeon RX 6800, Radeon RX 6800 XT and Radeon RX 6900 XT run on a stack that has undergone full QA verification of the ISA code generated that is specific to this GPU architecture. Of course, at the moment no official support is promised for the consumer GPUs. And performance optimizations for the supported GPUs may not carry over to the unsupported gfx1030 GPUs due minor hardware differences. 

Going forward, the lack of clarity on GPU support will be addressed. Please be patient and continue to report issues.



---

### 评论 #24 — Bengt (2022-05-17T09:24:16Z)

@saadrahim thanks for clarifying the matter. I created a pull request documenting the current state of unofficial support in the README. Would you please extend your statement to the recently released "50" variants of cards? The AMD Radeon 6950XT is also using the gfx1030 ISA and should therefore also be unofficially supported, right?

---

### 评论 #25 — wsippel (2022-05-17T12:11:55Z)

I successfully use HIP and rocm-opencl on a 5700XT, so RDNA1 evidently works, even if it's not officially supported. AMD's own recently released HIP-RT officially supports Vega1, Vega2, RDNA1 and RDNA2, and runs on ROCm - which officially only supports one of those GPU generations. There appears to be a lot of confusion on AMD's side what "supported" means and what ROCm even is in the first place. 

---

### 评论 #26 — saadrahim (2022-05-17T14:10:04Z)

Based @wsippel , there needs more thought on how to classify what works and doesn't on ROCm. The ROCm stack is composed of software broadly split into categories consisting of kernel module (or driver), runtime, compiler, libraries and AI. Official support for GPU architectures in these categories is not all or nothing, some GPU architectures are supported in the kernel module, runtime and compiler only. That same architecture may unofficially be known to just work on libraries and AI software in the ROCm stack. This creates confusion that is evident in this thread. To address this effectively, a table summarizing our support is needed. Please don't expect an overnight solution to this. However, I will look at #1738. At present, I do not want to merge it in without addressing all the nuances.

---

### 评论 #27 — cgmb (2022-05-17T18:32:11Z)

> I successfully use HIP and rocm-opencl on a 5700XT, so RDNA1 evidently works, even if it's not officially supported.

rocBLAS and rocSOLVER will also work on the RX 5700 XT, though it's not officially supported. Many ROCm libraries will also work on other unsupported Navi1X and Navi2X GPUs if built from source. Your mileage may vary.

> There appears to be a lot of confusion on AMD's side what "supported" means

This rings true to me. I can't speak for AMD as a whole, but I personally don't know what it means. As a library developer, I can tell you what definitely works, what probably works, what probably doesn't work, and what definitely doesn't work. However, my understanding is that "works" is not the same thing as "supported" and I have never been given a clear definition of the latter.

> Going forward, the lack of clarity on GPU support will be addressed.

I'm thrilled to hear that, @saadrahim.

---

### 评论 #28 — ffleader1 (2022-05-17T18:44:34Z)

> Based @wsippel , there needs more thought on how to classify what works and doesn't on ROCm. The ROCm stack is composed of software broadly split into categories consisting of kernel module (or driver), runtime, compiler, libraries and AI. Official support for GPU architectures in these categories is not all or nothing, some GPU architectures are supported in the kernel module, runtime and compiler only. That same architecture may unofficially be known to just work on libraries and AI software in the ROCm stack. This creates confusion that is evident in this thread. To address this effectively, a table summarizing our support is needed. Please don't expect an overnight solution to this. However, I will look at #1738. At present, I do not want to merge it in without addressing all the nuances.

Would definitely love this.
Also, if a GPU is "supported", as the Navi 21 series, please make sure it is included in the document.
It seems counter intuitive to literally have 6800, 6800 XT, 6900 XT (and probably 6950 XT) work, but they got mention nowhere in the document, and people have to look into the code to find the compatibility check line, which works in the same way with the "officially supported" WX 6800.

---

### 评论 #29 — wsippel (2022-05-17T19:48:28Z)

I get that ROCm is a bunch of different modules. That's my point. I'm currently working with the Monado team, they developed a hand tracking solution for XR, but it's slow. So the hand tracking lead said he's looking into a CUDA implementation. I told him to consider HIP instead, he looked at the ROCm documentation and concluded that HIP only supports expensive workstation and datacenter cards, so it wouldn't be worth it. That's a shit situation to be in, and it's 100% because the documentation sucks. Because it would work on way more cards, consumer cards included. The official documentation leaves a really bad impression. That's what need's fixing. HIP and OpenCL are the two parts of ROCm most developers and end users care about, and those two modules work on way more GPUs than what's officially supported by ROCm as a whole, so focus on that and clear things up.

---

### 评论 #30 — FCLC (2022-05-17T19:57:48Z)

> Navi1x GPU support will not be available in ROCm. My apologies for the delays in confirming this.
> 
> AMD GPU support is based on ISA architectures. We officially support two Navi21 GPUs that use the gfx1030 architecture. These two GPUs are Radeon Pro V620 and Radeon Pro W6800. However, if you look at https://github.com/ROCmSoftwarePlatform/rocBLAS/blob/be030feb91fff8d6d2b4409153fe549b81237580/CMakeLists.txt#L113-L118, our code only incorporates GPU support based on the ISA architecture. The model name only impacts official support. As a result, you can be confident that Radeon RX 6800, Radeon RX 6800 XT and Radeon RX 6900 XT run on a stack that has undergone full QA verification of the ISA code generated that is specific to this GPU architecture. Of course, at the moment no official support is promised for the consumer GPUs. And performance optimizations for the supported GPUs may not carry over to the unsupported gfx1030 GPUs due minor hardware differences.
> 
> Going forward, the lack of clarity on GPU support will be addressed. Please be patient and continue to report issues.


Any insight onto why this change was made to the roadmap? and how that matches with previous comments?

As for the implications, does this mean that Navi1 won't receive official binaries? or are there other implications? 

---

### 评论 #31 — Bengt (2022-05-17T22:20:37Z)

Please review the library target matrix as requested in this issue that I created in this pull request:

[Document Supported GPUs and Library Targets (#1738)](https://github.com/RadeonOpenCompute/ROCm/pull/1738)

---

### 评论 #32 — littlewu2508 (2022-05-18T07:08:27Z)

ROCm is an open-source platform which has a huge advantage -- communities can join and contribute. Various distribution are packaging ROCm. As the maintainer of rocBLAS package in Gentoo, I already [patched the source to include gfx1031 with decent performance](https://gitweb.gentoo.org/repo/gentoo.git/commit/?id=f1dcb1e8ba4936959138ccf747400d0d54d87b26) which is not originally supported, because I bought 6700xt on my desktop for daily usage and accelerated computing in research. It is OK for AMD, as a company, to privide **enterprise** support for **enterprise** card on **enterprise** Linux distribution; and open-source leaves enough space for communities to expand the support.

However, as @wsippel said, it's sad when people are frightened seemingly poor support matrix away in the official document. I suggest @ROCmSupport that AMD can emphasize **that there is way more support exists in the community** in the official document, and give some useful links to suggest consumer-card-users **seek help from community**, as well as encourage them to **contribute**.

---

### 评论 #33 — Bengt (2022-05-18T07:18:52Z)

Hi, @littlewu2508! Thanks for your contribution to ROCm. Are these changes, you made for Gentoo, upstream and in the current release, yet? In that case, I would like to extend my library matrix to gfx1031.

---

### 评论 #34 — Bengt (2022-05-18T07:23:47Z)

[As recently stated, rocWMMA does not support RDNA2 GPUs.](https://github.com/ROCmSoftwarePlatform/rocWMMA/issues/31) @saadrahim, would you please also comment on what this means for the GPU support statement? It seems to me, that full library coverage currently only exists for the enterprise AMD Instinct GPUs implementing the CDNA architecture. In your earlier statement, you said that the workstation Radeon PRO W6800 and V620 GPU products implementing the RDNA2 GPUs are supported. What do you mean by this support, and how does it compare to support for PRO and Radeon GPUs?

---

### 评论 #35 — littlewu2508 (2022-05-18T07:33:47Z)

> 

These changes are not upstreamed yet, but thanks for reminding me. I'll open a PR to rocBLAS as soon as possible.

---

### 评论 #36 — keryell (2022-05-18T23:47:24Z)

> @littlewu2508 However, as @wsippel said, it's sad when people are frightened seemingly poor support matrix away in the official document. I suggest @ROCmSupport that AMD can emphasize **that there is way more support exists in the community** in the official document, and give some useful links to suggest consumer-card-users **seek help from community**, as well as encourage them to **contribute**.

I am pushing for this internally. The problem is that we need to fix a better build system just to have more external (and even internal!) contributions.

---

### 评论 #37 — saadrahim (2022-05-19T05:04:26Z)

> [As recently stated, rocWMMA does not support RDNA2 GPUs.](https://github.com/ROCmSoftwarePlatform/rocWMMA/issues/31) @saadrahim, would you please also comment on what this means for the GPU support statement? It seems to me, that full library coverage currently only exists for the enterprise AMD Instinct GPUs implementing the CDNA architecture. In your earlier statement, you said that the workstation Radeon PRO W6800 and V620 GPU products implementing the RDNA2 GPUs are supported. What do you mean by this support, and how does it compare to support for PRO and Radeon GPUs?

rocWMMA is a specialized library and support for Navi21 is not planned. I appreciate your thoroughness in exposing this flaw in the documentation. Clarification of this case should be added to the documentation text. I will look into it.

---

### 评论 #38 — cgmb (2022-05-19T06:04:09Z)

> rocWMMA is a specialized library and support for Navi21 is not planned. I appreciate your thoroughness in exposing this flaw in the documentation.

Just to be clear, this is because the purpose of rocWMMA is to help developers structure their calculations to take advantage of matrix cores. Navi21 does not have matrix cores, so the optimizations that rocWMMA was created to provide cannot be done on that architecture. The library exists to help developers use a specific hardware feature.

---

### 评论 #39 — Bengt (2022-05-19T07:42:12Z)

@saadrahim , @cgmb, thanks for clarifying that rocWMMA  can only support devices which have the relevant hardware. In cases like this, official support could perhaps mean "library coverage for all advertised features" or something along those lines. In the library matrix, we would need a marker for "no hardware for the functions of this library, so it is okay to not be covered as a target". I will add those over in my pull request.

---

### 评论 #40 — yacc143 (2022-11-24T08:53:05Z)

> gfx1031

I'm uncertain if AMD is realizing that they are also loosing sales.

I currently need to add a private PC (because my private usage of my work laptop becomes untenable), so I'm looking for something small, that can also do reasonable AI homework (yes I'm one of these unreasonable software developers who decided to study AI in their old age).

I'd really prefer to go with AMD. Likewise, I'm delighted with my Zen 2 based work laptop.

But let's summarize:

* Here, let's say Miniforum HX90G, R9-5900HX + RX 6600M €799 for the barebone.
* versus an Intel NUC 12 i7 Extreme. i7 12700 and support for any 12" GPU. €1050 for the barebone.

Problem here is that the second option, will be in all €600 pricier. But I lose out on the joy of figuring out which architecture the RX6600M is (AMD usually does not mention it, googling around like a crazy is the usual way), then figuring out if such a thing like unofficial ROCm support exists, …

---

### 评论 #41 — wangling12 (2023-01-31T03:39:52Z)

The current meaning of the official document seems to be: "Never use ROCm, because we only support 8 expensive GPUs".
![image](https://user-images.githubusercontent.com/24770600/215655438-0767e918-1218-4a9a-a763-a8d7092be658.png)
I believe that most people will turn around and buy a NVIDIA GPU to start their work or study after browsing the document...

---

### 评论 #42 — Bengt (2023-01-31T10:13:30Z)

@wangling12 Yes, the current documentation feels pretty snobbish because it only mentions prosumer/enterprise hardware. I get that AMD wants to address their best-paying costumers first and foremost. That makes sense, especially with the lackluster ROCm support for other hardware. Maybe there is some way of clearly communicating the limited support ("works" etc.) for other products without the risk of steering customers from one product segment to another. Isn't exactly the official support where I would expect AMD to closely work with their enterprise customers a unique selling point of this class of products?

---

### 评论 #43 — muziqaz (2023-04-04T07:27:36Z)

In my interactions with HIP for OpenMM, everything worked after Polaris. Polaris is no longer supported by AMD OpenCL in Linux, and HIP failed too.

---

### 评论 #44 — JeLuF (2023-05-08T21:28:19Z)

A year has passed, Release 5.5 has just seen the light of day, and the support list in the documentation isn't mentioning any non-enterprise GPUs:
![image](https://user-images.githubusercontent.com/5852422/236938280-0a91f10d-e3ed-4894-8979-b271cfb60719.png)
Everyone is hyped about AI (e.g. Stable Diffusion), so it's odd to see that AMD still doesn't show any interest in supporting their products.

---

### 评论 #45 — yacc143 (2023-05-09T18:46:05Z)

Any idea how one could get AMD kicked into their posterior, I mean this is not even about improving software or software quality, this is purely about improving documentation.

Let me rephrase it differently.

And the current going rate for freelance python developers in Germany, loosing 2 days to set up a working environment for an AMD GPU is a commercially non-viable proposal, the Nvidia 4080/4090 is cheaper than the work time of the developer.

(Especially if you take the incremental cost over a top of the line AMD GPU, which AMD isn't giving out as freebies either.)

Now ML development, either happens directly in relevant instance models in the cloud, OR initially on developer's personal machines which often start out with high-end consumer kit. AMD seems to have missed that tiny detail?


---

### 评论 #46 — muziqaz (2023-05-09T19:00:23Z)

From my understanding, AMD management who decide whether to expand software dev teams or not, has not bought into the idea that ROCm/HIP for Desktop market could bring money back to AMD. Seeing a perfect example of how CUDA got into the market and everyone and their dog is doing basement AI/ML with nVidia cards through CUDA, I can only wonder why ROCm to broader markets is not a priority number one right now :/
But then again, building reliable, efficient teams also takes time, we never know, they might have brought required talent and they are just getting into the gear. Or this is just wishful thinking, and ROCm remains just a side project from their HPC division (where ROCm/HIP was born)

---

### 评论 #47 — thyTwilightGoth (2023-06-03T23:23:26Z)

As a Consumer I would like to know what my rx 580 definitivly supports in rocm, and improved documentation would be very helpful in that end goal.

---

### 评论 #48 — viraj-s15 (2023-08-14T10:13:12Z)


![image](https://github.com/RadeonOpenCompute/ROCm/assets/79002760/32526ee9-ee11-4c5a-9768-ca43dc9c859d)


![screenshot](https://github.com/RadeonOpenCompute/ROCm/assets/79002760/ffed3ada-7c78-4d20-bd26-13471869f419)


Just gonna leave this here in case it helps someone, ROCm is not supported but works on the 6650M as well. I am using arch linux. I built pytorch from source using the instructions from <a href="https://github.com/pytorch/pytorch#from-source">here</a>



---

### 评论 #49 — fredi-python (2023-08-23T15:54:25Z)

@viraj-s15 Do you think there is a way for finetuning maybe a small 3B Language Model model with a AMD RX 5700 XT?

---

### 评论 #50 — muziqaz (2023-08-23T16:02:40Z)

Now that HIP SDK was released for Windows, we managed to get it running on rx460 as well as rx550 and even Zen 4 iGPU

---

### 评论 #51 — fredi-python (2023-08-23T16:04:10Z)

But how is it with Linux? I use arch btw

---

### 评论 #52 — viraj-s15 (2023-08-23T16:10:15Z)

> @viraj-s15 Do you think there is a way for finetuning maybe a small 3B Language Model model with a AMD RX 5700 XT?

Could be possible if you are using peft. Not the entire model though. I would recommend using google colab as I have found success in fine tuning llama-7b on it with peft(the free tier). 

---

### 评论 #53 — yuuahmad (2023-08-23T16:10:19Z)

Is there anyone out there who has already installed and tested mobile GPUs like the ones on this list?
![Web capture_23-8-2023_2399_www amd com](https://github.com/RadeonOpenCompute/ROCm/assets/22028802/1bd2ab11-8ab0-45ab-9657-8a57387e994e)


---

### 评论 #54 — viraj-s15 (2023-08-23T16:13:34Z)

> But how is it with Linux? I use arch btw

My laptop 6650 gave me a lot of driver issues in the beginning(for some reason PyTorch wasn't picking it up, even though other libraries were). It has been working well since a bit. My Rx 6800 desktop never gave me any issues. Both running arch Linux. 

---

### 评论 #55 — viraj-s15 (2023-08-23T16:17:42Z)

> Is there anyone out there who has already installed and tested mobile GPUs like the ones on this list?
> 
> ![Web capture_23-8-2023_2399_www amd com](https://github.com/RadeonOpenCompute/ROCm/assets/22028802/1bd2ab11-8ab0-45ab-9657-8a57387e994e)
> 
> 

6650M and 6800M seem to work out of the box for linux as the kernel comes installed with AMD drivers.(I had some issues with it but that was just me). Was looking for a similar resource but couldn't find anything. 

---

### 评论 #56 — fredi-python (2023-08-23T16:19:51Z)

> > @viraj-s15 Do you think there is a way for finetuning maybe a small 3B Language Model model with a AMD RX 5700 XT?
> 
> Could be possible if you are using peft. Not the entire model though. I would recommend using google colab as I have found success in fine tuning llama-7b on it with peft(the free tier).

So I want to upgrade my system, I want to generate some Images with stable diffusion xl.
3060 is quite expensive.
So i thought about the RX 5700 XT, as it is really cheap for its performing

---

### 评论 #57 — viraj-s15 (2023-08-23T16:30:18Z)

> > > @viraj-s15 Do you think there is a way for finetuning maybe a small 3B Language Model model with a AMD RX 5700 XT?
> 
> > 
> 
> > Could be possible if you are using peft. Not the entire model though. I would recommend using google colab as I have found success in fine tuning llama-7b on it with peft(the free tier).
> 
> 
> 
> So I want to upgrade my system, I want to generate some Images with stable diffusion xl.
> 
> 3060 is quite expensive.
> 
> So i thought about the RX 5700 XT, as it is really cheap for its performing

Sadly gpu prices aren't very stable even now. The only issue I found with ROCm against CUDA is that the documentation is not very verbose. With respect to stable diffusion, I still recommend using cloud services as and when you need them and only pay when you use them. You'll have a much better experience with more compute to work with. I'm genuinely interested about how intel plays this with their Arc gpus as they seem to have the best value for the hardware, they don't support many newer technologies though. 

---

### 评论 #58 — cgmb (2023-08-23T19:17:54Z)

It's somewhat off-topic, but folks may also be interested in [Debian's Supported GPU List](https://salsa.debian.org/rocm-team/community/team-project/-/wikis/supported-gpu-list) for their ROCm packages.

---

### 评论 #59 — FCLC (2023-08-23T19:22:23Z)

Briefly jumping in: 

a few factors will dictate if you can run a model: 

1. Software Support (binary yes or no)
2. Quantization level (does the model use quanta? if so, to what level? and does the HW/SW stack in question support that level)
3. parameter count 

assuming you run a 3b model at int8 quanta, that's 3GBs of model data in vram. add some margin for pointers, maths and so on (context/tokens for 1k length can be ~500MB) and you're at 3.5GBs.

Don't forget you also have a desktop environment to run. 

In essence, a 3B model can barely fit on a 4GB card, but will fit (depending on your setup). Navi10 GPUs (5600xt, 5700, 5700xt) all ship with 6 to 8 GBs of vram. 



---

### 评论 #60 — fredi-python (2023-08-24T07:44:49Z)

> It's somewhat off-topic, but folks may also be interested in [Debian's Supported GPU List](https://salsa.debian.org/rocm-team/community/team-project/-/wikis/supported-gpu-list) for their ROCm packages.

What architecture does RX 5700 XT use?

---

### 评论 #61 — cgmb (2023-08-24T08:20:44Z)

The RX 5700 XT is gfx1010.

---

### 评论 #62 — fredi-python (2023-08-25T18:09:44Z)

Thanks for the info!

---

### 评论 #63 — grigio (2023-08-28T09:16:39Z)

> It's somewhat off-topic, but folks may also be interested in [Debian's Supported GPU List](https://salsa.debian.org/rocm-team/community/team-project/-/wikis/supported-gpu-list) for their ROCm packages.

I don't understand why Debian have to list AMD gpus supported by ROCm and not AMD officially

---

### 评论 #64 — FCLC (2023-08-28T12:12:02Z)

Because when a HW vendor says something is supported, they can be taken to task for it when it breaks. 

When opensource gets something that's sort of working/running, there's a larger understanding of what that does and doesn't mean. 

It's the same reason you'll always see the WS/enterprise cards supported "first" by a vendor, because the support surface area for specific applications being problematic is much smaller 

---

### 评论 #65 — yacc143 (2023-08-28T18:49:19Z)

Sure, you mean like Intel or AMD that were taken to task for all their
security related hardware bugs, which they mostly fixed by new microcode
that made their CPUs run slower. Significantly slower. And in some cases,
Intel just cancelled some features in their CPUs that caused problems.

Spectre, Meltdown, Zenbleed,SQUIP, AEPIC, Downfall, the list is very long,
on average gets longer by ~2 entries per year, the newest ones are really
irritating as they relate to CPUs that might old, but laptops with 10th &
11th generation Intel CPUs are still sold today.

Sure, HW vendors that don't deliver their documented promises get punished.
ROTFL.

I mean, it took nearly a decade for German courts to come to the conclusion
that a car with patched engine firmware that does not deliver the promised
performance is less valuable than the car offered and sold. And IT HW
vendors seem to have yet to been sued for their "security fixes" that kind
of break the product, only a cynic would think that making old CPUs run
either in an unsafe way or slowly was a hint to upgrade to new hardware?

Am Mo., 28. Aug. 2023 um 14:12 Uhr schrieb FelixCLC <
***@***.***>:

> Because when a HW vendor says something is supported, they can be taken to
> task for it when it breaks.
>
> When opensource gets something that's sort of working/running, there's a
> larger understanding of what that does and doesn't mean.
>
> It's the same reason you'll always see the WS/enterprise cards supported
> "first" by a vendor, because the support surface area for specific
> applications being problematic is much smaller
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/RadeonOpenCompute/ROCm/issues/1714#issuecomment-1695587204>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/AAH5B3CBEND2QP356RZC7ZLXXSDJ5ANCNFSM5RSXBIRQ>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


---

### 评论 #66 — fredi-python (2023-09-23T00:24:14Z)

So, I got a used RX 5700 XT from ebay and want to get things running.
I have arch linux and debian testing.
IG debian works better than arch linux in case of ROCM.
So I want to inference some LLMs with the transformers library, what are the first steps to take?

---

### 评论 #67 — cgmb (2023-09-23T05:31:53Z)

> So I want to inference some LLMs with the transformers library, what are the first steps to take?

You mean [huggingface/transformers](https://huggingface.co/docs/transformers/index)? It seems to depend on PyTorch, Tensorflow or Jax.

The RX 5700 XT is gfx1010. It is not officially supported by ROCm. To my knowledge, only Debian is building the ROCm math libraries for that architecture. However, Debian has not yet packaged miopen or pytorch-rocm.

You can use the Debian packages for most of the ROCm libraries, but would need to extend MIOpen and PyTorch with support for gfx1010, then build them from source.

---

### 评论 #68 — fredi-python (2023-09-23T13:06:29Z)

> > So I want to inference some LLMs with the transformers library, what are the first steps to take?
> 
> You mean [huggingface/transformers](https://huggingface.co/docs/transformers/index)? It seems to depend on PyTorch, Tensorflow or Jax.
> 
> The RX 5700 XT is gfx1010. It is not officially supported by ROCm. To my knowledge, only Debian is building the ROCm math libraries for that architecture. However, Debian has not yet packaged miopen or pytorch-rocm.
> 
> You can use the Debian packages for most of the ROCm libraries, but would need to extend MIOpen and PyTorch with support for gfx1010, then build them from source.

Yes the huggingface transformers library, exactly
If Ubuntu works better with ROCM I could also install that, Seems to be quite tricky on debian

And another question:
How well does the RX 6650 XT perform against the RX 5700 XT in ML tasks?
And is the RX 6650 XT easier to setup with ROCM?
I am a bit confused what gfx the 6650 has, as I can't find it in https://llvm.org/docs/AMDGPUUsage.html#processors


---

### 评论 #69 — cgmb (2023-09-23T17:25:12Z)

> How well does the RX 6650 XT perform against the RX 5700 XT in ML tasks?

I don't know.

> I am a bit confused what gfx the 6650 has

It is Navi 23 and is therefore gfx1032.

> And is the RX 6650 XT easier to setup with ROCM?

Neither is officially supported, but the gfx1032 ISA is identical to the gfx1030 ISA. It can probably be made to work by setting the environment variable `HSA_OVERRIDE_GFX_VERSION=10.3.0` and using the official binaries. Navi 21 GPUs [RX 6800 / RX 6800 XT / RX 6900 XT / RX 6950 XT ] require less fiddling as they are already gfx1030.

As one of the members of the Debian AI team working on packaging this stuff, I think you can expect improvements for all RDNA cards over the next year as we've nearly finished packaging the ROCm math libraries and are moving on to packaging the AI libraries. For the most part, it has not been very difficult to extend basic functionality to all discrete AMD GPUs as we've prepared the packages.

---

### 评论 #70 — fredi-python (2023-09-24T22:03:01Z)

For AI stuff and some gaming would the RTX 3060 be the best price to performence option?
I have the feeling there is no real mid range Card that works very good with ROCm, If there is please tell me.

---

### 评论 #71 — muziqaz (2023-09-24T22:56:06Z)

> For AI stuff and some gaming would the RTX 3060 be the best price to performence option? I have the feeling there is no real mid range Card that works very good with ROCm, If there is please tell me.

For AI, yes, for gaming, no. But we are getting off topic here.
It is safe to assume that generation (RDNA3) which has GPUs supported by ROCm, will work throughout all GPUs from that generation, so if 6900xt is supported, it is safe to assume rx6600 will also work. The reason we are not seeing all GPUs marked as supported is because those who are deploying ROCm to desktop space do not have time (or means) to run all the GPUs on the market to tick the box that they are supported. We managed to run HIP in Windows on ryzen 7000 iGPUs and rx550, as well as 7900xtx, 6900xt, rx6600, Radeon 7, 5700xt, etc

---

### 评论 #72 — littlewu2508 (2023-09-25T02:40:14Z)

> For AI stuff and some gaming would the RTX 3060 be the best price to performence option? I have the feeling there is no real mid range Card that works very good with ROCm, If there is please tell me.

For RDNA3 optimization is still on-going, e.g. https://github.com/ROCmSoftwarePlatform/rocBLAS/commit/247d4a968a6007af275e18baffbafdae3ce6d10e is still in develop branch and do not enter any release yet. With out that optimization you will get poor FP32 performance (https://github.com/ROCmSoftwarePlatform/Tensile/issues/1715). However its FP16 and FP32+=FP16*FP16 mixed performance already looks good. So wait for optimizations for RDNA3.

---

### 评论 #73 — fredi-python (2023-10-20T14:26:22Z)

Now with the release of ROCm 5.7.1, does only the RX 7900 xtx work or also GPUs like the RX 7600?

---

### 评论 #74 — muziqaz (2023-10-20T17:26:35Z)

> Now with the release of ROCm 5.7.1, does only the RX 7900 xtx work or also GPUs like the RX 7600?

I am very confident, that AMD did not remove any before supported GPUs, and those we managed to get working. It would be extremely counter productive to wipe all the previous support and start from zero.
This support by the way is just a validation.

---

### 评论 #75 — tperka (2023-12-22T17:30:53Z)

I think that thread is a good place to ask - I'm a daily Linux user and ML student. I'd like to buy myself RX 6700 XT for Christmas. Has anyone made it work with Pytorch on Linux with ROCM 5.6/5.7? Is the performance of this GPU better than RTX 3060 or does lack of official support for Linux slow it down in any way?

I'm fine with tinkering, just curious if it's even possible before buying

---

### 评论 #76 — littlewu2508 (2023-12-23T04:36:04Z)

> I think that thread is a good place to ask - I'm a daily Linux user and ML student. I'd like to buy myself RX 6700 XT for Christmas. Has anyone made it work with Pytorch on Linux with ROCM 5.6/5.7? Is the performance of this GPU better than RTX 3060 or does lack of official support for Linux slow it down in any way?
> 
> I'm fine with tinkering, just curious if it's even possible before buying

On Linux, after the rocr-runtime/hsa level, you can get nearly same level of support of Pro W6800 (gfx1030) which is on the official support list, via environment variable `HSA_OVERRIDE_GFX_VERSION=10.3.0`.

References:
https://github.com/ROCm/ROCm/issues/1756
https://github.com/ROCmSoftwarePlatform/rocBLAS/pull/1251

---

### 评论 #77 — nix-wolf (2024-01-09T08:55:42Z)

> I think that thread is a good place to ask - I'm a daily Linux user and ML student. I'd like to buy myself RX 6700 XT for Christmas. Has anyone made it work with Pytorch on Linux with ROCM 5.6/5.7? Is the performance of this GPU better than RTX 3060 or does lack of official support for Linux slow it down in any way?
> 
> I'm fine with tinkering, just curious if it's even possible before buying

I have 2 6750xt 12gb, and it works pretty good, if your having troubles and picked up a card. I have a list of maybe 25 calls from a minimal rhel install to running ml, pytorch/diffusers/transformers and such do work as well and nearly out of box, just a little memory management needs to be done. 

---

### 评论 #78 — capsicumw (2024-01-10T01:42:35Z)

> > How well does the RX 6650 XT perform against the RX 5700 XT in ML tasks?
> 
> I don't know.
> 
> > I am a bit confused what gfx the 6650 has
> 
> It is Navi 23 and is therefore gfx1032.
> 
> > And is the RX 6650 XT easier to setup with ROCM?
> 
> Neither is officially supported, but the gfx1032 ISA is identical to the gfx1030 ISA. It can probably be made to work by setting the environment variable `HSA_OVERRIDE_GFX_VERSION=10.3.0` and using the official binaries. Navi 21 GPUs [RX 6800 / RX 6800 XT / RX 6900 XT / RX 6950 XT ] require less fiddling as they are already gfx1030.
> 
> As one of the members of the Debian AI team working on packaging this stuff, I think you can expect improvements for all RDNA cards over the next year as we've nearly finished packaging the ROCm math libraries and are moving on to packaging the AI libraries. For the most part, it has not been very difficult to extend basic functionality to all discrete AMD GPUs as we've prepared the packages.

Is Debian going to be an officially supported hip/ROCm distro? 
It would be an amazing step up since we can't expect long-term support for CentOS and Debian is upstream for so many other distros. (And Debian stable has been my default distro for 6 years.)  
The two Enterprise Linuxes aren't products well suited to single desktop users, and I refuse to use Ubuntu(to much forced "not invented here" breaking compatibility with the rest of Linux). OpenSUSE-leap would be a decent option too, but it is not on the official support list.

---

### 评论 #79 — capsicumw (2024-01-10T02:15:35Z)

Has AMD made any firm support-date commitments for officially supported cards? 

I mean nVidia has demonstrated continued cuda support for many cards that are nearly 10 years old so their actions are proof enough.  
Microsoft provides formal end of support dates for its various software eg "Product ZYX will be supported at least through 2025 May 31st", same goes for most major Linux distributions.

I would like to avoid the proprietary Cuda garden and maybe program with openSyCL. But why should I gamble thousands of USD assembling a new machine when hip/ROCm/pro-driver support can be haphazardly pulled out from under me next month? And AMD has a bad habit of eliminating access to older versions of software/firmware that could be used on older systems. (My current system doesn't support PCIe atomics, so a new AMD card would mean a fresh build.)

On the CPU side AMD has shown excellent long-term support, but my experience on the GPGPU side has burned me twice due to poor/misleading marketing of features and compatibility. 
One was a high-end workstation card (W7000 way back in the southern islands era) and the other was a more cautious purchase of a consumer polaris card where I only considered the implied GPGPU compute features as a side bonus.

---

### 评论 #80 — darkshvein (2024-02-10T13:27:43Z)

> The list of supported GPUs is also found [here](https://docs.amd.com/bundle/ROCm_Installation_Guidev5.0/page/Prerequisite_Actions.html)

404 - Page Not Found
Return [home](https://docs.amd.com/bundle/ROCm_Installation_Guidev5.0/page/index.html) or use the sidebar navigation to get back on track.
))))

---

### 评论 #81 — darkshvein (2024-02-10T13:30:35Z)

> but am I an idiot or is this documentation just abysmal?

The same issue for me. I search support list for blender, and my rx480 but documentation very ugly.

---

### 评论 #82 — cgmb (2024-02-13T19:09:07Z)

> > The list of supported GPUs is also found [here](https://docs.amd.com/bundle/ROCm_Installation_Guidev5.0/page/Prerequisite_Actions.html)
> 
> 404 - Page Not Found Return [home](https://docs.amd.com/bundle/ROCm_Installation_Guidev5.0/page/index.html) or use the sidebar navigation to get back on track. ))))

The list for ROCm 6.0.2 can be found at https://rocm.docs.amd.com/projects/install-on-linux/en/docs-6.0.2/reference/system-requirements.html#supported-gpus

---
