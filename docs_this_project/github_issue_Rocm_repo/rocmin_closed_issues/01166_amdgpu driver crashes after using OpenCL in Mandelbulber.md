# amdgpu driver crashes after using OpenCL in Mandelbulber

- **Issue #:** 1166
- **State:** closed
- **Created:** 2020-06-25T12:08:43Z
- **Updated:** 2020-12-17T04:36:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/1166

Please see this issue for reference:
https://github.com/buddhi1980/mandelbulber2/issues/663

When rendering reflective or transparent images using ROCm's OpenCL implementation, the amdgpu Linux kernel driver crashes.
This leaves the desktop unusable - "X is wedged". In my case, I saw heavy graphical artifacts, a crashed KDE session and the desktop left in an unresponsive state.

Multiple users reported this issue with at least these cards:
AMD Radeon RX 580
AMD Radeon RX 570