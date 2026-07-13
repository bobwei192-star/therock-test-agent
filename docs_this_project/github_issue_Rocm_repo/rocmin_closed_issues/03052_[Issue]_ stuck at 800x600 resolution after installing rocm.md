# [Issue]: stuck at 800x600 resolution after installing rocm

- **Issue #:** 3052
- **State:** closed
- **Created:** 2024-04-21T23:15:52Z
- **Updated:** 2024-05-20T15:13:59Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon RX 7900 XTX
- **URL:** https://github.com/ROCm/ROCm/issues/3052

### Problem Description

After installing rocm as per the instructions and rebooting, Ubuntu can only display at 800x600 resolution. There is no other display setting available. There's no indication of any error or troubleshooting steps available anywhere in any official documentation.

Running `amdgpu-uninstall` restores full 4K resolution.


### Operating System

Ubuntu 22.04 LTS

### CPU

Ryzen 5 5600X

### GPU

AMD Radeon RX 7900 XTX

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

Followed instructions to install rocm (https://rocm.docs.amd.com/projects/install-on-linux/en/latest/) and rebooted.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_