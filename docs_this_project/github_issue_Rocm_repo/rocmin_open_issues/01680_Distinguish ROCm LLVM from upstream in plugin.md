# Distinguish ROCm LLVM from upstream in plugin

- **Issue #:** 1680
- **State:** open
- **Created:** 2022-02-16T14:25:41Z
- **Updated:** 2024-10-24T19:36:57Z
- **Labels:** Under Investigation
- **Assignees:** searlmc1
- **URL:** https://github.com/ROCm/ROCm/issues/1680

Hi,
hipSYCL builds a Clang and LLVM plugin to support SYCL on top of HIP but also upstream Clang.
We currently have multiple issues where providing compatibility with both, upstream and ROCm Clang releases, results in having to specify explicit workaround macros while building the plugin for ROCm Clang (https://github.com/illuhad/hipSYCL/pull/702, https://github.com/illuhad/hipSYCL/issues/709).

This is due to ROCm Clang providing the `LLVM_VERSION_MAJOR` (and friends) value of upstream Clang at the time of the last pull, which usually is the version of the next release already. It is however not (easily) possible to determine at buildtime at which point this was and which APIs have already or not been changed in ROCm Clang, that are changed in the corresponding released LLVM version.

E.g. LLVM 14 is not yet released, ROCm 5.0 is released, but already provides `LLVM_VERSION_MAJOR==14` and thus building the Clang plugin expects the `release/14.x` branch's API state. But ROCm 5.0's LLVM still provides comparatively old APIs (e.g. https://github.com/llvm/llvm-project/commit/1d8750c3dad432bf01f708eb2e67a6e18757c379 is not included yet).

So is there any version macro defined in the ROCm LLVM headers that we can use to add another bunch of compatibility `#ifdef`s explicitly for ROCm versions? I.e. is there a `ROCM_LLVM_VERSION_MAJOR 5` (and friends) that we haven't found yet, but could use? Do you have any other recommended way of detecting ROCm LLVM's exact version at plugin compile time?

Apart from the issue-related work-around macros, another worst-case option for us would be either requiring the user to set a `-DROCM_LLVM_VERSION=050000` macro or similar at build time or detecting that ourselves using CMake.

I hope you can help us find better ways to deal with this and if not fix this for the future.
Thanks!

cc @illuhad