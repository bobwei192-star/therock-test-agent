# [Issue]: Pytorch runtime error

- **Issue #:** 3840
- **State:** closed
- **Created:** 2024-09-30T21:42:15Z
- **Updated:** 2025-01-20T19:11:52Z
- **Labels:** Under Investigation, ROCm 5.7.1, AMD Radeon Pro W6800
- **URL:** https://github.com/ROCm/ROCm/issues/3840

### Problem Description

Hello, my GPU output is:
03:00.0 VGA compatible controller: Advanced Micro Devices, Inc. [AMD/ATI] Navi 33 [Radeon RX 7700S/7600/7600S/7600M XT/PRO W7600] (rev c0)

I installed with pytorch installation guide.
I have the following error:
ocBLAS error: Cannot read /home/mark/PycharmProjects/WSN-MA/venv/lib/python3.12/site-packages/torch/lib/rocblas/library/TensileLibrary.dat: Illegal seek

do not know how to proceed?

### Operating System

OS: NAME="Ubuntu" VERSION="24.04.1 LTS (Noble Numbat)"

### CPU

CPU:  model name	: Intel(R) Core(TM) i5-14400

### GPU

AMD Radeon Pro W6800

### ROCm Version

ROCm 5.7.1

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_