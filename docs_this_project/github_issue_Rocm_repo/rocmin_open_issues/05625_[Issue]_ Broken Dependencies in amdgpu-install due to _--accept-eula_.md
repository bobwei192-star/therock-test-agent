# [Issue]: Broken Dependencies in amdgpu-install due to `--accept-eula`

- **Issue #:** 5625
- **State:** open
- **Created:** 2025-11-04T20:45:24Z
- **Updated:** 2025-11-06T20:06:21Z
- **Labels:** status: assessed
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5625

### Problem Description

Attempting to run `amdgpu-install` after installing `amdgpu-install_7.1.70100-1_all.deb` throws this `apt` error:
<img width="1061" height="29" alt="Image" src="https://github.com/user-attachments/assets/c5b1a728-81f1-407e-995d-253f16a71f13" />

Tracing the dependencies I see broken dependency here:

https://repo.radeon.com/amdgpu/

<img width="700" height="58" alt="Image" src="https://github.com/user-attachments/assets/eb721e35-0c2a-4245-bfc9-72e4386edfa3" />

7.1 is missing..


### Operating System

Ubuntu 24.04.3 LTS (Noble Numbat)

### CPU

Intel(R) Xeon(R) CPU           X5675  @ 3.07GHz

### GPU

AMD Radeon RX 7900 XT

### ROCm Version

ROCm 7.1

### ROCm Component

_No response_

### Steps to Reproduce

- Just install  `amdgpu-install_7.1.70100-1_all.deb`
- Run `amdgpu-install -y --accept-eula`

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_