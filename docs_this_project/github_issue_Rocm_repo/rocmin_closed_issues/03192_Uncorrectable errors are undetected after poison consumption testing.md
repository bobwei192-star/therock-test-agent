# Uncorrectable errors are undetected after poison consumption testing

- **Issue #:** 3192
- **State:** closed
- **Created:** 2024-05-30T18:06:25Z
- **Updated:** 2024-05-31T15:24:06Z
- **Labels:** Verified Issue, AMD Instinct MI300X, 6.1.2
- **URL:** https://github.com/ROCm/ROCm/issues/3192

During poison consumption testing, the injection of uncorrectable errors can fail to generate an interrupt to the driver, resulting in undetected errors. This can result in reliability and recovery issues on MI300X accelerator-based setups.

This issue has been investigated and will be fixed in a future release.