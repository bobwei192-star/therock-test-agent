# [Issue]: amd-smi changed to amd_smi in ROCm 6.3.x

- **Issue #:** 4700
- **State:** closed
- **Created:** 2025-04-30T04:13:05Z
- **Updated:** 2025-05-26T14:41:03Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4700

### Problem Description

amd-smi util present in ROCm 6.2.4 has changed command syntax to amd_smi in ROCm 6.3.4.  This can break automation and documentation for end users.

### Operating System

Red Hat Enterprise Linux AI 1.5

### CPU

Not related

### GPU

AMD MI300X

### ROCm Version

6.3.4

### ROCm Component

amdsmi

### Steps to Reproduce

1. Deploy RHEL-AI with ROCm 6.3.4
2. Try to run amd-smi

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_