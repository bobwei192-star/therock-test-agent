# ROCgdb might fail on SR-IOV guest VMs

- **Issue #:** 5607
- **State:** open
- **Created:** 2025-10-31T18:00:12Z
- **Updated:** 2025-10-31T18:00:28Z
- **Labels:** Verified Issue, ROCm 7.1.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5607

ROCgdb might fail when running the `step-schedlock-spurious-waves.exp` test case on SR-IOV guest virtual machines (VMs). As a workaround, avoid running an inferior in ROCgdb if a background process is already heavily utilizing the GPU. The issue is currently under investigation and will be fixed in a future ROCm release.