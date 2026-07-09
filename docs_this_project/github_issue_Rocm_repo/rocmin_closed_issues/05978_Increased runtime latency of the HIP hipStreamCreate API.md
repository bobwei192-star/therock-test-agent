# Increased runtime latency of the HIP hipStreamCreate API

- **Issue #:** 5978
- **State:** closed
- **Created:** 2026-02-18T15:07:52Z
- **Updated:** 2026-03-25T23:49:47Z
- **Labels:** Verified Issue, ROCm 7.2.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5978

Doubling of runtime latency of the [HIP](https://rocmdocs.amd.com/projects/HIP/en/latest/doxygen/html/group___stream.html) `hipStreamCreate` API might be observed. While this affects RCCL `all_reduce_perf` tests, it has minimal impact on real production workloads. No slowdowns have been observed in other common benchmarks, including PyTorch, vLLM, and other application‑level tests. The issue is currently under investigation and will be fixed in an upcoming ROCm release. 