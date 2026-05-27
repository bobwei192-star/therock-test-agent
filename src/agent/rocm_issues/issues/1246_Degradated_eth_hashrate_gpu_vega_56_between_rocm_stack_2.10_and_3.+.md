# Degradated eth hashrate gpu vega 56 between rocm stack 2.10 and 3.+

> **Issue #1246**
> **状态**: closed
> **创建时间**: 2020-09-25T20:30:22Z
> **更新时间**: 2020-12-15T21:38:04Z
> **关闭时间**: 2020-12-15T21:37:16Z
> **作者**: perestoronin
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1246

## 描述

My Vega56 timing apply no effect with a new drivers rocm 3.+, ethereum 33.9mh/s.

With old rocm 2.10 driver - 45mh/s.

Please direct me to solve this troubles with new amd gpu drivers from rock-kernel or amdgpu-pro.

https://github.com/Eliovp/amdmemorytweak/issues/46

https://github.com/justxi/rocm/issues/172

---

## 评论 (10 条)

### 评论 #1 — baryluk (2020-09-26T20:44:15Z)

Could you link to the source or binaries of the miner that you are using, so we can test it? Any relevant flags / options you use would also be useful so it is easy to reproduce.

Is this OpenCL app or HIP app?


---

### 评论 #2 — perestoronin (2020-09-27T17:16:15Z)

> Could you link to the source or binaries of the miner that you are using, so we can test it? Any relevant flags / options you use would also be useful so it is easy to reproduce.
> 
> Is this OpenCL app or HIP app?

It's OpenCL based.

Intresting, on days ethminer new commit https://github.com/ethereum-mining/ethminer/tree/1536abba52dbc7f0812dec37a448568cd53563d9

I tested it - same results - 36Mh.

But I think thing in core driver in rock-dkms and same thing in linux kernel amgpu drivers, begin from 5.4 and to latest 5.18.12

---

### 评论 #3 — baryluk (2020-09-28T01:08:53Z)

Did you run both tests on the same kernel?

Do you use the dkms amdgpu kernel driver or upstream kernel driver?

Maybe something in kernel changed, like power management, not rocm code.

I managed to make the rocm 3.8 (and kernel 5.7.6, with upstream amdgpu driver) work (`LD_LIBRARY_PATH=/opt/rocm-3.8.0/lib:/opt/rocm-3.8.0/opencl/lib ./ethminer/ethminer --opengl --benchmark 10947900`), on my AMD Fury X (FIJI, GFX8, 4GB VRAM), and I am getting 30.93 Mh.

I am not sure where to get rocm 2.10 to test it with older rocm.


---

### 评论 #4 — perestoronin (2020-09-28T19:04:26Z)

> Did you run both tests on the same kernel?

Yes. I have two same stands, but for rock-dkms 2.10 needs kernel 5.4 and early.
 
> Do you use the dkms amdgpu kernel driver or upstream kernel driver?

I tried amdgpu drivers as module from rock-dkms, and from kernel upstream, and from amdgpu-pro distribution, troubles was same, this dark for me part code I think in kernel or driver (also in rock-dkms and ROCK-Kernel-Driver too).

> Maybe something in kernel changed, like power management, not rocm code.

Troubles in https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver.

> I managed to make the rocm 3.8 (and kernel 5.7.6, with upstream amdgpu driver) work (`LD_LIBRARY_PATH=/opt/rocm-3.8.0/lib:/opt/rocm-3.8.0/opencl/lib ./ethminer/ethminer --opengl --benchmark 10947900`), on my AMD Fury X (FIJI, GFX8, 4GB VRAM), and I am getting 30.93 Mh.

Excellent result for Fury X !

> I am not sure where to get rocm 2.10 to test it with older rocm.

From applied archives https://github.com/justxi/rocm/issues/172#issuecomment-699557619


---

### 评论 #5 — baryluk (2020-09-28T21:01:25Z)

I see. I need to build old version from source. Well, I can't even build 3.8.0 from source at the moment, because I have various cmake issues.


---

### 评论 #6 — preda (2020-09-29T13:33:02Z)

@baryluk previous binary packages:
https://repo.radeon.com/rocm/apt/
https://repo.radeon.com/rocm/apt/2.10.0/

---

### 评论 #7 — perestoronin (2020-10-24T08:19:31Z)

I checked my Vega 56 on hiveOS from USB-flash drive and find some differences:
on hiveOS I have 50mx+ and 
```
# cat /sys/class/drm/card0/device/pp_sclk_od
0
# cat /sys/class/drm/card0/device/pp_mclk_od
0
and on kernel 5.8.15 I have 36mx-:
# cat /sys/class/drm/card0/device/pp_sclk_od
-36
# cat /sys/class/drm/card0/device/pp_mclk_od
18
```

---

### 评论 #8 — rkothako (2020-11-18T08:48:39Z)

Hi @perestoronin 
Can you please confirm whether the issue is still observed with the latest ROCm like ROCm 3.9?
Please validate and confirm so that I can take a look.
Thank you.

---

### 评论 #9 — perestoronin (2020-11-26T17:50:46Z)

> Hi @perestoronin
> Can you please confirm whether the issue is still observed with the latest ROCm like ROCm 3.9?
> Please validate and confirm so that I can take a look.
> Thank you.

Hi, @rkothako 

Issue exists with kernel newer than 5.4, for example 5.8 and 5.9 on any version rocm newer than 2.10.

On linux kernel 5.4 this issue not reproduced at all.

In downgrade on all my stands kernel version to 5.4 and hashrate obtain over 44Mx on ethminer and 50Mx+ on trm.


---

### 评论 #10 — perestoronin (2020-12-15T21:37:16Z)

To solve this issue needs adopt rocm to new kernel.

Solutions of this case not exists.

I rollback to kernel 5.4 to obtain max performance on GPU.


---
