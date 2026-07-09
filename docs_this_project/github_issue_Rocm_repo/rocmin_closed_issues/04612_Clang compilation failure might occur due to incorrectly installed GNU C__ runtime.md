# Clang compilation failure might occur due to incorrectly installed GNU C++ runtime

- **Issue #:** 4612
- **State:** closed
- **Created:** 2025-04-11T23:17:29Z
- **Updated:** 2025-10-30T18:18:13Z
- **Labels:** Verified Issue, ROCm 6.4.0
- **Assignees:** prbasyal-amd
- **URL:** https://github.com/ROCm/ROCm/issues/4612

Clang compilation failure with the error `fatal error: 'cmath' file not found` might occur if the GNU C++ runtime is not installed correctly. The error indicates that the `libstdc++-dev` package, compatible with the latest installed GNU Compiler Collection (GCC) version, is missing. This issue is a result of Clang being unable to find the newest GNU C++ runtimes it recognizes and the associated header files. As a workaround, install the `libstdc++-dev` package compatible with the installed GCC version.