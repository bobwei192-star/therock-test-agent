# Vega 64 downclock memory

> **Issue #453**
> **状态**: closed
> **创建时间**: 2018-07-07T17:46:24Z
> **更新时间**: 2019-10-22T15:41:09Z
> **关闭时间**: 2019-10-22T15:41:09Z
> **作者**: evgeniyosipov
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/453

## 描述

Hello,
I can't change memory clock - rocm 1.8.1 kernel 4.13.0-45 x64
Tried use /opt/rocm/bin/rocm-smi --setmclk 0 (also1 and 2) - same 945.

---

## 评论 (6 条)

### 评论 #1 — chromakey-io (2018-07-09T15:14:41Z)

it seems like with my RX570 you can't alter the memory clocks on the fly either.  Both overdrive and perf-levels don't let you change the settings.

What does seem to work if your goal is to OC is the overdrive functionality when configured with the AMDCOVC app.  Many of the settings do nothing, but setting amdcovc memod=5 (5% ... you can do up to 20%) works and reports in rocm-smi -a as it should.

Unfortunately it doesn't seem like the rocm-smi OD settings have any effect on memory clocks :(

https://github.com/matszpk/amdcovc

I haven't tried super hard to get the perflevels working in rocm-smi, but I think there are some kernel params that you might want to try toggling.

amdgpu.dpm=0  (this disables the Dynamic Power Management ... which might be usurping control and preventing you from overriding the memory clock perf levels)

amdgpu.ppfeaturemask=1 (pretty sure this will enable manual control over all of the perf level, fan, etc functionality ... it's meant to be a mask like 0xFFFFFFFF with each bit controlling a feature ... though it seems like setting it to 1 or 0 works just as well)

In ubuntu you can add those to the kernel params in /etc/default/grub ... then update your boot grub by calling "sudo update-grub".

---

### 评论 #2 — kentrussell (2019-03-12T12:21:21Z)

Sorry for the incredibly late reply, are you still seeing the same issue in 2.2? We have some patches in 2.2 to address issues where DPM is disabled and not reported correctly (so it doesn't change the mclk, even though it implies that it can), so it should work now. If it doesn't please attach the dmesg and I'll take a look.

---

### 评论 #3 — Moading (2019-03-12T12:57:22Z)

Hi, I was wondering if 2.2 is available yet. If there are some beta packages, I would be happy to try them. The main reason for me is issue #701

---

### 评论 #4 — kentrussell (2019-03-12T14:06:05Z)

The 2.2 source code has been pushed, I think that the apt servers will be updated in the next day or two. You can definitely download the kernel code and build it yourself if need be, but it should be updated soon.

---

### 评论 #5 — jlgreathouse (2019-05-03T16:48:40Z)

2.2 has been out for a while. @evgeniyosipov @kevin are you still observing this issue?

---

### 评论 #6 — kentrussell (2019-10-22T15:41:09Z)

Please re-open this if the issue persists. I haven't seen it locally though

---
