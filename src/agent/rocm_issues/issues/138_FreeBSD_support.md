# FreeBSD support

> **Issue #138**
> **状态**: closed
> **创建时间**: 2017-06-30T08:21:00Z
> **更新时间**: 2025-05-09T07:49:36Z
> **关闭时间**: 2017-07-02T00:17:56Z
> **作者**: kev009
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/138

## 描述

Hi,

 I run a core engineering group at one of the largest CDNs.  We use FreeBSD for a variety of reasons and find it offers a pleasant long term development experience with stable APIs and KPIs over Linux, while meeting a variety of other complex demands.  We are experimenting with ML in addition to other GPU workloads such as transcoding.  Will AMD support ROCm on FreeBSD?  A lot of the effort to do so is already done:  https://github.com/freebsddesktop.  Nvidia offers a driver as an interesting data point.

---

## 评论 (13 条)

### 评论 #1 — gstoner (2017-07-02T00:17:48Z)

The FreeBSD Comunity has shown interest in this, right now we have few more Linux distro to finish out REHL and SUSE first in next few quarters for existing customers before we could entertain this.   
 
But I know our Business Development team would love to talk to you about the opportunity.    

 One thing our driver stack is a bit more complex than a standard graphics driver, there is the KFD and Thunk + ROCr, modified TTM interface. But weight now is all the components that sit on the stack that would need to be ported and tested as well.  HCC, OpenCL, HIP, Math Libraries and applications 

---

### 评论 #2 — gstoner (2017-07-03T17:29:54Z)

We may see some activity here now.   I know more soon 

---

### 评论 #3 — kev009 (2017-07-03T20:43:22Z)

@gstoner thanks, I will try to come in through sales.  We've lost our past contacts with AMD but the modern EPYC and Radeon look like prime contenders for our workloads.

---

### 评论 #4 — palevas (2019-07-21T17:41:39Z)

@gstoner Any updates about FreeBSD support?

---

### 评论 #5 — ghost (2019-10-05T16:03:43Z)

+1 for some BSD love

---

### 评论 #6 — OlCe2 (2020-04-07T09:07:11Z)

+1 as well. Any news? Regards.

---

### 评论 #7 — dchmelik (2020-04-25T04:31:36Z)

I'd also love to see FreeBSD Unix ROCm (and ROCm for any main/other strictly Unix[-like] (i.e., non-systemd, etc.) OSes, like *BSD (three classic) & OpenSolaris/IllumOS Unixes, Slackware GNU/Linux.  I know ROCm builds on a newer non-systemd GNU/Linux.)  My only AMDGPU-pro option had been OSes I questioned were worth extreme emotional pain of systemd, and many other issues, just for newer Radeon.  Of course, my first choice would be FreeBSD & Slackware w/ROCm,  but eventually, Unix[-like] variety would be good.

---

### 评论 #8 — ghost (2021-01-05T14:05:04Z)

Any update on this?

---

### 评论 #9 — pbpjackd (2022-02-17T07:08:10Z)

> We may see some activity here now. I know more soon

Did this thread continue elsewhere or is there simply no news on that topic ?

---

### 评论 #10 — ROCmSupport (2022-02-21T08:38:11Z)

This is a closed thread and so i request/recommend to file a new issue, if any. Thank you.

---

### 评论 #11 — ghost (2022-02-21T17:22:20Z)

> > We may see some activity here now. I know more soon
> 
> Did this thread continue elsewhere or is there simply no news on that topic ?

Idk. It would have been nice to have at least ROCm support, if we don't have CUDA. It is still better than CPU...

---

### 评论 #12 — rajhlinux (2022-09-11T06:12:03Z)

Also would like to use ROCm on FreeBSD... Need it for machine learning on AMD GPUs.

---

### 评论 #13 — fipti (2022-12-18T23:56:59Z)

I'm also interested in Freebsd support.

---
