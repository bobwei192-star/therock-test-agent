# Incorrect Returns for hipSetDevice and hipSetDeviceFlags APIs

- **Issue #:** 2288
- **State:** closed
- **Created:** 2023-06-28T22:00:43Z
- **Updated:** 2024-03-18T15:48:34Z
- **Labels:** Under Investigation, Verified Issue, 5.6.0
- **URL:** https://github.com/ROCm/ROCm/issues/2288

hipSetDevice and hipSetDeviceFlags APIs return hipErrorInvalidDevice instead of hipErrorNoDevice on a system without a GPU.

This issue is under investigation and will be fixed in a future release.