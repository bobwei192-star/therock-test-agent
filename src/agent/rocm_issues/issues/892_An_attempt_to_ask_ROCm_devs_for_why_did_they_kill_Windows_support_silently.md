# An attempt to ask ROCm devs for why did they kill Windows support silently?

> **Issue #892**
> **状态**: closed
> **创建时间**: 2019-09-26T16:11:10Z
> **更新时间**: 2024-10-24T19:43:41Z
> **关闭时间**: 2024-10-24T19:43:41Z
> **作者**: ugahugo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/892

## 描述

Just read this:

https://github.com/RadeonOpenCompute/ROCm/issues/18

following:

https://github.com/RadeonOpenCompute/ROCm/issues/666

which is following:

https://www.reddit.com/r/Amd/comments/b1kq1h/what_happened_to_gpu_programming_with_amd/

https://www.reddit.com/r/Amd/comments/bmyux8/opencl_no_longer_supported_by_amd/

https://www.reddit.com/r/Amd/comments/aun3y2/amd_cpus_no_longer_have_opencl_support/

This thread doesn't aim to insult any of ROCm developers but here I and, I am sure, other Windows-part of AMD community want to raise questions: WHAT THE HELL DID YOU DO?!

What did you do? You turned everything off last years, there is no any opportunity to work with GPU and C++ code under Windows, you killed everything, discontinued, cancelled, by your beautiful initiatives and here we ask you, why did you do that, why you report for 250K+ lines wrote for ROCm 1.6 release which is totally useless for 90+% PCs and users worldwide?

These are you who tied everything on Linux one the driver-level and these are you who promoted an initiative to cancel Windows support. So please, find a courage to put at least a few rational strings to answer for what you did.




---

## 评论 (31 条)

### 评论 #1 — himanshugoel2797 (2019-09-26T16:40:18Z)

If you check the third link you posted, it points out that the libraries are included with the drivers so there's no need for a separate thing. You can still write opencl code for GPUs as normal, even on Windows.

I recommend learning what you're talking about or asking for help before embarrassing yourself like this.

---

### 评论 #2 — ugahugo (2019-09-26T17:21:49Z)

You can write a code using C Runtime, not a C++ for Windows which is crazy for 2019. There is also a set of limitations regarding this case of "development under Windows and AMD".

@himanshugoel2797 , you can check #18 and what I posted here. I am sure you didn't write a single string of code for Windows AMD GPUs :).

---

### 评论 #3 — himanshugoel2797 (2019-09-26T17:34:52Z)

What limitations in particular are you facing in the case of "development under Windows and AMD"? You're free to assume whatever you want about me, but it only makes you look bad, especially given the website.

---

### 评论 #4 — ugahugo (2019-09-26T17:58:46Z)

C++ is just missing, is it not enough? Ok, here is the short list came into my head immediately:

- Overlapping implementation limitations;
- No nested parallelism support (which is dynamic parallelism in CUDA);
- No atomic operations support;
- Very limited threads sync mechanisms and there is no way to work with what is called "named barriers" in CUDA (you actually can do nothing in device code with so limited OCL AMD Windows support). No CUDA "threadfence" etc;
- No driver API support at all from OCL side;
- We don't use the virtual addressing but still it is missing.

You can even compare the HIP implementation over CUDA 10.1 etc, they did what they didn't for OCL, but still, it is for Linux only, because a whole ROCm team "can't (do) in Windows"

---

### 评论 #5 — himanshugoel2797 (2019-09-26T18:08:28Z)

So, let me get this right, you're complaining about HIP not having Windows support, by linking OCL related threads, and ranting about ROCm devs silently killing Windows support, even though they never promised it in the first place?

---

### 评论 #6 — ugahugo (2019-09-26T18:20:33Z)

So, now you're actually started interesting in the topic and not seeing me embarrassing anymore? 

Alright then,

Shortly: no C++, no normal programming in 2019 for Windows AMD GPUs. And this is not like they didn't implement it. They killed silently the OCL support (canceled), the only way to work under Windows (which was the C - runtime and driver approach, the old, limited and ugly) and published a communistic "Boltzmann Initiative" with implementations and support for Linux only. 

Latest work under Windows was published in 2015. And that was C runtime. 2015. C. What the heck they were doing in 2015 with C? That was even not fully implemented OCL 2.0! This is most like building Frankenstein's zombie those times! Now it is 2019 and everything is just dead. The whole AMD Windows market for 3rd party developers is closed and dead!

And, yes, the gstoner is one of who did that (you can find the information about that on AMD forum). He was one of the persons decided to cancel OCL implementation. lol, I just read that he left the AMD Radeon unit (being a director of it) for Intel. Great!

---

### 评论 #7 — himanshugoel2797 (2019-09-26T19:37:05Z)

You're still embarrassing yourself, I was just trying to steer the conversation in a more productive direction than your initial crazed rant. Doesn't seem to be working so I'll be dipping out.

---

### 评论 #8 — gstoner (2019-11-23T18:39:52Z)

Throw all the anger and angst at me as you want.  I know the real story.  ROCm did not do this to Windows.  


Also Boltzmann was not a Communist, please do no label him as so.   He was an Austrian physicist and philosopher that for lot of who were in Physics we have huge respect for his work he did in Statistical Mechanics, his discovery had profound effect on what we know in modern physics and even effect Deep learning.   

  I will tell you we worked hard with Microsoft on C++ AMP that had biggest potential to clean up the mess in GPU Computing created by CUDA well before SYCL was invented,  Microsoft stopped development.  With the limited resource we had at much tinnier scale continue spirt of that project through HCC as proof point for our HSA work.  Remember Window team shifted focus to Vulkan/PAL to support Gaming not compute. I had few think cooking before I left to bring goodness what I doing to your favorite platform. 

ROCm was fundamental platform and driver  foundation  to take on Tesla GPU and it driver platform.  It was from day one designed for HPC market and to support effort to win Supercomputer and latter to support large scale Deep Learning.  Ultimately it did win Exascale system, Frontier before I left which I am proud of the team hitting this accomplishment.  For me personally, I had accomplished core set of goals I had it was time to pass baton give back time to my family who lost me for the last 3 year working prove we take on massive machine Tesla/CUDA.   

At  the time the core market for Tesla was almost 100% Linux.  if you look to Microsoft Azure there is reason they run Linux especially with GPU for Deep Learning.   Even for NVIDA GPU server business is it fastest growing  business. 
<img width="566" alt="Screen Shot 2019-11-23 at 12 21 31 PM" src="https://user-images.githubusercontent.com/4129721/69483391-5fdd4100-0dec-11ea-8d5a-f631b30e0d78.png">

Ultimately it about funding, resource, focus of company and this comes from CXX and VP level    

I am still proud of what the team accomplished it was colossal effort for very small team, I just now watch from a different window.  I am sorry when I was in charge I could not make everyone happy but we had to focus getting platform in place for target set of customer and they were on linux.  

---

### 评论 #9 — ugahugo (2020-05-15T01:27:32Z)

Hey @gstoner,

It's funny you mentioned the NVIDIA sales report, and you referred to the datacenter revenue which is basically not the same as COGS (cost of goods).

My point is the decision to start with the Linux-based platform wasn't just unwise... I don't want to criticize you or your colleagues anymore. I am just sorry to telling you all of this right into your face (I wish this will work somehow in that case).

I am angry because I know you guys will never introduce Windows support because of no HAL implemented etc, you actually introduced NOTHING in order to even think of supporting Windows someday!

The AMP was just one nonsense but I believe this thing "happened" just because of lack of management charged for this initiative.

By pasting images of competitor's report you killing young (and not) businesses that wanted help AMD to grow and thrive. Together with other geniuses like Apple you finally closed another platform for any third-parties (I meant such nonsense as Metal and Nvidia driver support cancellation), but this is just another story of how big companies just sitting on the chair and can't do simple things while building something "GREAT".

__

And please stop comparing AMD with Nvidia. AMD introduced ISA years after Nvidia did (producing incompatible GPUs before GCN), and Volta architecture milestones for a whole AMD GPU is still something unreachable (you know what I meant by one-thread independent context support which is the HW solution for code branch conditional divergence which is critical in ML and other recursive-based applications). Hearing such comparison is nonsense. I really wish you luck with all of this great you guys building, that's how AMD will bury its GPU market share next decade.

This, current message, wasn't personally addressed to you, @gstoner. But I hope someday AMD GPU business unit will hear this and think about all once again and make tough but right decisions.

---

### 评论 #10 — YellowOnion (2020-07-23T07:49:07Z)

AMD clearly doesn't get it, Imagine you're college student, looking to built a gaming computer and do a bit of coding on the side. There's zero reason to buy AMD, you're slower with most games and Tensorflow just doesn't work.

Why the hell would I waste days/weeks of my life coding and porting Tensorflow to OpenCL when I can just buy an nvidia card and have it all up and running in a few minutes?

You're not keeping customers this way, You're making us choose between your inferior software and poor gaming support and the competition.

---

### 评论 #11 — MathiasMagnus (2020-09-22T22:54:51Z)

I know I'm late to the party, but, eh...

@himanshugoel2797 The hurdles of GPGPU development on Windows using AMD is that aside from an extremely outdated OpenCL runtime, there's nothing to chose from. (Vulkan and DX12 aren't really GPGPU, at least far from the core skill set of a "classic" GPGPU programmer). HIP isn't supported, SYCL used to work, before `cl_khr_spir` extension got axed from the OpenCL runtime (by the way, ~18 months later it's still erronously reported as present), the CPU runtime got ditched even though they got the best CPUs in town... basically you're screwed. I'm primarily an OpenCL/SYCL programmer, tangentially interested in HIP, but on Windows none of them really work. OpenCL performance is drastically behind any Linux runtime (AMDGPU, AMDGPU-PRO, ROCm)

@YellowOnion Yeah, AMD turned their steady quarterly losses into stead gains (mostly thanks to Ryzen, but still) and they did it mostly off the back of datacenter, where the big money is, not by the tiny margins laptops/DIY PCs have that college students are willing to buy.

Having that said, it's true that being ubiquitous is important and giving your users _some_ options to put your GPUs to good use is a minimum. As Linus Torvalds said, ARM won't take off in the datacenter until consumer devices won't readily be available. There is great power in tinkerers at home, outside office hours. Nvidia is just a far more compelling choice on Windows, as I could develop OpenCL, SYCL, CUDA reliably, whereas AMD only has half-baked OpenCL support on Windows. (As far as gaming is concerned, AMD is doing fairly well, just marginally behing, though the RX 580 and RX 5700 GPUs really hit the nail on the head.)

FWIW, people disappointed in AMD, [OpenCLOn12](https://github.com/microsoft/OpenCLOn12) will be the homework AMD didn't do and restore OpenCL and SYCL support.

---

### 评论 #12 — himanshugoel2797 (2020-09-22T23:29:00Z)

Haha, over the past year I've flipped. Having gotten some work that won't be supporting AMD simply because they need Windows support as an option, can't compromise on speed and being scientific compute have no qualms with requiring specific hardware. So I can understand the desire for Windows support on ROCm. I believe there's been talk from Khronos about building some sort of GPGPU platform on top of Vulkan compute, but otherwise you're right that we're screwed.

---

### 评论 #13 — ugahugo (2020-11-10T23:16:21Z)

> Haha, over the past year I've flipped. Having gotten some work that won't be supporting AMD simply because they need Windows support as an option, can't compromise on speed and being scientific compute have no qualms with requiring specific hardware. So I can understand the desire for Windows support on ROCm. I believe there's been talk from Khronos about building some sort of GPGPU platform on top of Vulkan compute, but otherwise you're right that we're screwed.

>If you check the third link you posted, it points out that the libraries are included with the drivers so there's no need for a separate thing. You can still write opencl code for GPUs as normal, even on Windows.

It's funny that it took a year for you to prove you were lying to the public about "even on Windows" but for me, it's not a surprise just as no surprise that Radeon devs did nothing for these years because Linux red-eyers "can't in Mac OS or Windows by default"

---

### 评论 #14 — ugahugo (2020-11-10T23:19:04Z)

if you look to Microsoft Azure there is reason they run Linux especially with GPU for Deep Learning. Even for NVIDA GPU server business is it fastest growing business.
> <img alt="Screen Shot 2019-11-23 at 12 21 31 PM" width="566" src="https://user-images.githubusercontent.com/4129721/69483391-5fdd4100-0dec-11ea-8d5a-f631b30e0d78.png">

Interesting to see how these dreamy charts came real for the Radeon unit this year. I believe it is still just wet dreams because of bad decisions / management / skills (no skills in Windows / Mac OS)

---

### 评论 #15 — kirawi (2020-12-08T17:36:54Z)

I'm usually not one for such angry posts, but it feels like this one was necessary to drive home how subpar AMD is in comparison to Nvidia even for non-programmers, i.e. Blender. I may dislike Nvidia's practices, but at least I can trust that their products will work and deliver everything I need on Windows. However, I realize that the devs don't really have much say in what the company does.

---

### 评论 #16 — JonathanDotCel (2022-09-28T23:32:33Z)

> I'm usually not one for such angry posts, but it feels like this one was necessary to drive home how subpar AMD is in comparison to Nvidia even for non-programmers, i.e. Blender. I may dislike Nvidia's practices, but at least I can trust that their products will work and deliver everything I need on Windows. However, I realize that the devs don't really have much say in what the company does.

Same...
But I've wasted several days now trying to use Ubuntu 18.04 LTS, 20.04 LTS and 22.04 LTS with official packages.
All seem to have to varying degrees of issues ranging from "if you updated it (even during the installer), you're screwed" to packages depending on specific (now missing) python versions (which would've been an easy update).

Meanwhile, I can just use cuda.
So many exciting ML projects right now, nvidia has the edge for me.

---

### 评论 #17 — WASasquatch (2022-09-30T16:38:30Z)

AMD/ATI is a self-sabotaging joke, for 20+ years now. The boards over there are so out of touch with the general consumer, let alone programmers, or even reality. Every move has been an industry flop. I'm sure AMD GPUs are going to end the same way as LG's phone line. Doing everything no one wants, until they've cut themselves too deep, and the whole limb has to be cut off. 

I've only ever used AMD and I'm just done. Over it. Just like I used LG phones, and the last couple flag ships were so out of touch, even compared to their last, it's no wonder they dropped the ball. I honestly don't know how companies this big conceive the goal posts they put out for themselves, let alone their products to begin with. Has focus testing just gone out the window? 

---

### 评论 #18 — saadrahim (2022-09-30T18:58:30Z)

https://github.com/amd/rocm-examples#windows-1


---

### 评论 #19 — JonathanDotCel (2022-10-01T12:08:36Z)

> 

Thanks for the link, but it really just serves to elucidate the frustration people are having.

Prerequisites (windows):
"ROCm toolchain for Windows (No public release yet)"

Or from Visual Studio:
"Install HIP to build using the HIP build tools."  (No ROCm HIP SDK for windows)

Even if it did work, There's no reason I should have to build from source on a fixed platform like Windows, and there's not a huge motivation for ML libs & projects to support "random git commits" of the project, vs a semi stable, versioned release where everyone benefits from using the same or similar versions, locked down APIs, documentation, support, etc.

---

### 评论 #20 — MathiasMagnus (2022-10-10T07:40:07Z)

@JonathanDotCel Nobody's expecting you or anyone to build from source. It doesn't come as a surprise that there are working compilers for Windows in the wild, otherwise Blender couldn't ship. The runtime has already been shipping with drivers for over a year now. Rest assured that AMD won't be sitting on a compiler if it was known to have no issues and ecosystem coverage is otherwise in sufficiently good shape. If you follow along the [code repositories](https://github.com/ROCmSoftwarePlatform/rocRAND/commit/8dbfc31974ce5be433fce70e52388ac0203d2943#diff-1e7de1ae2d059d21e1dd75d5812d5a34b0222cef273b7c3a2af62eb747f9d20a), you can see that Windows support is spreading steadily and has been for a while now. I know everyone is eager to get HIP into their hands, but there are many aspects of making a proper release (precisely because no one is expected to build from source) and there's no reason to release it only to spawn floods of comments on demanding tooling support, library coverage, device coverage or whatever kinds of pains they may have. You listed some things yourself:
> versioned release where everyone benefits from using the same or similar versions, locked down APIs, documentation, support, etc.

I know it doesn't help hearing vague hints at whenever it will land, but AMD employees can't and won't make public statements on that (neither will I). There are people hard at work on connecting all the dots.

---

### 评论 #21 — JonathanDotCel (2022-10-10T09:44:03Z)

@MathiasMagnus Cheers for the detailed response, but it would be nice if there was some official communication, vaguely detailing this.

A quick "the first page of stuff from google" search returns little in the way of information.
E.g. a post on Blender's devtalk explaining in Dec '21 that they have a beta version -- I wouldn't even have looked for that unless you'd tipped me off that there was support in the wild.

A 404:
https://docs.amd.com/bundle/HIP_Programming_Guide_v4.5/page/Programming_with_HIP.html

A 5 year old issue, alluding only to the driver package shipping with amdhip.dll.
https://github.com/ROCm-Developer-Tools/HIP/issues/84

And there are breakages installing from a clean install of Ubuntu 2018.4, 2020.4 and 2022.4 (or updated installs).

It's *very* easy to feel like we're being left in the dark here, or that the drive to roll out wider support has dried up somewhat.




---

### 评论 #22 — MathiasMagnus (2022-10-10T12:01:49Z)

The 404 is fairly recent and is quite a large facepalm indeed.

---

### 评论 #23 — Rmalavally (2022-10-10T13:47:36Z)

@JonathanDotCel @MathiasMagnus 

To access the ROCm v4.5 HIP Programming Guide, see:

https://docs.amd.com/bundle/HIP-Programming-Guide-v4.5/page/Introduction_to_HIP_Programming_Guide.html

Or 

Users can click[ Release Documentation](https://docs.amd.com/category/Release%20Documentation) and refer to the documentation for any release. 

As always, please contact us for ROCm documentation questions or concerns.

ROCm Documentation Team



---

### 评论 #24 — Looong01 (2023-01-01T17:05:59Z)

Hey, bro. You can try DirectML on Radeom Cards.
Like PyTorch for DML or TensorFlow for DML on Win/Wsl2.

Please don't afflict yourself.

After having been afflicted by programming on Radeom for the last 5 days, I give it up.

---

### 评论 #25 — JonathanDotCel (2023-01-02T11:14:22Z)

> Hey, bro. You can try DirectML on Radeom Cards. Like PyTorch for DML or TensorFlow for DML on Win/Wsl2.
> 
> Please don't afflict yourself.
> 
> After having been afflicted by programming on Radeom for the last 5 days, I give it up.

TBH, after weeks of faffing around I bought a 3080 and everything worked out of the box.

Literally none of the recommended AMD OS setups I tried were working (and often, that was due to requiring just a simple python update or the like), and I got a bit sick of "just compile x" or "just use y instead". No thanks.
100% done with AMD dragging their heels with updates, documentation, etc.



---

### 评论 #26 — Looong01 (2023-01-02T11:25:53Z)

> > Hey, bro. You can try DirectML on Radeom Cards. Like PyTorch for DML or TensorFlow for DML on Win/Wsl2.
> > Please don't afflict yourself.
> > After having been afflicted by programming on Radeom for the last 5 days, I give it up.
> 
> TBH, after weeks of faffing around I bought a 3080 and everything worked out of the box.
> 
> Literally none of the recommended AMD OS setups I tried were working (and often, that was due to requiring just a simple python update or the like), and I got a bit sick of "just compile x" or "just use y instead". No thanks. 100% done with AMD dragging their heels with updates, documentation, etc.

Alright, what I'm talking about above may be a bit confusing.
I mean, I spent a lot of time trying to run the native ROCm version of PyTorch from official in Windows/WSL2, and I still failed.

And I go to use DirectML version of PyTorch and it works well.
The backend of this version is DirectML, not ROCm. It support any GPU that support DirectX12 on Windows10/11, including Nvidia, AMD and Intel.

Here is the document:
https://learn.microsoft.com/en-us/windows/ai/directml/gpu-pytorch-windows

---

### 评论 #27 — Looong01 (2023-01-02T11:30:33Z)

> > Hey, bro. You can try DirectML on Radeom Cards. Like PyTorch for DML or TensorFlow for DML on Win/Wsl2.
> > Please don't afflict yourself.
> > After having been afflicted by programming on Radeom for the last 5 days, I give it up.
> 
> TBH, after weeks of faffing around I bought a 3080 and everything worked out of the box.
> 
> Literally none of the recommended AMD OS setups I tried were working (and often, that was due to requiring just a simple python update or the like), and I got a bit sick of "just compile x" or "just use y instead". No thanks. 100% done with AMD dragging their heels with updates, documentation, etc.

And these days I noticed that Microsoft has another amazing project, called Antares. It is an automatic engine for multi-platform kernel generation and optimization. Supporting CPU, CUDA, ROCm, DirectX12, GraphCore, SYCL for CPU/GPU, OpenCL for AMD/NVIDIA, Android CPU/GPU backends.

The author said that it will make the ROCm version of PyTorch successful running in WSL2. I'm trying it.

Here is the repo:
https://github.com/microsoft/antares

---

### 评论 #28 — JonathanDotCel (2023-01-02T11:36:03Z)

> > > Hey, bro. You can try DirectML on Radeom Cards. Like PyTorch for DML or TensorFlow for DML on Win/Wsl2.
> > > Please don't afflict yourself.
> > > After having been afflicted by programming on Radeom for the last 5 days, I give it up.
> > 
> > 
> > TBH, after weeks of faffing around I bought a 3080 and everything worked out of the box.
> > Literally none of the recommended AMD OS setups I tried were working (and often, that was due to requiring just a simple python update or the like), and I got a bit sick of "just compile x" or "just use y instead". No thanks. 100% done with AMD dragging their heels with updates, documentation, etc.
> 
> And these days I noticed that Microsoft has another amazing project, called Antares. It is an automatic engine for multi-platform kernel generation and optimization. Supporting CPU, CUDA, ROCm, DirectX12, GraphCore, SYCL for CPU/GPU, OpenCL for AMD/NVIDIA, Android CPU/GPU backends.
> 
> The author said that it will make the ROCm version of PyTorch successful running in WSL2. I'm trying it.
> 
> Here is the repo: https://github.com/microsoft/antares

Aaah cheers, nice one.
DirectML was not an option for me right now, but Antares seems exciting - thanks for the info!


---

### 评论 #29 — ehartford (2023-01-19T04:58:13Z)

> > > Hey, bro. You can try DirectML on Radeom Cards. Like PyTorch for DML or TensorFlow for DML on Win/Wsl2.
> > > Please don't afflict yourself.
> > > After having been afflicted by programming on Radeom for the last 5 days, I give it up.
> > 
> > 
> > TBH, after weeks of faffing around I bought a 3080 and everything worked out of the box.
> > Literally none of the recommended AMD OS setups I tried were working (and often, that was due to requiring just a simple python update or the like), and I got a bit sick of "just compile x" or "just use y instead". No thanks. 100% done with AMD dragging their heels with updates, documentation, etc.
> 
> Alright, what I'm talking about above may be a bit confusing. I mean, I spent a lot of time trying to run the native ROCm version of PyTorch from official in Windows/WSL2, and I still failed.
> 
> And I go to use DirectML version of PyTorch and it works well. The backend of this version is DirectML, not ROCm. It support any GPU that support DirectX12 on Windows10/11, including Nvidia, AMD and Intel.
> 
> Here is the document: https://learn.microsoft.com/en-us/windows/ai/directml/gpu-pytorch-windows

I tried that DirectML link but it only had instructions for CPU
How did you make it work with your AMD GPU?

---

### 评论 #30 — Looong01 (2023-01-19T06:30:35Z)

> > > > Hey, bro. You can try DirectML on Radeom Cards. Like PyTorch for DML or TensorFlow for DML on Win/Wsl2.
> > > > Please don't afflict yourself.
> > > > After having been afflicted by programming on Radeom for the last 5 days, I give it up.
> > > 
> > > 
> > > TBH, after weeks of faffing around I bought a 3080 and everything worked out of the box.
> > > Literally none of the recommended AMD OS setups I tried were working (and often, that was due to requiring just a simple python update or the like), and I got a bit sick of "just compile x" or "just use y instead". No thanks. 100% done with AMD dragging their heels with updates, documentation, etc.
> > 
> > 
> > Alright, what I'm talking about above may be a bit confusing. I mean, I spent a lot of time trying to run the native ROCm version of PyTorch from official in Windows/WSL2, and I still failed.
> > And I go to use DirectML version of PyTorch and it works well. The backend of this version is DirectML, not ROCm. It support any GPU that support DirectX12 on Windows10/11, including Nvidia, AMD and Intel.
> > Here is the document: https://learn.microsoft.com/en-us/windows/ai/directml/gpu-pytorch-windows
> 
> I tried that DirectML link but it only had instructions for CPU How did you make it work with your AMD GPU?

Did your code return that any operator does not support on DML backend and it will go back to CPU?

---

### 评论 #31 — sorpfenvier (2023-04-20T04:41:40Z)

I'm just a passer-by who do not know much in programming. But I suppose that, seeing the boom of AI related contents and the enormous demand on consumer level GPUs with the support for high efficiency AI computing (which mostly means, CUDA, nowadays), the AMD management team would feel a little regretful. However, they may still feel nothing since they did make a lot money in the B2B market with their Linux support.

---
