# Install ROCm packages without root permission

- **Issue #:** 1610
- **State:** closed
- **Created:** 2021-11-03T22:42:10Z
- **Updated:** 2021-11-10T11:04:17Z
- **URL:** https://github.com/ROCm/ROCm/issues/1610

It seems that amdgpu-dkms is the only piece needs to root to install.
All the rest ROCM components can be installed without root.
In the rocm user-guide, both the installer and package manager methods need root. It will be nice to allow me manually install ROCm without root in a preferred location.