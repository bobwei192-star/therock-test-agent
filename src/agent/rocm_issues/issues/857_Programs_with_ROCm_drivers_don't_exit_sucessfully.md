# Programs with ROCm drivers don't exit sucessfully

> **Issue #857**
> **状态**: closed
> **创建时间**: 2019-08-05T01:04:29Z
> **更新时间**: 2020-04-20T11:42:16Z
> **关闭时间**: 2019-09-04T14:12:40Z
> **作者**: iszotic
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/857

## 描述

dkms status: amdgpu, 2.6-22, 4.15.0-55-generic, x86_64
gpu: 2 Vega 56, gfx900
cpu: AMD 1700 with X370

Hi, so every time I execute a program with rocm drivers, be HIP with tensorflow or OpenCL with Luxcore, the program doesn't exit successfully as if it is waiting in an infinite loop, but not consuming resources of the GPU (half of the GPU taches are on and it makes a scary coil whine and the watts consumed are like it is idling). It stops doing this after executing another program(and starts doing it again when it finishes), rebooting the computer, or executing a program and stop the execution of the program from terminal so it doesn't exit.

I have no idea how to debug GPUs so some help would be appreciated. This has been a recurrent problem with past ROCm releases and it occurs with the display GPU and the extra one, this doesn't occur with AMDGPU-pro OpenCL drivers.


---

## 评论 (9 条)

### 评论 #1 — Bengt (2019-09-02T11:51:09Z)

Hi @iszotic,

I ran into the same issue with rocm-tensorflow:

<https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/621>

I am also puzzled on how to debug this, but maybe my reproduction procedure can serve as a starting point.

Regards,
Bengt

---

### 评论 #2 — iszotic (2019-09-03T05:29:37Z)

hi @Bengt, I should have posted before, I really thought this only happened to me because of how many releases have passed without a fix.

I realized it has something to do with the clocks and I mitigated somehow the issue using radeon-profile, a 3rd party tool (by casualty, because I needed more control over the fans because the first GPU was throttling a lot), if you set the preset to min_sclk or low the GPU uses the lowest clock possible, in your post is like the 850mhz state and it doesn't whine, but the problem persists, changing the profile to the default (auto profile) again raises the clock to 1250 mhz with whining, so I have to keep changing profiles all the time, I check the clocks using the same tool.

Funny enough when you set the preset to high the whine is even worse and all the taches light up with 1600mhz clock.

---

### 评论 #3 — Bengt (2019-09-03T12:08:38Z)

Hi @iszotic,

yes, the issue does definitely affect multiple users and also both of my Vega 64 cards.

I can confirm, that  manually choosing a low-gpu-clock power profile in radeon profile works. For me, the cards does indeed clock down and 7 of the the GPUTach LEDs turn off. However, radeon profile needs to be compiled from source and is far from perfect. This workaround might be viable for you and me, but not the vast majority of users. Less savvy users still need to perform a reboot as a workaround, which is very cumbersome and breaks workflows. Power state management should definitely work near-flawlessly.

---

### 评论 #4 — Bengt (2019-09-03T12:24:59Z)

Another application provoking this behavior is clpeak, which can be easily installed via snap:

<https://snapcraft.io/clpeak>

---

### 评论 #5 — Bengt (2019-09-03T12:34:12Z)

A gfx803 (Fury X, Fiji) installed in the same system is not affected. So this issue seems to only affect gfx900 (Vega 64/56, Vega 10).

---

### 评论 #6 — Bengt (2019-09-03T21:22:32Z)

Restricting the DPM states was found to solve this issue for tensorflow and clpeak workloads:
 
```
/opt/rocm/bin/rocm-smi --setsclk 0 6 7
[...]
GPU[0] 		: Successfully set sclk frequency mask to Level 0 6 7
[...]
```

---

### 评论 #7 — iszotic (2019-09-04T14:12:40Z)

`/opt/rocm/bin/rocm-smi --setsclk 0 1 2 3 4 5 6 7`, setting all states works too, after booting or in the middle of a program running

---

### 评论 #8 — Bengt (2020-04-20T11:41:56Z)

Folding at Home (F@H) can also trigger this behavior. Picture of the aftermath:

![IMG_20200420_133729](https://user-images.githubusercontent.com/11575/79747679-696fc400-830c-11ea-86ca-93e9dd4fb6da.jpg)


---

### 评论 #9 — Bengt (2020-04-20T11:42:15Z)

See https://github.com/RadeonOpenCompute/ROCm/issues/1081

---
