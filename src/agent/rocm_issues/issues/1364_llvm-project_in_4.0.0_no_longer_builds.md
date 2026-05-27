# llvm-project in 4.0.0 no longer builds

> **Issue #1364**
> **状态**: closed
> **创建时间**: 2021-01-21T21:15:53Z
> **更新时间**: 2021-02-01T07:06:28Z
> **关闭时间**: 2021-02-01T07:06:28Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1364

## 描述

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



---

## 评论 (4 条)

### 评论 #1 — xuhuisheng (2021-01-22T00:25:11Z)

In my ubuntu-20.04.1, I can build llvm-project successfully, using the `cmake ../llvm` similarily scripts.
The source of llvm-project is got by repo.

Could you check if there is CMakeLists.txt file in llvm directory?

---

### 评论 #2 — ROCmSupport (2021-01-25T07:03:37Z)

@gggh000 , 
       As @xuhuisheng  pointed out, we are successfully able to build. Request you to kindly sync your code once more & check.
       If you are still face the problem do let us know with the logs of your commands


---

### 评论 #3 — ROCmSupport (2021-01-27T10:34:05Z)

Hi @gggh000 
Can you please share some progress/update on this.
Request you to close this issue, if not reproducible.
Thank you.

---

### 评论 #4 — ROCmSupport (2021-02-01T07:06:28Z)

No response from user as per previous comments.
Hope issue is fixed.
Request you to file a new issue, if you observe any.
Thank you.

---
