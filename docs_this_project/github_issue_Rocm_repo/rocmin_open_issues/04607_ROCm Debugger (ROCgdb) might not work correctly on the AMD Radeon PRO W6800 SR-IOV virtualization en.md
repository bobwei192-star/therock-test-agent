# ROCm Debugger (ROCgdb) might not work correctly on the AMD Radeon PRO W6800 SR-IOV virtualization environment

- **Issue #:** 4607
- **State:** open
- **Created:** 2025-04-11T23:13:15Z
- **Updated:** 2025-04-11T23:13:15Z
- **Labels:** Verified Issue, ROCm 6.4.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4607

The ROCm Debugger (ROCgdb) component needs access to some registers to fetch debugging information. These registers are blocked in the AMD Radeon PRO W6800 SR-IOV virtualization environment, resulting in the ROCm Debugger (ROCgdb) being non-functional. The issue is due to the limitation in the virtualization environment and isn't specific to ROCm. Further investigation is in progress.