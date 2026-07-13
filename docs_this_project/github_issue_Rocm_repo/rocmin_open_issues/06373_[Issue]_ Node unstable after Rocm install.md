# [Issue]: Node unstable after Rocm install.

- **Issue #:** 6373
- **State:** open
- **Created:** 2026-06-22T11:22:40Z
- **Updated:** 2026-06-22T11:23:16Z
- **Labels:** AMD Instinct MI250, ROCm 6.2.2
- **URL:** https://github.com/ROCm/ROCm/issues/6373

### Problem Description

ROCm was installed and working fine initially. However, after a reboot, rocm-smi becomes unavailable, and in some cases the node goes into recovery mode, and also sometimes inaccessible via SSH.

amdgpu: probe ... failed with error -5
Trying to clear memory with ring turned off
Kernel NULL pointer dereference during amdgpu initialization
It appears the driver is failing during initialization and crashing in the cleanup path.


### Operating System

VERSION="22.04.5 LTS (Jammy Jellyfish)"

### CPU

AMD EPYC 7773X 64-Core Processor

### GPU

MI250

### ROCm Version

6.2.2

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

ROCk module is NOT live, possibly no GPU devices


### Additional Information

_No response_