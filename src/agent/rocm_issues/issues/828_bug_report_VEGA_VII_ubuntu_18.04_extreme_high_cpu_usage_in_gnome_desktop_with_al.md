# bug report: VEGA VII ubuntu 18.04 extreme high cpu usage in gnome desktop with all rocm version.

> **Issue #828**
> **状态**: closed
> **创建时间**: 2019-06-25T14:49:58Z
> **更新时间**: 2023-12-21T14:34:55Z
> **关闭时间**: 2023-12-21T14:34:54Z
> **作者**: smartbitcoin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/828

## 描述

Since the day vega vii released and  I started test it with linux ( ubuntu ). but I have no way to use it as a desktop environment , simple because the gnome library based app even as simple as gnome terminal will burn CPU resource crazy.

as it show in following print screen.

![image](https://user-images.githubusercontent.com/5984485/60108300-62047c00-9736-11e9-89ab-1372a19b1654.png)

at least in my stand ubuntu environment , it's a bug.   

anybody know any tricky to make it works?   either patch the driver or what ever.  
or dear rocm team,  are there anyway can fix this?



---

## 评论 (5 条)

### 评论 #1 — kentrussell (2019-06-28T13:23:46Z)

Looks like it could be an issue with Gnome, not ROCm:
https://bugs.launchpad.net/ubuntu/+source/gnome-shell/+bug/1773959
Though this is something that gets reported to Gnome yearly (seen bug reports as old as 2012 with the same symptoms).

But to do the whole "check everything ROCm" checklist, do you see this issue with a different GPU? Is this issue present with the ROCm driver, or the upstream/stock kernel driver, or both?  Is the issue limited to a specific monitor/output, or is it present with multiple monitors (with different resolutions/refresh rates) and different output types (HDMI/DIsplayport/DVI)?


---

### 评论 #2 — smartbitcoin (2019-06-28T19:34:20Z)

this issue is fully on rocm stack , not up steam kernel.  and it should be vega vii related, b/c I use vega 64 with same OS environment ( still pure rocm stack ) never have this problem.  that 's why I don't think it should be gnome-shell bug. 

---

### 评论 #3 — kentrussell (2019-06-29T19:16:41Z)

So to confirm, you didn't see this issue with Radeon VII using the upstream kernel, and on the same machine with ROCm 2.5 installed, it didn't happen on the Vega64 card. Does dmesg have anything in it to indicate anything from the kernel? Is it a DKMS installation, or did you build the kernel and install it as a monolithic kernel?

---

### 评论 #4 — tasso (2023-12-19T15:55:15Z)

Can you please retest with ROCm 6.0?  If the issue is not reproducible, can you please close it?  Thanks!

---

### 评论 #5 — tasso (2023-12-21T14:34:55Z)

Original ticket is more than a year old and the person that opened ticket originally has not responded to the latest request.  If this is still an issue, please file a new ticket and we will happy to investigate it.  Thanks!

---
