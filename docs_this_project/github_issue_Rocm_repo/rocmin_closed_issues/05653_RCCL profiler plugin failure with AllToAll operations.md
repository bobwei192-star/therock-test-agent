# RCCL profiler plugin failure with AllToAll operations

- **Issue #:** 5653
- **State:** closed
- **Created:** 2025-11-11T21:41:52Z
- **Updated:** 2025-11-27T15:04:06Z
- **Labels:** Verified Issue, ROCm 7.1.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5653

The RCCL profiler plugin `librccl-profiler.so` might fail with a segmentation fault during `AllToAll` collective operations due to improperly assigned point-to-point task function pointers. This leads to invalid memory access and prevents profiling of `AllToAll` performance. Other operations, like `AllReduce`, are unaffected. It's recommended to avoid using the RCCL profiler plugin with `AllToAll` operations until the fix is available. This issue is resolved in the [RCCL `develop` branch](https://github.com/ROCm/rccl/tree/develop) and will be part of a future ROCm release.