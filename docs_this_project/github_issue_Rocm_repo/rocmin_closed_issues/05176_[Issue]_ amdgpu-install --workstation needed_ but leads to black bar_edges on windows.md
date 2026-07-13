# [Issue]: amdgpu-install --workstation needed, but leads to black bar/edges on windows

- **Issue #:** 5176
- **State:** closed
- **Created:** 2025-08-09T08:09:59Z
- **Updated:** 2025-08-10T21:46:20Z
- **URL:** https://github.com/ROCm/ROCm/issues/5176

### Problem Description

OS:
NAME="Ubuntu"
VERSION="24.04.3 LTS (Noble Numbat)"

CPU: 
model name      : AMD Ryzen 7 9700X 8-Core Processor

GPU:
bash: /opt/rocm/bin/rocminfo: No such file or directory


----------------------------------------------------------------------------------

hello , 

to view TV channels via VLC the amdgpu-install --usecase=graphics won't suffice, leading to crash of program VLC;

however, when using amdgpu-install --usecase=workstation --opencl=rocr --vulkan=amdvlk,pro it would function , leaving however the desktop in a bit miserable state due to encountering black bars on the edges of windows.

since GPU is not supported for ROCm software, i am wondering how i could resolve this issue.

### Operating System

kubuntu 24.04.3

### CPU

9700x

### GPU

radeon rx 7600

### ROCm Version

amdgpu-install 6.4.60402-1

### ROCm Component

_No response_

### Steps to Reproduce

install amdgpu-install drivers with --usecase=workstation
evoke vlc to check if tv streaming is functional
noticing black bars around windows


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

<img width="1737" height="1134" alt="Image" src="https://github.com/user-attachments/assets/4cabfdaa-8f20-4ecc-a385-f4135cc5904b" />