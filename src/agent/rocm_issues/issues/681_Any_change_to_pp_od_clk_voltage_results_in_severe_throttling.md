# Any change to pp_od_clk_voltage results in severe throttling

> **Issue #681**
> **状态**: closed
> **创建时间**: 2019-01-19T20:06:58Z
> **更新时间**: 2023-12-12T22:35:01Z
> **关闭时间**: 2023-12-12T22:35:01Z
> **作者**: w23
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/681

## 描述

Kernel: 5.0-rc2
GPU: Vega 64 (MSI 8G OC one)

Even slight change to voltage (e.g. just +/-1mV is enough) for any power level results in severe throttling.

E.g. when running Unigine Superposition w/ default pp_table I get ~40fps while maintaining sclk about 1400 and mclk=945.

If I run this, however:
```
DEV=/sys/class/drm/card0/device
echo "manual" > $DEV/power_dpm_force_performance_level
echo "s 0 852 800" > $DEV/pp_od_clk_voltage #800 -- commented are the default values
echo "s 1 991 900" > $DEV/pp_od_clk_voltage #900
echo "s 2 1084 950" > $DEV/pp_od_clk_voltage #950
echo "s 3 1138 1000" > $DEV/pp_od_clk_voltage #1000
echo "s 4 1200 1050" > $DEV/pp_od_clk_voltage #1050
echo "s 5 1401 1100" > $DEV/pp_od_clk_voltage #1100
echo "s 6 1576 1150" > $DEV/pp_od_clk_voltage #1150
echo "s 7 1663 1199" > $DEV/pp_od_clk_voltage #1200 <---- note the -1mV difference
echo "c" > $DEV/pp_od_clk_voltage
echo "m 0 167 800" > $DEV/pp_od_clk_voltage #800
echo "m 1 500 800" > $DEV/pp_od_clk_voltage #800
echo "m 2 800 950" > $DEV/pp_od_clk_voltage #950
echo "m 3 945 1100" > $DEV/pp_od_clk_voltage #1100
echo "c" > $DEV/pp_od_clk_voltage
```
sclk immediately drops to ~1300. After a couple of seconds it drops further down below ~1200, fps drops to about 20, and mclk starts to randomly oscillate between 200 and 945 every few dozen ms. Power consumption and GPU load stay the same.

If I change the 1199 back to 1200, then the performance and frequencies go back to normal.

The same behavior is observed with changing any other voltage (for memory too) by any other amount.

The behavior is the same if the voltage is changed using the rock_smi.py util instead of the custom command above.

Other notes:
- kernel parameters: `amd_iommu=on vfio-pci.ids=10de:1005,10de:0e1a,1912:0014,1106:3483 iommu=pt vfio-pci.disable_vga=1 hpet=disable nohpet amdgpu.ppfeaturemask=0xfffd7fff amdgpu.gpu_recovery=1 pcie_aspm=off zfs_arc_max=4294967296`
- at idle sclk is at level 3 (1138MHz), mclk stays at max, power draw is ~40W. (the same config on windows stays at min levels with just 20W)
- I am unable to properly dump the video bios of this card on Linux. It is truncated to 60928 bytes, and the contents seem to be slightly different by a few bytes here and there from the dump extracted on Windows. (there's a dozen of "No more image in the PCI ROM" lines in dmesg when the BIOS is being dumped)
- I'm doing this in a (still futile) attempt to mitigate "ring gfx timeout" issue that this GPU has been randomly experiencing since forever. It is hardly related to the issue being reported here, but for context: the timeout happens at random (it can be stable for weeks, and then hang several times in one evening). It often happens either when using OBS for streaming, or when running some heavy raytracing shader e.g. from shadertoy, or when doing some opencl load, or even when GPU is completely idle, but CPU is busy (Threadripper 1950X compiling a huge C++ codebase in 32 threads). Sometimes it timeouts right away (10sec - 20min of load), but sometimes it can survive for many consecutive hours. The same hw doesn't seem to be unstable on Windows, at least while doing limited stress tests, so it doesn't look like a hardware issue.
- amdgpu recovery doesn't work and a hard reset is needed (soft reset e.g. by ssh hangs).

---

## 评论 (4 条)

### 评论 #1 — w23 (2019-01-21T04:09:22Z)

Tried downgrading to kernel 4.20.0, and it has the same issue: any however insignificant change to any of the sclk/mclk voltages result in severe throttling. Small changes to frequencies have no visible effect.

---

### 评论 #2 — mistarz (2019-04-20T21:56:48Z)

I concur with above my reference Vega 64 with Morpheus II on 5.0.8 & 4.20.6. The only way to improve performance is to modify HBM clock

`echo "m 3 1100 1000" > /sys/class/drm/card0/device/pp_od_clk_voltage`

without confirming by sending

`echo "c" > /sys/class/drm/card0/device/pp_od_clk_voltage`

core GPU clock seems to boost only with increased power limit. touching anything else does not seem to matter and driver sets high voltages leading to thermal throttling. Typical Vega undervolt/overclock does not work.



---

### 评论 #3 — tasso (2023-12-12T21:54:49Z)

Is this still an issue?  if not, can we please close it?  Thanks!

---

### 评论 #4 — w23 (2023-12-12T22:35:01Z)

This issue is no longer relevant for me, I'm not using that Vega 64 card anymore.

---
