# reduced number of registers per thread in ROCm 4.1

- **Issue #:** 1442
- **State:** closed
- **Created:** 2021-04-06T10:17:21Z
- **Updated:** 2021-04-13T12:01:04Z
- **URL:** https://github.com/ROCm/ROCm/issues/1442

from https://github.com/RadeonOpenCompute/ROCm/issues/1380

ROCm 4.0 had an issue - hipDeviceAttributeMaxThreadsPerBlock was reporting 1024 even when the ROCm was configured with 256 max threads. It seems that in ROCm 4.1 it was also increased to 1024, but this reduced the number of registers a thread can use before spilling to global memory (https://rocmdocs.amd.com/en/latest/Current_Release_Notes/Current-Release-Notes.html). 

Some of my kernels at VkFFT experience a drop in performance from this, so I wanted to ask if it is possible to provide the exact value of registers per thread I need at compile-time to avoid the spilling in HIPRTC? launch_bounds doesn't seem to have any impact in HIPRTC.

Thank you!
Best regards,
Dmitrii