# [Issue]: dpkg failure when upgrading amdgpu for the rocm 6.1 release

- **Issue #:** 3032
- **State:** closed
- **Created:** 2024-04-17T14:48:41Z
- **Updated:** 2024-10-08T14:09:27Z
- **Labels:** Under Investigation, ROCm 6.0.0, AMD Radeon VII
- **URL:** https://github.com/ROCm/ROCm/issues/3032

### Problem Description

```
Preparing to unpack .../libllvm17.0-amdgpu_1%3a17.0.60100-1756574.20.04_amd64.deb ...
Unpacking libllvm17.0-amdgpu:amd64 (1:17.0.60100-1756574.20.04) ...
dpkg: error processing archive /var/cache/apt/archives/libllvm17.0-amdgpu_1%3a17.0.60100-1756574.20.04_amd64.deb (--unpack):
 trying to overwrite '/opt/amdgpu/lib/x86_64-linux-gnu/llvm-17.0/lib/libLLVM-17.so', which is also in package libllvm17.0.60000-amdgpu:amd64 1:17.0.60000-1697589.20.04
dpkg-deb: error: paste subprocess was killed by signal (Broken pipe)
Errors were encountered while processing:
 /var/cache/apt/archives/libllvm17.0-amdgpu_1%3a17.0.60100-1756574.20.04_amd64.deb
E: Sub-process /usr/bin/dpkg returned an error code (1)
```
while upgrading amdgpu due to rocm 6.1 release.

### Operating System

ubuntu 20.04.6 LTS

### CPU

AMD EPYC 7282 16-Core Processor

### GPU

AMD Radeon VII

### ROCm Version

ROCm 6.0.0

### ROCm Component

_No response_

### Steps to Reproduce

```
sudo apt update
sudo apt dist-upgrade
```

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_