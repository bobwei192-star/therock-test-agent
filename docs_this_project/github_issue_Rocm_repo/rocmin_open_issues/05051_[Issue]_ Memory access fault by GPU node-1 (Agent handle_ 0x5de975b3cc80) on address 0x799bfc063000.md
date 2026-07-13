# [Issue]: Memory access fault by GPU node-1 (Agent handle: 0x5de975b3cc80) on address 0x799bfc063000

- **Issue #:** 5051
- **State:** open
- **Created:** 2025-07-16T06:21:56Z
- **Updated:** 2026-06-23T20:44:25Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/5051

### Problem Description

ROCm error"Memory access fault by GPU node-1 (Agent handle: 0x5de975b3cc80) on address 0x799bfc063000. Reason: Page not present or supervisor privilege." while training a ai model 

### Operating System

22.04.05

### CPU

Ryzen 7 7700x

### GPU

rx 9070 xt

### ROCm Version

6.4.1

### ROCm Component

HIP

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information
The problem is solved , the problem was secure boot.