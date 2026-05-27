# [CMake] troublesome libclang_rt.builtins-x86_64.a

> **Issue #1717**
> **状态**: closed
> **创建时间**: 2022-03-31T04:36:34Z
> **更新时间**: 2022-07-06T16:38:51Z
> **关闭时间**: 2022-07-06T16:38:51Z
> **作者**: ye-luo
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1717

## 描述

libclang_rt.builtins-x86_64.a got pulled in by 
```
/opt/rocm/lib/cmake$ grep -R CLANGRT_BUILTINS 
hip-lang/hip-lang-config.cmake:find_library(CLANGRT_BUILTINS
hip-lang/hip-lang-config.cmake:if(CLANGRT_BUILTINS-NOTFOUND)
hip-lang/hip-lang-config.cmake:    INTERFACE_LINK_LIBRARIES "$<$<LINK_LANGUAGE:HIP>:${CLANGRT_BUILTINS}>"
hip/hip-config.cmake:  find_library(CLANGRT_BUILTINS
hip/hip-config.cmake:  if(CLANGRT_BUILTINS-NOTFOUND)
hip/hip-config.cmake:    set_property(TARGET hip::host APPEND PROPERTY INTERFACE_LINK_LIBRARIES "${CLANGRT_BUILTINS}")
hip/hip-config.cmake:    set_property(TARGET hip::device APPEND PROPERTY INTERFACE_LINK_LIBRARIES "${CLANGRT_BUILTINS}")
```
Add unnecessary library just add unintended side effect. Either make it optional or allow user to opt-out.

```
$ /usr/bin/mpicxx  -fopenmp -fstrict-aliasing -Wvla -Wall -Wno-unused-variable -Wno-overloaded-virtual -Wno-unused-private-field -Wno-unused-local-typedef -Wsuggest-override -Wno-unknown-pragmas -Wmisleading-indentation -ffast-math -march=native -fopenmp-targets=amdgcn-amd-amdhsa -Wno-linker-warnings -Xopenmp-target=amdgcn-amd-amdhsa -march=gfx906 -O3 -DNDEBUG CMakeFiles/test_particle.dir/test_particle.cpp.o CMakeFiles/test_particle.dir/test_distance_table.cpp.o CMakeFiles/test_particle.dir/test_walker.cpp.o CMakeFiles/test_particle.dir/test_particle_pool.cpp.o CMakeFiles/test_particle.dir/test_sample_stack.cpp.o CMakeFiles/test_particle.dir/test_DTModes.cpp.o CMakeFiles/test_particle.dir/test_SoaDistanceTableAA.cpp.o CMakeFiles/test_particle.dir/test_MCCoords.cpp.o -o test_particle  -Wl,-rpath,/home/packages/spack/opt/spack/linux-ubuntu20.04-zen2/gcc-9.3.0/openblas-0.3.18-kweo57mpfcetbxacn565yvasen3pjq6d/lib:/usr/lib/x86_64-linux-gnu/hdf5/openmpi:/opt/rocm-5.0.0/hip/lib ../../Message/libcatch_main.a ../libqmcparticle.a ../../Platforms/CPU/libplatform_cpu_LA.a /home/packages/spack/opt/spack/linux-ubuntu20.04-zen2/gcc-9.3.0/openblas-0.3.18-kweo57mpfcetbxacn565yvasen3pjq6d/lib/libopenblas.so -lm -ldl ../../Numerics/libqmcnumerics.a ../../Utilities/libqmcutil.a ../../io/hdf/libqmcio_hdf.a ../../Message/libmessage.a /usr/lib/x86_64-linux-gnu/hdf5/openmpi/libhdf5.so /usr/lib/x86_64-linux-gnu/libsz.so /usr/lib/x86_64-linux-gnu/libz.so /usr/lib/x86_64-linux-gnu/libdl.so -lm ../../io/OhmmsData/libqmcio_xml.a ../../Containers/libcontainers.a ../../Platforms/libplatform_runtime.a ../../Platforms/libplatform_host_runtime.a ../../Platforms/OMPTarget/libplatform_omptarget_runtime.a ../../Platforms/CUDA/libplatform_cuda_runtime.a /opt/rocm-5.0.0/hip/lib/libamdhip64.so.5.0.50000 /opt/rocm-5.0.0/llvm/lib/clang/14.0.0/lib/linux/libclang_rt.builtins-x86_64.a ../../Utilities/libcxx_helpers.a ../../Utilities/libqmcrng.a /usr/lib/x86_64-linux-gnu/libxml2.so 
/opt/rocm-5.1.0/llvm/bin/clang-build-select-link: /tmp/libclang_rt-b6e9cd.o:1:2: error: expected integer
!<arch>
 ^
/opt/rocm-5.1.0/llvm/bin/clang-build-select-link: error:  loading file '/tmp/libclang_rt-b6e9cd.o'
clang-14: error: amdgcn-link command failed with exit code 1 (use -v to see invocation)
```
Just removing the builtin library, my code compiles fine.

---

## 评论 (1 条)

### 评论 #1 — ye-luo (2022-07-06T16:38:51Z)

The non-working guard has been fixed in https://github.com/ROCm-Developer-Tools/HIP/blob/f5685158ad11c45c4c568135b865b69201a11904/hip-lang-config.cmake.in#L139
although it didn't make it to ROCm 5.2.

---
