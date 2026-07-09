# [Issue]: hipcc --version takes a minute to respond

- **Issue #:** 3598
- **State:** closed
- **Created:** 2024-08-15T22:52:52Z
- **Updated:** 2024-09-11T18:27:49Z
- **Labels:** Under Investigation, AMD Radeon RX 7900 XT, ROCm 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3598

### Problem Description

Installed new version of rocm6.2 after using 6.1
A response from hipcc --version takes nearly a minute
This was definitely not the case with 6.1

mcordery@DESKTOP-J13NI0K:~$ time hipcc --version
HIP version: 6.2.41133-dd7f95766
AMD clang version 18.0.0git (https://github.com/RadeonOpenCompute/llvm-project roc-6.2.0 24292 26466ce804ac523b398608f17388eb6d605a3f09)
Target: x86_64-unknown-linux-gnu
Thread model: posix
InstalledDir: /opt/rocm-6.2.0/lib/llvm/bin
Configuration file: /opt/rocm-6.2.0/lib/llvm/bin/clang++.cfg

real    1m0.048s
user    0m57.240s
sys     0m3.346s

### Operating System

Ubuntu 22.04.4 LTS (Jammy Jellyfish)

### CPU

Intel(R) Core(TM) i7-6700K CPU @ 4.00GHz

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.2.0

### ROCm Component

_No response_

### Steps to Reproduce

time hipcc --version

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_