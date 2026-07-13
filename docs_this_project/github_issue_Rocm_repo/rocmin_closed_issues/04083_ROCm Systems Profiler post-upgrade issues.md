# ROCm Systems Profiler post-upgrade issues

- **Issue #:** 4083
- **State:** closed
- **Created:** 2024-12-03T22:19:33Z
- **Updated:** 2024-12-20T23:09:18Z
- **Labels:** Verified Issue, 6.3.0
- **URL:** https://github.com/ROCm/ROCm/issues/4083

In ROCm 6.3.0, the `omnitrace` package is now named `rocprofiler-systems`. As a result, running `apt install omnitrace` will fail to locate the package. Instead, use `apt install rocprofiler-systems`. See [ROCm Systems Profiler 0.1.0](https://rocm-stg.amd.com/en/latest/about/release-notes.html#rocm-systems-profiler-0-1-0).

When upgrading from ROCm 6.2 to 6.3, any existing `/opt/rocm-6.2/../omnitrace` folders are not automatically removed. To clean up these folders, manually uninstall Omnitrace using `apt remove omnitrace`.