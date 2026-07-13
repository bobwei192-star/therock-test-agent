# On a ARM AArch64 System:  Building HCC from source code failed

- **Issue #:** 211
- **State:** closed
- **Created:** 2017-09-18T01:43:55Z
- **Updated:** 2018-06-03T14:59:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/211

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