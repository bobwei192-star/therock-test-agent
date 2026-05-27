# Question about ROCm

> **Issue #44**
> **状态**: closed
> **创建时间**: 2016-10-30T15:29:44Z
> **更新时间**: 2016-10-31T01:56:25Z
> **关闭时间**: 2016-10-30T22:49:12Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/44

## 描述

I have a GPU-accelerated video compression application - very memory intensive.

I use OpenCL 1.2.  There is no need for device side enqueue, or to have different
GPUs communicate with each other.

Is there an advantage to using ROCm over regular OpenCL runtime, for my application?

I have heard that performance is better due to lower host-side overhead.

Thanks so much,
Aaron


---

## 评论 (13 条)

### 评论 #1 — gstoner (2016-10-30T15:53:42Z)

Big change for you will be we lift the 4 GB single memory allocation limit.   We can allocate in single allocation all but 250 mb of local memory on card.    The core ROCm driver aggressively has much lower overhead on data transfer via PCIe bus, queueing  and many more thing over the existing drivers

One thing you will want is Large Bar enabled cards to really push your application.  It make the whole local memory visible from the host.

On Oct 30, 2016, at 10:29 AM, Aaron Boxer <notifications@github.com<mailto:notifications@github.com>> wrote:

I have a GPU-accelerated video compression application - very memory intensive.

I use OpenCL 1.2. There is no need for device side enqueue, or to have different
GPUs communicate with each other.

Is there an advantage to using ROCm over regular OpenCL runtime, for my application?

I have heard that performance is better due to lower host-side overhead.

Thanks so much,
Aaron

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/44, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuZNoB4eL6izkh26SrPHjl9nfUc9Iks5q5LfogaJpZM4KkZ6q.


---

### 评论 #2 — boxerab (2016-10-30T16:20:53Z)

Sounds cool. Which are the large bar cards?


---

### 评论 #3 — boxerab (2016-10-30T16:24:42Z)

I don't think I can use the over 4 GB limit, but I can definitely benefit from lower pcie transfer overhead.  Thanks for this information 


---

### 评论 #4 — gstoner (2016-10-30T16:27:25Z)

RX480 has 8 GB of memory, S9170 has 32 GB of memory this show you why we support this feature ; )


---

### 评论 #5 — boxerab (2016-10-30T16:35:55Z)

Ahhh I see, so large bar is greater than 4 GB 


---

### 评论 #6 — gstoner (2016-10-30T17:01:07Z)

BAR is Base Addressable  Register of the PCIe Spec , when talk about Large Bar we talking about BAR1 VRAM Aperture size,  this controls the amount of GPU memory visible to the CPU

On Oct 30, 2016, at 11:35 AM, Aaron Boxer <notifications@github.com<mailto:notifications@github.com>> wrote:

Ahhh I see, so large bar is greater than 4 GB

—
You are receiving this because you commented.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/44#issuecomment-257161771, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuU2-sA3_TPYBPgeEZAilE9hbVUfaks5q5MdrgaJpZM4KkZ6q.


---

### 评论 #7 — boxerab (2016-10-30T18:31:57Z)

Thanks! One more question: I have a z170 Asus motherboard with two 470s, one with 16 PCI lanes and one with 4 lanes. Will this present any problems with rocm and multi gpu compute ?


---

### 评论 #8 — gstoner (2016-10-30T19:08:06Z)

The only issue it will have you will not be getting the full performance of the GPU on data transfer from the CPU.     A single PCIe 3.0 lane runs at 8GT/s theoretical, which can send 985MB/s.  4x ~4 GB and x16 ~16 GB/s theoretical.   So you looking at a 4x drop in bandwidth.  For programs that communicate a lot with the host, it will hurt.   Remember compute is round-trip transaction, there is cost coming and going back to the host. 


---

### 评论 #9 — ghost (2016-10-30T19:10:20Z)

You will see degraded host-to-device, device-to-host and peer-to-peer memory transfer speeds on the card that only has 4xlanes allocated.

However, if you are mostly using the cards VRAM then you should see comparable performance. The main hit may be during initialization when most of the host-to-device transfers occur. This is of course not knowing the specifics of how your app works.

One thing that you may wish to experiment with is whether a PCIe lane split of 16x/4x or a 8x/8x split works better for your use case.

BTW two other small things:
- Besides what Greg mentioned, you might also benefit from reduced job submission latency, since with ROCm the usermode queues are directly mapped to the hardware.
- Small note, Large Bar is sometimes referred to as Large Aperture depending on the source of the literature (hooray for consistency). So watch out for that whenever reading spec manuals.


---

### 评论 #10 — boxerab (2016-10-30T22:47:39Z)

@gstoner thanks. For my application, I am trying to achieve 100 frames per second encode, where each frame is 10 MB transfer to device, and 10 MB transfer back to host. So, 100 FPS would be 2 GB/s.

4x would be enough for this.  

What I do worry about is whether asymmetric 16x/4x will have a negative impact on performance,
vs 8x/8x

Perhaps for ROCm you guys could make some recommendations on best hardware specs.


---

### 评论 #11 — boxerab (2016-10-30T22:49:06Z)

@arodrigx7 thanks. Its a cost issue: 16x/16x boards are considerably more expensive.  


---

### 评论 #12 — briansp2020 (2016-10-31T00:30:11Z)

@boxerab Just curious, did you find out whether your SSD can provide enough bandwidth for your application for the target performance?


---

### 评论 #13 — boxerab (2016-10-31T01:55:02Z)

Hi Brian,
Thanks - turns out my SSD (non nvme) does not provide the bandwidth for this target performance.

100 FPS is more a benchmark for me for my kernel performance. Also, there are streaming applications where video is arriving from the network card, where 10 Gig network + system RAM does provide necessary bandwidth.

Radeon pro cards have DirectGMA, which might be interesting to connect to network card for fast 
streaming. 


---
