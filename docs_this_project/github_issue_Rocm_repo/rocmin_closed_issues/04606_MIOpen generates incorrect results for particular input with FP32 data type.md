# MIOpen generates incorrect results for particular input with FP32 data type

- **Issue #:** 4606
- **State:** closed
- **Created:** 2025-04-11T23:12:30Z
- **Updated:** 2025-07-21T20:48:13Z
- **Labels:** Verified Issue, ROCm 6.4.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4606

In ROCm 6.4.0, MIOpen generates incorrect results on the `conv2dbackward` function for a particular input with 32-bit floating point (FP32) data types. The issue is only specific to FP32 data types with 2 * 2 kernel size and dilation 2 * 1. As a workaround, change the data type from FP32 to FP16. The issue will be addressed in a future ROCm release.