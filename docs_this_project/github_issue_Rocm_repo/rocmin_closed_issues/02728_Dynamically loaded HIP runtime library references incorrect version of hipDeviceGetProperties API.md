# Dynamically loaded HIP runtime library references incorrect version of hipDeviceGetProperties API

- **Issue #:** 2728
- **State:** closed
- **Created:** 2023-12-15T21:46:14Z
- **Updated:** 2024-09-09T19:37:55Z
- **Labels:** Under Investigation, Verified Issue, 6.0.0
- **URL:** https://github.com/ROCm/ROCm/issues/2728

When an application loads the HIP runtime library dynamically from ROCm 6.0 and attempts to use hipDeviceGetProperties, the application incorrectly uses the hipDeviceGetProperties API from a previous ROCm release instead of the newer ROCm 6.0 implementation.

The issue will be fixed in a future release.
