# RCCL - MSCCL initialization failure

- **Issue #:** 4769
- **State:** open
- **Created:** 2025-05-21T18:45:58Z
- **Updated:** 2025-05-21T18:47:12Z
- **Labels:** Verified Issue, ROCm 6.4.1
- **URL:** https://github.com/ROCm/ROCm/issues/4769

When splitting a communicator using `ncclCommSplit` in some GPU configurations, MSCCL initialization can cause a segmentation fault. The recommended workaround is to disable MSCCL with `export RCCL_MSCCL_ENABLE=0`. This issue will be fixed in a future ROCm release.