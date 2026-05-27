# On vega64, rocm 1.9.0: luxmark 3.1 and blender 2.79 not works

> **Issue #555**
> **状态**: closed
> **创建时间**: 2018-09-23T13:39:10Z
> **更新时间**: 2020-12-16T12:22:09Z
> **关闭时间**: 2020-12-16T12:22:09Z
> **作者**: sp82
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/555

## 描述

Hi,
in particular the 2 programs wait long time in "...Compiling kernels ..." than nothing happend.
Best Regards,
Salvatore.

---

## 评论 (8 条)

### 评论 #1 — kentrussell (2018-09-25T11:14:00Z)

Can you attach a dmesg? Did these work in 1.8 or are you only trying it now in 1.9?

---

### 评论 #2 — jlgreathouse (2018-09-25T15:21:28Z)

I believe he means the OpenCL kernels, rather than the Linux kernel modules.  I suspect this is a dupe of the Blender problem in #503 

---

### 评论 #3 — sp82 (2018-09-26T15:06:39Z)

I tested with 1.8 on Ubuntu16.04 and 1.9 on Ubuntu18.04. 
Broken in both cases the compilation of OpenCL kernels.
Update:
I run Ubuntu18.04 with the Linux Kernel 4.18.7-041807-generic from here: http://kernel.ubuntu.com/~kernel-ppa/mainline/v4.18.7/
and rocm 1.9
this is the rendering of the Ryzen Logo console log :
![screenshot_20180928_113656](https://user-images.githubusercontent.com/549045/46200957-47ba8080-c313-11e8-900f-2e2e3aeebd00.png)
After a long time the opencl kernels get compiled but the rendering do not start.
The long time to compile the kernels is another issue, waiting soooo long is not good.
Blender 2.79b or 2.8 alpha same result.


---

### 评论 #4 — illwieckz (2018-10-16T17:52:17Z)

I face the same issue with Luxmark 3.1 (Ubuntu 18.04 and Radeon R9 390X here). The _LuxBall HDR_ benchmark runs and completes (see [results](http://www.luxmark.info/node/5725)) and performs better than my [previous attempt](http://www.luxmark.info/node/3629) with AMDGPU-PRO but the _Microphone_ benchmark never stops to compile OpenCL kernel, o r I have not waited enough.

While compiling OpenCL kernel the `Graphics pipe` bar in [`radeontop`](https://github.com/clbr/radeontop) shows a 100% usage while other statistic bars are idling. CPU usage is idling too. It behaves like an infinite loop.

---

### 评论 #5 — boberfly (2018-11-07T09:51:31Z)

I just tried with the latest bleeding edge branch of Mesa's OpenCL 1.1:
http://luxmark.info/node/5806
Speed demon :)
ROCm/AMD-APP 2679.0 isn't as good unfortunately:
http://luxmark.info/node/5807


---

### 评论 #6 — ubombi (2018-11-23T22:05:13Z)

Same on  Manjaro 
**Kernel**: _4.19.1-1_ _(No dkms)_
**ROCm**:  _1.9_ 
**GPU**: _Vega FE_
Packages from AMD's ubuntu repository converted via `deptap`.

It can render just a basic blender cube and freeze on any real scene.

---

### 评论 #7 — sp82 (2018-12-01T07:44:28Z)

Still not working. OpenCL landscape is a mess like OpenGL, no one get it right. I hope to see a Vulkanized version of OpenCL, simplified and easy to implement. An Open Computing Language is not important anymore. The important, in my opinion, is a simple api to run spir-v kernels, whatever high language you wonna use.

---

### 评论 #8 — ROCmSupport (2020-12-16T12:22:09Z)

This is 2 years old issue and the environment is very old.
Recommend to try with the latest ROCm release and file a ticket if any.

---
