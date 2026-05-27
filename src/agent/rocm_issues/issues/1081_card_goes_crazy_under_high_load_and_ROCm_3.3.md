# card goes crazy under high load and ROCm 3.3

> **Issue #1081**
> **状态**: closed
> **创建时间**: 2020-04-13T08:27:58Z
> **更新时间**: 2021-06-02T12:15:58Z
> **关闭时间**: 2021-06-02T12:15:58Z
> **作者**: akostadinov
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1081

## 描述

At the moment I'm running Folding@Home. I figured running two GPU slots on same card bringd higher efficiency but after some time Fan goes to 100% and I see the following non-sense from `rocm-smi`:
```
$ rocm-smi 
========================ROCm System Management Interface========================
================================================================================
GPU  Temp    AvgPwr        SCLK  MCLK  Fan     Perf  PwrCap  VRAM%  GPU%  
0    511.0c  1072.741824W  N/A   N/A   100.0%  auto  220.0W    2%   100%  
================================================================================
==============================End of ROCm SMI Log ==============================
```

To reproduce, one needs to run `FAHClient` first. Then using `FAHControl` add a second GPU slot and hardcode GPU and OpenCL index to `0`. btw there seems to be a configurator bug because FAHClient loses this configuration on restart.

While running 2 tasks on same GPU simultaneously for awhile the situation described above happens.

-- fahclient-7.5.1-1.x86_64 on Red Hat Enterprise Linux 7.7
-- Vega 10 XTX [Radeon Vega Frontier Edition] with ROCm 3.3 driver

---

## 评论 (5 条)

### 评论 #1 — Bengt (2020-04-17T02:39:14Z)

Interesting. Is running two slots in one gpu a supported use case by Folding@Home? Last time I checked, the workload would not even run on Vega. I would like to give that another try.

---

### 评论 #2 — akostadinov (2020-04-20T10:31:15Z)

@Bengt , F@H works since ROCm 3.3. Supported use case by who? 

Standard user software shouldn't be able to cause card to behave in this way. Card should never show 511°C and should not block like this. This is default settings, no over/underclocking, fan control changes or anything.

Also issue is not that it doesn't work. Just after some time cooling management or something seems to become busted.

---

### 评论 #3 — Bengt (2020-04-20T11:37:51Z)

@akostadinov I can confirm that F@H works fine now. I have already completed several work units on my 4 Vegas, but I did not yet test running multiple slots per card. I did not observe the erroneous power and temperature readings and the fans did not go to full speed. I run into this issue, though:

https://github.com/ROCmSoftwarePlatform/tensorflow-upstream/issues/621

---

### 评论 #4 — ROCmSupport (2021-03-17T07:40:01Z)

Thanks @akostadinov for reaching out.
Can you please try with the latest ROCm 4.0 or 4.1 and share an update.
Thank you.

---

### 评论 #5 — ROCmSupport (2021-06-02T12:15:58Z)

Am closing this as there is no update for > 1 month.
Thank you.

---
