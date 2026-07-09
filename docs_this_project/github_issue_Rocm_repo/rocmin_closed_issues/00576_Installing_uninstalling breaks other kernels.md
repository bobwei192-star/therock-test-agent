# Installing/uninstalling breaks other kernels

- **Issue #:** 576
- **State:** closed
- **Created:** 2018-10-06T20:23:25Z
- **Updated:** 2021-01-07T09:56:49Z
- **URL:** https://github.com/ROCm/ROCm/issues/576

I have encountered a strange issue, I am on Fedora 28 and I wanted to try out ROCm.  So I installed the 4.19.0-rc6 mainline kernel, and installed rocm from the Centos repos.  But I encountered the *Updating firmware may not trigger a rebuilding of ramfs* issue mentioned in the [install FAQ](https://rocm.github.io/install_issues.html). I eventually uninstalled the kernel and rocm, however now my older kernels also have the same problem!

I have tried reinstalling the old kernels, regenerating the initramfs as recommended by the FAQ, reinstalled the firmware and tried regenerating the initramfs again, nothing seems to help.  Any thoughts what I can do?  