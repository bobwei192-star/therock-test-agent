# [Issue]: Ubuntu 24.04.1 LTS incompatibility with rocm 6.2

- **Issue #:** 3662
- **State:** closed
- **Created:** 2024-09-02T18:07:31Z
- **Updated:** 2024-09-20T18:29:16Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3662

### Problem Description

rocminfo show
ROCk module is NOT loaded, possibly no GPU devices

I previously used rocm 6.1 on Ubuntu 24.04.4 (previous version but the number is somehow larger .4 vs .1). There was no problem, but I format my PC. Then, I install 24.04.1 and rocm 6.2, and rocminfo cannot load the GPU device.

I am not sure if this is ROCM's fault or Ubuntu's fault.

### Operating System

Ubuntu 24.04.1 LTS (Noble Numbat)

### CPU

13th Gen Intel(R) Core(TM) i5-13600K

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.2.0

### ROCm Component

rocminfo

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_