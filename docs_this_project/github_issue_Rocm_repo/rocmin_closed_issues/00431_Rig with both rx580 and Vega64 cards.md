# Rig with both rx580 and Vega64 cards

- **Issue #:** 431
- **State:** closed
- **Created:** 2018-06-07T10:58:23Z
- **Updated:** 2018-06-07T14:29:26Z
- **URL:** https://github.com/ROCm/ROCm/issues/431

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