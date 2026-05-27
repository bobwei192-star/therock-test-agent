# Installing rocm-1.6 makes DVI image blocky (RX 480, ubuntu 16.04)

> **Issue #144**
> **状态**: closed
> **创建时间**: 2017-07-03T11:15:03Z
> **更新时间**: 2017-07-26T13:48:46Z
> **关闭时间**: 2017-07-26T13:48:46Z
> **作者**: gsedej
> **标签**: Bug_Functional_Issue
> **URL**: https://github.com/ROCm/ROCm/issues/144

## 标签

- **Bug_Functional_Issue** (颜色: #d93f0b)

## 描述

Hi. I have dual monitor configuration - old Symcaster 2443 (vga+dvi) and new aoc I2475PXQU (DP + others). If i connect any of those via DVI-DVI cable, I get "blocky" or "pixalized" image on that monitor (font is hard to read). The non DVI monitor is ok. But if I connect via HDMI-DVI cable (hdmi on card) it is ok (on both "HDMI->DVI" and "DP-DP").

This is visible already in booting process.

In the ROCm-1.5 it was working (still kernel 4.9)

---

## 评论 (5 条)

### 评论 #1 — gstoner (2017-07-03T15:06:55Z)

This is going to be AMDGPU driver related,  we will talk to that team about it.   We mostly operate ROCm as headless driver and SSH into the box, since the driver is really focused on the needs of Servers with things like Large Bar for P2P and P2P RDMA and many other features.   

---

### 评论 #2 — gsedej (2017-07-03T18:03:01Z)

Thanks for reply. 

I wanted just to note, if someone else has same problem. 

It might be something with amdgpu kernel driver, but this is only present in rocm-1.6  with kernel `4.9.0-kfd-compute-rocm-rel-1.6-77`. The rocm-1.5  also included kernel `4.9-kfd-something` but the output on DVI was fine. Also i did use "regular" ubuntu kernels - newer versions (4.10, 4.11 4.12) as well as older (4.8) and the issue was not present there.

---

### 评论 #3 — ptsant (2017-07-22T11:39:42Z)

I want to add that I am having the same problem. Display is perfect via DP or HDMI, blocky via DVI. I am running a trimonitor setup.

It used to work perfectly well with AMDGPU-PRO drivers, all tested versions (16, 17) but does not work well with ROCm.

This is the relevant section from Xorg log. The appropriate resolution (1280x1024) seems to be detected and selected, but the monitor reports 640x1024 (64KHz / 60Hz), so the horizontal res is halved:
```
32.343] (II) AMDGPU(0): EDID for output DVI-D-0
[    32.343] (II) AMDGPU(0): Manufacturer: ENC  Model: 1833  Serial#: 16843009
[    32.343] (II) AMDGPU(0): Year: 2007  Week: 7
[    32.343] (II) AMDGPU(0): EDID Version: 1.3
[    32.343] (II) AMDGPU(0): Digital Display Input
[    32.343] (II) AMDGPU(0): Max Image Size [cm]: horiz.: 38  vert.: 30
[    32.343] (II) AMDGPU(0): Gamma: 2.20
[    32.343] (II) AMDGPU(0): DPMS capabilities: StandBy Suspend Off
[    32.343] (II) AMDGPU(0): Supported color encodings: RGB 4:4:4 YCrCb 4:4:4 
[    32.343] (II) AMDGPU(0): First detailed timing is preferred mode
[    32.343] (II) AMDGPU(0): redX: 0.640 redY: 0.330   greenX: 0.290 greenY: 0.605
[    32.343] (II) AMDGPU(0): blueX: 0.145 blueY: 0.075   whiteX: 0.313 whiteY: 0.329
[    32.343] (II) AMDGPU(0): Supported established timings:
[    32.343] (II) AMDGPU(0): 720x400@70Hz
[    32.343] (II) AMDGPU(0): 640x480@60Hz
[    32.343] (II) AMDGPU(0): 800x600@60Hz
[    32.343] (II) AMDGPU(0): 1024x768@60Hz
[    32.343] (II) AMDGPU(0): Manufacturer's mask: 0
[    32.343] (II) AMDGPU(0): Supported standard timings:
[    32.343] (II) AMDGPU(0): #0: hsize: 1280  vsize 1024  refresh: 60  vid: 32897
[    32.343] (II) AMDGPU(0): Supported detailed timing:
[    32.343] (II) AMDGPU(0): clock: 108.0 MHz   Image Size:  376 x 301 mm
[    32.343] (II) AMDGPU(0): h_active: 1280  h_sync: 1328  h_sync_end 1440 h_blank_end 1688 h_border: 0
[    32.343] (II) AMDGPU(0): v_active: 1024  v_sync: 1025  v_sync_end 1028 v_blanking: 1066 v_border: 0
[    32.343] (II) AMDGPU(0): Serial No: 70048027
[    32.343] (II) AMDGPU(0): Ranges: V min: 59 V max: 61 Hz, H min: 31 H max: 64 kHz, PixClock max 115 MHz
[    32.343] (II) AMDGPU(0): Monitor name: S1931
[    32.343] (II) AMDGPU(0): EDID (in hex):
[    32.343] (II) AMDGPU(0):    00ffffffffffff0015c3331801010101
[    32.343] (II) AMDGPU(0):    0711010380261e78eae415a3544a9b25
[    32.343] (II) AMDGPU(0):    135054a1080081800101010101010101
[    32.343] (II) AMDGPU(0):    010101010101302a009851002a403070
[    32.343] (II) AMDGPU(0):    1300782d1100001e000000ff00373030
[    32.343] (II) AMDGPU(0):    34383032370a20202020000000fd003b
[    32.343] (II) AMDGPU(0):    3d1f400b000a202020202020000000fc
[    32.343] (II) AMDGPU(0):    0053313933310a20202020202020002b
[    32.343] (II) AMDGPU(0): Printing probed modes for output DVI-D-0
[    32.343] (II) AMDGPU(0): Modeline "1280x1024"x60.0  108.00  1280 1328 1440 1688  1024 1025 1028 1066 +hsync +vsync (64.0 kHz eP)
[    32.343] (II) AMDGPU(0): Modeline "1280x800"x60.0  108.00  1280 1328 1440 1688  800 1025 1028 1066 +hsync +vsync (64.0 kHz e)
[    32.343] (II) AMDGPU(0): Modeline "1280x720"x60.0  108.00  1280 1328 1440 1688  720 1025 1028 1066 +hsync +vsync (64.0 kHz e)
[    32.343] (II) AMDGPU(0): Modeline "1024x768"x60.0   65.00  1024 1048 1184 1344  768 771 777 806 -hsync -vsync (48.4 kHz e)
[    32.343] (II) AMDGPU(0): Modeline "800x600"x60.3   40.00  800 840 968 1056  600 601 605 628 +hsync +vsync (37.9 kHz e)
[    32.343] (II) AMDGPU(0): Modeline "640x480"x59.9   25.18  640 656 752 800  480 490 492 525 -hsync -vsync (31.5 kHz e)
[    32.343] (II) AMDGPU(0): Modeline "720x400"x70.1   28.32  720 738 846 900  400 412 414 449 -hsync +vsync (31.5 kHz e)
[    32.343] (II) AMDGPU(0): Output DisplayPort-0 connected
[    32.343] (II) AMDGPU(0): Output DisplayPort-1 disconnected
[    32.343] (II) AMDGPU(0): Output HDMI-A-0 disconnected
[    32.343] (II) AMDGPU(0): Output HDMI-A-1 disconnected
[    32.343] (II) AMDGPU(0): Output DVI-D-0 connected
[    32.343] (II) AMDGPU(0): Using spanning desktop for initial modes
[    32.343] (II) AMDGPU(0): Output DisplayPort-0 using initial mode 2560x1440 +0+0
[    32.343] (II) AMDGPU(0): Output DVI-D-0 using initial mode 1280x1024 +2560+0
[    32.343] (II) AMDGPU(0): Using default gamma of (1.0, 1.0, 1.0) unless otherwise stated.
[    32.343] (II) AMDGPU(0): mem size init: gart size :fb45e9000 vram size: s:1f70db000 visible:70db000
[    32.343] (==) AMDGPU(0): DPI set to (96, 96)
```

Base system is Mint (Ubuntu/Debian derivative), equivalent to 16.04. ROCm 1.6.77. 
Hardware is RX480/Ryzen 1700X: [https://valid.x86.fr/fwc5tn](CPU-Z link)

---

### 评论 #4 — gstoner (2017-07-22T13:11:17Z)

We going to move 1.6.1 to new Linux kernel and new base AMDGPU driver 4.11 based,   we were chasing down way too many problems in the base Linux driver and AMDGPU driver which the Linux team layer update KFD and TTM.  Which we run the thunk and ROCr on for the language runtimes.    Working on bringing it out early next week. 

---

### 评论 #5 — ptsant (2017-07-26T09:43:50Z)

I no longer have this issue with the new release. Thanks for migrating to the 4.11 kernel, it is supposedly better for Ryzen.

---
