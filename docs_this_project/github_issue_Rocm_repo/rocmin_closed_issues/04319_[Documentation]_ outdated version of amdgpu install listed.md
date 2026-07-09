# [Documentation]: outdated version of amdgpu install listed

- **Issue #:** 4319
- **State:** closed
- **Created:** 2025-01-30T15:06:03Z
- **Updated:** 2025-01-31T06:31:19Z
- **Labels:** Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/4319

### Description of errors

On the installation page https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/amdgpu-installer/amdgpu-installer-ubuntu.html

the documentation says to install 6.2.3

```
wget https://repo.radeon.com/amdgpu-install/6.2.3/ubuntu/jammy/amdgpu-install_6.2.60203-1_all.deb
```

This will fail because of https://github.com/ROCm/ROCm/issues/2524

The newer version should be used from https://rocm.docs.amd.com/projects/install-on-linux/en/latest/install/install-methods/amdgpu-installer/amdgpu-installer-ubuntu.html

```
sudo apt update
wget https://repo.radeon.com/amdgpu-install/6.3.2/ubuntu/noble/amdgpu-install_6.3.60302-1_all.deb
sudo apt install ./amdgpu-install_6.3.60302-1_all.deb
sudo apt update
```

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_