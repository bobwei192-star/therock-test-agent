# [Feature]: Shrink rocm-llvm distribution packages by not statically linking libLLVM, libclang-cpp etc.

- **Issue #:** 2703
- **State:** closed
- **Created:** 2023-12-11T02:21:32Z
- **Updated:** 2024-04-17T05:01:17Z
- **Assignees:** lamb-j
- **URL:** https://github.com/ROCm/ROCm/issues/2703

### Suggestion Description

For the various supported systems, the `rocm-llvm` rpm/deb packages are about 1GB of total download size and about 4GB in installation size. The main reason for this seems to be that all `llvm` binaries were statically linked with `libLLVM`, `libclang-cpp` and so on. That means multiple binaries all have their own copy of `libLLVM` (~130MB), `libclang-cpp` (~50MB). It also seems they contain superfluous symbols, since they shrink a bit when applying `strip` on them. The installation also includes static libraries used for linking to llvm/clang libraries.

This makes downloading and installing the ROCm stack unnecessarily cumbersome, specifically when building base containers for development.

Is there a technical reason for the static linking of LLVM? If not, the suggestion would be to make the installation use shared libraries and appropriate RPATHs instead. Debug symbols and static libraries, if needed, should be moved into something like `rocm-llvm-dev` and not be part of the `rocm` use case in the installer.

### Operating System

_No response_

### GPU

_No response_

### ROCm Component

rocm-llvm