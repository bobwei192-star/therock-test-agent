# Vega FE slow OpenCL performance for Mining applications

> **Issue #147**
> **状态**: closed
> **创建时间**: 2017-07-03T22:14:05Z
> **更新时间**: 2018-08-24T00:47:42Z
> **关闭时间**: 2018-08-24T00:47:42Z
> **作者**: jstefanop
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/147

## 描述

Vega FE has very slow OpenCL performance under ROCm 1.6 and Ubuntu 16.04. Card Boots and initialized properly, and confirmed that Vega is running at full clocks during openCL tests via SMI utility. 

Performance is about 20% of what is achieved under same OpenCL app under windows driver. 

Same performance is also verified under AMDGPU-PRO with ROCm package installed. 

---

## 评论 (62 条)

### 评论 #1 — gstoner (2017-07-04T04:28:44Z)

How may PCIe lanes are exposed
On Jul 3, 2017, at 5:14 PM, jstefanop <notifications@github.com<mailto:notifications@github.com>> wrote:


Vega FE has very slow OpenCL performance under ROCm 1.6 and Ubuntu 16.04. Card Boots and initialized properly, and confirmed that Vega is running at full clocks during openCL tests via SMI utility.

Performance is about 20% of what is achieved under same OpenCL app under windows driver.

Same performance is also verified under AMDGPU-PRO with ROCm package installed.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/147>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuQl5g7B5Xy4wOlzxSgK3M_6BxjYnks5sKWeugaJpZM4OMuLL>.



---

### 评论 #2 — gstoner (2017-07-04T18:00:33Z)

For what application  minner applications are you running

---

### 评论 #3 — jstefanop (2017-07-04T18:06:57Z)

Not sure what you mean by last comment, but tested on both 16x and 1x lanes. Both lanes do full performance under windows, and both do the same ~20% under Rocm. 

We just got in a ryzen 5 with b350 motherboard and will test against that as well. 

---

### 评论 #4 — gstoner (2017-07-04T18:11:37Z)

What application.

Get Outlook for iOS<https://aka.ms/o0ukef>



On Tue, Jul 4, 2017 at 1:07 PM -0500, "jstefanop" <notifications@github.com<mailto:notifications@github.com>> wrote:


Not sure what you mean by last comment, but tested on both 16x and 1x lanes. Both lanes do full performance under windows, and both do the same ~20% under Rocm.

We just got in a ryzen 5 with b350 motherboard and will test against that as well.

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/147#issuecomment-312929067>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuaI9a_-cLUqdrelEEnspydXoiStvks5sKn9CgaJpZM4OMuLL>.


---

### 评论 #5 — gstoner (2017-07-04T20:00:52Z)

Here is my problem,  I have no idea how your measuring performance, or what the application you're measuring performance on.  

I do now know if it is memory bound application or a compute-bound application.   Does the application use single precision, integer only. 

I just know you're making general statements about performance which we need to narrow down to specifics that are actionable. 



---

### 评论 #6 — jstefanop (2017-07-05T22:06:00Z)

The vega card is specifically (or will hopefully be) used on a new platform we are building for HPC solution using memory hard proprietary algorithms for machine learning type application. We do also build mining servers for some clients, so i can confirm this issue is also present on those algorithms. 

Here are some open source tests you can use to profile the kernel and see where the bottleneck in the driver is. 

Basic OpenCL Memory bandwidth test: github.com/krrishnarraj/clpeak
Getting about 260 gb/s on Vega FE on ROCm kernel, which is about half its theoretical performance (should come close to achieving that on this test). 
Polaris card on same system does about 190gb/s which is about 90% of its theoretical bandwidth. 

Open Source Ethereum Kernel: https://github.com/Genoil/cpp-ethereum
Vega FE on ROCm does ~5 mh/s
Polaris on ROCm does ~24 mh/s
Vega FE on windows Radeon Pro driver does ~30 mh/s

---

### 评论 #7 — JustinTArthur (2017-07-05T22:38:57Z)

Can corroborate @jstefanop's findings. Using Linux 4.9 from [ROCK-Kernel-Driver master](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver) in Gentoo and the pre-compiled ROCm stack and card firmwares from AMDGPU-Pro 17.20, I get around 5 mh/s in [ethminer](https://github.com/ethereum-mining/ethminer). rocm-smi never reads a power level above 7 watts, regardless of performance level or fan level settings.

Happy to stop by with my motherboard+linux this week if it can help w/ testing, @gstoner.

---

### 评论 #8 — gstoner (2017-07-06T05:26:27Z)

@JustinTArthur The ROCm -SMI output is concerning, sounds like the clock are not right on your setup 

---

### 评论 #9 — gstoner (2017-07-06T05:33:51Z)

Are you guys trying run max clock on Frontier Edition, aka 1600 MHz, it will not run sustained with throttling.  you need to dial fans up and run around 1400 MHz, 

---

### 评论 #10 — JustinTArthur (2017-07-06T18:37:21Z)

Here is a quick recording of me watching the SMI stats, starting the miner, increasing fan speed then decreasing clock speeds. Very little difference is made to performance or reported wattage.
![vega_fe_ethminer_smi_tests](https://user-images.githubusercontent.com/577312/27926786-3a4752d2-624f-11e7-9409-6f7f2f44557e.gif)

The OpenCL kernel used is [here](https://github.com/ethereum-mining/ethminer/blob/master/libethash-cl/ethash_cl_miner_kernel.cl).

Some common algorithms miners buy GPUs for these days:
* Keccak (SHA-3) — Ethereum, Monero
* Blake  — zCash, Monero
* AES  — Monero
* scrypt  — Litecoin
* SHA-2  — Bitcoin, Peercoin, Unbreakable (all less common on GPUs now)

Many of the hashing pipelines employ reading and writing from large blocks of memory of dynamic size to make the pipelines harder to replicate on-chip in ASICs. There's an overlap with the pay-for-password-help community that use these GPUs primarily for SHA-1, SHA-2, SHA-3, MD5, Blake, bcrypt, scrypt, PBKDF2, and others.

---

### 评论 #11 — jstefanop (2017-07-06T19:38:16Z)

@gstoner like justin mentioned there is no need to run vega at full clocks for the memory bound kernels we work with. For example the same ethminer kernel runs at ~25 mh/s on windows system with Radeon Pro drivers on Vega FE with its core clock forced to lowest state (850 mhz) and HBM2 @ 945. 

The issue definitely resides with the ROCm Vega drivers(or at least how the ROCm OpenCL driver runs this particular kernel vs Windows Radeon Pro). 

---

### 评论 #12 — gstoner (2017-07-06T20:04:49Z)

Ok…. That detail helps.   We force the clock low and do thread trace to see what is going on.  I suspect we have done some optimization in the compiler on load stores

We tried to replicate your RX480 issue first via an  Intel system everything checked out,  we are looking at RYZEN,  we see the issue in how the Linux kernel is configured via ACPI, the Linux kernel team is digging through this now.





---

### 评论 #13 — jstefanop (2017-07-07T03:16:28Z)

Posting the mixbench and BabelStream benches here since its more relevant than the closed issue:

Stock clocks on Vega 1600/945
Polaris 570 4GB 1244/2000

Polaris + AMDGPU-Pro 17.10 = https://pastebin.com/E90aSqx6
Polaris + ROCm 1.6 = https://pastebin.com/n14UD7ve
Vega + ROCm 1.6 = https://pastebin.com/DzGTAtj8

As you can see Polaris + AMDGPU-Pro is at near saturation on the memory controller, with closer but a bit slower on the ROCm stack.

Vega on the other hand is underperforming and not coming close to saturating HBM2 (polaris card actually beat it on mem bandwidth on some tests). The raw compute performance is about where it should be though, but there is obviously something going on with the memory.

Vega also failed the alternating mix bench test with following error:
Memory access fault by GPU node-1 on address 0x500000000. Reason: Page not present or supervisor privilege.
Aborted (core dumped)

---

### 评论 #14 — gstoner (2017-07-07T03:38:17Z)

Thank you, I look this over tonight, I need to plot the Mixbench data as roofline, as memory plot,  

---

### 评论 #15 — jstefanop (2017-07-10T19:17:59Z)

@gstoner any updates on this front?

---

### 评论 #16 — gstoner (2017-07-14T13:06:04Z)


I did find we need to tune the compiler for Polaris 10,   


Vega10 with Bable stream comparing the same compiler we use of Windows and AMDGPUpro vs LC 
<img width="533" alt="screen shot 2017-07-14 at 7 31 28 am" src="https://user-images.githubusercontent.com/4129721/28213283-01904602-686b-11e7-8141-de83a3888add.png">
<img width="533" alt="screen shot 2017-07-14 at 7 31 49 am" src="https://user-images.githubusercontent.com/4129721/28213287-0475255e-686b-11e7-9820-ffd4f35f450d.png">

Vega10 Show it is draw on Mixbench between the two compilers 
<img width="615" alt="screen shot 2017-07-14 at 7 57 29 am" src="https://user-images.githubusercontent.com/4129721/28213250-e5127932-686a-11e7-97ff-5a04120dd61e.png">
<img width="614" alt="screen shot 2017-07-14 at 7 54 32 am" src="https://user-images.githubusercontent.com/4129721/28213254-ea14f95a-686a-11e7-915f-c13a9fd8a16b.png">

Now we still have corner case around register utilization we need to look at in LC this dependent on the Application code. 

---

### 评论 #17 — gstoner (2017-07-14T13:09:50Z)

We do have a new drop of ROCm coming out Monday 1.6.1 which has a number of Firmware fixes and OpenCL RT fix to re-enable SDMA.    I plan on doing 1.6.x drops until we close this issue out.  

---

### 评论 #18 — jstefanop (2017-07-14T18:27:36Z)

Have you guys uncovered why vega does not seem to saturate its memory controller? Numbers are pretty much what I got, and the graph on vega vs fiji shows this discrepancy. Vega is saturating about half its bandwidth, and fiji is at nearly 80% utilization. 

---

### 评论 #19 — gstoner (2017-07-14T19:03:38Z)

Theoretical performance at 950 MHz is 480 GB/s  we think we found  ~48 GB/s of fall off in HBM hardware how it stacked, but double checking,  which puts you at 432 GB/s  We do not see this on 8 GB cards.  But. your  90% efficiency at 390 GB/s.  But we are digging deeper.  

---

### 评论 #20 — jstefanop (2017-07-14T19:15:18Z)

@gstoner, fiji is at 390 GB/s....vega is at 260 GB/s currently. Is the 48GB drop off due to the double stacks a hardware limitation or something that can be fixed driver side?

If its not occurring on 8GB cards then this should  be able to be worked around by limiting memory access to the lower 4GB stack on the two banks when memory used is < 8GB. 

---

### 评论 #21 — gstoner (2017-07-22T17:03:31Z)

@jstefanop  Status Update,  So I personally we have been digging through performance issues and doing code review on the entire source base of the driver.  My team normally sits above the Thunk layer on what we work on.  But we now going down and debugging firmware and base Linux kernel and AMDGPU driver to sort where sources is. 

The issue with Ryzen was a Linux Kernel issue, 

We found in the AMDGPU base driver an issue power management code not correctly setting voltages forcing the chip not run efficiently on Vega 10. 

We found few another issue in the base kernel driver.  Based on this 1.6.1 is moving to Linux Kernel 4.11 and the respective AMDGPU base driver that goes with it.   

At the Thunk Layer, We found VMA alignment issue  that affects GFX8 devices ( Fiji and Polaris 10, which the fix is now in 1.6.1 

At the ROCr runtime time level we are now seeing, we have an internal test we use. 

Fiji Device Memory, Coarse-Grained
  Load:  458.7 GiB/s. = 492 GB/s 
  Store: 333.1 GiB/s = 355 GB/s 

Polaris 10 Device Memory, Coarse-Grained
  Load:  193.5 GiB/s = 207.8 GB/s
  Store: 174.9 GiB/s=187.8 GB/s 

Vega10 Device Memory, Coarse-Grained
  Load:  347.4 GiB/s =  373 GB/s 
  Store: 349.2 GiB/s = 374.9

We are now back up through the language stack to push them on getting memory performance. 
On Vega10 we looking at few other ideas to close the gap.  As you can see FIJI is north of 90% efficiency on Loads 

On ethash if we comment out isolate flag: and also set the compiler parameters --cl-local-work 512 --cl-global-work 10752 we see big jump in performance to 37 Mh/s

One thing with the new compiler the same flag and setting you did in the past for HSAIL/SC compiler may not work on LLVM based OpenCL compiler to get the best performance.  

--- a/libethash-cl/ethash_cl_miner_kernel.cl
+++ b/libethash-cl/ethash_cl_miner_kernel.cl
@@ -221,7 +221,7 @@ static void keccak_f1600_no_absorb(uint2* a, uint out_size, uint isolate)
                // much we try and help the compiler save VGPRs because it seems to throw
                // that information away, hence the implementation of keccak here
                // doesn't bother.
-               if (isolate)
+//             if (isolate)
                {
                        keccak_f1600_round(a, r++);
                        //if (r == 23) o = out_size;


We are finalizing 1.6.1, which I am hoping we have out by Tuesday,  note we will have 1.6.2 release following this release,  I am looking at few other areas right now I like to address in the HIP and OpenCL Runtime which will not make it into 1.6.1 

---

### 评论 #22 — JustinTArthur (2017-07-22T18:10:19Z)

Thanks for the thorough update, @gstoner. I'm also on the Ryzen platform and look forward to the new release. \*takes cards off eBay\*

Where is the best place to find the updated Vega firmware once its released? It seems to take a while for them to land in @airlied's drm repos and I couldn't find them in the ROCK repo.

---

### 评论 #23 — gstoner (2017-07-22T18:20:51Z)

We bundle it part of the driver now.   You do not need VBIOS update.

Greg


---

### 评论 #24 — jstefanop (2017-07-22T19:04:02Z)

@gstone good news! As a side note why are you setting local work to 512? Has the max increased from 256 for vega? Is there a public branch we can test these updates before point releases?

BTW will you be at Caspian next weekend? AMD has invited me to the event and might be able to make it!

---

### 评论 #25 — gstoner (2017-07-22T19:23:02Z)

No, I will not be at Caspian/Siggraph but will be in Sunnyvale.  Normally I am in Austin.  

With OpenCL on ROCm and our new LLVM compiler, we relaxed the limits we had with our Previous runtime and Compiler.  You see where people trying to report bugs on this since we had them programmed to just use 256 due to an artificial constraint in the old OpenCL stack.  Remember  DX uses 1024.   Let me try and find the reported issue. 

---

### 评论 #26 — JustinTArthur (2017-07-22T19:23:02Z)

@jstefanop it looks like the Vega voltage settings he mentioned are in the Linux 4.9 kernel in the master and roc-1.6.x branches of [ROCK](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/). I'll be giving it a whirl tonight. I haven't seen the kernel patches for Ryzen yet.

---

### 评论 #27 — JustinTArthur (2017-07-23T22:51:02Z)

Voltage patch in ROCK alone didn't help much. Will have to try the latest ROCm stack once I figure out how to build it on Gentoo.

---

### 评论 #28 — gstoner (2017-07-23T23:00:10Z)

You will not see it until next week, we will release the source code as well. 

---

### 评论 #29 — gsedej (2017-07-26T10:19:57Z)

@jstefanop how did get ~24mh/s? Did you use genoil ethminer? I am not able to get past 21. The frequency past 1000MHz does not affect performace (level 3)
(i am using 480 8gb shappire)

---

### 评论 #30 — gstoner (2017-07-26T13:46:10Z)

ROCm 1.6.1 was posted yesterday afternoon

---

### 评论 #31 — jstefanop (2017-07-26T17:02:49Z)

@gsedej this thread is about Vega FE and its stock performance. 21 mh/s is about right for stock polaris (our polaris card runs faster due to custom BIOS with higher mem clocks and tighter timings). 

@gstoner I dont see a tag in repo..will an update under ubuntu pull updated installer packages?

---

### 评论 #32 — jedwards-AMD (2017-07-26T17:20:29Z)

I will have the OpenCL developers tag their release.

---

### 评论 #33 — jstefanop (2017-07-27T02:07:54Z)

@gstoner how are you setting local work to greater than 256? If we try this we get 
OpenCL Error: clEnqueueNDRangeKernel -55

We also cant reproduce the bandwith improvements you are seeing with 1.6.1. Were the changes you were testing pushed to the latest installer packages on your repo server?

We are seeing about a 10GB/s gain over 1.6, but no where near the 70-80GB/s gains you posted above. 

Version: 3.2
Implementation: OpenCL
Running kernels 100 times
Precision: double
Array size: 268.4 MB (=0.3 GB)
Total size: 805.3 MB (=0.8 GB)
Using OpenCL device gfx900
Driver: 1.1 (HSA,LC)
Reduction kernel config: 256 groups of size 256
Function    MBytes/sec  Min (sec)   Max         Average     
Copy        295464.553  0.00182     0.00229     0.00211     
Mul         298450.968  0.00180     0.00238     0.00211     
Add         286923.670  0.00281     0.00336     0.00312     
Triad       285306.484  0.00282     0.00368     0.00313     
Dot         280934.954  0.00191     0.00242     0.00220  


---

### 评论 #34 — gstoner (2017-07-27T04:52:31Z)

I told you we do a ROCr level test with a Optimized Blit kernel,  I said I am now going up into the OpenCL runtime and optimizing it to match the ROCr level test.   We have few more performance optimization

Greg
On Jul 26, 2017, at 7:07 PM, jstefanop <notifications@github.com<mailto:notifications@github.com>> wrote:


@gstoner<https://github.com/gstoner> how are you setting local work to greater than 256? If we try this we get
OpenCL Error: clEnqueueNDRangeKernel -55

We also cant reproduce the bandwith improvements you are seeing with 1.6.1. Were the changes you were testing pushed to the latest installer packages on your repo server?

We are seeing about a 10GB/s gain over 1.6, but no where near the 70-80GB/s gains you posted above.

Version: 3.2
Implementation: OpenCL
Running kernels 100 times
Precision: double
Array size: 268.4 MB (=0.3 GB)
Total size: 805.3 MB (=0.8 GB)
Using OpenCL device gfx900
Driver: 1.1 (HSA,LC)
Reduction kernel config: 256 groups of size 256
Function MBytes/sec Min (sec) Max Average
Copy 295464.553 0.00182 0.00229 0.00211
Mul 298450.968 0.00180 0.00238 0.00211
Add 286923.670 0.00281 0.00336 0.00312
Triad 285306.484 0.00282 0.00368 0.00313
Dot 280934.954 0.00191 0.00242 0.00220

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/147#issuecomment-318237675>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuXeCiiZliH_FKgIxsP8wEphzHYogks5sR_D9gaJpZM4OMuLL>.



---

### 评论 #35 — jstefanop (2017-07-27T23:42:11Z)

@gstoner Is this optimized kernel only available internally? If the best performance is achieved by avoiding the OpenCL runtime entirely, then we would like to explore that path. 

---

### 评论 #36 — gstoner (2017-07-28T00:46:52Z)

It is asm kernel + using the ROCr API directly.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: jstefanop <notifications@github.com>
Sent: Thursday, July 27, 2017 4:42:12 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] Vega FE slow OpenCL performance for Mining applications (#147)


@gstoner<https://github.com/gstoner> Is this optimized kernel only available internally? If the best performance is achieved by avoiding the OpenCL runtime entirely, then we would like to explore that path.

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/147#issuecomment-318516416>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuQ2JBCMqmlStOk11AspF18YLtcqNks5sSSBUgaJpZM4OMuLL>.


---

### 评论 #37 — jstefanop (2017-07-28T02:17:30Z)

Is it possible to build ASM kernels from opencl using the rocm tools?

---

### 评论 #38 — aditya4d (2017-07-31T01:43:49Z)

@jstefanop , yes. Use clang-ocl binary that gets installed with `rocm-opencl-dev`. Use the command here: https://github.com/RadeonOpenCompute/clang-ocl/blob/master/clang-ocl.in
The repo is used by MIOpen to generate ASM kernels and use OpenCL/HIP to run them. Sample: https://github.com/ROCm-Developer-Tools/HIP/blob/master/samples/0_Intro/module_api/runKernel.cpp

---

### 评论 #39 — gstoner (2017-08-09T22:07:21Z)

Update  On 8 GB Vega10 we measuring this with a new build. 

|Vega                                                    | OCLWin10  |Eff    |Rocm OCL |Eff        |  Rocr API/ASM  |Eff           |
|:-----------------------------------|:--------|:-------|:----------|:---------|:---------------|:--------|
|OCLPerfDevMemReadSpeed (GB/s) | 392.28 | 81.08% | 411.598 | 85.08%   | 425.52.             | 87.95%|
|OCLPerfDevMemWriteSpeed(GB/s) | 386.484 | 79.89% | 413.551 | 85.48% | 424.12               | 87.66%|

On second test  for 8GB Vega10
- Load: 361 GiB/s (81% peak) = 387.7 GB/s
- Store: 386 GiB/s (86% peak) = 414.6 GB/s

---

### 评论 #40 — JustinTArthur (2017-08-11T18:17:12Z)

@jstefanop have you been able to get the Vega FE working at a single PCIe 3.0 x1 lane on either Windows or Linux? With ROC Kernel, PCI errors flood my kernel buffer.

---

### 评论 #41 — jstefanop (2017-08-12T04:22:42Z)

No, it's in a full 16x slot. I put it in an 8x and 4x slot with no issues. 

---

### 评论 #42 — jstefanop (2017-08-12T04:24:49Z)

@gstoner cool work...seems like we are near 90%

In terms of the opencl optimizations are you seeing improvements?

---

### 评论 #43 — gstoner (2017-08-12T14:32:09Z)

Across the board improvements on memory bandwidth fixes.     Also finalizing few more fixes in HCC and HIP as well to improve GPU Stream performance. 

One thing we testing new VBIOS for Frontier Edition  which with the 2  MB Page update, which will get this card back close to what we seeing on 8 GB cards on loads and stores

 It took longer then I like but I had to drive teams outside of mine to do a number of fixes, post my team doing analysis and triage. 



> Greg



---

### 评论 #44 — gstoner (2017-08-24T01:49:06Z)

We rolled out ROCm 1.6.3 with 2MB support.   I working to release a firmware solution to get you to symmetric 413 GB/s on one our key memory tests

---

### 评论 #45 — jstefanop (2017-08-24T16:04:24Z)

@gstoner awesome work. Im curious as to the status of the > 2GB memory allocation issue that was fixed on windows side with the "Blockchain" driver update. This has the same performance impact on large datasets on linux as well, so is this fixed going to be implemented on the ROCm stack/AMDGPU-Pro?

---

### 评论 #46 — gstoner (2017-08-24T16:48:28Z)

On the  Windows side, we also were working it in for the blockchain driver.  What we did on the Linux side will ultimately fix all stack since our fixes we did 4.11 went in 4.14 Linux kernel upstream. our work is going into AMDGPUpro,  it is just on slower update cadence.    

We still have firmware fix coming to lift the load memory bandwidth performance on the FE cards   I pushing the team hard to get this out.    We saw 2TFLOP lift in performance on new SGEMM kernel with this update Firmware. 

We have also been working on Compiler performance improvement for Gird Dispatch for HIP  and Also HCC around thread index Optimation in the intrinsics which improve memory performance for kernels like in GPU-Stream ( now Babbel-Stream)  


---

### 评论 #47 — jstefanop (2017-08-25T18:32:53Z)

@gstoner so > 2GB memory paging issue that was fixed in the windows blockchain driver is present in 4.11 ROCm update?

---

### 评论 #48 — gstoner (2017-08-25T18:38:06Z)

We have support by default in ROCm 1.6.3

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: jstefanop <notifications@github.com>
Sent: Friday, August 25, 2017 11:32:54 AM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] Vega FE slow OpenCL performance for Mining applications (#147)


@gstoner<https://github.com/gstoner> so > 2GB memory paging issue that was fixed in the windows blockchain driver is present in 4.11 ROCm update?

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/147#issuecomment-325003344>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DubldguuzTMe0i6_yqH03gE0JSOldks5sbxNWgaJpZM4OMuLL>.


---

### 评论 #49 — jstefanop (2017-08-27T19:07:07Z)

@gstoner FYI we are seeing this fix work for Vega FE, but not polaris based cards in ROCm 1.6.3

---

### 评论 #50 — gstoner (2017-08-27T20:02:10Z)

I need to send out a flag

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: jstefanop <notifications@github.com>
Sent: Sunday, August 27, 2017 2:07:08 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Mention
Subject: Re: [RadeonOpenCompute/ROCm] Vega FE slow OpenCL performance for Mining applications (#147)


@gstoner<https://github.com/gstoner> FYI we are seeing this fix work for Vega FE, but not polaris based cards in ROCm 1.6.3

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/147#issuecomment-325217817>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuYnDbRk90psx72mD-p_L1AtR7FQoks5scb5cgaJpZM4OMuLL>.


---

### 评论 #51 — gstoner (2017-08-29T01:44:52Z)

@jstefanop

2MB fragments for Ellesmere are enabled with a grub option:
    amdgpu.vm_fragment_size=9

GRUB_CMDLINE_LINUX="... amdgpu.vm_fragment_size=9"

To see it worked at the shell prompt 

 dmesg | grep fragment

---

### 评论 #52 — jstefanop (2017-08-29T05:05:14Z)

Is this option work only with the ROCm kernel?

---

### 评论 #53 — clever999 (2017-08-29T08:21:31Z)

@gstoner 
Mining works great with ROCm 1.6.3 and GRUB_CMDLINE_LINUX="amdgpu.vm_fragment_size=9".
Hashrate went from 155 > 168 Mhs/s with 6*RX470, so we have the DAG fix!!
Great Job!!
Thx

---

### 评论 #54 — gstoner (2017-08-29T13:03:07Z)

@jstefanop only ROCm for now.  

---

### 评论 #55 — gstoner (2017-08-29T13:22:08Z)

@jstefanop only ROCm for now. It is going upstream the changes for Polaris as well, but you need the flag. 

---

### 评论 #56 — jstefanop (2017-09-13T23:30:50Z)

@gstoner whatever happened to the BIOS/firmware fix for Vega FE?

---

### 评论 #57 — thagrisu (2017-09-14T00:58:26Z)

@gstoner 
maybe you can help me on thos. 
i'm trying to get rocm kernel with opencl running. Kernel and rocm-opencl ist installed.

```
Distributor ID:	Ubuntu
Description:	Ubuntu 16.04.1 LTS
Release:	16.04
Codename:	xenial
Kernel: 4.11.0-kfd-compute-rocm-rel-1.6-148
```

but when i try to run HelloWorld Script
`[ 1068.117765] HelloWorld[5074]: segfault at 8 ip 00007fd2466a84e6 sp 00007ffe75469380 error 4 in libamdocl64.so[7fd246273000+31aa000]`

echo $OPENCL_ROOT
/opt/rocm/opencl

Thanks
regards



---

### 评论 #58 — gstoner (2017-09-14T02:33:31Z)

@jstefanop  it is VBIOS update done outside my team. I am still pushing the team get it out

---

### 评论 #59 — gstoner (2017-09-14T15:54:38Z)

@thagrisu can you tell me which Hello World app you are using 

---

### 评论 #60 — thagrisu (2017-09-15T07:22:22Z)

@gstoner  your Hello World  from this guide: https://rocm.github.io/install.html 
Right now i was able to get rid of this problem. Not with  the rocm open-cl but with the AMDGPU-PRO opencl -> is working.

Just to make sure whats the right Installation Procedure. 
* Installing ROCM Kernel  and ROCM Komponents 
* Installation AMDGPU-Pro driver 
* Installing additional ROCM  AMDGPU-Pro components with `sudo apt install -y rocm-amdgpu-pro`

is it the right way ? 

with this i was able to fix the known Ethereum DAG Size issue you maybe know. Even without the `amdgpu.vm_fragment_size=9` you mentioned (?)

But know i experience very fluctuate performance in terms of mining Hashrate. Normaly i see this behaviour if card get limited by powerplay or power consumption. Have tried all tweaks with rocm-smi but cannot get stable hashrate. a

Maybe you have an idea where to look or what can be the limitation ? 

Thanks

---

### 评论 #61 — gstoner (2017-09-15T13:28:18Z)

This is not the right way to do the Install with ROCm

This is proper way to install ROCm on Ubuntu ->. https://rocm.github.io/ROCmInstall.html

Ok your mixing components from the ROCm Project component with  AMDGPUpro.  This is not Supported today.    We had conversation with this team to see if this can be remedied but these dialogs continue.


So what your trying to do is get ROCm to fix AMDGPUpro.    We use a much newer linux kernel and THUNK layer.


Greg




On Sep 15, 2017, at 2:22 AM, thagrisu <notifications@github.com<mailto:notifications@github.com>> wrote:


@gstoner<https://github.com/gstoner> your Hello World from this guide: https://rocm.github.io/install.html
Right now i was able to get rid of this problem. Not with the rocm open-cl but with the AMDGPU-PRO opencl -> is working.

Just to make sure whats the right Installation Procedure.

  *   Installing ROCM Kernel and ROCM Komponents
  *   Installation AMDGPU-Pro driver
  *   Installing additional ROCM AMDGPU-Pro components with sudo apt install -y rocm-amdgpu-pro

is it the right way ?

with this i was able to fix the known Ethereum DAG Size issue you maybe know. Even without the amdgpu.vm_fragment_size=9 you mentioned (?)

But know i experience very fluctuate performance in terms of mining Hashrate. Normaly i see this behaviour if card get limited by powerplay or power consumption. Have tried all tweaks with rocm-smi but cannot get stable hashrate. a

Maybe you have an idea where to look or what can be the limitation ?

Thanks

—
You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/147#issuecomment-329703329>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuXLuAuxXJN-M7Z9Swml5gZBxUBn8ks5siiWwgaJpZM4OMuLL>.



---

### 评论 #62 — JustinTArthur (2017-11-25T01:24:48Z)

> We rolled out ROCm 1.6.3 with 2MB support. I working to release a firmware solution to get you to symmetric 413 GB/s on one our key memory tests

@gstoner, is the 2MB update the [commit made to acg_smc, asd, and sos firmwares in Linus' repo on 8/29](https://git.kernel.org/pub/scm/linux/kernel/git/firmware/linux-firmware.git/commit/amdgpu?id=51b4a8700017fe98b4c9da4e6c2cbcfd4cf21dc1)? Is Linus' firmware repo the best place to get these firmwares?

---
