# Segmentation fault in ROCprofiler-SDK due to ABI mismatch affecting std::regex

- **Issue #:** 5343
- **State:** closed
- **Created:** 2025-09-16T15:38:31Z
- **Updated:** 2025-10-30T18:17:29Z
- **Labels:** Verified Issue, ROCm 7.0.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/5343

Starting with GCC 5.1, GNU `libstdc++` introduced a dual Application Binary Interface (ABI) to adopt `C++11`, primarily affecting the `std::string` and its dependencies, including `std::regex`. If your code is compiled against headers expecting one ABI but linked or run with the other, it can cause problems with `std::string` and `std::regex`, leading to a segmentation fault in ROCprofiler-SDK, which uses `std::regex`. This issue is resolved in the [ROCm Systems `develop` branch](https://github.com/ROCm/rocm-systems) and will be part of a future ROCm release.