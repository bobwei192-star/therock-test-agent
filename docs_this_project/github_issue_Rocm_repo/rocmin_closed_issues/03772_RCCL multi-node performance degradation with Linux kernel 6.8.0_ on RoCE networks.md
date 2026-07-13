# RCCL multi-node performance degradation with Linux kernel 6.8.0+ on RoCE networks

- **Issue #:** 3772
- **State:** closed
- **Created:** 2024-09-20T23:04:52Z
- **Updated:** 2024-12-03T23:35:21Z
- **Labels:** Verified Issue, 6.2.0, 6.2.1
- **URL:** https://github.com/ROCm/ROCm/issues/3772

On systems running Linux kernel 6.8.0, such as Ubuntu 24.04, Direct Memory Access (DMA) transfers between the GPU and NIC are disabled and impacts multi-node RCCL performance.
 
This issue was reproduced with RCCL 2.20.5 (ROCm 6.2.0 and 6.2.1) on systems with Broadcom Thor-2 NICs and affects other systems with RoCE networks using Linux 6.8.0 or newer. Older RCCL versions are also impacted.
 
This issue will be addressed in a future ROCm release.