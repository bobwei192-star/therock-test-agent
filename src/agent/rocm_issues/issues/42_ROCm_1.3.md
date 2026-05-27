# ROCm 1.3

> **Issue #42**
> **状态**: closed
> **创建时间**: 2016-10-30T13:41:55Z
> **更新时间**: 2016-10-30T15:25:42Z
> **关闭时间**: 2016-10-30T15:25:42Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/42

## 描述

I have two RX 470s on my system, and I am really looking forward to the 1.3 release.
Currently, using both 470s causes a race condition on windows 10, and the system often
freezes.  So, I can't use both in production - have to stick with single card for now.

When you do release 1.3, could you please give detailed install instructions for XUbuntu system?
(XUBuntu 16.04)  Last time I tried, I was not able to get AMDGPU-PRO driver working - no cards were
recognized.

Thanks!!


---

## 评论 (2 条)

### 评论 #1 — gstoner (2016-10-30T13:56:21Z)

ROCm does not use the AMDGPU-Pro driver foundation it is base off the AMDGPU Open Driver.    1.3 will be released with Ubuntu 16.04 support.

greg
On Oct 30, 2016, at 8:41 AM, Aaron Boxer <notifications@github.com<mailto:notifications@github.com>> wrote:

I have two RX 470s on my system, and I am really looking forward to the 1.3 release.
Currently, using both 470s causes a race condition on windows 10, and the system often
freezes. So, I can't use both in production - have to stick with single card for now.

When you do release 1.3, could you please give detailed install instructions for XUbuntu system?
(XUBuntu 16.04) Last time I tried, I was not able to get AMDGPU-PRO driver working - no cards were
recognized.

Thanks!!

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHubhttps://github.com/RadeonOpenCompute/ROCm/issues/42, or mute the threadhttps://github.com/notifications/unsubscribe-auth/AD8DudLX5TzBicNzumQCrtWzW0eNKnxPks5q5J6jgaJpZM4KkYNZ.


---

### 评论 #2 — boxerab (2016-10-30T15:25:42Z)

Thanks.


---
