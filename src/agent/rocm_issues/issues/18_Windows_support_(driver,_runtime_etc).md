# Windows support (driver, runtime etc)

> **Issue #18**
> **状态**: closed
> **创建时间**: 2016-07-12T19:01:37Z
> **更新时间**: 2019-04-13T20:09:55Z
> **关闭时间**: 2016-07-12T21:44:32Z
> **作者**: ugahugo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/18

## 描述

See subj.

Wondering why AMD always releases their frameworks on Linux / Unix platforms only.

Guys, do you have in mind that GPGPU developers can't build their products for Windows users (98% of them in mass markets)?

This problem relates to the problem of compiling C++11 - compatible code for AMD GPU as well. I see that AMD puts a lot of efforts to use HIP infrastructure to build nvcc - compatible code (with its own C++ implementation) but all of these efforts are useless considering no Windows support. Yet.


---

## 评论 (30 条)

### 评论 #1 — briansp2020 (2016-07-12T20:54:18Z)

This is just an observation as an outsider.
I think ROCm requires extensive OS support. So, for AMD to support Windows, MS has to be willing to modify Windows to accommodate it. Given that 1) AMD cannot change Windows development schedule/roadmap. 2) HPC business is high margin business and use Linux. I think it makes sense for them to target Linux and go after HPC/Datacenter business first.

Just my 2 cents.


---

### 评论 #2 — ugahugo (2016-07-12T21:10:06Z)

@briansp2020,

The typical open-sourcer overview you posted here. So why didn't ask Apple to do the same? And how the NVIDIA is able to build its own dev driver years ago (!) for all OSes including C++ compiler support? Interesting to know your opinion.

And please do not even tell me that HPC / GPGPU business is something enterprise - oriented only. AMD already missed mass markets such as automobile etc. But I don't care, I'm just wondering that huge corporation supports C99 - compatible compilers only for Windows OS (the most popular OS on the planet, CO). Today is 2016. Great job, AMD, you did.

The AMD politics / roadmap for last five years leads company to decreasing market share (people vote using their money). Only Apple contracts keep the AMD GPU division alive.

I'm sorry for the offtopic. 

I really start thinking that since AMD purchased ATI they want ruin the last one as MS did with Nokia (but this is just my personal opinion, do not keep it in mind).


---

### 评论 #3 — briansp2020 (2016-07-12T21:29:23Z)

@ugahugo 
What AMD is doing with ROCm is much more than what NVidia is currently offering. When NVidia launches a kernel, it has to ask OS to launch it for the user. With ROCm, kernel launch does not involve OS system call. This seemingly simple difference actually requires huge change in OS and is fundamental in making GPU to become as important as CPU.

If you are interested, read up on HSA and its advantages over traditional GPGPU programming model. It is true that AMD has suffered market loss and had many missteps in the past. They had problem getting people to rewrite their applications using OpenCL. However, I think they have found the right programming model to promote. Since they do not have the resources to do everything, they have to do what will make them most money first. I'm sure MS Windows & Apple MAC support will come in due time.


---

### 评论 #4 — ugahugo (2016-07-12T21:48:44Z)

What's the exact reason of closing this topic?

There is no official answer for the issue, @gstoner, could you provide some details please?


---

### 评论 #5 — gstoner (2016-07-12T22:01:30Z)

We here your request for Windows support of the ROCm tools, but the direction you took the conversation became unprofessional.   For ROCm the issue management tool is for exactly this issue and feature requests it where the conversation should have stopped.  

Thank you for your input. 


---

### 评论 #6 — akostadinov (2018-03-27T13:09:37Z)

We should also praise AMD for going the open source route instead of creating yet another walled garden. And this is for the long term benefit of all developers and users. I wish things could get ready faster and I'm sure there is always room to improve how things are done. But they deserve more respect IMO than what I see in this discussion.

Sorry for the off topic but couldn't resist.

---

### 评论 #7 — gstoner (2018-03-27T14:01:23Z)

Guys,  Step 1 is getting foundation on Windows that support what we doing.  This is happing.   We will have HIP and the LC compiler on Windows the work is in full earnest.  This step one.  Once we have this in place,  everything else can fall into place.    

---

### 评论 #8 — briansp2020 (2018-03-27T20:01:44Z)

ETA? 

Just kidding. I know you can't really say it in public. But glad to hear confirmation of windows support.

One serious question. once windows support arrives, would it be possible to use ROCm docker image on window? I'm ok with using linux for ML development and stuff since ML frameworks are better supported under linux. But I still prefer windows for all other things. So, I think it would be perfect for me if I can have ROCm in docker under windows (or ROCm in Linux subsystem for windows, which ever is easier). Do you think that will be a possibility in the near future?

---

### 评论 #9 — gstoner (2018-03-27T20:24:02Z)

ROCm Linux Docker would be a bridge too far, we do not have the plumbing in window os 

greg

---

### 评论 #10 — ugahugo (2018-04-09T20:48:20Z)

I really do my best to do not be an offensive idiot but...

>>

Guys, Step 1 is getting foundation on Windows that support what we doing. This is happing. We will have HIP and the LC compiler on Windows the work is in full earnest. This step one. Once we have this in place, everything else can fall into place.
--

...Ok, so,

It took two years to tell us that you actually started your work on Windows driver for HIP compiler (and so far no Mac OS / UNIX support announced yet)...

HIP tricky compiler support means lots of consequences such as no Driver API direct support, lots of difficulties in work with ISA ASM AMD did etc.

Also, HIP compiler will definitely kill any program that operates in low latency mode because of solution requirements (e.g. frames more than 200 etc).

Good job guys, hope that your HSA will do all things you do (for whom actually? For 3rd party developers? For what sort of developers? Who works on the biggest market / Windows OS? lmao)

---

### 评论 #11 — ghostplant (2019-02-14T05:15:00Z)

@gstoner Any AMD compiler available to generator **HSACO code or LLVM-IR only** on windows platform? I just require this kind of compiler to get the device code on windows like what `KMDUMPISA=1` does on Linux does, **not necessarily to get the full ROCm stack for windows such as their execution and related driver**. Thanks!

---

### 评论 #12 — MathiasMagnus (2019-04-13T14:48:30Z)

It's simply astonishing to see how neglected Windows is in terms of SW support. I'm out of words here...

---

### 评论 #13 — gbeatty (2019-04-13T17:13:02Z)

Agreed. It's no wonder adoption is low

---

### 评论 #14 — ugahugo (2019-04-13T17:25:40Z)

Almost three years passed since I started this thread and still no changes... 

All efforts they put to support obsolete Thrust and TensorFlow versions may be measured with 0 output (because libraries version support is meaningless for most use cases in production, nobody will deploy obsolete stuff in the Web).

We built a low-latent GPU AUDIO brand technology using CUDA and its driver API. Since 2016, Nvidia released RTX technology, custom precision support and other incredible things based on new hardware and what we have here, at AMD, for third-party developers? 2019 and still no C++ support for Windows!

---

### 评论 #15 — ghostplant (2019-04-13T17:35:24Z)

@ugahugo There is a way to run ROCm applications using Windows Bash system, which has been verified.

---

### 评论 #16 — ugahugo (2019-04-13T17:37:05Z)

> @ugahugo There is a way to run ROCm applications using Windows Bash system, which has been verified.

Yeah but still there is no way to compile them under Windows, correct?

---

### 评论 #17 — ghostplant (2019-04-13T17:47:07Z)

@ugahugo Compiling also works using Windows Bash of course, as long as you install ROCm toolkit in Windows Bash.

---

### 评论 #18 — ugahugo (2019-04-13T18:11:17Z)

> @ugahugo Compiling also works using Windows Bash of course, as long as you install ROCm toolkit in Windows Bash.

Excuse me, may I ask you to link any appropriate example? Am I correct that ROCm driver is a kinda implemented for Windows, so I'm able to compile HIP sources under Windows and run the output binary?

I checked ROCm Kernel Driver page and no updates so far regarding Windows or Mac. I'm sure you misunderstood me. "These guys" told us several times that entire ROCm code is built upon its driver which depends on Linux internals... This is a fundamental reason that ROCm will stay useless and will die soon (2-3 years when corporate sector will be lost again by AMD), "Linux red eyeers" doesn't know such things as HAL and way to use such an abstractions, that's actually why Linux will never go to mass market and actually, this is another form of open-source vs commercial development paradigm dilemma (open-source will never handle such problem as "support anything on everything", it requires to put so much effort in a very strict way, people shall be managed by supervisor, which is almost impossible)

Releasing ROCm driver is the same-level-problem as releasing some driver for some laptop built for Linux only but for Windows.

---

### 评论 #19 — ghostplant (2019-04-13T18:19:33Z)

Compiling HIP sources doesn't need ROCm driver, you can try compiling a hip code yourself over WSL.

---

### 评论 #20 — ugahugo (2019-04-13T18:24:39Z)

> WSL

This means that it will work with HIP over CUDA - implemented code, so no CUDA driver API and other stuff? I shall handle any third-party library calls within my code etc? So this means almost no usefulness...

e.g.: https://github.com/ROCm-Developer-Tools/HIP/blob/master/docs/markdown/hip_porting_driver_api.md

For 2019, same, I shall handle just a mess of code... This means I have to overwrite hundreds of thousands of our code which is not a solution for us.

Also, there is no guarantee that this will perform on AMD GPU with an equivalent level of performance that it does on nVidia using its proprietary driver.

---

### 评论 #21 — ugahugo (2019-04-13T18:32:46Z)

https://github.com/ROCm-Developer-Tools/HIP/blob/master/docs/markdown/hip_porting_guide.md

I also shall wrap calls by ROCm infrastructure which supports the obsolete versions of libraries. A whole solution is just meaningless, sorry. 

The only way to make an appropriate workaround is to build ROCm driver for each OS. 

---

### 评论 #22 — ghostplant (2019-04-13T18:33:47Z)

@ugahugo It is not related to CUDA, the compilation of HIP for HCC platform is always working at the moment for WSL, including generating related device codes and binaries, and you can regard it as cross compiling. However, if you want to execute it on Windows, it is possible but requires some virtualization techniques.

---

### 评论 #23 — ugahugo (2019-04-13T18:41:33Z)

> @ugahugo It is not related to CUDA, the compilation of HIP for HCC platform is always working at the moment for WSL, including generating related device codes and binaries, and you can regard it as a cross compiling. However, if you want to execute it on Windows, it is possible but requires some virtualization techniques.

yes, I know that. But maximum you may achieve by putting big efforts to do that is the inpredicteble performance on obsolete libraries and Linux-based stack...

The point of why the ROCm will never support a normal way of HIPify your solution or will never support other ways to get C++ for AMG GPUs under Windows because of the fact that only 2 persons are sitting in a chair and deciding this:

https://github.com/HSAFoundation

One is a Linux Kernel Developer, so this is why you will always have anything on Linux stack, the whole Boltzmann Initiative was designed only for this and this was the original mistake. The only hope is that AMD will fail on the market again and this initiative will be frozen and, e.g., OCL 2.1. will finally be supported by AMD GPUs (and we will see C++ for AMG GPUs for almost any platform we want).

---

### 评论 #24 — ghostplant (2019-04-13T18:43:28Z)

Is OCL 2.1 not supporting Windows at the moment?

---

### 评论 #25 — ugahugo (2019-04-13T18:44:08Z)

I ask @gstoner to do not clean offtopic comments because people will finally understand the nature of your decision and never will ask questions about AMD GPUs C++ on Windows support regarding ROCm environment you develop (this is actually what 3rd-party developers need from AMD, not a new environment to work with and you do). I hope, you understand me very well and thank you.

---

### 评论 #26 — ugahugo (2019-04-13T18:45:49Z)

> Is OCL 2.1 not supporting Windows at the moment?

OCL 2.1 for AMD GPUs which shall support C++ - not. This fact is my original point where I started to look for any other solution and why I (and most of the developers, I'm sure) came here.

And even 2.0 for AMG GPUs are not (regarding an OCL 2.0 full-feature set). Sorry for the off topic again. 

---

### 评论 #27 — ghostplant (2019-04-13T18:50:04Z)

@ugahugo It's interesting AMD OCL 2.x is not supporting Windows at the moment?

---

### 评论 #28 — ugahugo (2019-04-13T18:51:42Z)

> @ugahugo It's interesting AMD OCL 2.x is not supporting Windows at the moment?

Yes, and Mr. Stoner is directly responsible for this fact...

https://community.amd.com/thread/209410

---

### 评论 #29 — ghostplant (2019-04-13T19:12:53Z)

@ugahugo So what is this file used for in Windows: `amdocl64.dll`?

---

### 评论 #30 — jlgreathouse (2019-04-13T20:09:44Z)

Hello @ugahugo 

I'm locking this conversation because it has devolved from a technical request to insults and griping. This is not a forum for insulting members of the ROCm team. Thank you.

---
