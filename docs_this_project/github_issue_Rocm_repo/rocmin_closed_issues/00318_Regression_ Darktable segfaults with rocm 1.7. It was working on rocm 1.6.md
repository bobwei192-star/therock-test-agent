# Regression: Darktable segfaults with rocm 1.7. It was working on rocm 1.6.

- **Issue #:** 318
- **State:** closed
- **Created:** 2018-01-30T17:41:09Z
- **Updated:** 2018-03-11T15:42:51Z
- **URL:** https://github.com/ROCm/ROCm/issues/318

Steps to reproduce on Ubuntu 17.10, with rocm 1.7:

1. Make sure you have the rocm ppa in your repository.
2. Uninstall rocm and restore the firmware for amdgpu (work-around for another bug)
`apt remove rocm-dkms rocm-opencl`
`apt autoremove`
`apt install --reinstall linux-firmware`
`reboot`
3. Install darktable and verify that it works:
`apt install darktable`
`darktable`
4. Install rocm afresh
`apt install rocm-dkms rocm-opencl`
`reboot`
5. Start darktable and watch it segfault.
`darktable`
6. If it does not segfault: Go to settings and ensure that OpenCl is available and enabled, then restart darktable.
