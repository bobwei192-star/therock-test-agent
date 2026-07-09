# rocminfo error Unable to open /dev/kfd read-write Failed to get user name to check for video group membership

- **Issue #:** 1174
- **State:** closed
- **Created:** 2020-07-03T19:17:02Z
- **Updated:** 2021-01-28T11:09:02Z
- **URL:** https://github.com/ROCm/ROCm/issues/1174

my system - Linux shreyash-Nitro-AN515-42 4.15.0-99-generic #100~16.04.1-Ubuntu SMP Wed Apr 22 23:56:30 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
acer nitro 5 ryzen 5 
processor - AMD Ryzen 5 2500U with Radeon Vega Mobile Gfx × 8 
graphics - AMD RAVEN (DRM 3.36.0 / 4.15.0-99-generic, LLVM 6.0.0) in all setting-> details
                 amd radeon rx560x real hardware from manufacturer, are these same or not

(base) shreyash@shreyash-Nitro-AN515-42:~$ /opt/rocm/bin/rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
Failed to get user name to check for video group membership
hsa api call failure at: /src/rocminfo/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.

(base) shreyash@shreyash-Nitro-AN515-42:~$ groups
shreyash adm cdrom sudo dip video plugdev lpadmin sambashare




