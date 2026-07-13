# Failure to use –kokkos-trace option in ROCm Compute Profiler

- **Issue #:** 4604
- **State:** closed
- **Created:** 2025-04-11T23:11:09Z
- **Updated:** 2025-09-16T17:38:21Z
- **Labels:** Verified Issue, ROCm 6.4.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4604

In ROCm 6.4.0, it’s not recommended to use the `--kokkos-trace` option. `--kokkos-trace` has been partially implemented in the `rocprofv3` tool, resulting in a difference between the output of `--kokkos-trace` and the `counter_collection.csv` output file. The program will exit with a warning message if the `-kokkos-trace` option is detected in the ROCm Compute Profiler. The issue will be addressed in a future ROCm release.