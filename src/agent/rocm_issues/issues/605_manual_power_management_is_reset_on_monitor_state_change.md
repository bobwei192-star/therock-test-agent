# manual power management is reset on monitor state change.

> **Issue #605**
> **状态**: closed
> **创建时间**: 2018-11-07T08:02:52Z
> **更新时间**: 2019-03-17T17:21:27Z
> **关闭时间**: 2019-03-12T12:13:45Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/605

## 描述

ROCm 1.9.1 OpenCL, Ubuntu 18.10, two Vega 64 GPUs reference air.

I have two GPUs that I use mainly for compute (OpenCL), but one of them also drives the monitor.

I manually set the power state on the GPUs with: rocm-smi --setsclk 5
(which brings the power use per GPU around 150W and prevents thermal throttling).

But, on some monitor actions such as:
- monitor enters "power save" mode (triggered with "Lock screen", keyboard Super+L)
- monitor power ON (following manual monitor power OFF using the monitor switch)
- monitor DP cable reconnect to the GPU (following manual DP cable unplug from GPU)

the power state is reset on the GPU that is connected to the monitor. It seems it is set to state "6" (instead of the state "5" that I set manually), which uses around 200W of power, and overheats + thermal throttling the GPU.

In practice, after each such monitor action, I have to re-issue the rocm-smi --setsclk 5 to bring the GPU back to the desired state.

This is a long-standing issue for me, not limited to ROCm 1.9.1 or Ubuntu 18.10 (I've seen it with other version previously). It happens every time, thus should be easy to reproduce.


---

## 评论 (3 条)

### 评论 #1 — preda (2019-01-03T23:42:19Z)

Could somebody please help with this issue, as it is not only annoying but even potentially dangerous to the GPU. Let me explain.

ROCm 2.0, Ubuntu 18.10, Linux kernel 4.20, OpenCL, 2x Vega64. ROCm is installed without rock-dkms (i.e. using the amdgpu coming with the 4.20 kernel).

I manually set clock and fan on the GPUs like this:
~/ROC-smi/rocm-smi --setsclk 5 --setfan 110

On the GPU that is driving the display, every time that the monitor is turned on or the video cable (DP) re-connected to the GPU, the GPU clock (sclk) is reset to a very high state (state 6 or 7). I have to go and run the setsclk again after each monitor-on in order to turn the clock back to the desired state 5.

The "jumping up" of the sclk on display reconnect is dangerous because it does not affect the fanspeed on the GPU (which I set manually based on the sclk==5). This produces overheating of the GPU, to 84C, at which point the GPU self-protects and throttles thermally.

Please, could this issue be looked into a bit, and routed to the appropriate team (maybe it's not a ROCm issue at all, but rather a base amdgpu issue?)

This issue, in exactly this form, has been present for about 2years now.

---

### 评论 #2 — kentrussell (2019-03-12T12:13:45Z)

This would definitely be an amdgpu issue, since the issue seems to be related to the Power management not being retained when changing the connectors. Obviously the manual setting of the fan is part of it, but it's still a kernel bug that the sclk is changing when the monitor is connected/disconnected. You should try the upstream kernel first (the SMI will still work with upstream's kernel) and if it persists, raise a bug report with the kernel team (https://bugs.freedesktop.org) and get them to take a look. If it's not present in the upstream kernel, try the 2.2 release. If it's present in 2.2 but not upstream, then we obviously missed a patch

---

### 评论 #3 — preda (2019-03-17T17:21:27Z)

Thanks @kentrussell , this seems to be the corresponding amdgpu bug:
https://bugs.freedesktop.org/show_bug.cgi?id=107141

I added info there, I can still repro on Linux kernel 5.0 with ROCm 2.2.

---
