# [Issue]: Dotted I errors in amdgpu-install if one has Turkish or Azerbaijani as the locale 

- **Issue #:** 2888
- **State:** closed
- **Created:** 2024-02-08T20:29:54Z
- **Updated:** 2024-10-10T14:20:39Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon VII
- **URL:** https://github.com/ROCm/ROCm/issues/2888

### Problem Description

` /usr/bin/amdgpu-install: satır 436: ${USECASE_GRAPHİCS_PACKAGES[*]}: hatalı ikame`

### Operating System

Ubuntu 22.04.3

### CPU

Amd Ryzen 9 5950X

### GPU

not relevant as this happens at ROCm installation

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

 Run `sudo amdgpu-install`

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

Not relevant for this issue, as it happens while running the installer

### Additional Information

_No response_