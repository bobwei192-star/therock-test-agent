# Direct firmware load failed

> **Issue #912**
> **状态**: closed
> **创建时间**: 2019-10-17T08:59:04Z
> **更新时间**: 2019-10-22T15:04:31Z
> **关闭时间**: 2019-10-22T15:04:30Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/912

## 描述

Ubuntu 19.10, ROCm 2.9, kernel 5.4.0-rc3, 2x RadeonVII, I see this in dmesg:

[    3.353884] amdgpu 0000:19:00.0: Direct firmware load for amdgpu/vega20_ta.bin failed with error -2
[    3.353886] amdgpu 0000:19:00.0: psp v11.0: Failed to load firmware "amdgpu/vega20_ta.bin"

What does it mean? Should I worry?


---

## 评论 (2 条)

### 评论 #1 — selroc (2019-10-17T10:45:09Z)

The file is missing, but to be found nowhere:
https://github.com/M-Bab/linux-kernel-amdgpu-binaries/issues/82

This page has the firmware files, notice that the "ta" file is missing.
https://people.freedesktop.org/~agd5f/radeon_ucode/vg20/

I would not worry about it unless opencl is not working.


---

### 评论 #2 — kentrussell (2019-10-22T15:04:30Z)

That firmware is for Trusted Applications (hence _ta), which is part of the PSP. But it's not a requirement for basic ROCm functionality, so you don't need to worry. If you want it, you can always use the rock-dkms package, since it's included there. It's not good to try to mix-and-match PSP (TA/ASD/SOS) firmware though, so I can't recommend trying to bring that .bin from 2.9 into your local installation, as that's likely going to cause some major issues.

---
