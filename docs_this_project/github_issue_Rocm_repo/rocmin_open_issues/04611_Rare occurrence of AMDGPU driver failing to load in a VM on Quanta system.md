# Rare occurrence of AMDGPU driver failing to load in a VM on Quanta system

- **Issue #:** 4611
- **State:** open
- **Created:** 2025-04-11T23:16:40Z
- **Updated:** 2025-04-11T23:16:40Z
- **Labels:** Verified Issue, ROCm 6.4.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4611

In a rare occurrence (1 in 500 reboots), the guest kernel might display the call trace due to the AMDGPU driver failing to load in a repeated power cycle virtual machine (VM) on a Quanta system. This issue will limit you from using the AMD GPUs in the guest kernel. As a workaround, reboot the VM to avoid the failure.