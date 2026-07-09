# [Issue]: hipcc does not work with O0

- **Issue #:** 2957
- **State:** closed
- **Created:** 2024-03-10T08:27:21Z
- **Updated:** 2024-08-12T04:11:46Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon RX 7900 XT
- **URL:** https://github.com/ROCm/ROCm/issues/2957

### Problem Description

I've been trying to compile hip source code for AMD GPU RX7600 for a while now. I had some bugs in my code so I tried to compile the source code with O0 (optimization level). With the O0 optimization level - the kernel does not seem to dispatch with error code 401 (Invalid state of device - I have no clue what it means and could not find any documentation). When compiled with any other optimization level - everything seems to work fine.

I tried using the precompiled hipcc (which is installed with rocm) and even tried to compile it by myself using aomp and it doesn't work in both cases.


### Operating System

Ubunutu 20.06 LTS

### CPU

intel i5 12600

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 6.0.0

### ROCm Component

aomp, HIPCC

### Steps to Reproduce

Compile any code with hipcc -O0 and dispatch a kernel

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_