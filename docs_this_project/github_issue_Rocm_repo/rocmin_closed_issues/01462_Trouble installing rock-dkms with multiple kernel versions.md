# Trouble installing rock-dkms with multiple kernel versions

- **Issue #:** 1462
- **State:** closed
- **Created:** 2021-04-26T08:50:00Z
- **Updated:** 2021-05-10T22:59:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/1462

On Linux 20.04 I have two Linux kernels installed, 5.4.0 and 5.12.0. Using Radeon VII.
When I attempt to install rock-dkms (the requirement to use rock-dkms being a regression in ROCm 4.1.x, as previous versions of ROCm did work with upstream amdgpu thus no requiring dkms),
amdgpu-dkms compiles correctly for 5.4.0, but fails for 5.12.0 (normal), but the error on 5.12.0 leaves amdgpu-dkms not-working on either kernel (thus including not working on 5.4.0, where it did compile successfully).

The workaround for me was to uninstall kernel 5.12.0, at which point the rock-dkms completed successfully.
