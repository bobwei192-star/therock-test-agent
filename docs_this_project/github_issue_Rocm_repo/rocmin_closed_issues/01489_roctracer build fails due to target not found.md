# roctracer build fails due to target not found

- **Issue #:** 1489
- **State:** closed
- **Created:** 2021-06-04T18:47:30Z
- **Updated:** 2021-06-07T09:45:07Z
- **URL:** https://github.com/ROCm/ROCm/issues/1489

Ubuntu1804 ROCM4.2
It appears it set target as follows and then throws following error:

```
+ sed -n s/^.*amdgcn-amd-amdhsa--\(\w*\).*$/\1/p
+ TGT_LIST=
Error: GPU targets not found

```

Full log below based on README.md build steps: 

```

root@guest:~/ROCm-4.2/roctracer/build# cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm ..
----------------NBit: 64
----------Build-Type: release
----------C-Compiler: /usr/bin/cc
--C-Compiler-Version: 7.5.0
--------CXX-Compiler: /usr/bin/c++
CXX-Compiler-Version: 7.5.0
-----HSA-Runtime-Inc: /opt/rocm/include/hsa
-----HSA-Runtime-Lib: /opt/rocm/lib
----HSA_KMT_LIB_PATH: /opt/rocm/lib
-------ROCM_ROOT_DIR: /opt/rocm
-------ROCM_INC_PATH: /opt/rocm/include
-------------KFD-Inc: /opt/rocm/lib/../include
-------------HIP-Inc: /opt/rocm/hip/include
-------------HIP-VDI: 0
-----CMAKE_CXX_FLAGS: -std=c++11 -Wall -Werror -Werror=return-type -fexceptions -fvisibility=hidden -fno-math-errno -fno-threadsafe-statics -fmerge-all-constants -fms-extensions -fmerge-all-constants -fPIC -m64  -msse -msse2
---CMAKE_PREFIX_PATH: /opt/rocm
---------GPU_TARGETS:
--------LIBRARY_TYPE: SHARED
-- LIB-VERSION: 1.0.0
+ mkdir -p /root/ROCm-4.2/roctracer/build/inc
+ mkdir -p /root/ROCm-4.2/roctracer/build/src
+ /usr/bin/cc -E /opt/rocm/include/hsa/hsa.h
+ /usr/bin/cc -E /opt/rocm/include/hsa/hsa_ext_amd.h
+ python3 /root/ROCm-4.2/roctracer/script/gen_ostream_ops.py -in /root/ROCm-4.2/roctracer/build/inc/hsa_pp.h,/root/ROCm-4.2/roctracer/build/inc/hsa_ext_amd_pp.h -out /root/ROCm-4.2/roctracer/build/inc/hsa_ostream_ops.h
[1133] WARN-enum: nameless enum ['enum', '{', 'HSA_EXT_STATUS_ERROR_IMAGE_FORMAT_UNSUPPORTED', '=', '0x3000', ',', 'HSA_EXT_STATUS_ERROR_IMAGE_SIZE_UNSUPPORTED', '=', '0x3001', ',', 'HSA_EXT_STATUS_ERROR_IMAGE_PITCH_UNSUPPORTED', '=', '0x3002', ',', 'HSA_EXT_STATUS_ERROR_SAMPLER_DESCRIPTOR_UNSUPPORTED', '=', '0x3003', '}']
[1133] WARN-enum: nameless enum ['enum', '{', 'HSA_EXT_AGENT_INFO_IMAGE_1D_MAX_ELEMENTS', '=', '0x3000', ',', 'HSA_EXT_AGENT_INFO_IMAGE_1DA_MAX_ELEMENTS', '=', '0x3001', ',', 'HSA_EXT_AGENT_INFO_IMAGE_1DB_MAX_ELEMENTS', '=', '0x3002', ',', 'HSA_EXT_AGENT_INFO_IMAGE_2D_MAX_ELEMENTS', '=', '0x3003', ',', 'HSA_EXT_AGENT_INFO_IMAGE_2DA_MAX_ELEMENTS', '=', '0x3004', ',', 'HSA_EXT_AGENT_INFO_IMAGE_2DDEPTH_MAX_ELEMENTS', '=', '0x3005', ',', 'HSA_EXT_AGENT_INFO_IMAGE_2DADEPTH_MAX_ELEMENTS', '=', '0x3006', ',', 'HSA_EXT_AGENT_INFO_IMAGE_3D_MAX_ELEMENTS', '=', '0x3007', ',', 'HSA_EXT_AGENT_INFO_IMAGE_ARRAY_MAX_LAYERS', '=', '0x3008', ',', 'HSA_EXT_AGENT_INFO_MAX_IMAGE_RD_HANDLES', '=', '0x3009', ',', 'HSA_EXT_AGENT_INFO_MAX_IMAGE_RORW_HANDLES', '=', '0x300A', ',', 'HSA_EXT_AGENT_INFO_MAX_SAMPLER_HANDLERS', '=', '0x300B', ',', 'HSA_EXT_AGENT_INFO_IMAGE_LINEAR_ROW_PITCH_ALIGNMENT', '=', '0x300C', '}']
[1133] WARN-enum: nameless enum ['enum', '{', 'HSA_STATUS_ERROR_INVALID_MEMORY_POOL', '=', '40', ',', 'HSA_STATUS_ERROR_MEMORY_APERTURE_VIOLATION', '=', '41', ',', 'HSA_STATUS_ERROR_ILLEGAL_INSTRUCTION', '=', '42', ',', '}']
File /root/ROCm-4.2/roctracer/build/inc/hsa_ostream_ops.h generated
+ python3 /root/ROCm-4.2/roctracer/script/hsaap.py /root/ROCm-4.2/roctracer/build /opt/rocm/include/hsa
Generating "/root/ROCm-4.2/roctracer/build/inc/hsa_prof_str.h"
+ python3 /root/ROCm-4.2/roctracer/script/kfdap.py /root/ROCm-4.2/roctracer/build /opt/rocm/lib/../include
Generating "/root/ROCm-4.2/roctracer/build/inc/kfd_prof_str.h"
Generating "/root/ROCm-4.2/roctracer/build/src/kfd_wrapper.cpp"
+ /usr/bin/cc -E /opt/rocm/lib/../include/hsakmttypes.h
+ python3 /root/ROCm-4.2/roctracer/script/gen_ostream_ops.py -in /root/ROCm-4.2/roctracer/build/inc/hsakmttypes_pp.h -out /root/ROCm-4.2/roctracer/build/inc/kfd_ostream_ops.h
File /root/ROCm-4.2/roctracer/build/inc/kfd_ostream_ops.h generated
+ /usr/bin/cc -E /opt/rocm/hip/include/hip/hip_runtime_api.h -D__HIP_PLATFORM_HCC__=1 -I/opt/rocm/hip/include -I/opt/rocm/hsa/include
+ python3 /root/ROCm-4.2/roctracer/script/gen_ostream_ops.py -in /root/ROCm-4.2/roctracer/build/inc/hip_runtime_api_pp.h -out /root/ROCm-4.2/roctracer/build/inc/hip_ostream_ops.h
[1133] WARN-enum: nameless enum ['enum', '{', 'HIP_SUCCESS', '=', '0', ',', 'HIP_ERROR_INVALID_VALUE', ',', 'HIP_ERROR_NOT_INITIALIZED', ',', 'HIP_ERROR_LAUNCH_OUT_OF_RESOURCES', '}']
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __locale_data
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __buflen)
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
[1485] WARN unresolved __restrict
File /root/ROCm-4.2/roctracer/build/inc/hip_ostream_ops.h generated
+ mkdir /root/ROCm-4.2/roctracer/build/inc/rocprofiler
mkdir: cannot create directory '/root/ROCm-4.2/roctracer/build/inc/rocprofiler': File exists
+ ln -s /root/ROCm-4.2/roctracer/../rocprofiler/inc/rocprofiler.h /root/ROCm-4.2/roctracer/build/inc/rocprofiler/rocprofiler.h
ln: failed to create symbolic link '/root/ROCm-4.2/roctracer/build/inc/rocprofiler/rocprofiler.h': File exists
+ ln -s /root/ROCm-4.2/roctracer/../rocprofiler/src/core/activity.h /root/ROCm-4.2/roctracer/build/inc/rocprofiler/activity.h
ln: failed to create symbolic link '/root/ROCm-4.2/roctracer/build/inc/rocprofiler/activity.h': File exists
+ [ ! -e /root/ROCm-4.2/roctracer/test/hsa ]
+ [ -e /root/ROCm-4.2/roctracer/test/hsa ]
+ cd /root/ROCm-4.2/roctracer/test/hsa
+ git fetch origin
+ git checkout a4fcdae
HEAD is now at a4fcdae adding prefix path to hsa handles output file
+ /root/ROCm-4.2/roctracer/test/hsa/test/../script/build_kernel.sh /root/ROCm-4.2/roctracer/test/hsa/test/dummy_kernel/dummy_kernel /root/ROCm-4.2/roctracer/build /opt/rocm
+ SO_EXT=hsaco
+ TEST_NAME=/root/ROCm-4.2/roctracer/test/hsa/test/dummy_kernel/dummy_kernel
+ DST_DIR=/root/ROCm-4.2/roctracer/build
+ ROCM_DIR=/opt/rocm
+ TGT_LIST=
+ [ -z /root/ROCm-4.2/roctracer/test/hsa/test/dummy_kernel/dummy_kernel ]
+ sed+  -e s/_./\U&\E/g -e s/_//g
basename /root/ROCm-4.2/roctracer/test/hsa/test/dummy_kernel/dummy_kernel
+ echo _dummy_kernel
+ OBJ_NAME=DummyKernel
+ [ -z /root/ROCm-4.2/roctracer/build ]
+ [ -z /opt/rocm ]
+ [ -z  ]
+ grep amdgcn-amd-amdhsa--
+ + sed -n s/^.*amdgcn-amd-amdhsa--\(\w*\).*$/\1/p
+ head -n 1
/opt/rocm/bin/rocminfo
+ TGT_LIST=
+ [Error: GPU targets not found
 -z  ]
+ echo Error: GPU targets not found
+ exit 1
+ /root/ROCm-4.2/roctracer/test/hsa/test/../script/build_kernel.sh /root/ROCm-4.2/roctracer/test/hsa/test/simple_convolution/simple_convolution /root/ROCm-4.2/roctracer/build /opt/rocm
+ SO_EXT=hsaco
+ TEST_NAME=/root/ROCm-4.2/roctracer/test/hsa/test/simple_convolution/simple_convolution
+ DST_DIR=/root/ROCm-4.2/roctracer/build
+ ROCM_DIR=/opt/rocm
+ TGT_LIST=
+ [ -z /root/ROCm-4.2/roctracer/test/hsa/test/simple_convolution/simple_convolution ]
+ basename /root/ROCm-4.2/roctracer/test/hsa/test/simple_convolution/simple_convolution
+ sed -e s/_./\U&\E/g -e+ echo _simple_convolution
 s/_//g
+ OBJ_NAME=SimpleConvolution
+ [ -z /root/ROCm-4.2/roctracer/build ]
+ [ -z /opt/rocm ]
+ [ -z  ]
+ + /opt/rocm/bin/rocminfo
grep amdgcn-amd-amdhsa--
+ head -n 1
+ sed -n s/^.*amdgcn-amd-amdhsa--\(\w*\).*$/\1/p
+ TGT_LIST=
Error: GPU targets not found
+ [ -z  ]
+ echo Error: GPU targets not found
+ exit 1
+ cp /root/ROCm-4.2/roctracer/test/hsa/test/run.sh /root/ROCm-4.2/roctracer/build
+ cp /root/ROCm-4.2/roctracer/test/run.sh /root/ROCm-4.2/roctracer/build
+ ln -s run.sh /root/ROCm-4.2/roctracer/build/run_ci.sh
ln: failed to create symbolic link '/root/ROCm-4.2/roctracer/build/run_ci.sh': File exists
+ cp /root/ROCm-4.2/roctracer/script/check_trace.py /root/ROCm-4.2/roctracer/build/test/.
-----------Dest-name: roctracer
------Install-prefix: /opt/rocm
-----------CPACK-dir:
-- CPACK_PACKAGE_VERSION: 1.0.0
Using CPACK_DEBIAN_PACKAGE_RELEASE local
Using CPACK_RPM_PACKAGE_RELEASE local
RESULT_VARIABLE No such file or directory OUTPUT_VARIABLE:
CPACK_RPM_PACKAGE_RELEASE: local
-- Configuring done
-- Generating done
-- Build files have been written to: /root/ROCm-4.2/roctracer/build
root@guest:~/ROCm-4.2/roctracer/build# lspci | grep Disp^C
root@guest:~/ROCm-4.2/roctracer/build# egrep -irn TGT_LIST ../CMakeLists.txt
root@guest:~/ROCm-4.2/roctracer/build# egrep -irn TGT_LIST
root@guest:~/ROCm-4.2/roctracer/build# egrep -irn TGT_LIST ../
../test/hsa/script/build_kernel.sh:7:TGT_LIST=$4
../test/hsa/script/build_kernel.sh:24:if [ -z "$TGT_LIST" ] ; then
../test/hsa/script/build_kernel.sh:25:  TGT_LIST=`$ROCM_DIR/bin/rocminfo | grep "amdgcn-amd-amdhsa--" | head -n 1 | sed -n "s/^.*amdgcn-amd-amdhsa--\(\w*\).*$/\1/p"`
../test/hsa/script/build_kernel.sh:28:if [ -z "$TGT_LIST" ] ; then
../test/hsa/script/build_kernel.sh:73:for GFXIP in $TGT_LIST ; do
```