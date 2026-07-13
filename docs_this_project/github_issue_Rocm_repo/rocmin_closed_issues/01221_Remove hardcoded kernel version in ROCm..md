# Remove hardcoded kernel version in ROCm. 

- **Issue #:** 1221
- **State:** closed
- **Created:** 2020-09-17T21:48:35Z
- **Updated:** 2021-01-06T13:53:31Z
- **URL:** https://github.com/ROCm/ROCm/issues/1221

While compiling ROCm for Ubuntu 20.04 I see a couple of places where the kernel version has been hardcoded. It may be better for a script to detect the kernel version and inject it in these places. Specifically, 3.6.0 is assumed in:

1. ROCK-Kernel-Driver/include/config/kernel.release 
2. ROCK-Kernel-Driver/include/config/auto.conf.cmd

files. 