# retired...

> **Issue #345**
> **状态**: closed
> **创建时间**: 2018-02-22T18:03:34Z
> **更新时间**: 2018-08-19T16:46:03Z
> **关闭时间**: 2018-02-23T08:19:47Z
> **作者**: ghost
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/345

## 描述

*(无描述)*

---

## 评论 (9 条)

### 评论 #1 — dfad44 (2018-02-22T19:05:04Z)

Yet to try it but thank you for this!

---

### 评论 #2 — dfad44 (2018-02-23T00:35:41Z)

Tested the last 2hrs, Runs 1105MCLK with stability on gfx900


---

### 评论 #3 — preda (2018-02-23T02:37:04Z)

What is the issue here? Are you using "issues" for a product announcement?

---

### 评论 #4 — gstoner (2018-02-23T04:38:42Z)

@ Preda He is doing a custom ROCm

Get Outlook for iOS<https://aka.ms/o0ukef>
________________________________
From: Mihai Preda <notifications@github.com>
Sent: Thursday, February 22, 2018 8:37:05 PM
To: RadeonOpenCompute/ROCm
Cc: Subscribed
Subject: Re: [RadeonOpenCompute/ROCm] Here is the prebuilt userland/dev system with everything prebuilt and ohh when I find zed tested.. Plug it in and boot. The userland also alters the clocks on the 570s to faster speeds then the 580's 1632/2220 Mhz With no s...


What is the issue here? Are you using "issues" for a product announcement?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/345#issuecomment-367891912>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DubO0J4uRGVTpRSc39wpHAfZbTk78ks5tXiRRgaJpZM4SPvWX>.


---

### 评论 #5 — gstoner (2018-02-23T14:01:04Z)

@tekcomm that was long ago,  we never had those issue we subsidiary of Motorola,  But like you, I worked on Linux for embedded then.  So you were in BCS group for Motorola 

---

### 评论 #6 — dfad44 (2018-02-24T12:38:36Z)

@tekcomm 

Pardon my noob, I'm still a linux infant (started use Sept 2017). 

What is the equivalent for 1950x. I look inside /sys/devices/system/cpu/cpufreq/policy0/scaling_min_freq but it is not found.  I look a few folders up and see that the line ends at /sys/devices/system/cpu/cpufreq/(with nothing further). Should I append the folder starting with /policy(x)/scaling_min_freq and echo 4200000 for each line of all 15 cores. 

I'd really hate to do something stupid. Thanks for you help



---

### 评论 #7 — dfad44 (2018-02-24T12:47:56Z)

/sys | grep cpu | grep min returns blank unfortunately. I'm gonna need some coffee for this 

---

### 评论 #8 — dfad44 (2018-03-15T15:13:46Z)

looking forward to it. 

---

### 评论 #9 — ghost (2018-03-17T12:30:06Z)

Dfad, I did a rewrite to it with a few more mods.  email me a skype or something and Ill send it to you directly because its production ready but you still have to change a few things based on your hardware. :)
It Requires at least i7 gen3.

---
