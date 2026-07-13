# ROCm libraries install test binaries, which is not desired for distribution packaging

- **Issue #:** 1905
- **State:** closed
- **Created:** 2023-02-12T04:00:03Z
- **Updated:** 2024-02-23T23:04:38Z
- **Assignees:** cgmb, TorreZuk
- **URL:** https://github.com/ROCm/ROCm/issues/1905

Take rocBLAS as example

https://github.com/ROCmSoftwarePlatform/rocBLAS/blob/56c25c239782ce09b0445d794d183323af3ce963/clients/gtest/CMakeLists.txt#L220-L221

installs rocblas-test and test data into `<prefix>/bin`. Usually testing is executed after build and before install, and test binaries are not installed to the final location. Please consider adding an cmake option to turn off installing testing files. This also applies to other packages under https://github.com/ROCmSoftwarePlatform