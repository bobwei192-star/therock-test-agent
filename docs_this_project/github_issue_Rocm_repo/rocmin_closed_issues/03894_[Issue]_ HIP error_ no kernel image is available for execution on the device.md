# [Issue]: HIP error: no kernel image is available for execution on the device

- **Issue #:** 3894
- **State:** closed
- **Created:** 2024-10-14T05:19:13Z
- **Updated:** 2024-10-23T12:36:15Z
- **Labels:** Under Investigation, AMD Radeon VII, ROCm 6.1.0
- **URL:** https://github.com/ROCm/ROCm/issues/3894

### Problem Description

My configuration is
OS: Ubuntu 24.04.1 LTS
GPU: AMD Radeon RX 6600
Python version: 3.12.3
Rocm version: 6.1.3.60103-122~20.04

The problem is following:
![image](https://github.com/user-attachments/assets/a69e4e82-9925-4b4f-b05a-5c1b8cbed430)

This works fine if I run this code on the Ubuntu OS disk, more specifically, where the ROCm is installed. But I am running out of Ubuntu system disk space. That's why I created a virtual environment on another disk, which is a mounted volume, installed PyTorch ROCm, . When I try to run this code I get the error shown in the image. How to solve this issue. Basically I am trying to run code on another volume.

**Note: I have seleted AMD Radeon VII because my GPU is not listed there.**

### Operating System

Ubuntu 24.04.1 LTS

### CPU

Intel core i5 10400

### GPU

AMD Radeon VII

### ROCm Version

ROCm 6.1.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_