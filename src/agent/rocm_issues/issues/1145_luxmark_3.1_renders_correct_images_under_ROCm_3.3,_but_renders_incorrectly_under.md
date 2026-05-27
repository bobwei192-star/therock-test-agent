# luxmark 3.1 renders correct images under ROCm 3.3, but renders incorrectly under 3.5

> **Issue #1145**
> **状态**: closed
> **创建时间**: 2020-06-10T18:00:38Z
> **更新时间**: 2021-09-13T04:55:18Z
> **关闭时间**: 2021-09-13T04:55:18Z
> **作者**: ableeker
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1145

## 描述

I've checked ROCm 2.10, 3.0, 3.1, 3.3, and 3.5 by running luxmark 3.1. ROCm versions 2.10 up to 3.3 run just fine, and produce correct images (luxmark checks if the resulting images are correct).

However, 3.5 produces the following incorrect image.

![Screenshot from 2020-06-10 18-58-56](https://user-images.githubusercontent.com/2095835/84300929-3f3fc300-ab53-11ea-8fe3-84d2ea6ef1d8.png)

The black parts are incorrect. The builtin check shows the following result:

![Screenshot from 2020-06-10 19-52-50](https://user-images.githubusercontent.com/2095835/84301402-ffc5a680-ab53-11ea-90b5-2a0367185133.png)

ROCm 3.3, and earlier ran fine, as does luxmark 4.0 under any version of ROCm from 2.10 up to 3.5. Oddly enough, if I run LuxVR from within luxmark, it runs correctly.

![Screenshot from 2020-06-10 19-56-21](https://user-images.githubusercontent.com/2095835/84301745-97c39000-ab54-11ea-9b4b-96faa90c1be4.png)


---

## 评论 (22 条)

### 评论 #1 — preda (2020-06-11T08:54:48Z)

Out of curiosity, how does the score change between different ROCm versions you tried?
What GPU are you using?

---

### 评论 #2 — ableeker (2020-06-12T21:21:09Z)

Mine's a Radeon RX Vega 64. And the scores went down a bit going from 3.3 to 3.5. This first test for instance went from 31,214 to 30,351. That scores 3% lower.

---

### 评论 #3 — preda (2020-06-12T23:53:33Z)

@ableeker just to be sure that I understand correctly the direction of the change -- which was faster, 3.3 or 3.5? thanks.

---

### 评论 #4 — ableeker (2020-06-13T12:33:36Z)

Haha, I see what you mean... Well, 3.5 was 3% or so SLOWER, or to put it differently, 3.3 is about 3% faster than 3.5.

Actually, this ties in with you noticed about GpuOwl, doesn't?

---

### 评论 #5 — ableeker (2020-06-13T14:05:05Z)

I just noticed I had put the versions in the wrong order in comment 3. I've corrected it.

---

### 评论 #6 — preda (2020-06-18T23:27:04Z)

>Well, 3.5 was 3% or so SLOWER, or to put it differently, 3.3 is about 3% faster than 3.5.
> 
> Actually, this ties in with you noticed about GpuOwl, doesn't?

Yes indeed I made the same observation of 3.5 being slower than 3.3, unfortunately. For my usecase, a 3% performance cost is equivalent to a blocking bug.


---

### 评论 #7 — baryluk (2020-10-05T17:44:48Z)

This is still a problem in ROCm 3.8 with gfx803 (Fury X, FIJI, GFX8).

Disabling `-cl-fast-relaxed-math` is a workaround. However luxmark 3.1 HOTEL scene is rendered almost 2 times slower compared to Windows on the same GPU.


---

### 评论 #8 — baryluk (2020-11-23T03:23:08Z)

Still the same problem with ROCm 3.9 with gfx803 (Fury X, FIJI, GFX8).

It is hard to determine really if this is issue with ROCm, optimisations, or luxmark. Raytracing is known for being notorious with rounding issues instabilities. But it would be good if somebody how knows better the details if this is correct or not. It doesn't look correct to me, and other OpenCL implementations doesn't produce this result, so it is likely it is ROCm bug.


---

### 评论 #9 — baryluk (2020-12-03T23:35:50Z)

Still the same problem with ROCm 3.10 with gfx803 (Fury X, FIJI, GFX8).

Disabling `-cl-fast-relaxed-math` is a workaround, at least for the LuxBall HDR test. It ends with 5547 different pixels (0.87%), which is acceptable and passes image validation.

Disabling `-cl-fast-relaxed-math` for Neumann test, also makes it look good. 133 different pixels (0.02%). Nice!

Disabling `-cl-fast-relaxed-math` for HOTEL scene, makes  better, and pass image validation, but there is still many (≈20%) bad pixels. That is not too good IMHO.

With `-cl-fast-relaxed-math` all 3 scenes are still miss rendered heavily.


---

### 评论 #10 — ableeker (2020-12-05T13:49:17Z)

I can confirm that this issue still exists on a gfx900 (Vega 64), exactly as you've reported.

---

### 评论 #11 — ROCmSupport (2021-01-28T11:44:47Z)

Thanks @ableeker for reaching out.
I will check this for you.
Thank you.

---

### 评论 #12 — ROCmSupport (2021-02-01T11:25:11Z)

I am not able to reproduce this issue on vega10 card for all 3 scenes with ROCm 3.5 and 3.7 also

---

### 评论 #13 — ROCmSupport (2021-02-02T06:47:38Z)

Hi @ableeker and @baryluk 
I am not able to reproduce this issue on my Vega10 card with 3.5 and 3.7.
one observation is that: I observed broken image initially and next time onwards its showing proper image with all scenes.
Please find the scores here. I have observed properly rendered images also.

Rel# | Simple | Medium | Complex
3.3 | 31573 | 22117 | 2515
3.5 | 31393 | 21837 | 2676
3.7 | 31409 | 21854 | 2694





---

### 评论 #14 — ableeker (2021-02-06T13:14:15Z)

I've run LuxMark 3.1 with OpenCL from every release since 2.10, and I can confirm that it will fail to render correctly with each and every one since 3.3. I've just run it again with ROCm 4.0.1 (3212.0, rocm.list modified to point at 4.0.1), and it's still not correct, just like the images above. It fails to render a large number correctly, the Hotel lobby scene for instance fails 88.49% of the rendered pixels, which is quite evident in the rendered image. This uses the default settings, with -cl-fast-relaxed-math enabled. If you disable this setting, it will render correctly. So it seems fast relaxed math has been broken since 3.3, since 3.1 was rendering correctly.

4.0.1 | Simple | Medium | Complex
cl-fast-relaxed-math ON | 30.295 (failed: 62.60%) | 21.442 (failed: 23.54%) | 2854 (failed: 88.49%)
cl-fast-relaxed-math OFF | 29.673 (failed: 0.86%) | 20.442 (failed: 0.02%) | 2707 (failed: 21.44%)

I've installed only the OpenCL part of ROCm 4.0.1 on Ubuntu 20.10: `sudo apt install rocm-opencl`. I'm using a Vega 64, which is a 'gfx900', or a 'Vega 10 XL/XT [Radeon RX Vega 56/64]', according to ROCm clinfo.

amdgpu-pro used to render the LuxMark 3.1 scenes correctly with cl-fast-relaxed-math ON up to 20.40, but does fail with 20.45, which is using ROCm instead of PAL.

---

### 评论 #15 — ableeker (2021-02-06T13:56:35Z)

I've tried ROCm 3.1 (3084.0) as well, and I can confirm that it will render all LuxMark 3.1 scenes correctly with setting cl-fast-relaxed-math enabled.

---

### 评论 #16 — ableeker (2021-02-13T12:26:10Z)

I can also confirm that AMDGPU-PRO 20.40 will render the images correctly with cl-fast-relaxed-math enabled. Also, significantly, that 20.45 will NOT correctly render the images with this option enabled. And the big change going from 20.40 to 20.45 is the switch from PAL to ROCm. It's obvious that cl-fast-relaxed-math has been broken in ROCm since 3.5 (and still is).

---

### 评论 #17 — ROCmSupport (2021-02-15T05:19:57Z)

Thanks @ableeker 
I am trying on a different machine to reproduce the problem. Will move to component owner shortly.

---

### 评论 #18 — ROCmSupport (2021-03-01T08:51:24Z)

Hi All,

As per the latest information and clarity provided in our Documentation that ROCm does not support GUI applications officially.

Docs also updated accordingly @ https://github.com/RadeonOpenCompute/ROCm#hardware-and-software-support

_Hardware and Software Support
ROCm is focused on using AMD GPUs to accelerate computational tasks such as machine learning, engineering workloads, and scientific computing. In order to focus our development efforts on these domains of interest, ROCm supports a targeted set of hardware configurations which are detailed further in this section._
**Note: The AMD ROCm™ open software platform is a compute stack for headless system deployments. GUI-based software applications are currently not supported.**

---

### 评论 #19 — preda (2021-03-01T09:22:22Z)

@ROCmSupport did the ROCm team investigate in order to establish whether this bug report indicates a correctness issue in the ROCm stack (i.e. a bug) or not? Otherwise, closing a bug report without even doing the basic investigation to rule out ROCm's role as the bug-cause is a lost opportunity to uncover and fix *reported* bugs.


---

### 评论 #20 — ROCmSupport (2021-03-09T12:11:02Z)

We are going to rephrase the text about GUI apps in our rocm documentation.
We have come up with some plans to handle GUI apps in a way.
I am reopening it now.
Thank you.

---

### 评论 #21 — ableeker (2021-09-11T10:49:05Z)

ROCm 4.3.1 still renders the images incorrectly with -cl-fast-relaxed-math enabled. It will however render the images correctly when it's disabled.

---

### 评论 #22 — ROCmSupport (2021-09-13T04:55:18Z)

Hi @ableeker 
This is a manifestation of a known issue within the Luxmark 3.1 sources. See https://github.com/LuxCoreRender/LuxMark/issues/9 . The issue has been resolved in Luxmark 4 . For Luxmark 3.1, the issue can be worked-around by disabling the -cl-fast-relaxed-math option.
Hope this helps.
Thank you.

---
