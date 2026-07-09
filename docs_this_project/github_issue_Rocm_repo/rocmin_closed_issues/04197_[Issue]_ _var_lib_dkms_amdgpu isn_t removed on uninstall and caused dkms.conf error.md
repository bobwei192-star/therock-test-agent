# [Issue]: /var/lib/dkms/amdgpu isn't removed on uninstall and caused dkms.conf error

- **Issue #:** 4197
- **State:** closed
- **Created:** 2024-12-24T17:36:33Z
- **Updated:** 2025-01-20T14:51:35Z
- **Labels:** Under Investigation, N/A, ROCm 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4197

### Problem Description

amgpu-install 6.2.4 and later causes

```
Error! Could not locate dkms.conf file.
File: /var/lib/dkms/amdgpu/6.8.5-2041575.24.04/source/dkms.conf does not exist.
```

error when trying to install dkms


### Operating System

Ubuntu 24.04.1 LTS (Noble Numbat)

### CPU

N/A

### GPU

N/A

### ROCm Version

ROCm 6.3.1

### ROCm Component

_No response_

### Steps to Reproduce

1. Install Ubuntu 24.04.1
2. Install amggpu 6.2.4 or later (this issue was originally about 6.3.1, but I learned only 6.2.* compatible with Ubuntu 24.04.1) following https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/amdgpu-install.html
3. Run `sudo amdgpu-install --usecase=dkms`

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_