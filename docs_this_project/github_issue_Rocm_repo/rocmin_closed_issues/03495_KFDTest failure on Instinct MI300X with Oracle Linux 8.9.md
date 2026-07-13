# KFDTest failure on Instinct MI300X with Oracle Linux 8.9

- **Issue #:** 3495
- **State:** closed
- **Created:** 2024-08-02T18:27:18Z
- **Updated:** 2024-12-10T14:47:04Z
- **Labels:** Verified Issue, AMD Instinct MI300X, 6.2.0
- **URL:** https://github.com/ROCm/ROCm/issues/3495

The `KFDEvictTest.QueueTest` is failing on the MI300X platform during KFD (Kernel Fusion Driver) tests, causing the full suite to not execute properly. This issue is suspected to be hardware-related.