# Get UUID from HIP API level device

- **Issue #:** 1642
- **State:** closed
- **Created:** 2021-12-17T08:48:19Z
- **Updated:** 2023-06-07T16:06:54Z
- **URL:** https://github.com/ROCm/ROCm/issues/1642

Is there a way, to get the UUID of a device from the HIP API? I can see the UUID of devices with `rocm-smi --showuniqueid` and also with `rocminfo`. But I would like to relate them, without considering `HIP_VISIBLE_DEVICES`.