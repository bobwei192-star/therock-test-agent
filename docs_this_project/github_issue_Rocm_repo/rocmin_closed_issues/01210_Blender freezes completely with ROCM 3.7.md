# Blender freezes completely with ROCM 3.7 

- **Issue #:** 1210
- **State:** closed
- **Created:** 2020-09-01T18:06:23Z
- **Updated:** 2021-03-09T12:10:42Z
- **URL:** https://github.com/ROCm/ROCm/issues/1210

Blender freezes completely my whole PC with ROCM 3.7 on Manjaro Linux.

My test file: 
https://cloud.blender.org/p/gallery/5dd6d7044441651fa3decb56

My GPU: 
Vega 56

blender: /mnt/8942b2b9/tmp/pamac-build/hsa-rocr/src/ROCR-Runtime-rocm-3.7.0/src/core/runtime/runtime.cpp:1214: static bool rocr::core::Runtime::VMFaultHandler(hsa_signal_value_t, void*): Assertion `false && "GPU memory access fault."' failed.
zsh: abort (core dumped)  blender --debug


