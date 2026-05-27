# udev rule for kernel versioning - case kver (or not) then do

> **Issue #581**
> **状态**: closed
> **创建时间**: 2018-10-17T19:13:34Z
> **更新时间**: 2021-01-07T09:45:52Z
> **关闭时间**: 2021-01-07T09:45:52Z
> **作者**: BobDodds
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/581

## 描述

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

---

## 评论 (2 条)

### 评论 #1 — jlgreathouse (2018-10-25T01:06:30Z)

Tried this on Ubuntu 18.10, and here's some small modifications that appear to work for me to allow the use of upstream kernel.
```
# Install into /lib/udev/rules.d/50-rocm-or-not.rules
# "To try ROCm with an upstream kernel, install ROCm as normal,
#  but do not install the rock-dkms package. Also add a udev rule
#  to control /dev/kfd permissions:"
# See https://github.com/RadeonOpenCompute/ROCm/issues/581
IMPORT{cmdline}="BOOT_IMAGE"
ENV{BOOT_IMAGE}=="\*4.1[789].\*", GOTO="go_rocm"
SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video", MODE="0666"
LABEL="go_rocm"
```

---

### 评论 #2 — ROCmSupport (2021-01-07T09:45:52Z)

> 
> 
> Tried this on Ubuntu 18.10, and here's some small modifications that appear to work for me to allow the use of upstream kernel.
> 
> ```
> # Install into /lib/udev/rules.d/50-rocm-or-not.rules
> # "To try ROCm with an upstream kernel, install ROCm as normal,
> #  but do not install the rock-dkms package. Also add a udev rule
> #  to control /dev/kfd permissions:"
> # See https://github.com/RadeonOpenCompute/ROCm/issues/581
> IMPORT{cmdline}="BOOT_IMAGE"
> ENV{BOOT_IMAGE}=="\*4.1[789].\*", GOTO="go_rocm"
> SUBSYSTEM=="kfd", KERNEL=="kfd", TAG+="uaccess", GROUP="video", MODE="0666"
> LABEL="go_rocm"
> ```

Fixed with this.
Closing this now.

---
