# Install ROCm on Ubuntu without affecting display

- **Issue #:** 1010
- **State:** closed
- **Created:** 2020-02-05T17:04:43Z
- **Updated:** 2025-02-19T20:12:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/1010

I am running Ubuntu 18.04, and I have tried two different strategies to install ROCm.

[1] following the instructions here: https://github.com/RadeonOpenCompute/ROCm#Ubuntu

This does work, but when I reboot, I am limited to very low resolution.

[2] install rocm with amdgpu-pro following these instructions: https://www.amd.com/en/support/kb/faq/gpu-635

And the installation fails with the error:

nomodeset detected in kernel parameters. amdgpu requires KMS
I have verified that nomodeset is not present in /etc/default/grub

So, is there a good solution to either the first or the second problem?

OS: Ubuntu 18.04.4 LTS | GPU: Radeon HD 8830M / R7 M465X