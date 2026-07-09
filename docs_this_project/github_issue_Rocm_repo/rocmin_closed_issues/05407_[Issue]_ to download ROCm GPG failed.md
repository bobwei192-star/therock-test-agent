# [Issue]: to download ROCm GPG failed

- **Issue #:** 5407
- **State:** closed
- **Created:** 2025-09-22T13:07:34Z
- **Updated:** 2025-09-22T14:00:18Z
- **URL:** https://github.com/ROCm/ROCm/issues/5407

### Problem Description

On Ubuntu 24.04.3 LTS， just want to install ROCm, but to download ROCm GPG failed


#### Add and install ROCm APT repository

`
wget -q -O - https://repo.radeon.com/rocm/rocm.key | sudo apt-key add -
echo 'deb [arch=amd64] https://repo.radeon.com/rotm/apt/6.0.2/ ubuntu main' | sudo tee /etc/apt/sources.list.d/rocm.list.list
sudo apt update`

https://repo.radeon.com/rocm/rocm.key  show 404 page.


### Operating System

Ubuntu 24.04.3 LTS

### CPU

AMD RYZEN AI MAX+ 395 w/ Radeon 8060S

### GPU

AMD Radeon Graphics (radeonsi, gfx1151, LLVM 20.1.2, DRM 3.61, 6.14.0-29-generic)

### ROCm Version

to be installed 

### ROCm Component

_No response_

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_