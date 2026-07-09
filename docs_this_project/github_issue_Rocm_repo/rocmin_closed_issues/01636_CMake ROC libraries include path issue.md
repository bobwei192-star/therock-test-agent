# CMake ROC libraries include path issue

- **Issue #:** 1636
- **State:** closed
- **Created:** 2021-12-11T18:32:11Z
- **Updated:** 2024-02-21T23:18:01Z
- **Assignees:** pfultz2, lawruble13, dennyiriawan, TorreZuk, saadrahim, eidenyoshida, frepaul
- **URL:** https://github.com/ROCm/ROCm/issues/1636

hipblas, hipsparse, rocblas, rocsolver, rocprim, rocthrust all have a similar pattern.
hip runtime library is the only one get this right.

roc::hipblas target INTERFACE_INCLUDE_PATH is `/opt/rocm-4.5.0/include`
This is OK for people who only use ROCM installation but really bad for development.
I'm currently using AOMP which provides Clang and HIP but not hipblas.
Pulling `/opt/rocm-4.5.0/include` just pollutes all my include paths.

`/opt/rocm-4.5.0/lib/cmake/hipblas/hipblas-targets.cmake` has the following line.
```
# Compute the installation prefix relative to this file.
get_filename_component(_IMPORT_PREFIX "${CMAKE_CURRENT_LIST_FILE}" PATH)
get_filename_component(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
get_filename_component(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
get_filename_component(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
get_filename_component(_IMPORT_PREFIX "${_IMPORT_PREFIX}" PATH)
```
It goes four level up to get the ROCM root.

Instead the HIP runtime library got this right. In ``
```
get_filename_component(_DIR "${CMAKE_CURRENT_LIST_DIR}" REALPATH)
get_filename_component(_IMPORT_PREFIX "${_DIR}/../../../" REALPATH)
```
so use REALPATH to resolve softlinks and use three level up to locate the HIP root directory instead of the ROC directory.

It is better to have all the affected libraries to adopt the same scheme and get contained in its own folder not pulling the ROCM folder. This should help composability.
