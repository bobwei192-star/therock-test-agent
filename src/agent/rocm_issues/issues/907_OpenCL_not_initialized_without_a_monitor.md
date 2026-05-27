# OpenCL not initialized without a monitor

> **Issue #907**
> **状态**: closed
> **创建时间**: 2019-10-13T02:03:54Z
> **更新时间**: 2021-05-09T19:48:50Z
> **关闭时间**: 2021-05-09T19:48:50Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/907

## 描述

Using latest ROCm (2.9), Ubuntu 19.10, Linux kernel 5.4.0-rc2, GPUs 2x Radeon VII.
When I boot without any monitor connected:
- the ROCm stack is OK, GPUs detected correctly, rocm-smi works fine, sees both GPUs
- but OpenCL is not initialized, clinfo reports 0 devices.

As soon as a monitor is attached, OpenCL start working correctly, clinfo correctly reports all the devices (without reboot). This are the additional entries that appear in dmesg on monitor being connected:
[   91.028230] [drm] fb mappable at 0xC0785000
[   91.028231] [drm] vram apper at 0xC0000000
[   91.028231] [drm] size 16384000
[   91.028231] [drm] fb depth is 24
[   91.028232] [drm]    pitch is 10240
[   91.028321] fbcon: amdgpudrmfb (fb0) is primary device
[   91.073250] Console: switching to colour frame buffer device 160x50
[   91.087170] amdgpu 0000:06:00.0: fb0: amdgpudrmfb frame buffer device

After this, clinfo reports 2 devices (correct).

Expected behavior: OpenCL does not require a monitor being connected to initialize (similarly to the rest of the ROCm stack, that works fine without a monitor).


---

## 评论 (8 条)

### 评论 #1 — valeriob01 (2019-10-13T03:13:04Z)

It is different behavior from amdgpu-pro, where opencl works without any monitor. Perhaps they can be aligned in features/performance?


---

### 评论 #2 — Djip007 (2019-10-14T21:14:56Z)

what report:
```
cat /sys/bus/pci/drivers/amdgpu/*/power/control
```


---

### 评论 #3 — preda (2019-10-16T12:17:31Z)

now when OpenCL is working (i.e. after the attach-monitor):
cat /sys/bus/pci/drivers/amdgpu/*/power/control
on
on

I'll report the other situation (before monitor) when I restart that computer.

---

### 评论 #4 — preda (2019-11-07T10:56:42Z)

The bug is still present on kernel 5.4.0-050400rc6, and I have some new info:

1. after boot, if I ssh into the machine, I get "Number of devices 0" in clinfo.
2. I connect a monitor, login in the GUI (the default for Ubuntu 19.10), clinfo now reports 2 devices.
3. I logout on the GUI,
4. ssh clinfo now reports 0 devices
5. login on the GUI again, and *remain logged-in* ("lock screen")
6. ssh clinfo now reports 2 devices correctly


---

### 评论 #5 — pettai (2020-01-10T14:07:20Z)

Just curious;
You run Ubuntu 19.10 + ROCm 2.9 (+working graphics then the monitor is attached).
Did you manage to install rock-dkms/rocm-dkms without this issue ( Ref. https://github.com/RadeonOpenCompute/ROCm/issues/969 ) ?

---

### 评论 #6 — pettai (2020-01-10T14:21:45Z)

Did you try run clinfo as root vs a regular user (added to the video group)?
clinfo also reports 0 devices for me, but it reports all radean vega cards then I run clinfo as root.
I can also run an opencl application if I run it as root.

---

### 评论 #7 — BloodyIron (2020-02-18T16:48:39Z)

I'm not having any luck getting ROCM working with 19.10. I've tried 2.9, 2.10 and 3.0. I had 2.9 working before, unsure how I was able to get that working now that I think about it. Was really hoping ROCM 3.0 would work for me, since it supposedly works with Linux 5.3 that's now in 18.04.4.

:(

I'd be open to any keen ideas!

---

### 评论 #8 — preda (2021-05-09T19:48:50Z)

Closing as old, didn't check recently.

---
