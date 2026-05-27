# ROCm Kernel 4k resolution problem

> **Issue #227**
> **状态**: closed
> **创建时间**: 2017-10-16T18:11:42Z
> **更新时间**: 2018-06-03T15:11:15Z
> **关闭时间**: 2018-06-03T15:11:15Z
> **作者**: reger-men
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/227

## 描述

Hey everybody,

I installed new Ubuntu 16.04 on my PC. Then i followed the installation instruction as documented here: [ROCm](https://rocm.github.io/ROCmInstall.html).

![screenshot from 2017-10-16 18-32-28](https://user-images.githubusercontent.com/8779942/31627389-761f2088-b2ad-11e7-9182-944a621f918c.png)


After pc restart, I cannot select high resolution. (3840x2160)
![screenshot from 2017-10-16 18-31-06](https://user-images.githubusercontent.com/8779942/31627380-6d0ece94-b2ad-11e7-8c52-365117ca4674.png)

**OS:   Ubuntu 16.04
GPU: WX 7100**

Any idea?
 

---

## 评论 (6 条)

### 评论 #1 — gstoner (2017-10-16T23:17:33Z)

This is a mesa/amdgpu problem 

---

### 评论 #2 — reger-men (2017-10-17T15:35:57Z)

@gstoner I have no amdgpu-pro driver installed. 

---

### 评论 #3 — jamilbk (2017-10-17T17:05:31Z)

@reger-men The amdgpu and amdgpu-pro drivers are different. I use the amdgpu drivers from [this repository](https://launchpad.net/~oibaf/+archive/ubuntu/graphics-drivers) to get everything working for me, but I'm on Vega FE. Worth a shot.


---

### 评论 #4 — gstoner (2017-10-17T17:15:30Z)

ROCm Userland compute components sit on amdgpu Linux driver.    The amdgpu Linux driver supports all of the X11/OpenGL, display logic. you can look at here   https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/tree/master/drivers/gpu/drm/amd 

If the issue is in the MesaGL and X11 userland components are part of your distribution, we do not distribute these.      ROCm really is only about GPU Computing solution.   We notify the Linux driver team your having an issue 

---

### 评论 #5 — gstoner (2017-10-17T17:19:00Z)



Here is good article on what going on in AMDGPU from Display perspective  https://www.phoronix.com/scan.php?page=news_item&px=AMD-Open-FreeSync-Planning 

https://www.phoronix.com/scan.php?page=news_item&px=AMDGPU-DC-Cleaning-Pre-4.15 



---

### 评论 #6 — reger-men (2017-10-18T15:09:46Z)

I installed ampgpu-pro 17.30, the 4k resolution is supported on `kernel 4.10` but not on ROCm `kernel 4.11`. That mean the ROCm drivers doesn't support 4k, is that right?

---
