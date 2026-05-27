# GPU stuck on lowest power state with ppfeaturemask

> **Issue #504**
> **状态**: closed
> **创建时间**: 2018-08-19T14:39:36Z
> **更新时间**: 2018-09-19T09:18:36Z
> **关闭时间**: 2018-09-19T00:59:05Z
> **作者**: preda
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/504

## 描述

Ubuntu 18.04 4.15.0-32, ROCm 1.8.2, GPU FuryX, CPU AMD Ryzen 1700X.
The GPU was working fine with amdgpu-pro 18.20.
I installed ROCm 1.8.2, and clinfo works correctly.
I tried to run gpuowl https://github.com/preda/gpuowl ,
it runs correctly but very slowly (about 4 times slower than normal).

I see with rocm-smi that the GPU is stuck in the lowest power state, and it draws only 50W (while normally under load draws 220W).

I tried to manually set the power state higher with rocm-smi --setsclk 7, but it has no effect (or the state is immediately reset back to 0).

Seems a similar situation with what's reported here:
https://github.com/RadeonOpenCompute/ROCm/issues/491

Attached output of lshw
[lshw.txt](https://github.com/RadeonOpenCompute/ROCm/files/2300386/lshw.txt)



---

## 评论 (5 条)

### 评论 #1 — valeriob01 (2018-08-21T11:00:54Z)

@preda I have similar problem with amdgpu-pro. Sometimes a gpu starts correctly and after a while it gets stuck, temperature drops, and, when I stop the program, an error occurs: amdgpu_timedout. I have investigated my hardware bios settings but could not find anything related.

---

### 评论 #2 — preda (2018-08-25T05:23:42Z)

I found a workaround:
in /sys/class/drm/card0/device/
echo "s 0 1050 1210" > pp_od_clk_voltage
echo c > pp_od_clk_voltage

This sets the "0" power state higher, so that the GPU starts moving.


---

### 评论 #3 — preda (2018-09-18T23:41:09Z)

I think this is caused by setting
GRUB_CMDLINE_LINUX_DEFAULT="amdgpu.ppfeaturemask=0xffffffff"
In /etc/default/grub

I think that being stuck on lowest power in that case is still a bug, but at least now I have some understanding of the reason and a workaround.


---

### 评论 #4 — jlgreathouse (2018-09-19T00:59:05Z)

To start: if you're worried about frequencies and power states, it's probably worth reporting along with your initial report that you're running in a non-standard mode. How were any of us to know that you were setting a non-default ppfeaturemask? :)

You're turning on OverDrive in the powerplay featuremask. This features allows you to adjust the clocks and voltages associated with each of the DPM (voltage/frequency) states on the GPU. (Note that this is slightly different than the OverDrive features in `rocm-smi`, which allows you to add up to 20% more frequency to the highest DPM state for "high frequency overclocking".) This is set by bit 14 in the feature mask, and it [is normally off by default](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/amdgpu/amdgpu_drv.c#L128).

This feature enables, for instance, the "pp_od_clk_voltage" sysfs entry. You can find documentation [in the amdgpu driver code](https://github.com/RadeonOpenCompute/ROCK-Kernel-Driver/blob/roc-1.9.x/drivers/gpu/drm/amd/amdgpu/amdgpu_pm.c#L468) for what that sysfs entry means.

By default, the DPM table is filled in the VBIOS. So when you set SCLK to level 7 using rocm-smi, you would normally get the high-frequency DPM7 SCLK, which is high voltage and frequency.

If you are modifying your GPU's DPM states incorrectly, you may be causing the problems you are seeing. For instance, if you set all of your DPM states to a low frequency by accident, then it won't matter what SCLK state you choose using `rocm-smi` -- you will run at that low frequency.

Also note that you may not always run at the high DPM states that you request with `rocm-smi`. If, for example, your GPU is using too much power, the hardware frequency manager may force you into a lower DPM state in order to avoid damaging the card.

In any case, I am unable to reproduce this issue on ROCm 1.9, even with the ppfeaturemask enabling overdrive. Tested with gpuowl and other applications on a Fiji GPU -- frequencies hit where they are expected, as does performance.  I'm going to close this for now -- if you believe you have a set of steps that will reproduce this issue generally on ROCm 1.9, please post them. :)

---

### 评论 #5 — preda (2018-09-19T09:18:36Z)

The only change I did was enable the ppfeaturemask, but I didn't write or change anything on pp_od_clk_voltage. In that situation I would still expect the GPU to ramp up the clock on usage, as usual. So it still looks like something is not right, but I'm OK with closing this for now. It's indeed strange that you couldn't repro, thanks for looking into it by the way.

---
