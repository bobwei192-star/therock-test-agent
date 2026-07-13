# Hang while running rccl-perf alltoallv with 4 GPus

- **Issue #:** 2554
- **State:** closed
- **Created:** 2023-10-13T21:46:21Z
- **Updated:** 2024-02-02T21:59:51Z
- **Labels:** Under Investigation, 5.7.1, Workaround
- **URL:** https://github.com/ROCm/ROCm/issues/2554

When RCCL is tested on a machine with no XGMI, a hang is observed while running rccl-perf alltoallv with 4 GPus.
As a workaround, set the value of the variable to 2 while running the tests,

NCCL_MAX_P2P_NCHANNELS=2

This issue is under investigation and will be fixed in a future release.
