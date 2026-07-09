# OpenCL not initialized without a monitor

- **Issue #:** 907
- **State:** closed
- **Created:** 2019-10-13T02:03:54Z
- **Updated:** 2021-05-09T19:48:50Z
- **URL:** https://github.com/ROCm/ROCm/issues/907

Using latest ROCm (2.9), Ubuntu 19.10, Linux kernel 5.4.0-rc2, GPUs 2x Radeon VII.
When I boot without any monitor connected:
- the ROCm stack is OK, GPUs detected correctly, rocm-smi works fine, sees both GPUs
- but OpenCL is not initialized, clinfo reports 0 devices.

As soon as a monitor is attached, OpenCL start working correctly, clinfo correctly reports all the devices (without reboot). This are the additional entries that appear in dmesg on monitor being connected:
[   91.028230] [drm] fb mappable at 0xC0785000
[   91.028231] [drm] vram apper at 0xC0000000
[   91.028231] [drm] size 16384000
[   91.028231] [drm] fb depth is 24
[   91.028232] [drm]    pitch is 10240
[   91.028321] fbcon: amdgpudrmfb (fb0) is primary device
[   91.073250] Console: switching to colour frame buffer device 160x50
[   91.087170] amdgpu 0000:06:00.0: fb0: amdgpudrmfb frame buffer device

After this, clinfo reports 2 devices (correct).

Expected behavior: OpenCL does not require a monitor being connected to initialize (similarly to the rest of the ROCm stack, that works fine without a monitor).
