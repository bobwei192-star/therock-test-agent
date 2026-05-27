# On RX Vega, OpenCL with the new Rocm compiler on Linux, memory/cache problem?

> **Issue #182**
> **状态**: closed
> **创建时间**: 2017-08-21T01:17:49Z
> **更新时间**: 2018-06-03T15:17:21Z
> **关闭时间**: 2018-06-03T15:17:21Z
> **作者**: preda
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/182

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

I use AMDGPU-Pro 17.30 on Linux. On RX Vega 64 GPU. I see that the OpenCL compiler changed for this combination to the new Rocm compiler.

I see a regression in my application gpuOwL https://github.com/preda/gpuowl
The application has two modes (two equivalent sets of OpenCL kernels), the "slow" mode enabled with "-legacy" flag, and the "fast" mode used by default. This "fast" mode breaks with the new compiler.

The concerned kernel that breaks is the "amalgamation" kernel, which uses a trick "staircase workgroups" which involves memory communication between workgroups (workgroup K reading data that was written by workgroup K-1) of the same kernel launch.

I tried to debug this as a bug in my application, but I can't find a cause there yet. It seems related to memory/cache behavior and is timing sensitive. It clearly only triggers with the new Rocm compiler. Unfortunately I don't have a "stripped down" small repro case yet. I did try using both OpenCL 1.2 atomics, and OpenCL 2.0 atomics, but this didn't fix the behavior.

This seemed sufficiently alarming to me to point this to you early.

---

## 评论 (27 条)

### 评论 #1 — AirSquirrels (2017-08-21T01:35:49Z)

I see the same with gpuOwl on ROCm 1.6.127. I noted over in the HCC issues that the llvm-objdump does not support Vega, or even SI, so I wasn’t able to easily compare the output kernels.

---

### 评论 #2 — gstoner (2017-08-21T01:47:36Z)

HCC is supported on Vega 10, you have to force the flag to us GFX900. There is helper library that defaulting the compiler to GFX8 binary.  In 1.6.3 there is fix in HCC and HIP. since they use the same compiler foundation.  1.6.3 will be out this week also with 2 MB page support for Vega10.   It would be good to know which Vega10 GPU you're using. 

---

### 评论 #3 — AirSquirrels (2017-08-21T01:51:53Z)

I should clarify that I wasn’t seeing an issue with hcc itself. I can create, and run gfx900 objects . I can’t disassembly them though.

Glad to hear 1.6.3 will be out soon. Does this also include the ‘blockchain’ fix? (Aka will it resolve the drop in memory access performance when more than 2GB is used - as we can also hit this in some Number Theory use cases.)

---

### 评论 #4 — AirSquirrels (2017-08-21T01:54:19Z)

Re: hardware - Preda’s issue can be duplicated on both my RX64 (Air) and FE(Liquid)

---

### 评论 #5 — gstoner (2017-08-21T02:26:04Z)

We look this over if it compiler issue. 

One thing, the ROCm stack is a lot more pedantic about out of bound memory references, we fault the kenel.  We have Guard pages now enabled in the driver.  The older driver would pass this code on through.   We will be writing up debug steps to help you chase this class of issue down.    Dmesg log shows this failure.  I dig up the grep we use. 

Also in 17.40 AMDGPUPro they will be putting back in LLVM to HSAIL to SC based compiler.      ROCm will continue to use LC as the primary compiler,   it is evolving quickly.   One thing it does not more code run through it but report the issue we address it.    Also, remember with LC you can replace the compiler post the release of the base ROCm driver.  You need a whole new driver install a new compiler for our traditional driver.   Had some nice data come in from the Hashcat dev on LC and ROCm this week also Gromacs. 

On FE cards we have a fix that  is Firmware based that needs to be released to get us up to full performance, but 2MB driver support is also critical.    We seeing 413 GB/s post this combo. 

---

### 评论 #6 — preda (2017-08-21T02:41:56Z)

First, let me say that I do appreciate the work and effort you're putting in the open-source compiler! (and the memory protection is useful)

Back to the issue, I'd be happy to have the kernel killed with memory violation errors, that'd be easy to debug, but that's not the case. There are no new messages is dmesg when I run the kernels, and they're not killed, just the results are.. surprising.


---

### 评论 #7 — gstoner (2017-08-21T02:55:32Z)

I have the compiler team and SQE team look at this week.   Your app will get pulled into our regression suite. 

---

### 评论 #8 — gstoner (2017-08-21T03:10:03Z)

I figured you like to see, we have started in earnest our online documentation project for ROCm http://rocm-documentation.readthedocs.io/en/latest/index.html  it useful even now.  SInce the context is indexed and searchable.  It is all on Github as well so we accept community extensions.  



---

### 评论 #9 — AirSquirrels (2017-08-21T03:31:47Z)

We definitely all appreciate the hard work, and very good work you and your team are doing. Will continue to check the accuracy of results on ROCm across the OpenCL applications we use.

---

### 评论 #10 — gstoner (2017-08-21T03:50:16Z)

Thanks,  we appreciate all the help we can get.    Really we need more eyes and hands to help us take the product and project to next level.     There is a lot of great work going into the compiler, we need you guys to beat on it. 


---

### 评论 #11 — bragadeesh (2017-08-21T23:21:26Z)

@preda is the amalgmation kernel implemented with fft operations? just curious to know if ffts are involved and if you guys are using library or your own implementation on the gpu?

---

### 评论 #12 — preda (2017-08-21T23:48:10Z)

This app, gpuOwL, mainly does squaring of 75-million bits numbers (for the Lucas-Lehmer primality test). It does this using FFT. (the variant is called IBDWT, "irrational base discrete weighted transform", but it has FFT inside).
Right now I don't use AMD's FFT library because I do the FFTs in a "transposed space", i.e. the data is kept transposed in memory which saves two transpositions in an FFT-IFFT cycle. Another optimization is the squaring step that is merged with parts of FFT/iFFT in a single kernel. Combining these tricks I achieve a cycle of FFT-square-iFFT-carry, with FFTs on 4*1024*1024 doubles, in 2ms on FuryX.
(and a third optimization that's not in the FFT lib is an efficient *real* FFT).

---

### 评论 #13 — bragadeesh (2017-08-22T00:02:55Z)

thanks; so are you doing 2D 1024*1024 real fft in double precision? and you are leaving out the transpose at the end of forward and beginning of inverse, correct? the optional transpose would be easy to support in a lib; but operations you are fusing into the same kernel (that saves you roundtrip to mem) is a bit tricky to support, although we do have some simple (point-wise user op) support in clFFT

---

### 评论 #14 — preda (2017-08-22T02:23:45Z)

yes, 2048x1024 "complex" FFT in double, used to compute the 4M real FFT. Using the "matrix FFT" algorithm. What I leave out is the transpose at beginning and end of forward, and the transpose at beginning and end of inverse. The only transpose strictly needed is the one in the middle of forward, and the one in the middle of inverse (talking about "matrix FFT").
As data size I have 4x1024x1024 doubles. Each double can "hold" about 19bits through the convolution.


---

### 评论 #15 — preda (2017-08-22T02:36:01Z)

I think what could be exposed as a library interface would be "convolution" (in particular, real convolution, not complex), which would compute FFT-square-iFFT. The kernel-fusion would be hidden inside the operation.

Now, if this "convolution" operation would accept an input and output data format that would have the data already transposed (e.g. with a stride of 1024x2 in my case), I think this would allow almost ideal performance.

---

### 评论 #16 — bragadeesh (2017-08-22T15:48:01Z)

thanks for feedback; are you doing 1D convolution or 2D?
we have convolution support with ffts in our MIopen library, but with restricted set of sizes, we hope to expand coverage.

---

### 评论 #17 — preda (2017-08-23T00:37:26Z)

1D convolutions (as needed for bignum multiplication). I'll keep an eye on MIopen. But double-precision and large sizes may not be exactly a priority there.

---

### 评论 #18 — gstoner (2017-08-24T01:46:14Z)

We are still working on your issue but rolled out 1.6.3 with 2MB page support 

---

### 评论 #19 — AirSquirrels (2017-08-24T02:04:35Z)

I’m assuming this is 1.6-148?

---

### 评论 #20 — AirSquirrels (2017-08-24T02:16:20Z)

Additionally, maybe I’m missing something in the documentation, but are huge pages automatic or is something needed to enable them? Does 1.6.3 address huge pages only for gfx900, or is there any support for gfx803 (particularly interested in Fury X)

---

### 评论 #21 — gstoner (2017-08-24T03:05:24Z)

Yes

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: AirSquirrels <notifications@github.com>
Sent: Wednesday, August 23, 2017 7:04:36 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Comment
Subject: Re: [RadeonOpenCompute/ROCm] On RX Vega, OpenCL with the new Rocm compiler on Linux, memory/cache problem? (#182)


I’m assuming this is 1.6-148?

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/182#issuecomment-324511699>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuUdO6_zjWCZxQ2MDzfXXjEK3yO3Fks5sbNo0gaJpZM4O8ykO>.


---

### 评论 #22 — gstoner (2017-08-24T03:16:04Z)

They are automatic now on Vega 10.

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: AirSquirrels <notifications@github.com>
Sent: Wednesday, August 23, 2017 7:16:21 PM
To: RadeonOpenCompute/ROCm
Cc: Gregory Stoner; Comment
Subject: Re: [RadeonOpenCompute/ROCm] On RX Vega, OpenCL with the new Rocm compiler on Linux, memory/cache problem? (#182)


Additionally, maybe I’m missing something in the documentation, but are huge pages automatic or is something needed to enable them? Does 1.6.3 address huge pages only for gfx900, or is there any support for gfx803 (particularly interested in Fury X)

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/182#issuecomment-324513375>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuWBjThCEemUQAzT9ORtSxYQooEdYks5sbNz1gaJpZM4O8ykO>.


---

### 评论 #23 — preda (2017-09-03T02:44:02Z)

Hi, do you have some information about the cause of the problem? Is there a workaround that I can apply on my side?

I'm looking forward to the next release of amdgpu-pro, in the meantime I'm on amdgpu-pro 17.30 (on Linux).
Thank you!

---

### 评论 #24 — gstoner (2017-09-03T13:58:07Z)

@preda AMDGPUpro is separate driver effort then the driver discussed here. It has it own release train and team maintaining it.  17.40 is in development, I do not know when they will release it. 

---

### 评论 #25 — preda (2017-09-04T01:45:59Z)

Yes I understand; but the ROCm compiler was apparently included in amdgpu-pro 17.30 (OpenCL), at least on Linux.

About the problem, do you have an opinion WRT the cause? is it something with atomics? it would help me understand the behavior I see.

---

### 评论 #26 — gstoner (2017-09-04T20:07:47Z)

In 17.40 we are re-enabling the legacy HSAIL based compiler for Vega10 the AMDGPUpro driver,  we did get the app to compile.   We are debugging why LC compiler failed. 

---

### 评论 #27 — preda (2017-09-10T23:51:01Z)

I do not see the problem anymore with the head code at https://github.com/preda/gpuowl
It seems the problem was somehow related to the "max rounding error" computation that was taking place in the "mega" kernel. When the "max error" part was removed, the kernel started to function correctly.

I use AMDGPU-pro because I'm on Ubuntu 17.04, where I can get OpenCL by installing amdgpu-pro with --compute only. As soon as ROCm supports Ubuntu 17.04 I'll switch and enjoy the new compiler.

---
