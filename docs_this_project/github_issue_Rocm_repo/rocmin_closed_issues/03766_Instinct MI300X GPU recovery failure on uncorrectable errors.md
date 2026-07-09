# Instinct MI300X GPU recovery failure on uncorrectable errors

- **Issue #:** 3766
- **State:** closed
- **Created:** 2024-09-20T21:19:48Z
- **Updated:** 2024-09-27T19:24:35Z
- **Labels:** Verified Issue, AMD Instinct MI300X, 6.2.1
- **URL:** https://github.com/ROCm/ROCm/issues/3766

For the AMD Instinct MI300X accelerator, GPU recovery resets triggered by uncorrectable errors (UE) might not complete successfully, which can result in the system being left in an undefined state. A system reboot is needed to recover from this state. Additionally, error logging might fail in these situations, hindering diagnostics.

This issue is under investigation and will be resolved in a future ROCm release.