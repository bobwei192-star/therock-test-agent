# ROCm Compute Profiler CTest failure in CI

- **Issue #:** 4085
- **State:** closed
- **Created:** 2024-12-03T22:19:41Z
- **Updated:** 2025-01-28T20:33:53Z
- **Labels:** Verified Issue, 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4085

When running ROCm Compute Profiler’s (`rocprof-compute`) CTest in the Azure CI environment, the `rocprof-compute` execution test fails. This issue is due to an outdated test file that was not renamed (`omniperf` to `rocprof-compute`), and due to the `ROCM_PATH` environment variable not being set in the Azure CI environment, causing the tool to be unable to extract chip information as expected. This issue will be addressed in a future ROCm release.