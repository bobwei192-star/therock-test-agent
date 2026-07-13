# ROCm Compute Profiler post-upgrade issues

- **Issue #:** 4082
- **State:** closed
- **Created:** 2024-12-03T22:19:32Z
- **Updated:** 2025-03-16T07:14:10Z
- **Labels:** Verified Issue, 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4082

In ROCm 6.3.0, the omniperf package is now named rocprofiler-compute. As a result, running `apt install omniperf` will fail to locate the package. Instead, use `apt install rocprofiler-compute`. See [ROCm Compute Profiler 3.0.0](https://rocm-stg.amd.com/en/latest/about/release-notes.html#rocm-compute-profiler-3-0-0).

When upgrading from ROCm 6.2 to 6.3, any existing `/opt/rocm-6.2/../omniperf` folders are not automatically removed. To clean up these folders, manually uninstall Omniperf using `apt remove omniperf`.