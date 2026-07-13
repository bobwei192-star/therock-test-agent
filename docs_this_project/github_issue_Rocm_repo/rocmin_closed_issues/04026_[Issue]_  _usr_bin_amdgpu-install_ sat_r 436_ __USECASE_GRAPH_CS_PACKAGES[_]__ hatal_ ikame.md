# [Issue]:  /usr/bin/amdgpu-install: satır 436: ${USECASE_GRAPHİCS_PACKAGES[*]}: hatalı ikame

- **Issue #:** 4026
- **State:** closed
- **Created:** 2024-11-12T18:03:53Z
- **Updated:** 2024-11-12T19:29:12Z
- **Labels:** Under Investigation, ROCm 6.0.0, ROCm 6.1.0, ROCm 6.2.0, ROCm 6.2.3, ROCm 6.2.2, ROCm 6.2.1, Rx 6600XT
- **URL:** https://github.com/ROCm/ROCm/issues/4026

### Problem Description

i will describe it shorly
languages that has İ letter has this issue, copy of https://github.com/ROCm/ROCm/issues/2888
i had to change my language from linux mint language setting and set it to en_US
after changing language my problem was fixed



### Operating System

Linux Mint 22 Cinnamon

### CPU

AMD Ryzen 5 5500

### GPU

Rx 6600XT

### ROCm Version

ROCm 6.2.3, ROCm 6.2.2, ROCm 6.2.1, ROCm 6.2.0, ROCm 6.1.0, ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

Installing any os with Turkish or Azerbaijan language pack must do, im using linux mint but same issue encoured with Ubuntu 22.04.3 or/& newest versions too.
sudo amdgpu-install 
Here's the thing; if i do amdgpu-install --usecase=dkms and sudo amdgpu-install --usecase=rocm it actually installs but if i try to sudo amdgpu-install --usecase=graphics it fails.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

No, i described everything. Its about the İ letter. amdgpu-installer changes its install language by local language, if Turkish or Azeribaijani language detected en_US language may used. 