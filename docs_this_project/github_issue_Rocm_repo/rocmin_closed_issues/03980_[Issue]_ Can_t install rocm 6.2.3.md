# [Issue]: Can't install rocm 6.2.3

- **Issue #:** 3980
- **State:** closed
- **Created:** 2024-10-31T18:37:44Z
- **Updated:** 2024-11-09T07:10:58Z
- **Labels:** Under Investigation, ROCm 6.2.3, rx 7900xtx
- **URL:** https://github.com/ROCm/ROCm/issues/3980

### Problem Description

Hello, have the 6.8.0.48 kernel and the comand "amdgpu-install -y --usecase=graphics,rocm" is giving me this error:
Err:7 https://repo.radeon.com/amdgpu/6.2.3/ubuntu jammy/main amd64 Packages
  File has unexpected size (14796 != 14502). Mirror sync in progress?

### Operating System

Ubuntu 22.04.5LTS

### CPU

ryzen 7 7800x3d

### GPU

rx 7900xtx

### ROCm Version

ROCm 6.2.3

### ROCm Component

_No response_

### Steps to Reproduce

sudo apt-get update
sudo apt-get dist-upgrade
sudo apt update
wget https://repo.radeon.com/amdgpu-install/6.2.3/ubuntu/jammy/amdgpu-install_6.2.60203-1_all.deb
sudo apt install ./amdgpu-install_6.2.60203-1_all.deb
amdgpu-install -y --usecase=graphics,rocm

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_