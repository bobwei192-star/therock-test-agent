# GFX Freq information is unavailable in the rocm-smi when running in SRIOV mode enabled on MI210

- **Issue #:** 4603
- **State:** open
- **Created:** 2025-04-11T23:09:59Z
- **Updated:** 2025-04-11T23:09:59Z
- **Labels:** Verified Issue, ROCm 6.4.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4603

In ROCm 6.4.0, you cannot see the GFX Freq information in the guest VM. In SRIOV mode, the AMD Platform Management Firmware (PMFW) does not share the graphics frequency information with the guest VMs and is only available to Host systems. This issue will be addressed in a future ROCm release.