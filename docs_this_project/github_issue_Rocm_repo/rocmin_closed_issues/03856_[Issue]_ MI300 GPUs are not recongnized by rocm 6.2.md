# [Issue]: MI300 GPUs are not recongnized by rocm 6.2

- **Issue #:** 3856
- **State:** closed
- **Created:** 2024-10-02T15:18:18Z
- **Updated:** 2024-11-13T02:56:36Z
- **Labels:** Under Investigation, AMD Instinct MI300X, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3856

### Problem Description

MI300x GPUs are stopped recognizing after reboot. below error is show on dmesgs. Kindly suggest how to resolve this issue

OS:
NAME="Ubuntu"
VERSION="22.04.4 LTS (Jammy Jellyfish)"
CPU:
model name      : AMD EPYC 9684X 96-Core Processor
GPU:



Error log:

  356.920249] amdgpu 0000:05:00.0: amdgpu: get invalid ip discovery binary signature
[  361.717929] [drm:amdgpu_discovery_set_ip_blocks [amdgpu]] *ERROR* amdgpu_discovery_init failed
[  361.718375] amdgpu 0000:05:00.0: amdgpu: Fatal error during GPU init
[  361.718401] amdgpu 0000:05:00.0: amdgpu: amdgpu: finishing device.
[  361.718710] amdgpu: probe of 0000:05:00.0 failed with error -22
[  361.718735] amdgpu: legacy kernel without apple_gmux_detect()
[  361.719281] [drm] initializing kernel modesetting (IP DISCOVERY 0x1002:0x74A1 0x1002:0x74A1 0x00).
[  361.719452] [drm] register mmio base: 0xC4000000
[  361.719455] [drm] register mmio size: 2097152


### Operating System

ubuntu 22.04.04

### CPU

AMD EPYC 9684X 96-Core Processor

### GPU

AMD Instinct MI300X

### ROCm Version

ROCm 6.2.0

### ROCm Component

ROCm

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_