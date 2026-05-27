# Vega 64/56/FE how to change SoC Clock from 1107 to 1200?

> **Issue #713**
> **状态**: closed
> **创建时间**: 2019-02-18T19:35:36Z
> **更新时间**: 2023-12-12T21:47:10Z
> **关闭时间**: 2023-12-12T21:47:10Z
> **作者**: marcrblevins
> **标签**: Question
> **URL**: https://github.com/ROCm/ROCm/issues/713

## 标签

- **Question** (颜色: #cc317c)

## 描述

Can rocm-smi change the SoC Clock value?
Not talking about Core or Memory frequencies.
Look at:
https://docs.google.com/spreadsheets/d/1-rhYsaRXO1ahk3PyrEgT9gXzs7ImAzh-sbqtgwy8HQg/edit#gid=964538665
See SoC Clock?
6C B0 01 -> 1107
C0 D4 01 -> 1200
Thanks,
Marc

---

## 评论 (11 条)

### 评论 #1 — jlgreathouse (2019-02-18T19:59:57Z)

@kentrussell can tell you more about this. I believe that we do not support changing SOCCLK as of ROCm 2.1, but it is an expected feature in a future ROCm release.

---

### 评论 #2 — marcrblevins (2019-02-18T20:40:38Z)

For mining purposes, we need that 1200 SoC clock to compete with the FPGAs and ASIC.  GPU mining is a dying breed.  :(  Thanks for your quick response...

---

### 评论 #3 — kentrussell (2019-02-19T14:00:56Z)

Indeed, 2.2 will have support for this in the SMI. If /sys/class/drm/card0/device/pp_dpm_socclk exists, you can modify it yourself by doing:
echo # | sudo tee /sys/class/drm/card0/device/pp_dpm_socclk
Where # is the level that you want to apply. I can't remember if those changes are in the 2.1 kernel or not, but the SMI supports it in 2.2 once it comes out. 
Note: I used card0 assuming that you don't have any integrated graphics or control GPUs installed. It might be card1/card2/etc, depending on your system configuration

---

### 评论 #4 — jlgreathouse (2019-02-19T14:56:59Z)

The `rock-dkms` module that comes with ROCm 2.1 does not include `pp_dpm_socclk`, at least on my test system with a Vega 10 GPU.

---

### 评论 #5 — marcrblevins (2019-02-19T15:35:54Z)

Found this link:
https://www.phoronix.com/scan.php?page=news_item&px=Vega-10-More-PowerPlay-Controls

I’ll wait.

Thanks,
Marc

From: Joseph Greathouse <notifications@github.com>
Sent: Tuesday, February 19, 2019 8:59 AM
To: RadeonOpenCompute/ROCm <ROCm@noreply.github.com>
Cc: marcrblevins <marcrblevins@hotmail.com>; Author <author@noreply.github.com>
Subject: Re: [RadeonOpenCompute/ROCm] Vega 64/56/FE how to change SoC Clock from 1107 to 1200? (#713)


The rock-dkms module that comes with ROCm 2.1 does not include pp_dpm_socclk, at least on my test system with a Vega 10 GPU.

—
You are receiving this because you authored the thread.
Reply to this email directly, view it on GitHub<https://github.com/RadeonOpenCompute/ROCm/issues/713#issuecomment-465162348>, or mute the thread<https://github.com/notifications/unsubscribe-auth/Aifn46_Rig7movA1kQYMvtkQOzuzF2kfks5vPBEvgaJpZM4bBfws>.


---

### 评论 #6 — nioroso-x3 (2019-03-05T03:25:37Z)

I use pptables to change clocks on my vegas, does that mean the soc clock in is ignored then?
If I create a pptable with the soc clock at 1300mhz my vegas crash, so that means something is changing.

---

### 评论 #7 — marcrblevins (2019-03-05T06:45:13Z)

> I use pptables to change clocks on my vegas, does that mean the soc clock in is ignored then?
> If I create a pptable with the soc clock at 1300mhz my vegas crash, so that means something is changing.

What do you use to create pptables?  Editor?  You can only go up to 1200mhz max for Vega FE/64s.

---

### 评论 #8 — ddobreff (2019-03-06T13:41:08Z)

Socclk above 1107Mhz requires a bit more voltage, you should keep Socclk idx you use usually just a tad upper than actual Memclk. 

---

### 评论 #9 — nioroso-x3 (2019-03-28T23:21:52Z)

> > I use pptables to change clocks on my vegas, does that mean the soc clock in is ignored then?
> > If I create a pptable with the soc clock at 1300mhz my vegas crash, so that means something is changing.
> 
> What do you use to create pptables? Editor? You can only go up to 1200mhz max for Vega FE/64s.

Just convert hex to binary, I used a python script for it. Then you can load it to /sys/class/cardX/device/pp_table using cat.

---

### 评论 #10 — tasso (2023-12-08T18:23:31Z)

Is this issue still reproducible?  If not; can we please close it?  Thanks!

---

### 评论 #11 — tasso (2023-12-12T21:47:06Z)

Original ticket is more than a year old and the person that originally opened ticket  has not responded to the latest request.  If this is still an issue, please file a new ticket and we will investigate it.  Thanks!

---
