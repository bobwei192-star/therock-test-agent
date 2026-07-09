# Is it necessary to use AMD proprietary graphcs drivers to install ROCm on Linux?

- **Issue #:** 2457
- **State:** closed
- **Created:** 2023-09-14T23:47:30Z
- **Updated:** 2023-09-15T00:42:49Z
- **URL:** https://github.com/ROCm/ROCm/issues/2457

I was thinking it was required to install the proprietary AMD graphics drivers on Ubuntu in order to use ROCm but then I read [this](https://rocm.docs.amd.com/en/latest/deploy/linux/os-native/install.html) can someone clarify if it's necessary to install the proprietary AMD graphics drivers to use ROCm on Ubuntu Linux?

Is it possible to successfully install ROCm on Ubuntu 22.04.3 LTS jammy and an AMD Radeon RX 5700 XT (navi10, LLVM 15.0.7, DRM 3.49, 6.2.0-32-generic) while keeping the open source graphics drivers? I see there's a list of officially supported GPU on Linux though elsewhere I see instructions for various other AMD GPU's is it just that they're not _officially_ supported?