# Rocm just... hangs

> **Issue #850**
> **状态**: closed
> **创建时间**: 2019-07-27T16:10:41Z
> **更新时间**: 2019-07-27T16:42:23Z
> **关闭时间**: 2019-07-27T16:42:23Z
> **作者**: ffleader1
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/850

## 描述

So i put together some old PC part and got this PC
System spec:
- Intel C2Q Q8400
- Main G41M VS3 r3 
- RAM 5GB (weird, I know)
- Rx 560 2GB

Not an ideal PC for ML but I just want to try.
I installed rocm before, and it works fine on my R7 1700/Vega 56 PC. However, when I install rocm on this one, it does not work.

No error, but everything related to rocm just hang.
For example, I install rocm-profiler, and it hangs:
![image](https://user-images.githubusercontent.com/15016720/61996855-8c45b280-b0c3-11e9-968c-079073cdc2d4.png)
I tried to run rocminfo, and it hangs also.
I got the ```strace rocminfo``` here:
https://pastebin.com/raw/KBAemKUT

Point is EVERYTHING related to Rocm just hang, and it does not even throw and error for me to understand what to google. So can any expert have a look?
Thanks

---

## 评论 (2 条)

### 评论 #1 — JMadgwick (2019-07-27T16:25:40Z)

> System spec:
>     * Intel C2Q Q8400
>     * Main G41M VS3 r3
>     * RAM 5GB (weird, I know)
>     * Rx 560 2GB

RX 560 is a GFX8 GPU. These GPUs need a Haswell/Zen CPU or newer in order to work with ROCm.
Your System is many years to old to support ROCm. [It's all detailed in this section of the Readme](https://github.com/RadeonOpenCompute/ROCm#hardware-support).

---

### 评论 #2 — ffleader1 (2019-07-27T16:42:23Z)

> > System spec:
> > * Intel C2Q Q8400
> > * Main G41M VS3 r3
> > * RAM 5GB (weird, I know)
> > * Rx 560 2GB
> 
> RX 560 is a GFX8 GPU. These GPUs need a Haswell/Zen CPU or newer in order to work with ROCm.
> Your System is many years to old to support ROCm. [It's all detailed in this section of the Readme](https://github.com/RadeonOpenCompute/ROCm#hardware-support).

I feel stupid now. Thank you :D

---
