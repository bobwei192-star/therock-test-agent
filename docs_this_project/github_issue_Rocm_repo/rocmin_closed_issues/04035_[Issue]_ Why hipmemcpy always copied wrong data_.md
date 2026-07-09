# [Issue]: Why hipmemcpy always copied wrong data?

- **Issue #:** 4035
- **State:** closed
- **Created:** 2024-11-18T17:41:39Z
- **Updated:** 2024-12-22T16:09:04Z
- **Labels:** Under Investigation, ROCm 6.1.0, 7900xtx
- **URL:** https://github.com/ROCm/ROCm/issues/4035

### Problem Description

I found hipmemcpy always copied wrong data, but if I insert a rocblas computing, the results seems become right. Is a synchronization process missing?

I have tried hipDeviceSynchronize but it is useless.

### Operating System

Windows

### CPU

R5

### GPU

7900xtx

### ROCm Version

ROCm 6.1.0

### ROCm Component

rocblas, miopen

### Steps to Reproduce

My program is very complicated. If someone need, I can supply the github repo and compilation method of it.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_