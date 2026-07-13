# udev rule for kernel versioning - case kver (or not) then do

- **Issue #:** 581
- **State:** closed
- **Created:** 2018-10-17T19:13:34Z
- **Updated:** 2021-01-07T09:45:52Z
- **URL:** https://github.com/ROCm/ROCm/issues/581

We could take some responsibility, faq:

```
# /etc/udev/rules.d/00-rocm-or-not
# "To try ROCm with an upstream kernel, install ROCm as normal,
#  but do not install the rock-dkms package. Also add a udev rule
#  to control /dev/kfd permissions:"
IMPORT{cmdline}="BOOT_IMAGE"
ENV{BOOT_IMAGE}=="\*4.1[234567].\*", GOTO="go_rocm"
SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video"
LABEL="go_rocm"
# https://github.com/RadeonOpenCompute/ROCm/issues/581
```