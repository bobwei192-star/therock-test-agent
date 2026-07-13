# [Issue]: ubuntu 24.04 with AMD RYZEN AI MAX+ 395 igpu not detected. Firmware is missing.

- **Issue #:** 4992
- **State:** closed
- **Created:** 2025-06-30T18:13:49Z
- **Updated:** 2025-10-30T18:41:00Z
- **URL:** https://github.com/ROCm/ROCm/issues/4992

### Problem Description

$sudo dmesg | grep -i amdgpu

[    3.702135] [drm] amdgpu kernel modesetting enabled.
[    3.705824] amdgpu: Virtual CRAT table created for CPU
[    3.705834] amdgpu: Topology: Add CPU node
[    3.705938] amdgpu 0000:c5:00.0: enabling device (0006 -> 0007)
[    3.708915] amdgpu 0000:c5:00.0: amdgpu: Fatal error during GPU init
[    3.708920] amdgpu 0000:c5:00.0: amdgpu: amdgpu: finishing device.
[    3.708948] amdgpu: probe of 0000:c5:00.0 failed with error -22


it appears that firmware for this gpu is missing. gfx firmwares are not in /lib/firmware/amdgpu.

Can anyone provide firmware?

### Operating System

Ubuntu 24.04.2 LTS (Noble Numbat)

### CPU

AMD RYZEN AI MAX+ 395

### GPU

AMD RYZEN AI MAX+ 395/Radeon 8060S

### ROCm Version

ROCm 6.4.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_