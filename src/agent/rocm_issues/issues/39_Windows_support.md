# Windows support?

> **Issue #39**
> **状态**: closed
> **创建时间**: 2016-10-21T09:30:17Z
> **更新时间**: 2019-01-11T14:28:36Z
> **关闭时间**: 2016-10-22T17:11:34Z
> **作者**: JacksonFurrier
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/39

## 描述

Hello,

are you planning to support Windows platform for the upcoming 1.3 release?


---

## 评论 (15 条)

### 评论 #1 — jedwards-AMD (2016-10-21T14:41:15Z)

ROCm 1.3 will not support Windows. Also, ROCm support on the Windows operating system has not been announced in any public road map.


---

### 评论 #2 — vstallins (2016-10-22T17:05:00Z)

Any date for 1.3? Looking forward to it detecting my GTX 1070 instead of saying no nvidia devices.


---

### 评论 #3 — gstoner (2016-10-23T14:41:51Z)

 I think you have install issue @vstallins  Since we run dual config boxes in houses. 


---

### 评论 #4 — gstoner (2016-10-25T18:15:10Z)

I think your talking about HIP since GTX1070 device would never be support by ROCm Driver.

greg

On Oct 22, 2016, at 12:05 PM, vstallins <notifications@github.com<mailto:notifications@github.com>> wrote:

Any date for 1.3? Looking forward to it detecting my GTX 1070 instead of saying no nvidia devices.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/39#issuecomment-255540508, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DuQF7gFqEtiLSKenCw-lXuYo-kuVHks5q2kI9gaJpZM4KdCRA.


---

### 评论 #5 — gstoner (2016-10-25T18:17:35Z)

What are you looking for on windows,   HIP and HCC.

greg
On Oct 21, 2016, at 9:41 AM, James Edwards <notifications@github.com<mailto:notifications@github.com>> wrote:

ROCm 1.3 will not support Windows. Also, ROCm support on the Windows operating system has not been announced in any public road map.

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/39#issuecomment-255395524, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8Dud2uUol1Ae03qypAxqion3z0u8dkks5q2M8MgaJpZM4KdCRA.


---

### 评论 #6 — vstallins (2016-10-25T19:03:32Z)

I'm using Ubuntu 16.04LTS I have HIP and ROCm installed and HCC as well I think. Just trying to figure things out and get into computing with GPUs. I have a GTX 1070 and 12 R9 390s. So if I need to I can put a 390 in with the 1070. Just wanting to learn as I think this area has a bright future.


---

### 评论 #7 — ghost (2016-10-25T19:24:14Z)

The HIP layer provides source level compatibility between CUDA and ROCm. That's probably a good place to start reading. Depending on whether you have a CUDA or ROCm enabled system, HIP will compile using either NVCC or HCC (respectively).

Link to the HIP project:
https://github.com/GPUOpen-ProfessionalCompute-Tools/HIP

Btw, HIP is automatically installed with ROCm. So if you plug in one of your 390's it should be detected. If you want to use your GTX 1070, you will need to install NVCC and its dependencies. The HIP FAQ should have more information on this.

If you have further questions you can let us know.


---

### 评论 #8 — vstallins (2016-10-25T19:27:17Z)

Ok thanks. I have all of that stuff installed already. Just new to all of this and trying to learn. If anyone makes tutorial videos, etc. let me know the links as it would help likely or if anyone has free time and feels like teaching I am open to that as well. I think GPU computing has huge potential especially with the next gen SSD GPUs.


---

### 评论 #9 — JacksonFurrier (2016-11-18T10:25:54Z)

I would need HIP and HCC on Windows, but since its not in the roadmap I can leave it. Thanks for the reply :)


---

### 评论 #10 — dtmoodie (2017-07-23T11:26:08Z)

Any chance you can compile a binary with hip with  Nvidia and amd code which can be selected at runtime?

---

### 评论 #11 — gstoner (2017-07-23T13:25:36Z)

Have you look at the documentation on HIP.  

https://github.com/ROCm-Developer-Tools/HIP/blob/master/docs/markdown/hip_porting_guide.md

https://github.com/ROCm-Developer-Tools/HIP/blob/master/docs/markdown/hip_faq.md 

---

### 评论 #12 — dtmoodie (2017-07-23T13:45:40Z)

Given the FAQ states that the tool does not create a binary for both platform, any ideas around bring around that limitation? Perhaps delay loading different libraries based on detected hardware?

---

### 评论 #13 — gstoner (2017-07-23T14:00:54Z)

I have one of the lead get back on this 

---

### 评论 #14 — HECer (2018-11-18T14:40:22Z)

I really hope Windows support will come soon, i think my next graphics card will be an nvidia, because of this. It is really sad how amd cannot serve good support for the current software trends like neuronal networks.
I really hope they will change their focus a little more.

---

### 评论 #15 — cmpute (2019-01-11T05:08:17Z)

+1. I will definitely choose to buy amd graphics cards if it support kernel acceleration tools on Windows!

---
