# GpuOwl 5% performance regression in ROCm 3.5.0 vs. 3.3.0

> **Issue #1124**
> **状态**: closed
> **创建时间**: 2020-06-03T00:32:43Z
> **更新时间**: 2021-02-16T08:48:00Z
> **关闭时间**: 2021-02-16T08:47:59Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1124

## 描述

Measuring with GpuOwl head version, Linux kernel 5.7.0, Radeon VII,
This is the timing with ROCm 3.3:
```
2020-06-03 10:14:53 XFXsec 96359411 OK 41600000  43.17%;  690 us/it; ETA 0d 10:29; b728b504917920a7 (check 0.48s) 1 errors
2020-06-03 10:14:53 XFXsec 38.07% carryFused     :    252 us/call x 99750 calls
2020-06-03 10:14:53 XFXsec 26.91% tailFusedSquare :    178 us/call x 100000 calls
2020-06-03 10:14:53 XFXsec 17.63% fftMiddleOut   :    116 us/call x 100249 calls
2020-06-03 10:14:53 XFXsec 16.87% fftMiddleIn    :    111 us/call x 100498 calls
```
And this is timing with ROCm 3.5:
```
2020-06-03 10:02:39 XFXsec 96359411 OK 40915600  42.46%;  738 us/it; ETA 0d 11:22; 10ef7daaa7bbd0e8 (check 0.52s)
2020-06-03 10:02:39 XFXsec 37.50% carryFused     :    266 us/call x 115311 calls
2020-06-03 10:02:39 XFXsec 27.63% tailFusedSquare :    196 us/call x 115600 calls
2020-06-03 10:02:39 XFXsec 17.18% fftMiddleIn    :    121 us/call x 116176 calls
2020-06-03 10:02:39 XFXsec 17.16% fftMiddleOut   :    121 us/call x 115888 calls
```
The performance regression is of about 5% overall. Also, it is interesting that the performance hit is distributed "uniformly" over multiple kernels. I.e. it's not an isolated issue hitting only one kernel while leaving other kernels unaffected.

To reproduce: run
./gpuowl -prp 96359411 -time


---

## 评论 (3 条)

### 评论 #1 — valeriob01 (2020-06-03T03:45:55Z)

Personally after reading this I have avoided upgrading ROCm.

---

### 评论 #2 — preda (2020-06-20T08:19:19Z)

Quoting another independent datapoint:
```
2 instances at 5.5M FFT with sclk 4
3.5.0: 1312 µs/it
3.3.0: 1248 µs/it

A huge difference!
```
See also similar observation with different software in https://github.com/RadeonOpenCompute/ROCm/issues/1145#issuecomment-643617442_


---

### 评论 #3 — ROCmSupport (2021-02-16T08:47:59Z)

Thanks @preda for filing this issue and reaching us.
This is the exact duplicate of #1196 and so request you to see app updates there.
#1196 is regressed to comgr and fix will be pushed soon.
I am closing this.
Thank you.

---
