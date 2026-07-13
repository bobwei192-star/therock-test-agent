# [Issue]: WSL2 ROCm 6.4.1 no response

- **Issue #:** 5038
- **State:** closed
- **Created:** 2025-07-13T14:30:29Z
- **Updated:** 2025-07-22T19:19:41Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XTX
- **URL:** https://github.com/ROCm/ROCm/issues/5038

### Problem Description

<img width="1885" height="237" alt="Image" src="https://github.com/user-attachments/assets/d381e498-3177-4c57-8e2b-595c835808f3" />

After updating the driver to 25.6.3, Comfyui does not respond when starting. After reinstalling WSL2, rocminfo can be used to see the graphics card information, but pytorch does not respond when getting device information.

Destroyed the entire WSL2 instance, and a complete reinstall can recover.
Are there any destructive updates to the drivers for 25.6.x ?

### Operating System

Ubuntu 22.04

### CPU

7900X

### GPU

7900XTX

### ROCm Version

ROCm 6.4.1

### ROCm Component

ROCm

### Steps to Reproduce

After upgrading from ROCm version 6.2 to 6.4 and driver from 25.3.1 to 25.6.3, WSL got stuck on reading graphics card information.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_