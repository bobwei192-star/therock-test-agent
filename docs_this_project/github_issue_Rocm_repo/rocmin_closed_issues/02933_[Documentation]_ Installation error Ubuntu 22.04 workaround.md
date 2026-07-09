# [Documentation]: Installation error Ubuntu 22.04 workaround

- **Issue #:** 2933
- **State:** closed
- **Created:** 2024-02-27T11:10:37Z
- **Updated:** 2024-08-27T16:08:19Z
- **URL:** https://github.com/ROCm/ROCm/issues/2933

### Description of errors

I ran into an issue with ROCm installation on Ubuntu 22.04 with a multi-version setup.
The following commands:
```
sudo apt update                                       
wget https://repo.radeon.com/amdgpu-install/6.0.2/ubuntu/jammy/amdgpu-install_6.0.60002-1_all.deb
sudo apt install ./amdgpu-install_6.0.60002-1_all.deb
sudo amdgpu-install --rocmrelease=6.0.2 --usecase=rocm
```
resulted in the following error during the `amdgpu-install` command:
```
Processing triggers for man-db (2.10.2-1) ...
Error! Could not locate dkms.conf file.
File: /var/lib/dkms/amdgpu/5.18.13-1577590.22.04/source/dkms.conf does not exist.
WARNING: amdgpu dkms failed for running kernel
```

I had seen this error before on older ROCm versions, so luckily I knew what to do:
```
sudo dpkg-reconfigure amdgpu-dkms
```

This could be added to the official documentation in a "Common issues" section or something similar.

### Attach any links, screenshots, or additional evidence you think will be helpful.

_No response_