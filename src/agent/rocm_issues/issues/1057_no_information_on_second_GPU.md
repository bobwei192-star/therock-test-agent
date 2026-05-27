# no information on second GPU

> **Issue #1057**
> **状态**: closed
> **创建时间**: 2020-03-23T21:38:10Z
> **更新时间**: 2021-04-05T10:18:00Z
> **关闭时间**: 2021-04-05T10:17:59Z
> **作者**: siorenai
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1057

## 描述

Why do these warnings appear and how can I fix it? Thank you.

> WARNING: GPU[1] : Unable to read /sys/class/hwmon/hwmon4/temp1_input
> WARNING: GPU[1] : Unable to read /sys/class/hwmon/hwmon4/power1_average
> WARNING: GPU[1] : Unable to read /sys/class/hwmon/hwmon4/pwm1
> 
> GPU  Temp   AvgPwr  SCLK    MCLK    Fan    Perf  PwrCap  VRAM%  GPU%
> 1            N/A    N/A     N/A     N/A         None%   off   25.0W     N/A        0%

---

## 评论 (1 条)

### 评论 #1 — ROCmSupport (2021-04-05T10:17:59Z)

Hi @siorenai 
Thanks for reaching out.
Until there is no hardware issue, this issue is no more observed with ROCm 4.1, I just tried with 4.1 locally and able to detect 2nd GPU also.
Feel free to open a new issue, if any, for quick resolution.
Thank you.

---
