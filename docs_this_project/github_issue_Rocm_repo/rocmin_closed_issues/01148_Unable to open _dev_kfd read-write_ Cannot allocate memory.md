# Unable to open /dev/kfd read-write: Cannot allocate memory

- **Issue #:** 1148
- **State:** closed
- **Created:** 2020-06-15T08:17:26Z
- **Updated:** 2024-01-27T20:12:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/1148

My OS is Arch Linux.
My PC is Xeon E5-2689, 32GB of RAM and RX570 8GB.

> $ sudo rocminfo
ROCk module is loaded
Unable to open /dev/kfd read-write: Cannot allocate memory
tolyprog is member of render group
hsa api call failure at: /home/tolyprog/.cache/yay/rocminfo/src/rocminfo-rocm-3.5.0/rocminfo.cc:1142
Call returned HSA_STATUS_ERROR_OUT_OF_RESOURCES: The runtime failed to allocate the necessary resources. This error may also occur when the core runtime library needs to spawn threads or create internal OS-specific events.