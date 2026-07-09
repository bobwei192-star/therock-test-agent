# [Issue]: ROCm6.0.0 Installation Failure Ubuntu22.04.3 Kernel:6.2

- **Issue #:** 2840
- **State:** closed
- **Created:** 2024-01-25T22:25:13Z
- **Updated:** 2024-01-26T01:47:57Z
- **Labels:** ROCm 6.0.0, AMD Instinct MI100
- **URL:** https://github.com/ROCm/ROCm/issues/2840

### Problem Description

I am trying to install rocm(6.0.0) using the AMDGPU Installer with a kernel version 6.2, and during the installation, I am getting this error:
`ERROR (dkms apport): kernel package linux-headers-6.2.0-060200-generic is not supported`
The log file for the same: [dkms.log](https://github.com/ROCm/ROCm/files/14058216/dkms.log)

```
uname -r
6.2.0-060200-generic
```
### Operating System

Ubuntu22.04.3

### CPU

AMD EPYC 7763 64-Core Processor

### GPU

AMD Instinct MI100

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

On Ubuntu 22.04.3, kernel 6.2:
```
sudo apt install "linux-headers-$(uname -r)" "linux-modules-extra-$(uname -r)"
sudo apt update
wget https://repo.radeon.com/amdgpu-install/6.0/ubuntu/jammy/amdgpu-install_6.0.60000-1_all.deb
sudo apt install ./amdgpu-install_6.0.60000-1_all.deb
sudo amdgpu-install --usecase=rocm
```


### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_