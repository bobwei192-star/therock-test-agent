# Inconsistent display output with 4.9.0-kfd-compute

> **Issue #111**
> **状态**: closed
> **创建时间**: 2017-05-03T05:05:53Z
> **更新时间**: 2017-10-17T14:03:55Z
> **关闭时间**: 2017-10-17T14:03:02Z
> **作者**: kyflores
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/111

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

Hi,

I installed the ROCm 1.5 release today and am experiencing some display issues. Sometimes, the display will come up without issue, other times it will remain black. A few times it came up with only low resolutions available, and I observed the following output while it was starting:

```
[    3.453722] Raw EDID:
[    3.453724]  	00 ff ff ff ff ff ff 00 ff ff ff ff ff ff ff ff
[    3.453726]  	56 50 9e 26 0d 50 54 21 0b 00 d1 c0 d1 fc 81 c0
[    3.453728]  	0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d 0d
[    3.453730]  	01 01 01 01 01 01 37 8b 80 18 71 38 2d 40 58 2c
[    3.453732]  	45 00 dd 0c 11 00 00 1e 00 00 00 fc 00 4e 58 2d
[    3.453734]  	56 55 45 32 34 0a 20 20 20 20 00 00 00 fd 00 1e
[    3.453735]  	90 a2 a2 24 01 00 20 20 20 20 20 20 00 00 00 ff
[    3.453737]  	00 4e 49 58 32 34 31 35 0a 20 20 20 20 20 01 54
[    3.453740] amdgpu 0000:03:00.0: DP-1: EDID invalid.
```

There are many nearly identical messages. Swapping DP outputs or to HDMI didn't change anything.
My system configuration is Intel 5820k on an Asrock Extreme 4 x99, with an RX 480 Reference model w/ Ubuntu 16.04, and monitor is Nixeus VUE24. Please tell me if I can supply any other messages/output that can help. I'm not sure this is exactly a ROCm problem, but I don't see this happen when booting Ubuntu's stock kernel or previously ROCm 1.4's kernel. Thanks!

---

## 评论 (4 条)

### 评论 #1 — gstoner (2017-07-02T17:46:25Z)

Can you try ROCm 1.6 it released on Thursday here are new install instructions https://rocm.github.io/ROCmInstall.html 

---

### 评论 #2 — kyflores (2017-07-05T11:02:00Z)

Hi,

Thanks for your reply - when I get back to my desktop in about a week, I will do as you suggested and report back. I understand that headless operation is sort of a priority over display stuff, so I appreciate you looking at this anyway.

---

### 评论 #3 — kyflores (2017-07-23T00:01:26Z)

I tried this on the same machine and the problem persists with about the same message. However, although it occurs with my Nixeus panel no matter what port is used (including DVI->HDMI), using a much older NEC monitor over the RX 480's HDMI port never causes a problem. I'd be happy to provide any other outputs if it would help.

---

### 评论 #4 — gstoner (2017-10-17T14:03:55Z)

This is the issue in the base Linux AMDGPU driver,  not ROCm stack, they are addressing this with Linux kernel 4.15 and 4.16 

---
