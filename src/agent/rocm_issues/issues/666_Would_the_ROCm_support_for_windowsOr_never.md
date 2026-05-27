# Would the ROCm support for windows?Or never?

> **Issue #666**
> **状态**: open
> **创建时间**: 2019-01-08T15:23:21Z
> **更新时间**: 2025-09-02T18:38:36Z
> **作者**: Color-Dark
> **标签**: Feature Request
> **URL**: https://github.com/ROCm/ROCm/issues/666

## 标签

- **Feature Request** (颜色: #fbca04)

## 描述

Would you have a plan for supporting ROCm in windows platform? 

---

## 评论 (100 条)

### 评论 #1 — jlgreathouse (2019-01-08T16:07:13Z)

Hi @Lucifer-Morning-Star 

If you mean the ROCm kernel driver and HSA stack, there are currently no plans to port our Linux driver or full HSA runtime to Windows. The driver itself is highly tied to Linux, and our HSA software stack (Thunk and ROCr) are themselves highly tied to our driver.

We already support OpenCL in Windows through software included with our Catalyst drivers.

Our HIP and HCC compilers/runtimes, and libraries and software built using them (such as rocBLAS, MIOpen, tensorflow and Pytorch built on MIOpen) may technically be possible to port to Windows, but I cannot give any public commitment about when or if AMD will perform these ports.

---

### 评论 #2 — musm (2019-10-07T17:23:56Z)

@jlgreathouse given the recent announcements and collaboration between microsoft and AMD on the Surface Laptop and their custom chips. Do you mind providing some insight if we an expect and support in the future? Thanks. 

---

### 评论 #3 — vickiegpt (2019-10-21T16:53:31Z)

when wsl makes gpu passthrough possible, everything solved

---

### 评论 #4 — xsacha (2019-11-18T10:44:19Z)

> when wsl makes gpu passthrough possible, everything solved

Not at all. There's no way to install drivers on WSL.

---

### 评论 #5 — briansp2020 (2019-12-10T21:08:12Z)

> Not at all. There's no way to install drivers on WSL.

Won't it change with WSL2? I was thinking that WSL2 and SR-IOV will make it possible to run ROCm on Windoes. Not that I'd be willing to pay for a GPU with SR-IOV...

---

### 评论 #6 — wwwguess (2020-03-04T01:47:11Z)

DeepLearning is future. Why doesn't AMD care this. Almost nobody did some studying and working with AMD gpus. My macbook pro 16 can't be used to work on DeepLearning with it's RadeonPro5500M. That's a piece of shit!

---

### 评论 #7 — Mandrewoid (2020-03-04T10:32:48Z)

> DeepLearning is future. Why doesn't AMD care this. Almost nobody did some studying and working with AMD gpus. My macbook pro 16 can't be used to work on DeepLearning with it's RadeonPro5500M. That's a piece of shit!

_**Edit: I originally thought you meant a 2016 macbook, I have since realized you mean the new 16 
 inch macbook. Nevertheless, the point I made below stil stands.** My vega 64 has **12Tflops fp32**. MPB16 is rated as **up to 4Tflops** When the laptop gets hot... speed will reduce._ 

This is not the place for comments like that, but even if it was... **your macbook 2016 does not have anywhere NEAR the compute capability of a modern GPU**. **You would be better off using google colab for free**
It has access to GPU's and TPU's, and won't load up your local computer.
Here's a beginner article.
https://towardsdatascience.com/getting-started-with-google-colab-f2fff97f594c

---

### 评论 #8 — papadako (2020-05-03T20:45:20Z)

> Would you have a plan for supporting ROCm in windows platform?

I think this is the first time that I find a correlation between the description of an issue in github and the issue number! :) 

---

### 评论 #9 — briansp2020 (2020-05-19T17:07:10Z)

Is ROCm coming to Windows through WSL2? MS just announced GPU compute workload support through WSL2. I hope it's not just for NVidia...
https://www.phoronix.com/scan.php?page=news_item&px=Linux-GUI-Apps-GPU-WSL2

---

### 评论 #10 — briansp2020 (2020-06-18T03:07:31Z)

It seems WSL2 will support DirectML and CUDA. Will HIP API be ported as well?

I have not dug into DirectML too deep. Is DirectML a machine learning specific API or it is general enough to support other GPGPU applications like CUDA/OpenCL.

So many API for GPU compute. I was hopeful that HIP will serve as a unifying GPGPU development API/language but alas...

---

### 评论 #11 — teddy-mindcompass (2022-11-20T10:26:27Z)

> Ok Goodbye, welcome Cuda 



---

### 评论 #12 — xsacha (2022-11-20T10:34:08Z)

Intel supports Windows on their new Arc GPUs and still nothing from AMD.

---

### 评论 #13 — teddy-mindcompass (2022-11-20T23:07:04Z)

> Intel supports Windows on their new Arc GPUs and still nothing from AMD.

It can work on windows using Microsoft Antares but i don't have the time for that!!! https://github.com/microsoft/antares

it's a big project to make it works perfectly 

---

### 评论 #14 — saadrahim (2022-11-21T02:22:07Z)

Work on a windows port is well underway.

https://github.com/amd/rocm-examples

You can see signs on many of our repositories. 



---

### 评论 #15 — xsacha (2022-11-21T02:37:39Z)

From that repo: "ROCm toolchain for Windows (No public release yet)"

Still waiting :( There has been talk of ROCm for Windows for roughly 5 years now with small hints like this on AMD repos and docs. It doesn't give me any more hope to see that.

I had fast GPGPU working on Windows with 'CTM' (Close to Metal) / Stream SDK over a decade ago. Then AMD went silent (buggy and slow OpenCL) and I've been forced to use CUDA ever since.

Pretty much overnight, Intel has appeared on the scene and offered cross-platform support without any issues.

---

### 评论 #16 — tallesairan (2023-01-10T13:45:33Z)

this is a shame, amd should follow nvidia's example with cuda, it seems to me that amd is lazy

---

### 评论 #17 — lshqqytiger (2023-02-13T03:20:40Z)

Good news? It is [Coming Soon](https://rocmdocs.amd.com/en/rtd/).

---

### 评论 #18 — xsacha (2023-02-13T03:32:39Z)

Coming Soon or Coming Soon™️?

We've seen Windows release notes and windows DLL files before.. :/

---

### 评论 #19 — Coderx7 (2023-02-13T07:21:38Z)

It's not needed as bad as before anyway, especially when the likes of mlir projects (like torch-mlir)are working very well today.
Though it's still very unfortunate! 

---

### 评论 #20 — YuriyTigiev (2023-02-26T13:28:38Z)

We all are waiting a big good surprise from AMD. 

---

### 评论 #21 — boxerab (2023-02-26T16:59:09Z)

probably dropping OpenCL in the windows port ...

---

### 评论 #22 — scarsty (2023-02-27T05:00:06Z)

mark...

---

### 评论 #23 — AlphaJuliettOmega (2023-02-28T09:52:43Z)

OpenCL being silently dropped when I upgraded from an RX480 + ROCM not even supporting 6xxx cards is very confusing to say the least.

Looking forward to see if ROCm is usable on Windows.

On Linux using ROCm causes driver timeouts, hard crashes, artifacting, complete crash if playing a video while computing etc. (assuming this is why it's not even officially supported)
Hopefully a fresh start on Windows allows a cleaner implementation, best of luck.

---

### 评论 #24 — boxerab (2023-02-28T12:56:30Z)

> OpenCL being silently dropped when I upgraded from an RX480 + ROCM not even supporting 6xxx cards is very confusing to say the least.

Really?  That is very disappointing.

> 
> Looking forward to see if ROCm is usable on Windows.
> 
> On Linux using ROCm causes driver timeouts, hard crashes, artifacting, complete crash if playing a video while computing etc. (assuming this is why it's not even officially supported) Hopefully a fresh start on Windows allows a cleaner implementation, best of luck.

AMD consumer compute is a disaster.  The writing is on the wall - OpenCL is not going to be a workable solution for AMD cards going forward. Time to build a HIP backend or switch to CUDA.




---

### 评论 #25 — iperov (2023-03-20T14:01:09Z)

currently you can use directml for tensorflow ~x1.6 slower

dml for pytorch is ~x2.2 slower, and has a lot of bugs.

onnxruntime-directml inference speed is the same as on CUDA

---

### 评论 #26 — YuriyTigiev (2023-03-20T15:08:44Z)

Time to change pc on compatible with CUDA. :( 

---

### 评论 #27 — countradooku (2023-03-27T20:01:46Z)

https://rocblas.readthedocs.io/en/latest/Windows_Install_Guide.html maybe thats a hint we will have rocm 5.5 on windows

---

### 评论 #28 — ttyyzz34 (2023-03-29T14:11:26Z)

I hope it coming soon! I hope we can see it as rocm 5.5!

---

### 评论 #29 — boxerab (2023-03-29T14:17:39Z)

ROCmCC & Win Install:  https://github.com/RadeonOpenCompute/ROCm/commit/20f8185e0d894373fe14d3ae8727063eceae20eb

---

### 评论 #30 — saadrahim (2023-03-29T14:23:25Z)

The Windows is release is pending. However, don't read too much into the presence in the documentation. I will update the readme to our documentation to explain our branching strategies and what the develop branch means.

---

### 评论 #31 — countradooku (2023-03-31T11:13:15Z)

https://rocmdocs.amd.com/projects/alpha/en/develop/hip_sdk_install_win/hip_sdk_install_win.html 

nice
We are almost there

---

### 评论 #32 — YuriyTigiev (2023-03-31T11:16:21Z)

> https://rocmdocs.amd.com/projects/alpha/en/develop/hip_sdk_install_win/hip_sdk_install_win.html
> 
> nice We are almost there

How we can use it with python ?

---

### 评论 #33 — iperov (2023-03-31T11:18:20Z)

I think it will take years to integrate this into pytorch :D

---

### 评论 #34 — countradooku (2023-03-31T11:21:45Z)

@YuriyTigiev this is alhpa docs. so not yet ready. i hope 5.5 will be the windows release

@iperov There is pytorch with rocm right now. rocm 5.4.3 but only on linux. 

---

### 评论 #35 — ttyyzz34 (2023-04-01T12:10:35Z)

> ROCmCC & Win Install: [20f8185](https://github.com/RadeonOpenCompute/ROCm/commit/20f8185e0d894373fe14d3ae8727063eceae20eb)

It that can work normal?

---

### 评论 #36 — sorryhorizonTT (2023-04-10T05:29:54Z)

mark

---

### 评论 #37 — boxerab (2023-04-11T11:44:32Z)

https://www.phoronix.com/news/AMD-ROCm-5.4.3

Windows support coming in version 6.0

Hopefully they don't drop support for older cards like Polaris, which were sold to customers as recently as 2019

---

### 评论 #38 — countradooku (2023-04-11T12:24:14Z)

@boxerab neah. I still think it will be 5.5. 

---

### 评论 #39 — Cyberhan123 (2023-04-12T15:13:53Z)

Unfortunately, as a newcomer who just learned machine learning, I bought RX7900XTX because it was cheap, but I have to install dual systems to solve this problem. If God gives me a chance, I choose to send money to Nvidia.

---

### 评论 #40 — countradooku (2023-04-12T15:30:21Z)

> Unfortunately, as a newcomer who just learned machine learning, I bought RX7900XTX because it was cheap, but I have to install dual systems to solve this problem. If God gives me a chance, I choose to send money to Nvidia.

Have patient bro. You will not regret your purchase

---

### 评论 #41 — TeddyAlbina (2023-04-12T15:40:02Z)

> Unfortunately, as a newcomer who just learned machine learning, I bought RX7900XTX because it was cheap, but I have to install dual systems to solve this problem. If God gives me a chance, I choose to send money to Nvidia.

I gave up on that one I use my 6900XT for everything and had to buy an nvidia card to work with.

---

### 评论 #42 — TeddyAlbina (2023-04-12T15:40:30Z)

> > Unfortunately, as a newcomer who just learned machine learning, I bought RX7900XTX because it was cheap, but I have to install dual systems to solve this problem. If God gives me a chance, I choose to send money to Nvidia.
> 
> Have patient bro. You will not regret your purchase

It's to late, Intel support everything on day one 😬

---

### 评论 #43 — iperov (2023-04-12T15:47:08Z)

@TeddyAlbina I cannot understand, why to use slow intel CPU in machine learning ? Any gtx1060+ is faster than top intel cpu in machine learning?

---

### 评论 #44 — TeddyAlbina (2023-04-12T15:48:32Z)

> @TeddyAlbina I cannot understand, why to use slow intel CPU in machine learning ? Any gtx1060+ is faster than top intel cpu in machine learning?

I was speaking about intel gpu not cpu

---

### 评论 #45 — iperov (2023-04-12T15:55:18Z)

@TeddyAlbina what is intel gpu ?

---

### 评论 #46 — lshqqytiger (2023-04-13T01:44:06Z)

Intel ARC GPUs. They support GPGPU through their own toolkit called oneAPI.

---

### 评论 #47 — iperov (2023-04-13T04:58:47Z)

According https://www.videocardbenchmark.net/high_end_gpus.html
Arc A770 is near rx 480

![firefox_2023-04-13_08-58-11](https://user-images.githubusercontent.com/8076202/231657684-acf000b7-19a4-4123-b47e-2360718155a4.png)

complete shit


---

### 评论 #48 — countradooku (2023-04-13T07:08:07Z)

<img width="574" alt="image" src="https://user-images.githubusercontent.com/52667211/231680897-28048d52-e0ff-4f54-a433-6f1a43b5f4e8.png">

so we will have rocm for windows in the next release (maybe the 5.5)

---

### 评论 #49 — xsacha (2023-04-13T23:54:47Z)

Official here:
https://www.tomshardware.com/news/amd-rocm-comes-to-windows-on-consumer-gpus

> According https://www.videocardbenchmark.net/high_end_gpus.html Arc A770 is near rx 480
> 

Unrelated discussion. We are talking about ROCm. You show a benchmark about GPU performance for gaming. Intel's GPUs aren't too bad for machine learning.

---

### 评论 #50 — boxerab (2023-04-14T02:18:03Z)

https://rocmdocs.amd.com/projects/alpha/en/develop/release/gpu_os_support.html

For consumer cards , only 6900XT and 6600 are supported on Windows.

---

### 评论 #51 — saadrahim (2023-04-14T02:25:49Z)

> https://rocmdocs.amd.com/projects/alpha/en/develop/release/gpu_os_support.html
> 
> For consumer cards , only 6900XT and 6600 are supported on Windows.


You are reading too much from a website marked alpha. Please see #2044 .

---

### 评论 #52 — OneiroXL (2023-04-14T08:10:04Z)

Without Windows support, AMD will no longer have a market share in graphics cards

---

### 评论 #53 — TeddyAlbina (2023-04-14T08:23:42Z)

> Without Windows support, AMD will no longer have a market share in graphics cards

This in fact should have been their first target platform 

---

### 评论 #54 — wsippel (2023-04-14T08:58:12Z)

@TeddyAlbina Linux is and has always been the default OS for compute and ML workloads, both on workstations and especially in the datacenter, so it makes perfect sense for ROCm to primarily target Linux. 

---

### 评论 #55 — OneiroXL (2023-04-14T09:04:52Z)

> @TeddyAlbina Linux is and has always been the default OS for compute and ML workloads, both on workstations and especially in the datacenter, so it makes perfect sense for ROCm to primarily target Linux.

But now AI painting and other products can be targeted towards the consumer market   ╮(╯▽╰)╭

---

### 评论 #56 — Cyberhan123 (2023-04-14T09:31:17Z)

> @TeddyAlbina Linux is and has always been the default OS for compute and ML workloads, both on workstations and especially in the datacenter, so it makes perfect sense for ROCm to primarily target Linux.

Windows is the platform of choice for many students, game developers, and gamers. If AMD can better support it, it will have a great influence. What's more, AMD is very cost-effective. If everyone is used to HIP, it will be very scary habits, which they bring to work.

---

### 评论 #57 — TeddyAlbina (2023-04-14T09:58:09Z)

> Windows is the platform of choice for many students, game developers, and gamers. If AMD can better support it, it will have a great influence. What's more, AMD is very cost-effective. If everyone is used to HIP, it will be very scary habits, which they bring to work.

No one is using it, on their computer. So, first they need to make it work on Windows, then just after that make it run on linux, so if people want to publish and run on it they can?

---

### 评论 #58 — LiBoHanse (2023-04-15T12:13:13Z)

> Unfortunately, as a newcomer who just learned machine learning, I bought RX7900XTX because it was cheap, but I have to install dual systems to solve this problem. If God gives me a chance, I choose to send money to Nvidia.

Maybe you can try HSA_OVERRIDE_GFX_VERSION=10.3.0 to disguise as a Navi 21 card, which is currently supported, there are rumors that even 5700xt owners had their cards working with this trick. 

---

### 评论 #59 — xsacha (2023-04-16T21:23:14Z)

If they don't enable it by default using such workarounds, I suppose there's a reason.
Maybe loss of performance or unstable?

---

### 评论 #60 — iAvoe (2023-04-22T05:23:32Z)

If AMD make CUDA-->ROCm migration works like a charm then it would be a full support.
CUDA is something that physcologically important to the value for a GPU. Like even just playing games, people would choose to buy a PC first instead of gaming console, and people who owns a gaming console are likely to also have a PC, not to say more people are actually in need of working with a PC. (P.S. I have no data to backup what I'm saying, though)
Also, nice issue number :)

---

### 评论 #61 — iperov (2023-04-22T05:42:01Z)

technically, the only value of CUDA is that it has in its drivers tuned matmul programs for every Nvidia GPU.
This is why the size of the CUDA dll is so large.
Matmul is a critical part of MLP and Conv block performance. 
Without tune, matmul programs will be slow, 2x to 4x slower than CUDA.

---

### 评论 #62 — countradooku (2023-04-26T08:44:07Z)

https://github.com/RadeonOpenCompute/ROCm/pull/2085

what the actual fck ??????

---

### 评论 #63 — xsacha (2023-04-26T19:53:16Z)

> #2085
> 
> what the actual fck ??????

I called it. It has happened before

---

### 评论 #64 — countradooku (2023-04-28T10:32:20Z)

https://github.com/RadeonOpenCompute/ROCm/pull/2094

cool. no windows uspport in release notes. They fcked us again. Thank u AMD

---

### 评论 #65 — MoonRide303 (2023-04-28T18:56:15Z)

If a company doesn't care for their (potential) customers, then why customers should care about the company? I am tired of waiting, just ordered 4080. Hell overpriced and low on VRAM (for that price), but at least NV supports Windows.

---

### 评论 #66 — iAvoe (2023-04-28T22:01:00Z)

> If a company doesn't care for their (potential) customers, then why customers should care about the company? I am tired of waiting, just ordered 4080. Hell overpriced and a low on VRAM (for that price), but at least NV supports Windows.

These kind of technology take years to prefect, if you need to get things done then don't wait for them

---

### 评论 #67 — MoonRide303 (2023-04-28T23:57:52Z)

> > If a company doesn't care for their (potential) customers, then why customers should care about the company? I am tired of waiting, just ordered 4080. Hell overpriced and a low on VRAM (for that price), but at least NV supports Windows.
> 
> These kind of technology take years to prefect, if you need to get things done then don't wait for them

If it was matter of weeks I could probably wait a bit - but I didn't notice single clear statement from the AMD that they care, and that they're working on adding Windows support. Or when (even very roughly) it could happen. And CUDA is available since like 2007, so AMD had plenty of time to catch-up (if they wanted to).

---

### 评论 #68 — countradooku (2023-05-02T06:17:31Z)

Rocm 5.5 = no windows or Rx 7900 xtx support. Thank u AMD 

---

### 评论 #69 — iperov (2023-05-02T15:03:39Z)

at least microsoft is working on pytorch-directml

---

### 评论 #70 — Coderx7 (2023-05-02T15:08:20Z)

> at least microsoft is working on pytorch-directml

If pytorch is your thing, then https://github.com/llvm/torch-mlir should be your first choice imho. It supports all GPUs and OSes .


---

### 评论 #71 — iperov (2023-05-02T15:33:10Z)

@Coderx7 definitelly not

---

### 评论 #72 — Coderx7 (2023-05-02T17:37:52Z)

@iperov suit yourself then. use whatever tools make you happy 

---

### 评论 #73 — Milor123 (2023-05-07T11:17:24Z)

Oh come AMD!! , We need full support in RX6000 and RX7000 on Windows !!! 

---

### 评论 #74 — iperov (2023-05-10T09:25:22Z)

Microsoft Working With AMD on Expansion Into AI Processors
https://www.bloomberg.com/news/articles/2023-05-04/microsoft-is-helping-finance-amd-s-expansion-into-ai-chips

---

### 评论 #75 — Spacefish (2023-06-11T22:19:38Z)

> Microsoft Working With AMD on Expansion Into AI Processors https://www.bloomberg.com/news/articles/2023-05-04/microsoft-is-helping-finance-amd-s-expansion-into-ai-chips

This is probably regarding the Versal AI Cores from the Xilinx acquisition, which are included in recent Phoenix APUs ("Ryzen 7040 Series")..
AMD had a demo running a yolov5 net at a recent event on windows. Code is here: https://github.com/amd/RyzenAI-cloud-to-client-demo

As far as i understand it, this "AI Core" is a really small version of a Versal AI Core embeeded on the Phoenix Die, using the Xilinx Toolstack (Vitis AI).
Furthermore currently int8 is supported as a datatype, so you typically have to quantize your model.. Not sure if this is a hardware limitition (could be to save chip area, which would make sense) or purely a software stack limitation.

These "AI Cores" excell at inference, but you would have a hard time using them for learning / development.. They are essentially there to improve power usage on laptops while running inference on networks which do image segmentation for background blur in video conferencing or do noise supression of the audio stream / detection of background noise.. So you get better battery life.

So i wouldn´t bet on Rocm stack support being the main thing behind this Microsoft <-> AMD AI cooperation.. Guess they are just trying to make Teams more energy efficient / upcoming "AI features" in Windows 11...

---

### 评论 #76 — countradooku (2023-06-28T22:52:00Z)

good news. 5.6 doesnt support windows


---

### 评论 #77 — hwkim1127 (2023-07-01T13:32:43Z)

> good news. 5.6 doesnt support windows

thank you for the info. just ordered RTX 4090. simple

---

### 评论 #78 — valeriob01 (2023-07-01T13:59:26Z)

On Sat, 2023-07-01 at 06:33 -0700, hwkim1127 wrote:
> > good news. 5.6 doesnt support windows
> 
> thank you for the info. just ordered RTX 4090. simple
> 

It is simpler to switch to Linux.
> Message ID: ***@***.***>
> 
> [
> {
> ***@***.***": "http://schema.org",
> ***@***.***": "EmailMessage",
> "potentialAction": {
> ***@***.***": "ViewAction",
> "target": "
> https://github.com/RadeonOpenCompute/ROCm/issues/666#issuecomment-1615917389
> ",
> "url": "
> https://github.com/RadeonOpenCompute/ROCm/issues/666#issuecomment-1615917389
> ",
> "name": "View Issue"
> },
> "description": "View this Issue on GitHub",
> "publisher": {
> ***@***.***": "Organization",
> "name": "GitHub",
> "url": "https://github.com"
> }
> }
> ]


---

### 评论 #79 — iperov (2023-07-01T15:01:52Z)

> simpler to switch to Linux

ROFL

---

### 评论 #80 — AKL55 (2023-07-02T23:38:36Z)

> > good news. 5.6 doesnt support windows
> 
> thank you for the info. just ordered RTX 4090. simple

I was also going for a RX 7900 XTX, But i guess amd doesn't really want to sell gpus.

---

### 评论 #81 — Milor123 (2023-07-03T01:38:51Z)

> > > good news. 5.6 doesnt support windows
> > 
> > 
> > thank you for the info. just ordered RTX 4090. simple
> 
> I was also going for a RX 7900 XTX, But i guess amd doesn't really want to sell gpus.

Yep, if u need use IA like stable diffusion, and other extensions, gpt, llm models, and want use windows, we are dead :/

according to Ancient gamplays, maybe we could have it soon. [AMD ROCm is COMING and you can now run CUDA on your AMD GPU!
](https://youtu.be/-u41fsG6foc) 

I only hope that is works in the next month. For now, i cant recommend AMD for AI and serius work in windows. DirectML is very innestable, have many bugs and so so perfomance. In voice IA, is very horrible, is unusable. only few like diffusion goals works with directML

---

### 评论 #82 — iperov (2023-07-03T04:39:35Z)

> DirectML is very innestable, have many bugs and so so perfomance

DirectML itself has no bugs.
It has bugs only in pytorch version.
tensorflow-directml works fine, but tensorflow is dead of course.
onnxruntime with directml works very well and inference performance 0-20% slower than cuda in various cases.

---

### 评论 #83 — Milor123 (2023-07-03T09:41:37Z)

> > DirectML is very innestable, have many bugs and so so perfomance
> 
> DirectML itself has no bugs. It has bugs only in pytorch version. tensorflow-directml works fine, but tensorflow is dead of course. onnxruntime with directml works very well and inference performance 0-20% slower than cuda in various cases.

Not works nice bro, all have many bugs, cant use some extension, cant use some models, upscalers have problem with AMD, its holy crappy break, AMD not working for it in windows. If you is reading it and thinking buy AMD considering that you need IA, please dont do it, or wait for ROCm SDK for windows, and wait for a review.

---

### 评论 #84 — countradooku (2023-07-03T09:47:14Z)

> > > DirectML is very innestable, have many bugs and so so perfomance
> > 
> > 
> > DirectML itself has no bugs. It has bugs only in pytorch version. tensorflow-directml works fine, but tensorflow is dead of course. onnxruntime with directml works very well and inference performance 0-20% slower than cuda in various cases.
> 
> Not works nice bro, all have many bugs, cant use some extension, cant use some models, upscalers have problem with AMD, its holy crappy break, AMD not working for it in windows. If you is reading it and thinking buy AMD considering that you need IA, please dont do it, or wait for ROCm SDK for windows, and wait for a review.

i dont understand why amd are so stubborn to not support windows. They dont event support rdna 3 properly and about 8 months or more have passed

---

### 评论 #85 — Milor123 (2023-07-03T09:54:17Z)

> > > > DirectML is very innestable, have many bugs and so so perfomance
> > > 
> > > 
> > > DirectML itself has no bugs. It has bugs only in pytorch version. tensorflow-directml works fine, but tensorflow is dead of course. onnxruntime with directml works very well and inference performance 0-20% slower than cuda in various cases.
> > 
> > 
> > Not works nice bro, all have many bugs, cant use some extension, cant use some models, upscalers have problem with AMD, its holy crappy break, AMD not working for it in windows. If you is reading it and thinking buy AMD considering that you need IA, please dont do it, or wait for ROCm SDK for windows, and wait for a review.
> 
> i dont understand why amd are so stubborn to not support windows. They dont event support rdna 3 properly and about 8 months or more have passed

It happend by years really! AMD never cared about developing the SDK for Windows or addressing the needs and requests of its Windows users. Now they are doing it, I suppose because we are in the era of artificial intelligence. Who knows? I appreciate their effort, but I will never take this work seriously, and I won't recommend them again. I've had to suffer a lot to somewhat use AI tools on Windows, and AMD does nothing to advance it. Thanks to DirectML, we can partially run some things like Stable Diffusion (and even that is mediocre).

---

### 评论 #86 — countradooku (2023-07-03T09:57:05Z)

Yeah. I use DirectML too. on tensorflow it has a serious bug and last commit was two montha ago. And on pytorch i have a bug with itereators on dataloader (idk why) @Milor123 

---

### 评论 #87 — countradooku (2023-07-03T09:58:43Z)

They announed they will have rdna 3 this autumn. But nothing about windows support. That piss me off

---

### 评论 #88 — srogatch (2023-07-23T05:44:17Z)

The lack of Windows support in AMD ROCm is the reason why I'm not buying an HPC processor from AMD. I can't run PyTorch on Windows with an AMD GPU.

---

### 评论 #89 — Coderx7 (2023-07-23T06:28:41Z)

> The lack of Windows support in AMD ROCm is the reason why I'm not buying an HPC processor from AMD. I can't run PyTorch on Windows with an AMD GPU.

not true, you can still use pytorch with AMD cards on windows regardless of rocm support. use the pytorch mlir : https://github.com/llvm/torch-mlir

---

### 评论 #90 — iperov (2023-07-23T06:56:00Z)

@Coderx7 but who use it? it looks not user-friendly. No info how to install and use in windows. Btw MLIR is compiled, while pytorch model execution is eager-like. I think it's suxx.

---

### 评论 #91 — Coderx7 (2023-07-23T07:40:02Z)

> @Coderx7 but who use it? it looks not user-friendly. No info how to install and use in windows. Btw MLIR is compiled, while pytorch model execution is eager-like. I think it's suxx.

head to the [releases](https://github.com/llvm/torch-mlir/releases)  section and download the windows version and install it. it currently has python 3.11 version built automatically though you can also follow the instructions on the repos readme section and build it from source. either way you treat it like a normal pytorch installation.

not sure what you mean by the mlir is compiled but pytorch is eager mode though. how mlir is doing its job under the hood is transparent(i.e it doesn't affect how you run your codes, it's inner workings/implementation details are hidden to you) and you should be able to run your pytorch code normally. 

[nod-ai](https://github.com/nod-ai/SHARK/tree/main)  for one, has been using it extensively.

they have been doing this for a few years now and have a close collaboration with the core pytorch devs, so it's good. 

---

### 评论 #92 — Spacefish (2023-07-24T16:00:26Z)

Your pytorch commands are transformed into a compute graph under the hood, which is converted to MLIR which is compiled to accelerator specific (in this case RDNA*) specific machine code.. This is done on the fly.. Like with shaders and such ;)

MLIR is just an intermediate representation for machine learning data flow graphs... So every framework (like PyTorch, Tensorflow, ) can emit MLIR and that MLIR is picked up by the accelerator specific compiler, which converts the MLIR into accelerator specific machine code / configures the accelerator accordingly.. That way you can execute your PyTorch Project on different accelerators, like NPUs, FPGAs and GPUs without PyTorch explicitly supporting the accelerator or the accelerator explicitly supporting PyTorch.

You don´t need to compile it in advance.

---

### 评论 #93 — iperov (2023-07-24T16:14:12Z)

@Spacefish can you show example of installation and training some model on Nvidia/AMD gpu using pytorch-mlir?

---

### 评论 #94 — kelteseth (2023-07-28T10:41:44Z)

So with HIP now working on Windows, is this enough to start coding or is more needed? 

https://www.amd.com/en/developer/rocm-hub/hip-sdk.html

---

### 评论 #95 — scarsty (2023-08-13T12:45:20Z)

I think we need dnn

---

### 评论 #96 — johnnynunez (2023-08-13T15:43:42Z)

> I think we need dnn

Miopen and another. Expected in September

---

### 评论 #97 — saadrahim (2023-09-19T21:53:55Z)

HIP SDK was released earlier this year. Please follow our documentation to keep abreast of further development of the Windows support. 

---

### 评论 #98 — ghost (2023-10-02T03:44:45Z)

please. i can't live without it 

---

### 评论 #99 — Spacefish (2023-10-02T07:16:06Z)

> please. i can't live without it 

So why don't you install a Linux Distribution then?

---

### 评论 #100 — SunGreen777 (2023-11-05T02:21:04Z)

Post created 4 years ago, you are a huge corporation and cannot organize support for Automatic1111
Should I buy AMD? No, I'll take 3070, report this to your management.

---
