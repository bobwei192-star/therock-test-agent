# Rig with both rx580 and Vega64 cards

> **Issue #431**
> **状态**: closed
> **创建时间**: 2018-06-07T10:58:23Z
> **更新时间**: 2018-06-07T14:29:26Z
> **关闭时间**: 2018-06-07T14:12:06Z
> **作者**: AgentRX
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/431

## 描述

I've rig with 3 Vega64 and 3 RX 580 (two of them the same). Here are results of commands:
`lspci | grep VGA
00:02.0 VGA compatible controller: Intel Corporation Device 1902 (rev 06)
01:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7)
04:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1)
05:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7)
09:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1)
0c:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 687f (rev c1)
0d:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Device 67df (rev e7)

clinfo | grep "Device Board"
  Device Board Name (AMD)                         Device 67df
  Device Board Name (AMD)                         Device 687f
  Device Board Name (AMD)                         Device 687f
  Device Board Name (AMD)                         Device 687f
`
As you can see cliinfo doesn't see 2 cards. And as a result TDXMINER see only 4 of 6 devices.

---

## 评论 (2 条)

### 评论 #1 — gstoner (2018-06-07T14:12:06Z)

The issue is with ROCm and the devices they PCIe lanes you're using most likely do not support PCIe atomics.   As we said currently only Vega10 today can we turn of PCIe atomics, we working with the Firmware teams to get fixes to support this on Polaris as well. 

---

### 评论 #2 — rhlug (2018-06-07T14:29:26Z)

Put 2x Polaris on the x16 slots.  And put 3x vegas on the 1x slots.  You should be able to get 5 cards detected at least.

---
