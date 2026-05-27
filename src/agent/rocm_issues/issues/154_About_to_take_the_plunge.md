# About to take the plunge

> **Issue #154**
> **状态**: closed
> **创建时间**: 2017-07-07T13:14:03Z
> **更新时间**: 2017-07-07T18:06:43Z
> **关闭时间**: 2017-07-07T18:06:43Z
> **作者**: boxerab
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/154

## 描述

I am about to install ROCm on my system, to run my OpenCL app. 
Just wanted to run this by you guys before I click install:

Hardware:

i7 6700 CPU
ASUS Z170-K MoBo
750W power supply
2X Saphire RX 470 GPUs : one card in 16x PCI slot, and one card in 4x PCI slot

Software:
Currently runs windows 10 - I want to dual bool to XUbuntu 16.04.2 
So, NOT a headless system.

Can anyone see any issues with this setup ? 

Thanks!







---

## 评论 (9 条)

### 评论 #1 — briansp2020 (2017-07-07T16:31:37Z)

Only one GPU will work on that mother board.
See https://github.com/RadeonOpenCompute/ROCm/issues/46#issuecomment-264081299

---

### 评论 #2 — boxerab (2017-07-07T16:38:35Z)

Thanks, Brian. I am happy use just one card - hopefully I don't have to actually remove the second card for this to work ?

---

### 评论 #3 — boxerab (2017-07-07T16:38:48Z)

Can I just disable the x4 slot in the bios ?

---

### 评论 #4 — boxerab (2017-07-07T16:39:28Z)

Also, are you able to verify that non-headless OS will be fine ?

---

### 评论 #5 — gstoner (2017-07-07T16:46:17Z)

That is perfect.

Greg
On Jul 7, 2017, at 11:39 AM, Aaron Boxer <notifications@github.com<mailto:notifications@github.com>> wrote:


Also, can you please verify that non-headless OS will be fine ?

—
You are receiving this because you are subscribed to this thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/154#issuecomment-313732301>, or mute the thread<https://github.com/notifications/unsubscribe-auth/AD8DuRF_rjm1LW2vEK2_ryBOzAVEDeFUks5sLl9BgaJpZM4OQ7N->.



---

### 评论 #6 — boxerab (2017-07-07T16:54:01Z)

Thanks, Greg. So, to confirm, I will only be able to use the card in the x16 slot.
Do I have to mess with the bios or remove the second card for this to work? 

---

### 评论 #7 — ekondis (2017-07-07T17:35:15Z)

Personally, I'm using the 1st GPU on a similar configuration without problems. I had experienced problems in the past with ROCm versions prior to 1.4 where I had to remove the 2nd GPU.

---

### 评论 #8 — boxerab (2017-07-07T17:37:49Z)

Thanks, Elias. Glad to hear that. 

---

### 评论 #9 — boxerab (2017-07-07T18:06:43Z)

Thanks everyone for all of your help! Opencl seems to be working fine for single card.
Closing.

---
