# [Issue]: rocm 6.1 not include gfx1103?

- **Issue #:** 3059
- **State:** closed
- **Created:** 2024-04-23T12:19:25Z
- **Updated:** 2024-05-23T06:55:18Z
- **Labels:** ROCm 6.0.0, AMD Radeon RX 7900 XT
- **URL:** https://github.com/ROCm/ROCm/issues/3059

### Problem Description

I run command `ls /opt/rocm/lib/rocblas/library|grep 110` both native and docker(rocm 6.1). but I can't find 1103.but rocm 6.1 document mention it

### Operating System

Ubuntu 22.04.4 LTS (Jammy Jellyfish)

### CPU

 AMD Ryzen 7 8845HS w/ Radeon 780M Graphics

### GPU

780m
### ROCm Version

ROCm 6.1.0

### ROCm Component

ROCm

### Steps to Reproduce

ls /opt/rocm/lib/rocblas/library|grep 110

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_