# On a ARM AArch64 System:  Building HCC from source code failed

> **Issue #211**
> **状态**: closed
> **创建时间**: 2017-09-18T01:43:55Z
> **更新时间**: 2018-06-03T14:59:07Z
> **关闭时间**: 2018-06-03T14:59:07Z
> **作者**: lintcoder
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/211

## 描述

I am trying to build ROCm from branch roc-1.6.3 on my ubunu16.04-arm64 server which is running on Cavium Thunder X. Now I have built ROCK-Kernel-Driver, ROCT-Thunk-Interface and ROCR-Runtime.
When it comes to HCC, I follow the steps in repo RadeonOpenCompute/hcc:
1.git clone --recursive -b clang_tot_upgrade https://github.com/RadeonOpenCompute/hcc.git
Now hcc is on branch clang_tot_upgrade
2.cd hcc
3.mkdir build; cd build
4.cmake -DNUM_BUILD_THREADS=96 -DCMAKE_BUILD_TYPE=Release ..
Output of cmake as follows(something omitted)
ROCm INFORMATION:
HSA_HEADER_DIR = , actually found at: /usr/local/include
HSA_LIBRARY_DIR = , actually found at: /usr/local/lib/libhsa-runtime64.so
ROCM_DEVICE_LIB_DIR = /home/cavium/rocm/hcc/rocdl
Installation path: /opt/rocm/hcc-1.0
Installer package installation path: /opt/rocm/hcc-1.0

HCC version: 1.0.17262-e8cf396-e8cf396-e8cf396

-- HCC configured with AMDGPU targets: auto
-- ROCm available, going to build HSA HCC Runtime
-- build HCC CPU Runtime
For the first time:
   'make' to build all
   'make docs' to build the HTML API reference

-- Configuring done
-- Generating done
-- Build files have been written to: /home/cavium/rocm/hcc/build
5. make -j96
Output as follows(something omitted)
error: unable to create target: 'No available targets are compatible with this triple.'
error: unable to create target: 'No available targets are compatible with this triple.'
2 errors generated.
lib/CMakeFiles/mcwamp_atomic.dir/build.make:62: recipe for target 'lib/CMakeFiles/mcwamp_atomic.dir/mcwamp_atomic.cpp.o' failed
make[2]: *** [lib/CMakeFiles/mcwamp_atomic.dir/mcwamp_atomic.cpp.o] Error 1
CMakeFiles/Makefile2:106730: recipe for target 'lib/CMakeFiles/mcwamp_atomic.dir/all' failed
make[1]: *** [lib/CMakeFiles/mcwamp_atomic.dir/all] Error 2
make[1]: *** Waiting for unfinished jobs....
......
[ 92%] Building OCL object rocdl/ocml/CMakeFiles/ocml_lib.dir/src/atanpiredH.cl
[ 92%] Building OCL object rocdl/ocml/CMakeFiles/ocml_lib.dir/src/copysignF.cl
[ 92%] Building OCL object rocdl/ocml/CMakeFiles/ocml_lib.dir/src/rintD.cl
error: unable to create target: 'No available targets are compatible with this triple.'
error: unable to create target: 'No available targets are compatible with this triple.'
2 errors generated.
[ 98%] Building OCL object rocdl/ocml/CMakeFiles/ocml_lib.dir/src/i0H.cl
[ 98%] Building OCL object rocdl/ocml/CMakeFiles/ocml_lib.dir/src/isnanF.cl
error: unable to create target: 'No available targets are compatible with this triple.'
error: unable to create target: 'No available targets are compatible with this triple.'
2 errors generated.
amp-conformance/CMakeFiles/amptest.dir/build.make:86: recipe for target 'amp-conformance/CMakeFiles/amptest.dir/amp_test_lib/src/device.cpp.o' failed
make[2]: *** [amp-conformance/CMakeFiles/amptest.dir/amp_test_lib/src/device.cpp.o] Error 1
CMakeFiles/Makefile2:107207: recipe for target 'amp-conformance/CMakeFiles/amptest.dir/all' failed
make[1]: *** [amp-conformance/CMakeFiles/amptest.dir/all] Error 2
...........
[ 98%] Linking OCL static library ocml.lib.bc
Generating ocml.amdgcn.bc
[ 98%] Built target ocml_lib
[ 98%] Linking OCL static library opencl.lib.bc
WARNING: Linking two modules of different data layouts: 'transformed_src/workgroup/wgscratch.ll' is 'e-p:32:32-p1:64:64-p2:64:64-p3:32:32-p4:64:64-p5:32:32-i64:64-v16:16-v24:32-v32:32-v48:64-v96:128-v192:256-v256:256-v512:512-v1024:1024-v2048:2048-n32:64' whereas 'llvm-link' is 'e-p:64:64-p1:64:64-p2:64:64-p3:32:32-p4:32:32-p5:32:32-i64:64-v16:16-v24:32-v32:32-v48:64-v96:128-v192:256-v256:256-v512:512-v1024:1024-v2048:2048-n32:64-A5'

[ 98%] Built target libclang
Generating opencl.amdgcn.bc
[ 98%] Built target opencl_lib
Makefile:149: recipe for target 'all' failed
make: *** [all] Error 2

@gstoner 

---

## 评论 (5 条)

### 评论 #1 — gstoner (2017-09-24T13:21:20Z)

@lintcoder  We are finally past some big deliverables,  we are going to get a formal build of HCC for ARM AArch64  in place,  once this in place  HIP will come up as well.  We push it out via HCC Github tree so you can build it as well. 

---

### 评论 #2 — gstoner (2017-10-17T12:48:13Z)

@lintcoder. we now have HCC compiling and running internally with ROCm 1.6.4 on Cavium ThunderX system,  we work to promote this out into source repo soon

---

### 评论 #3 — lintcoder (2017-10-18T01:37:31Z)

@gstoner thanks, I am looking forward to your promotion in this repo.

---

### 评论 #4 — lintcoder (2017-10-23T01:11:37Z)

@gstoner I‘ve noticed that ROCm platform relies on a few closed source components which are only available through the ROCm repositories as hsa-ext-rocr-dev package, since I have been building whole project on an aarch64 system, I wonder where could I get these components suitable for this platform?

---

### 评论 #5 — gstoner (2017-10-23T13:57:40Z)

lintcoder that is not a correct statement,  there was a set of historical test ( Vector Sample) that needed the HSAIl/Shader compiler,  this is not needed for the build. even the X86 version we are going to be removing this component  

---
