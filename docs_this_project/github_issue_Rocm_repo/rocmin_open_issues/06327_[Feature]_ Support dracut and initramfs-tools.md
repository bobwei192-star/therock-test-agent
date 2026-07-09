# [Feature]: Support dracut and initramfs-tools

- **Issue #:** 6327
- **State:** open
- **Created:** 2026-06-03T09:33:10Z
- **Updated:** 2026-06-09T05:43:05Z
- **URL:** https://github.com/ROCm/ROCm/issues/6327

### Suggestion Description

## Summary

The `amdgpu-dkms` Debian package currently hard-depends on `initramfs-tools` and uses `update-initramfs` in its maintainer scripts. This prevents clean installation on systems using **dracut** as their initramfs generator.

## What is dracut?

[dracut](https://github.com/dracutdevs/dracut) is an initramfs infrastructure used by Fedora, RHEL, openSUSE, and optionally on Debian/Ubuntu. It is a modern alternative to `initramfs-tools`.

## Why support it?

Users running custom kernels, immutable distributions, or Debian systems with `dracut` installed cannot install `amdgpu-dkms` without either switching initramfs generators or manually hacking the package. Adding `dracut` support makes the package work out-of-the-box on a broader range of systems.

## Proposed solution

The attached patch (`amdgpu-dkms-dracut-support.patch`) adds dual support:

- **`Depends:`** accepts `initramfs-tools | dracut` as an alternative dependency.
- **`postinst`/`postrm`**: detects which tool is available and calls the appropriate one (`update-initramfs` or `dracut --force --kver`).
- **`prerm`**: cleans up the dynamically installed initramfs-tools hook (unchanged logic for dracut, since dpkg handles the file).

### Hook installation difference

The `initramfs-tools` hook is installed dynamically in `postinst` (as in the original package) because AMD ships it inside the `DEBIAN/` directory.  
The `dracut` module is shipped as a regular package file under `/usr/lib/dracut/modules.d/90amdgpu-firmware/module-setup.sh`. This lets `dpkg` manage it automatically—no manual `cp`/`rm` in maintainer scripts is needed, which is cleaner and follows Debian best practices. Feel free to change this approach if AMD prefers a different layout.

### Additional fix

The patch also corrects a copy-paste error in `postrm` where the wrong script name was printed in the error message (`postinst` → `postrm`).

[amdgpu-dkms-dracut-support.patch](https://github.com/user-attachments/files/28544869/amdgpu-dkms-dracut-support.patch)

### Operating System

Debian and all based on it

### GPU

all

### ROCm Component

_No response_