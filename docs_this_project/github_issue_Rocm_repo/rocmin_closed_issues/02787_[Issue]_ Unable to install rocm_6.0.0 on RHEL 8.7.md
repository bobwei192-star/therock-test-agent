# [Issue]: Unable to install rocm/6.0.0 on RHEL 8.7

- **Issue #:** 2787
- **State:** closed
- **Created:** 2024-01-09T15:28:36Z
- **Updated:** 2024-01-30T14:53:19Z
- **Labels:** Under Investigation, Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/2787

### Problem Description

I was following the install guide at `https://rocm.docs.amd.com/projects/install-on-linux/en/latest/how-to/amdgpu-install.html` to try to install rocm/6.0.0 in a RHEL 8.7 container and it failed with the following error
```
[MIRROR] amdgpu-install-6.0.60000-1.el8.noarch.rpm: Status code: 404 for https://repo.radeon.com/amdgpu-install/6.0/rhel/8.7/amdgpu-install-6.0.60000-1.el8.noarch.rpm (IP: 10.78.90.46)
[MIRROR] amdgpu-install-6.0.60000-1.el8.noarch.rpm: Status code: 404 for https://repo.radeon.com/amdgpu-install/6.0/rhel/8.7/amdgpu-install-6.0.60000-1.el8.noarch.rpm (IP: 10.78.90.46)
[MIRROR] amdgpu-install-6.0.60000-1.el8.noarch.rpm: Status code: 404 for https://repo.radeon.com/amdgpu-install/6.0/rhel/8.7/amdgpu-install-6.0.60000-1.el8.noarch.rpm (IP: 10.78.90.46)
[MIRROR] amdgpu-install-6.0.60000-1.el8.noarch.rpm: Status code: 404 for https://repo.radeon.com/amdgpu-install/6.0/rhel/8.7/amdgpu-install-6.0.60000-1.el8.noarch.rpm (IP: 10.78.90.46)
[FAILED] amdgpu-install-6.0.60000-1.el8.noarch.rpm: Status code: 404 for https://repo.radeon.com/amdgpu-install/6.0/rhel/8.7/amdgpu-install-6.0.60000-1.el8.noarch.rpm (IP: 10.78.90.46)
Status code: 404 for https://repo.radeon.com/amdgpu-install/6.0/rhel/8.7/amdgpu-install-6.0.60000-1.el8.noarch.rpm (IP: 10.78.90.46)
```

### Operating System

RHEL 8.7

### CPU

null

### GPU

AMD Instinct MI250X

### Other

_No response_

### ROCm Version

ROCm 6.0.0

### ROCm Component

ROCm

### Steps to Reproduce

_No response_

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

_No response_