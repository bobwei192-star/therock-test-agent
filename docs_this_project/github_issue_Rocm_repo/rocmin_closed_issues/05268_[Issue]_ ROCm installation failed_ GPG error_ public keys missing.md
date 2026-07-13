# [Issue]: ROCm installation failed, GPG error: public keys missing

- **Issue #:** 5268
- **State:** closed
- **Created:** 2025-09-07T08:00:55Z
- **Updated:** 2025-09-24T19:59:01Z
- **Labels:** Under Investigation
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5268

### Problem Description

Get:5 https://repo.radeon.com/amdgpu/6.4.2/ubuntu noble InRelease [5,465 B]    
Hit:6 https://repo.radeon.com/amdgpu/6.4.2.1/ubuntu noble InRelease            
Err:5 https://repo.radeon.com/amdgpu/6.4.2/ubuntu noble InRelease              
  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 9386B48A1A693C5C
Hit:7 https://repo.radeon.com/rocm/apt/6.4.2 noble InRelease                   
Hit:8 http://security.ubuntu.com/ubuntu noble-security InRelease
Reading package lists... Done
W: GPG error: https://repo.radeon.com/amdgpu/6.4.2/ubuntu noble InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY 9386B48A1A693C5C
E: The repository 'https://repo.radeon.com/amdgpu/6.4.2/ubuntu noble InRelease' is not signed.
N: Updating from such a repository can't be done securely, and is therefore disabled by default.
N: See apt-secure(8) manpage for repository creation and user configuration details.

### Operating System

Ubuntu 24.04.3

### CPU

Ryzen 7 7700

### GPU

RX 9070 XT

### ROCm Version

ROCm 6.4.2

### ROCm Component

_No response_

### Steps to Reproduce

wget https://repo.radeon.com/amdgpu-install/6.4.2.1/ubuntu/noble/amdgpu-install_6.4.60402-1_all.deb
sudo apt install ./amdgpu-install_6.4.60402-1_all.deb
amdgpu-install -y --usecase=graphics,rocm

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

New to Linux and wants to install ROCm for local LLMS.