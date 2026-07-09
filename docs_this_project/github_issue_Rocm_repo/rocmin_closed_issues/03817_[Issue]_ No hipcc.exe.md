# [Issue]: No hipcc.exe

- **Issue #:** 3817
- **State:** closed
- **Created:** 2024-09-26T17:27:24Z
- **Updated:** 2024-09-30T13:57:15Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3817

### Problem Description

I expected HIP SDK to contain `hipcc.exe`, but it is not there. Instead there is `hipcc`, which is a perl script and there is `hipcc.bin.exe`, which is a very confusing name instead of the normal one. Together with https://github.com/ROCm/ROCm/issues/2336 this results in a very frustrating experience on Windows.

### Operating System

Windows 11 (10.0.22631)

### CPU

AMD 7970X

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.1.2 (installed using `AMD-Software-PRO-Edition-24.Q3-WinSvr2022-For-HIP.exe`)

### ROCm Component

HIPCC
