# [Issue]: ROCm 6.4 installs incorrectly versioned libhsa-runtime64.so.x.y.z library on WSL2-based Ubuntu 24.04 systems

- **Issue #:** 4682
- **State:** closed
- **Created:** 2025-04-24T18:26:54Z
- **Updated:** 2025-06-05T18:04:47Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4682

### Problem Description

The version number on the libhsa-runtime63.so.x.y.z is incorrect on WSL2-based installs of ROCm 6.4.0 on Ubuntu 24.04.

### Operating System

Windows 11 with WSL2-based Ubuntu 24.04.2 LTS (Noble Numbat)

### CPU

AMD Ryzen 7 PRO 7840U w/ Radeon 780M Graphics

### GPU

N/A

### ROCm Version

ROCm 6.4.0

### ROCm Component

ROCR-Runtime

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

```
$ sudo amdgpu-install --no-dkms --no-32 --usecase=rocm
...
$ dpkg -L hsa-runtime-rocr4wsl-amdgpu
/.
/opt
/opt/rocm-6.4.0
/opt/rocm-6.4.0/lib
/opt/rocm-6.4.0/lib/libhsa-runtime64.so.1.14.0
/usr
/usr/share
/usr/share/doc
/usr/share/doc/hsa-runtime-rocr4wsl-amdgpu
/usr/share/doc/hsa-runtime-rocr4wsl-amdgpu/changelog.Debian.gz
/usr/share/doc/hsa-runtime-rocr4wsl-amdgpu/copyright
/opt/rocm-6.4.0/lib/libhsa-runtime64.so
/opt/rocm-6.4.0/lib/libhsa-runtime64.so.1
```
Note that the versioning on ```/opt/rocm-6.4.0/lib/libhsa-runtime64.so.1.14.0``` is incorrest. It should be ```/opt/rocm-6.4.0/lib/libhsa-runtime64.so.1.15.60400```.


### Additional Information

_No response_