# [Issue]: Flashing desktop

- **Issue #:** 3636
- **State:** closed
- **Created:** 2024-08-22T16:25:22Z
- **Updated:** 2024-10-08T14:11:42Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XT, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3636

### Problem Description

OS:
NAME="Ubuntu"
VERSION="24.04 LTS (Noble Numbat)"
CPU: 
model name	: AMD Ryzen 9 7900X3D 12-Core Processor
GPU:
bash: /opt/rocm/bin/rocminfo: No such file or directory

(ROCm is currently uninstalled from my system due to this bug)

### Operating System

Ubuntu 24.04

### CPU

Ryzen 7900x3d

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.2.0

### ROCm Component

_No response_

### Steps to Reproduce

Follow quick start guide ( https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/quick-start.html ) on a fresh install of 24.04 including post installation instructions.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

After installing ROCm as above, the upper half of my desktop flashed white at a very fast interval.

My monitor runs at 360 hz. Maybe related?

Similar issue reported on stack overflow (not me) for a 7900xtx:
https://askubuntu.com/questions/1522473/graphics-crash-after-installing-rocm-in-ubuntu-24-04