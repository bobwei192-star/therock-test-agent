# WSL 2 Clarification

> **Issue #794**
> **状态**: closed
> **创建时间**: 2019-05-13T18:05:41Z
> **更新时间**: 2023-12-18T18:56:30Z
> **关闭时间**: 2023-12-18T18:56:30Z
> **作者**: iamkucuk
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/794

## 描述

As you may know, Microsoft is about to publish a new WSL version. My question is: How can we benefit from WSL 2.0 which will provide a full linux kernel?

---

## 评论 (17 条)

### 评论 #1 — MathiasMagnus (2019-05-29T22:01:24Z)

I believe nohow. WSL2 will use virtuization under the hood, so ROCm will only work as much as it does today in virtual machines: nohow. Because you cannot have two drivers controlling the same HW, someone has to create relay drivers that mediate various API calls to the actual host driver. VMWare and Virtual Box have such drivers for OpenGL primarily, but not for compute. XEN virtual machines can use PCI pass through, which gives exclusive rights to the HW for the guest OS. In such scenarios, WSL2 would have a chance, but Windows would "lose" the device.

GPGPU compute is high on the priority list of the WSL team, Tara Raj on Twitter had a poll which helps them prioritise target APIs and architectures. If AMD doesn't proactively help, it's gonna be a special CUDA driver that mediates between WSL and the host drivers. ROCm not even being native to Windows, I don't see how ROCm components could be tunneled to the Windows drivers. Plus it would require a significant amount of work, and it seems to me both the Linux and the Windows driver teams have quite a bit on their plates.

I'd love this to happen, I just don't realistically see any chance of it happening. I'd sooner like to see better OpenCL support in the vanilla Windows drivers.

---

### 评论 #2 — devksingh4 (2020-06-28T16:05:45Z)

Now that WSL2 will support GPU compute, has this situation changed?

---

### 评论 #3 — SomeAB (2020-06-30T07:09:36Z)

my question too

---

### 评论 #4 — MathiasMagnus (2020-06-30T08:53:06Z)

[An Early Benchmark Of The NVIDIA CUDA GPU Performance On WSL2](https://www.phoronix.com/scan.php?page=news_item&px=WSL2-CUDA-Perf-Early-Look) from Phoronix shows that initial CUDA performance under WSL2 isn't stellar, but it will likely improve, plus it's still good for validation and testing during development, even if there is a perf hit.

OpenCL, OpenGL and Vulkan will be taken care of by MS through translation layers to DX12 and routing it to the host drivers. CUDA likely routes driver calls to the host operating system, but becuase ROCm has no Windows support and the team is dead silent about it, my guess is it's still fair ways down the road. There are a few mentions of Windows in various parts of the build scripts, but I haven't seen code that would target Windows explicitly.

---

### 评论 #5 — SomeAB (2020-06-30T09:13:14Z)

Is it possible to run CUDA code with DirectML or ROCM on AMD GPU ? 

---

### 评论 #6 — MathiasMagnus (2020-06-30T11:08:27Z)

> Is it possible to run CUDA code with DirectML or ROCM on AMD GPU ?

With DirectML:no. With ROCm: yes, but this issue is about ROCm working under WSL2. Running / converting CUDA code to run atop ROCm is possible with HIP.

---

### 评论 #7 — SomeAB (2020-06-30T12:33:11Z)

@MathiasMagnus  I'm trying to make this run for like 4 days straight now. Could you try running it on your side? https://github.com/facebookresearch/pifuhd

My main goal is to run this on a local machine, and I have AMD Vega64. I would be grateful for any pointers. 

---

### 评论 #8 — littlewu2508 (2021-01-12T09:04:32Z)

It seems that AMD had provided [drivers](https://www.amd.com/en/support/kb/release-notes/rn-rad-win-wsl-support) that support DirectX® 12 within WSL 2, by introducing the device /dev/dxg, drivers /usr/lib/wsl/drivers and relative libs /usr/lib/wsl/lib (drivers and libs are mounted from windows).

CUDA support for WSL 2 seems to be achieved by introducing /usr/lib/wsl/lib/libcuda.so (which is brought by nvidia drivers for windows).

So is it possible that ROCm support WSL 2, by adding compenents in radeon drivers for windows which introduces relevant drivers and libs in /usr/lib/wsl, just like CUDA does?

---

### 评论 #9 — cmpute (2021-05-01T15:15:53Z)

Also looking forward to any update of support on WSL2. I tried installed AMD Adrenalin driver for WSL and installed the precompiled package of pytorch 1.8.0 supporting ROCm, but I still cannot get the GPU utilized. It will be awesome if there's some clarification on the current status, or some tutorials about this

---

### 评论 #10 — MathiasMagnus (2021-05-02T07:53:51Z)

FWIW AMD seems to have most things in place to get ROCm acceleration in WSL. Microsoft's Antares already uses the undocumented Windows HIP runtime shipping with drivers (amdhip64.dll or whatever), it's only hipcc that's missing. Compiling a kernel on Linux, extracting it and feeding through the runtime layer (not the single-source way) should work.

At this point if AMD made a similar relay runtime for WSL2 like they did with DX12, they're good to go. The infrastructure on the Windows side is already in place. (In fact, anyone could implement such a layer in user space, communicating API calls using sockets between host-guest. It'd be a mild waste of time, given how AMD likely has something in house for this.)

---

### 评论 #11 — bitnom (2022-04-26T14:18:46Z)

Wanting

---

### 评论 #12 — sal-versij (2022-05-18T15:51:02Z)

Is there any news about this topic?

---

### 评论 #13 — alex180500 (2022-12-02T10:25:40Z)

Any updates on this?

---

### 评论 #14 — jackoske (2022-12-02T12:05:02Z)

I couldn't get it to work in the end! Its quite difficult 🙁
in the end I have just stopped using my AMD for ML




Jack Skehan
Front-End Developer

[phone-icon]   +353 83 832 2466
[phone-icon]   +353 61 518 443
www.smartfactory.ie<https://www.smartfactory.ie>        [Logo] <https://www.smartfactory.ie>

Nexus Innovation Centre
University of Limerick
[Twitter icon]<https://twitter.com/SmartFactoryIE> [Youtube icon] <https://www.youtube.com/channel/UCQ7P1NPbLi5JtQYYlrj454g/videos>  [LinkedIn icon] <https://www.linkedin.com/in/jack-skehan-333010150/>


________________________________
From: Alessandro Romancino ***@***.***>
Sent: 02 December 2022 10:25
To: RadeonOpenCompute/ROCm ***@***.***>
Cc: Jack Skehan ***@***.***>; Manual ***@***.***>
Subject: Re: [RadeonOpenCompute/ROCm] WSL 2 Clarification (#794)


Any updates on this?

—
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/794#issuecomment-1335042809>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/A37LVRAKYFN72WWC2DYVEQTWLHFDDANCNFSM4HMSFL7A>.
You are receiving this because you are subscribed to this thread.Message ID: ***@***.***>


---

### 评论 #15 — JavenLiPl (2023-08-08T10:35:47Z)

Seems ROCm Windows is available by end of last month. Is there any difference on this topic?

---

### 评论 #16 — tasso (2023-12-12T20:06:50Z)

Is this still an issue? If not, can we please close it? Thanks!

---

### 评论 #17 — tasso (2023-12-18T18:56:30Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request. If this is still an issue, please file a new ticket and we will be more than happy to investigate it. Thanks!

---
