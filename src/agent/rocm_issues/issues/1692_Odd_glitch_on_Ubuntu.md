# Odd glitch on Ubuntu

> **Issue #1692**
> **状态**: closed
> **创建时间**: 2022-02-25T02:53:00Z
> **更新时间**: 2022-03-03T05:02:39Z
> **关闭时间**: 2022-03-03T04:31:52Z
> **作者**: dillfrescott
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1692

## 描述

I am experiencing a very odd glitch. So far I've tested this with focal, xenial, and also jammy, where it happens on all 3 fresh installs.

When I try to run any program that takes advantage of rocm 4.3, the program just gets stuck.

I've left it overnight to see if it would resume but it did not.

But the most odd thing about it is that for some reason my gpu, (RX Vega 56) becomes extra "sensitive" I wanna say...

For example, while the program is stuck, just moving or clicking the mouse shoots the gpu usage to 100%, and as soon as I pkill python it doesn't do it anymore.

I've been tinkering with this for days and I have no idea why it's doing this.

Any help at all would be appreciated.

---

## 评论 (12 条)

### 评论 #1 — ROCmSupport (2022-02-25T11:56:34Z)

Hi @DillFrescott 
Thanks for reaching out.
Can you please share the exact steps you followed so that I will try to replicate here.
Thank you.

---

### 评论 #2 — dillfrescott (2022-02-26T01:21:23Z)

Ok let me think.

I installed a fresh copy of Ubuntu 20.

It comes with python already installed. I installed rocm pytorch 4.3 using pip.

I try to run any program that takes advantage of the gpu, and the cursor just gets stuck, and the GPU Tachometer on the side just kind of flashes.

The GPU itself is fine, I use it to play games on Windows all the time at max settings.

For some odd reason it doesnt want to cooperate with rocm...

I dont think im doing anything out of the ordinary to cause issues.

---

### 评论 #3 — dillfrescott (2022-02-27T03:31:45Z)

@ROCmSupport Is there an easy way to install an even newer version of rocm pytorch? One newer than 4.3?

---

### 评论 #4 — ROCmSupport (2022-02-28T10:05:37Z)

Hi @DillFrescott 
Thanks for more data points. 
I am not able to reproduce your issue locally. I recommend to share dmesg output for more udnerstanding.
And also I suggest you to install the latest ROCm 5.0 + the latest pytorch docker: _rocm/pytorch:latest_
Thank you.

---

### 评论 #5 — dillfrescott (2022-03-02T03:25:03Z)

Okay

---

### 评论 #6 — dillfrescott (2022-03-02T03:27:28Z)

@ROCmSupport I would like to install rocm 5 + pytorch in a conda environment. Is that possible without using docker? If so, is there a way to do it that doesn't involve building things from scratch?

---

### 评论 #7 — ROCmSupport (2022-03-02T06:39:14Z)

Hi @DillFrescott 
ROCm supports pytorch in terms of docker only, which is a pip based environment.
We do not support conda for now, so can not comment on this.
Thank you.

---

### 评论 #8 — dillfrescott (2022-03-02T07:39:43Z)

@ROCmSupport Gotcha. Thank you for the info!

---

### 评论 #9 — dillfrescott (2022-03-02T08:15:47Z)

@ROCmSupport Can the rocm docker be run on a windows host?

---

### 评论 #10 — ROCmSupport (2022-03-02T13:03:26Z)

Hi @DillFrescott 

ROCm dockers(not only rocm, any linux dockers) can not be running on Windows host.
Containers are using the underlying operating system resources and drivers, so Windows containers can run on Windows only, and Linux containers can run on Linux only.

_But there is some other way like below, if you wish to:_
Docker for Windows allows you to simulate running Linux containers on Windows, but under the hood a Linux VM is created, so still Linux containers are running on Linux, and Windows containers are running on Windows.

Hope this information helps.
Thank you.

---

### 评论 #11 — dillfrescott (2022-03-02T22:24:14Z)

Oh cool! Thank you for the response! <3

---

### 评论 #12 — ROCmSupport (2022-03-03T04:31:52Z)

Hi @DillFrescott 
I hope I have shared all of the requested information. Feel free to file new issues, if any, for quick resolutions.
Thank you.

---
