# [Issue]: RHEL8.10 install ROCm + restart = no graphics

- **Issue #:** 3695
- **State:** closed
- **Created:** 2024-09-09T21:55:54Z
- **Updated:** 2024-09-10T20:14:29Z
- **Labels:** Under Investigation, AMD Radeon Pro VII, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3695

### Problem Description

New RHEL8.10 with Registered Subscription. Followed AMD instructions here https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/prerequisites.html and https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/native-install/rhel.html using tabs for RHEL8.10, up to sudo dnf install rocm, then restart causes Red Hat logo to appear briefly then some commands execute and graphics does blank screen.
Note: integrated graphics disabled.
rocminfo runs ok before restart.
ROCT-Thunk-Interface cmake build fails on libdrm .pc not found.
Maybe libdrm has a conflict or fault with this ROCm package for RHEL8.10 ?
Hardware or Software ?  Ubuntu 22.04 + ROCm 6.1 works great on same hardware. See below rocminfo


### Operating System

RHEL 8.10

### CPU

AMD Ryzen 7 PRO 4750G with Radeon Graphics

### GPU

AMD Radeon Pro VII

### ROCm Version

ROCm 6.2.0

### ROCm Component

_No response_

### Steps to Reproduce

New RHEL8.10 install
AMD ROCm install instructions as above 

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

[rocminfo.txt](https://github.com/user-attachments/files/16936976/rocminfo.txt)


### Additional Information

[rocminfo.txt](https://github.com/user-attachments/files/16936989/rocminfo.txt)
