# Scrub for references to HCC in documentation

- **Issue #:** 1954
- **State:** closed
- **Created:** 2023-03-16T14:00:48Z
- **Updated:** 2025-05-30T15:38:59Z
- **Labels:** Documentation
- **URL:** https://github.com/ROCm/ROCm/issues/1954

> on HCC hipMemcpyAsync does not support overlapped H2D and D2H copies. For hipMemcpy, the copy is always performed by the device associated with the specified stream.

https://github.com/ROCm-Developer-Tools/HIP/blob/develop/include/hip/hip_runtime_api.h#L3754

My read is that there is already on-going efforts to remove, but just a heads-up.

cc: @saadrahim 