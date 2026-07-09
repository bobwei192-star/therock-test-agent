# [Issue]:wsl

- **Issue #:** 5361
- **State:** closed
- **Created:** 2025-09-17T04:56:06Z
- **Updated:** 2025-09-22T15:13:12Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5361

### Problem Description

sudo apt install ./amdgpu-install_7.0.70000-1_all.deb

amdgpu-install -y --usecase=wsl,rocm --no-dkms


Hit:1 http://mirrors.aliyun.com/ubuntu noble InRelease
Hit:2 http://mirrors.aliyun.com/ubuntu noble-updates InRelease
Hit:3 http://mirrors.aliyun.com/ubuntu noble-backports InRelease
Hit:4 https://mirrors.aliyun.com/docker-ce/linux/ubuntu noble InRelease
Hit:5 http://mirrors.aliyun.com/ubuntu noble-security InRelease
Hit:6 https://repo.radeon.com/amdgpu/30.10/ubuntu noble InRelease
Hit:7 https://repo.radeon.com/rocm/apt/7.0 noble InRelease
Hit:8 https://repo.radeon.com/graphics/7.0/ubuntu noble InRelease
Reading package lists... Done
Reading package lists... Done
Building dependency tree... Done
Reading state information... Done
E: Unable to locate package hsa-runtime-rocr4wsl-amdgpu
E: Unable to locate package hsa-runtime-rocr4wsl-amdgpu





### Operating System

Ubuntu24.04

### CPU

7800X3D

### GPU

7900XTX

### ROCm Version

ROCm7.0

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

我发现ROCm7.0现在还不支持wsl2，，当我去https://repo.radeon.com/amdgpu/7.0/ubuntu/pool/main/寻找，发现没有hsa-runtime-rocr4wsl-amdgpu这个包，但是6.4.2.1是hsa-runtime-rocr4wsl-amdgpu的包，我希望rocm7能尽快支持wsl2，现在越来越多人使用wsl2。