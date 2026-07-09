# llvm-project in 4.0.0 no longer builds

- **Issue #:** 1364
- **State:** closed
- **Created:** 2021-01-21T21:15:53Z
- **Updated:** 2021-02-01T07:06:28Z
- **URL:** https://github.com/ROCm/ROCm/issues/1364

This is for sub-project: https://github.com/RadeonOpenCompute/llvm-project but in there, there is no issue tab so I opened here in ROCm project. The same instruction to generate make files using cmake in 3.8 version is no longer working in 4.0.0 and instruction still the same:

From https://github.com/RadeonOpenCompute/llvm-project, section Getting Started with the LLVM System-> Getting the Source Code and Building LLVM:
it says:
Configure and build LLVM and Clang:
cd llvm-project
mkdir build
cd build
cmake -G <generator> [options] ../llvm

actual command failed with "Unix Makefiles" option:

root@sriov-guest:~/ROCm/llvm-project/build# cmake -G "Unix Makefiles"  ../llvm                                                                  CMake Error: The source directory "/root/ROCm/llvm-project/llvm" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.

cmake -G "Unix Makefiles" -DCMAKE_INSTALL_PREFIX=/opt/rocm-4.0.0/llvm/ -DCMAKE_BUILD_TYPE=Release -DLLVM_ENABLE_PROJECTS="clang;lld;lldb;clang-tools-extra;compiler-rt" ../llvm
CMake Error: The source directory "/root/ROCm/llvm-project/llvm" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.

