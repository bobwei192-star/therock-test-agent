# Add HIP-Language support to "Using CMake" page

- **Issue #:** 1957
- **State:** closed
- **Created:** 2023-03-16T14:26:37Z
- **Updated:** 2023-05-17T13:07:24Z
- **Labels:** Documentation
- **Assignees:** pfultz2, cgmb, skyreflectedinmirrors, lawruble13, MathiasMagnus, nunnikri
- **URL:** https://github.com/ROCm/ROCm/issues/1957

Main points are:

- Requires CMake >= 3.21
- CMAKE_HIP_COMPILER=clang++ (in place of CMAKE_CXX_COMPILER=hipcc)
- Suffix of HIP files is '.hip', or use `source_files_properties` + `LANGUAGE hip` (https://cmake.org/cmake/help/latest/command/set_source_files_properties.html)
- Brief discussion of hip-lang:: targets

I can help contribute here, @saadrahim 