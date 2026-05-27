# Multi GPU scaling

> **Issue #38**
> **状态**: closed
> **创建时间**: 2016-10-15T17:03:35Z
> **更新时间**: 2016-10-18T03:04:12Z
> **关闭时间**: 2016-10-17T15:46:02Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/38

## 描述

Hello!
First of all, very cool project!

My question is not specific to ROCm, but it is related, and I thought you folks may have some advice on the following:

I have two RX 470 cards. I am running a series of OpenCL kernels which are fairly memory intensive : this is a video compression application, so a lot of data passes from host to GPU and back. There is also
high CPU usage.

When I run my kernels on a single 470, total frame rate is 40 FPS. When I use two 470s, frame rate equals
60 FPS.  There is no dependency in the code between the two devices.

 So, it looks like scaling is sub-optimal. I was hoping/expecting to get around 80 FPS for two cards. What factors may be affecting compute scaling on multiple cards?  How can I trouble-shoot this issue? 

Any advice would be greatly appreciated.

Thanks!
Aaron


---

## 评论 (12 条)

### 评论 #1 — briansp2020 (2016-10-16T01:30:51Z)

What kind of motherboard are you using? I have Z170 based motherboard with 2 Fury Nano board and noticed that one of the x16 PCIe slot is actually x4 electrically. If you need to send a lot of data to/from CPU to GPU, PCIe bandwidth will matter.


---

### 评论 #2 — boxerab (2016-10-16T13:15:21Z)

Hi Brian,
Thanks. I have a Z170-K, and I also noticed that the secondary PCI slot is only 4x lanes.  

For each frame, I send a 10 MB uncompressed image to the card, and receive a 1.5 MB compressed
image back from the card.  PCI 4x should be 32 Gb/second, so 4 GB/s at max bandwidth. 80 frames/second
would be less than 1 GB/s of bandwidth. So, it doesn't look to me like PCI is the bottleneck.

I guess I can check this by scheduling two compressions  per frame transfer, to see if frame rate goes up.


---

### 评论 #3 — boxerab (2016-10-16T13:43:32Z)

By the way, I tested my app on each card individually, as a single GPU, and each card achieved the
same frame rate of 40 FPS as a single GPU configuration.  


---

### 评论 #4 — briansp2020 (2016-10-16T22:34:08Z)

If you can run your app on each card individually, as a single GPU, can you run two instances of the app processing different videos on different video card and see what the performance is like?


---

### 评论 #5 — boxerab (2016-10-17T15:46:02Z)

Thanks, tried that but it didn't help. I also tried creating a unique OpenCL context per device.
Finally, in the end, it looks the issue is very high CPU usage. I guess the AMD driver can't get enough CPU cycles to schedule tasks and handle events when CPU usage is near 100 %


---

### 评论 #6 — ghost (2016-10-17T16:01:58Z)

Hey Aaron,

Can't really comment on the specifics of your issue, since you are probably using a driver stack different than ROCm.

However I can say that reducing the large CPU overhead to submit work to the GPU is one of the reasons the ROCm project was started. We've been using a lot of different techniques to get this overhead down, one of the most significant being submitting work to the hardware without any syscalls or context switches (usermode queues).


---

### 评论 #7 — boxerab (2016-10-17T16:07:48Z)

@arodrigx7  thanks a lot for this info. Would love to try out ROCm.
I have two 470s. Looking forward to Polaris support, then will give this a try.
Cheers,
Aaron


---

### 评论 #8 — briansp2020 (2016-10-17T20:26:18Z)

> For each frame, I send a 10 MB uncompressed image to the card, and receive a 1.5 MB compressed
> image back from the card. PCI 4x should be 32 Gb/second, so 4 GB/s at max bandwidth. 80 frames/second
> would be less than 1 GB/s of bandwidth. So, it doesn't look to me like PCI is the bottleneck.

What kind of drive are you using? Mechenical HD or SSD? Either way, no drive connected to your system through SATA will sustain 1GB/s. If you have access to NVMe M.2 SDD, you maybe able to sustain the bandwidth necessary to do what you are trying to do. Even there, I think that bandwidth is shared with your second graphics card. I think AMD made [Radeon Pro SSG](http://www.anandtech.com/show/10518/amd-announces-radeon-pro-ssg-fiji-with-m2-ssds-onboard) for exactly this use case.

Though I don't know the details of what you are doing, unless your CPU code is already heavily multi-threaded doing lots of processing, I can't see it being the bottleneck.


---

### 评论 #9 — boxerab (2016-10-17T22:02:03Z)

@briansp2020 thanks! I have a SATA SSD, not an nvme, so I guess bandwidth is limited.

The workflow for my app is:

1) Someone appears with an SSD filled with images 
2) Plug SSD into computer with 470s
3) Read images, compress, and store on computer's SSD.

I am quite interested in the Radeon SSG, by the way.

And, my application is heavily multi-threaded with a lot of of CPU processing, so 
I think this is the underlying reason for poor scaling up to two cards. 


---

### 评论 #10 — briansp2020 (2016-10-17T22:15:00Z)

Well, then, why don't you bench mark just copying the files over from the source SSD to your computer's SSD? That should give you the upper bound on performance you can expect from your setup.


---

### 评论 #11 — ghost (2016-10-17T22:18:15Z)

Or use separate SSDs as input to each card if you have one.

Regards,
Andres

On Mon, Oct 17, 2016 at 6:15 PM -0400, "Brian" <notifications@github.com<mailto:notifications@github.com>> wrote:

Well, then, why don't you bench mark just copying the files over from the source SSD to your computer's SSD? That should give you the upper bound on performance you can expect from your setup.

## 

You are receiving this because you were mentioned.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/38#issuecomment-254350690, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AOGxIDvGBmkHm8sk52lVx1MqUNp0HtJYks5q0_NmgaJpZM4KXwcO.


---

### 评论 #12 — boxerab (2016-10-18T03:04:12Z)

@briansp2020 good idea, thanks. Will try this.

@arodrigx7  also, good idea, thanks a lot. 


---
