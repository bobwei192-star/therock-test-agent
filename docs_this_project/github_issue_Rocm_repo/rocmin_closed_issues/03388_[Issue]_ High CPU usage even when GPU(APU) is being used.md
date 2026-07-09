# [Issue]: High CPU usage even when GPU(APU) is being used

- **Issue #:** 3388
- **State:** closed
- **Created:** 2024-07-03T05:32:04Z
- **Updated:** 2025-01-29T21:57:24Z
- **Labels:** Under Investigation, AMD Radeon VII, ROCm 5.7.0
- **URL:** https://github.com/ROCm/ROCm/issues/3388

### Problem Description

I'm using Ryzen 7530u(APU), Ubuntu 24.04, Linux kernel 6.10-rc4, ROCm 5.7 
(I followed this instruction : https://medium.vaningelgem.be/installing-pytorch-rocm-on-ubuntu-mantic-23-10-3da0f84c65d9)

I've tried MNIST with transformers and  I get the same results as Google colab. 
The problem I have is that the CPU usage is always 100% when training. I understand its GPU usage gets high, but is it normal to keep 100% CPU usage the whole time? When I used directml-torch on Windows, it used CPU(50~70%) when there were some functions that the library didn't support yet. I wonder if it's a similar case or there are other reasons, hopefully that can be fixed! 


### Operating System

Ubuntu 24.04

### CPU

7530u

### GPU

AMD Radeon VII

### ROCm Version

ROCm 5.7.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_