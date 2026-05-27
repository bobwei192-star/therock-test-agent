# Vega RX 64 Liquid fails to post

> **Issue #198**
> **状态**: closed
> **创建时间**: 2017-09-05T21:48:29Z
> **更新时间**: 2018-04-16T21:27:41Z
> **关闭时间**: 2017-09-24T20:35:24Z
> **作者**: AirSquirrels
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/198

## 描述

Using ROCm, amdgpu: logs gpu post error! And indicates a loop of more than 5 seconds in atombios. No problem with RX64 Air or FE Vegas.

Is this a firmware issue? Or a DOA card? This card shows rev c0, the others all show c1...

---

## 评论 (5 条)

### 评论 #1 — jedwards-AMD (2017-09-05T21:55:27Z)

Please attach dmesg output.

---

### 评论 #2 — AirSquirrels (2017-09-05T21:55:28Z)

[code][   12.000423] amdgpu 0000:0e:00.0: enabling device (0100 -> 0103)
[   12.000729] [drm] initializing kernel modesetting (VEGA10 0x1002:0x687F 0x1002:0x6B76 0xC0).
[   12.000958] [drm] register mmio base: 0xFB400000
[   12.001185] [drm] register mmio size: 524288
[   12.001430] [drm] probing gen 2 caps for device 1022:1471 = 700d03/e
[   12.001670] [drm] probing mlw for device 1022:1471 = 700d03
[   12.001915] [drm] UVD is enabled in VM mode
[   12.002161] [drm] UVD ENC is enabled in VM mode
[   12.002400] [drm] VCE enabled in VM mode
[   13.268730] ATOM BIOS: 113-D0500500-102
[   13.269126] [drm] GPU posting now...
[   18.270925] [drm:atom_op_jump [amdgpu]] *ERROR* atombios stuck in loop for more than 5secs aborting
[   18.271427] [drm:amdgpu_atom_execute_table_locked [amdgpu]] *ERROR* atombios stuck executing A900 (len 812, WS 8, PS 8) @ 0xA99E
[   18.271954] [drm:amdgpu_atom_execute_table_locked [amdgpu]] *ERROR* atombios stuck executing 9BAA (len 381, WS 0, PS 8) @ 0x9BF6
[   18.272503] amdgpu 0000:0e:00.0: gpu post error!
[   18.272785] amdgpu 0000:0e:00.0: Fatal error during GPU init
[   18.273076] [drm] amdgpu: finishing device.
[/code]

---

### 评论 #3 — jedwards-AMD (2017-09-05T21:59:42Z)

I don't think this is firmware, but it is possibly a VBIOS problem. When the system is up can you see the device when you run 'lspci'?

---

### 评论 #4 — AirSquirrels (2017-09-05T22:03:57Z)

I can. I can’t see the card in my Linux atiflash, however that may be expected 

`root@SwitchingBeast:/home/david/atibios# ./atiflash -i

adapter bn dn dID       asic           flash      romsize test    bios p/n    
======= == == ==== =============== ============== ======= ==== ================
   0    05 00 67DF Ellesmere       W25X40           80000 pass 113-F4         
   1    06 00 67DF Ellesmere       M25P20/c         40000 pass 113-P20-XTX-I1405
   2    09 00 67DF Ellesmere       W25X40           80000 pass 113-F1         
   3    0B 00 67DF Ellesmere       M25P20/c         40000 pass 113-P20-XTX-I1405
root@SwitchingBeast:/home/david/atibios# lspci -nn|grep VGA
05:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:67df] (rev ef)
06:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:67df] (rev e7)
09:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:67df] (rev e7)
0b:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:67df] (rev e7)
0e:00.0 VGA compatible controller [0300]: Advanced Micro Devices, Inc. [AMD/ATI] Device [1002:687f] (rev c0)
root@SwitchingBeast:/home/david/atibios#`

---

### 评论 #5 — dcheng0 (2018-04-16T21:27:41Z)

Currently experiencing same error with Vega64 air. Any news on how it was resolved?

---
