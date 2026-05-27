# power consumption of GPUs

> **Issue #607**
> **状态**: closed
> **创建时间**: 2018-11-07T08:45:10Z
> **更新时间**: 2021-01-07T10:59:13Z
> **关闭时间**: 2021-01-07T10:59:13Z
> **作者**: valeriob01
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/607

## 描述

With ROCm 1.9.211, kernel 4.19.0-rc7

The power consumption of one GPU (RX580) is ~30 Watts after boot, but does not return to ~30 Watts after stopping GPU computing program, it remains stuck at ~47 Watts.
Note that during the run of computing program the GPU power is ~144 Watts, it should return to ~30 Watts after stopping the program.

This issue was not present with kernel 4.17


---

## 评论 (12 条)

### 评论 #1 — preda (2018-11-07T21:02:22Z)

Do you set the sclk with e.g. rocm-smi --setsclk 5 ?
If so, that may explain it, because the clock remains fixed on a higher frequency even when the load is removed.

---

### 评论 #2 — valeriob01 (2018-11-07T22:05:50Z)

No I have never used rocm-smi to set the clock, but even so when I stop the program, the GPU Core Clock remains at 1319 Mhz instead of dropping to 300 Mhz.


---

### 评论 #3 — valeriob01 (2018-11-08T07:33:17Z)

Basically it seems like the "automatic mode" is not working properly, the "sensors" command reports the Core Clock at 300 Mhz after boot. Then when the program is launched the gpu core clock rises to 1319 Mhz, and when the program is stopped, it does not return to 300 Mhz.
It is working differently for GPU Memory Clock. The Memory clock is at 300 Mhz after boot, and rises to 2000 Mhz with load, and when the load is removed it returns to 300 Mhz.


---

### 评论 #4 — valeriob01 (2018-11-12T09:32:50Z)

On another main-board with one GPU, the power reported by sensors is 0 all the time.

---

### 评论 #5 — valeriob01 (2018-12-23T07:10:29Z)

The power consumption on multi-gpu systems is as follows, in a system with 2 gpu:

1. start a computation on the first gpu, all is good, sensor data is good.
2. The second gpu rises at 47Watts even if no computation was done on it.


---

### 评论 #6 — jlgreathouse (2018-12-24T21:42:31Z)

Does the temperature of the second GPU also rise from its original idle temperature? Note that it is possible to have thermal coupling between two GPUs if they are installed near one another (e.g. first GPU gets very hot, causing the air around it to warm; the second GPU thus runs hotter because the air it uses for cooling is warmer).

Higher temperatures can then lead to higher idle power, due to increases in static power usage.

---

### 评论 #7 — valeriob01 (2018-12-25T05:16:34Z)

Yes, it rises a few degrees. To notice in line with what you say: when both gpus are computing there is a difference of 10 C, the second gpu runs hotter.


---

### 评论 #8 — valeriob01 (2019-02-19T07:40:47Z)

> Yes, it rises a few degrees. To notice in line with what you say: when both gpus are computing there is a difference of 10 C, the second gpu runs hotter.

In the 2-gpu system one gpu runs hotter, but still within the thermal limits so there is no throttling.


---

### 评论 #9 — valeriob01 (2019-02-19T07:50:23Z)

News: in a single-gpu system, the gpu power is high at rest (43W vs. the previous 30W). So it is not a thermal-coupling issue. I include a screenshot of the temperature readings:

![20190219_082920](https://user-images.githubusercontent.com/25838910/52998203-fbd3b980-3422-11e9-8cc3-c0f2684b2870.jpg)

(it is being uploaded flipped upside-down, not my choice though, you can open it in a new tab, it will display right)).



---

### 评论 #10 — ROCmSupport (2021-01-07T09:22:50Z)

Hi @valeriob01 
Can you please verify with the latest ROCm 4.0 and share an update asap.
Thank you.

---

### 评论 #11 — valeriob01 (2021-01-07T10:31:50Z)

> Hi @valeriob01
> Can you please verify with the latest ROCm 4.0 and share an update asap.
> Thank you.

I hope you do realize that two years have passed and that I have replaced that GPU with a Radeon VII in 2019.


---

### 评论 #12 — ROCmSupport (2021-01-07T10:59:13Z)

Got it, thanks for the information @valeriob01 
I am closing this issue then as its irrelevant now.
As R7 is officially supported hardware now, you can file new issues, if any.
Thank you.


---
