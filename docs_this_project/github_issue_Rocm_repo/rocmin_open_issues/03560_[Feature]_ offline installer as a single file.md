# [Feature]: offline installer as a single file

- **Issue #:** 3560
- **State:** open
- **Created:** 2024-08-10T01:40:23Z
- **Updated:** 2025-05-07T20:52:11Z
- **Labels:** Feature Request, Under Investigation
- **URL:** https://github.com/ROCm/ROCm/issues/3560

### Suggestion Description

From: https://rocm.docs.amd.com/projects/install-on-linux/en/develop/install/rocm-offline-installer.html
>> The host system running the ROCm Offline Installer Creator and the target system running the installer must use the same Linux distribution, release version, and Linux kernel version.

My company has firewall and direct download is banned. We have to download all components from a separate environment (windows) and transfer them manually (to RockyOS). The current offline installer creator requires that the creator matches the target system, and this is not available for us.

Can AMD provide those offline installer as a single file (rpm or tar), like what Nvidia does? CUDA driver/toolkits are packaged as a single installer or tar file per OS/environment, and this simplifies the download/install steps.

### Operating System

RockyOS

### GPU

_No response_

### ROCm Component

_No response_