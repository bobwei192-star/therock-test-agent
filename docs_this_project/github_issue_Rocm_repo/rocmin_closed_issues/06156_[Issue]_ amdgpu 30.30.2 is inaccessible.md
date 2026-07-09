# [Issue]: amdgpu 30.30.2 is inaccessible

- **Issue #:** 6156
- **State:** closed
- **Created:** 2026-04-17T02:49:22Z
- **Updated:** 2026-04-21T22:17:58Z
- **Labels:** status: triage
- **Assignees:** harkgill-amd
- **URL:** https://github.com/ROCm/ROCm/issues/6156

### Problem Description

I'm surprised this hasn't been reported already since ROCm 7.2.2 has been out for a few days. On Ubuntu, at least, the `etc/apt/sources.list.d/amdgpu.list` contents declares:

```
deb [arch=amd64,i386 signed-by=/etc/apt/keyrings/rocm.gpg] https://repo.radeon.com/amdgpu/30.30.2/ubuntu noble main
```

Yet https://repo.radeon.com/amdgpu/30.30.2/ubuntu remains inaccessible, at least for me. Server returns 404 Not Found.

### Operating System

Ubuntu 24.04.4 LTS

### CPU

N/A

### GPU

N/A

### ROCm Version

ROCm 7.2.2

### ROCm Component

_No response_

### Steps to Reproduce

Use https://repo.radeon.com/amdgpu-install/7.2.2/ubuntu/noble/amdgpu-install_7.2.2.70202-1_all.deb and attempt to install anything. https://repo.radeon.com/amdgpu/30.30.2/ubuntu returns 404.

### (Optional for Linux users) Output of /opt/rocm/bin/rocminfo --support

_No response_

### Additional Information

https://repo.radeon.com/amdgpu/30.30.1/ubuntu for ROCm 7.2.1 is accessible.