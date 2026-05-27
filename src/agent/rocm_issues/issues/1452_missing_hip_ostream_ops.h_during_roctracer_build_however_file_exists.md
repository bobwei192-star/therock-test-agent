# missing hip_ostream_ops.h during roctracer build however file exists.

> **Issue #1452**
> **状态**: closed
> **创建时间**: 2021-04-12T19:57:46Z
> **更新时间**: 2021-06-08T11:21:25Z
> **关闭时间**: 2021-06-04T18:50:29Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1452

## 描述

Used usual instruction instruction in readme.md however hip header file below is missing. rocm-dkms + HIP was installed ok previously. File exists in /opt/rocm.


root@guest:~/ROCm-4.1/roctracer/build# find ../.. -name hip_ostream_ops.h
root@guest:~/ROCm-4.1/roctracer/build# find /opt -name hip_ostream_ops.h
/opt/rocm-4.1.0/roctracer/include/hip_ostream_ops.h
/opt/rocm-4.1.0/include/roctracer/hip_ostream_ops.h
root@guest:~/ROCm-4.1/roctracer/build#

cmake -DCMAKE_INSTALL_PREFIX=/opt/rocm ..
-- The C compiler identification is GNU 7.5.0
-- The CXX compiler identification is GNU 7.5.0
-- Check for working C compiler: /usr/bin/cc
-- Check for working C compiler: /usr/bin/cc -- works
-- Detecting C compiler ABI info
-- Detecting C compiler ABI info - done
-- Detecting C compile features
-- Detecting C compile features - done
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
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
-------------KFD-Inc: /opt/rocm/lib/../include
-------------HIP-Inc: /opt/rocm/hip/include
-------------HIP-VDI: 0
-----CMAKE_CXX_FLAGS: -std=c++11 -Wall -Werror -Werror=return-type -fexceptions -fvisibility=hidden -fno-math-errno -fno-threadsafe-statics -fmerge-all-constants -fms-extensions -fmerge-all-constants -fPIC -m64  -msse -msse2
---CMAKE_PREFIX_PATH:
---------GPU_TARGETS:
--------LIBRARY_TYPE: SHARED
-- LIB-VERSION: 1.0.0
+ mkdir -p /root/ROCm-4.1/roctracer/build/inc
+ mkdir -p /root/ROCm-4.1/roctracer/build/src
+ /root/ROCm-4.1/roctracer/script/hsaap.py /root/ROCm-4.1/roctracer/build /opt/rocm/include/hsa
Generating "/root/ROCm-4.1/roctracer/build/inc/hsa_prof_str.h"
+ /root/ROCm-4.1/roctracer/script/kfdap.py /root/ROCm-4.1/roctracer/build /opt/rocm/lib/../include
Generating "/root/ROCm-4.1/roctracer/build/inc/kfd_prof_str.h"
Generating "/root/ROCm-4.1/roctracer/build/src/kfd_wrapper.cpp"
+ /usr/bin/cc -E /opt/rocm/lib/../include/hsakmttypes.h
+ /root/ROCm-4.1/roctracer/script/gen_ostream_ops.py -in /root/ROCm-4.1/roctracer/build/inc/hsakmttypes_pp.h -out /root/ROCm-4.1/roctracer/build/inc/kfd_ostream_ops.h
Traceback (most recent call last):
  File "/root/ROCm-4.1/roctracer/script/gen_ostream_ops.py", line 4, in <module>
    import CppHeaderParser
ModuleNotFoundError: No module named 'CppHeaderParser'
+ /usr/bin/cc -E /opt/rocm/hip/include/hip/hip_runtime_api.h -D__HIP_PLATFORM_HCC__=1 -I/opt/rocm/hip/include -I/opt/rocm/hsa/include
+ /root/ROCm-4.1/roctracer/script/gen_ostream_ops.py -in /root/ROCm-4.1/roctracer/build/inc/hip_runtime_api_pp.h -out /root/ROCm-4.1/roctracer/build/inc/hip_ostream_ops.h
Traceback (most recent call last):
  File "/root/ROCm-4.1/roctracer/script/gen_ostream_ops.py", line 4, in <module>
    import CppHeaderParser
ModuleNotFoundError: No module named 'CppHeaderParser'
+ /usr/bin/cc -E /opt/rocm/include/hsa/hsa.h
+ /root/ROCm-4.1/roctracer/script/gen_ostream_ops.py -in /root/ROCm-4.1/roctracer/build/inc/hsa_pp.h -out /root/ROCm-4.1/roctracer/build/inc/hsa_ostream_ops.h
Traceback (most recent call last):
  File "/root/ROCm-4.1/roctracer/script/gen_ostream_ops.py", line 4, in <module>
    import CppHeaderParser
ModuleNotFoundError: No module named 'CppHeaderParser'
+ [ ! -e /root/ROCm-4.1/roctracer/test/hsa ]
+ [ -e /root/ROCm-4.1/roctracer/test/hsa ]
+ cd /root/ROCm-4.1/roctracer/test/hsa
+ git fetch origin
+ git checkout 19b1191
HEAD is now at 19b1191 v3 testing codeobject support
+ /root/ROCm-4.1/roctracer/test/hsa/test/../script/build_kernel.sh /root/ROCm-4.1/roctracer/test/hsa/test/dummy_kernel/dummy_kernel /root/ROCm-4.1/roctracer/build /opt/rocm
+ SO_EXT=hsaco
+ TEST_NAME=/root/ROCm-4.1/roctracer/test/hsa/test/dummy_kernel/dummy_kernel
+ DST_DIR=/root/ROCm-4.1/roctracer/build
+ ROCM_DIR=/opt/rocm
+ TGT_LIST=
+ [ -z /root/ROCm-4.1/roctracer/test/hsa/test/dummy_kernel/dummy_kernel ]
+ sed -e s/_./\U&\E/g -e s/_//g
+ basename /root/ROCm-4.1/roctracer/test/hsa/test/dummy_kernel/dummy_kernel
+ echo _dummy_kernel
+ OBJ_NAME=DummyKernel
+ [ -z /root/ROCm-4.1/roctracer/build ]
+ [ -z /opt/rocm ]
+ [ -z  ]
+ /opt/rocm/bin/rocminfo
+ grep amdgcn-amd-amdhsa--
+ head -n 1
+ sed -n s/^.*amdgcn-amd-amdhsa--\(\w*\).*$/\1/p
+ TGT_LIST=gfx900
+ [ -z gfx900 ]
+ OCL_VER=2.0
+ [ -e /opt/rocm/llvm ]
+ LLVM_DIR=/opt/rocm/llvm
+ LIB_DIR=/opt/rocm/lib
+ [ -e /opt/rocm/lib/bitcode/opencl.amdgcn.bc ]
+ [ -e /opt/rocm/lib/opencl.amdgcn.bc ]
+ [ -e /opt/rocm/amdgcn/bitcode/opencl.bc ]
+ BC_DIR=/opt/rocm/amdgcn/bitcode
+ CLANG_ROOT=/opt/rocm/llvm/lib/clang
+ ls -d /opt/rocm/llvm/lib/clang/12.0.0
+ head -n 1
+ CLANG_DIR=/opt/rocm/llvm/lib/clang/12.0.0
+ [ /opt/rocm/llvm/lib/clang/12.0.0 =  ]
+ BIN_DIR=/opt/rocm/llvm/bin
+ INC_DIR=/opt/rocm/llvm/lib/clang/12.0.0/include
+ [ -e /opt/rocm/amdgcn/bitcode/opencl.amdgcn.bc ]
+ BITCODE_OPTS=--hip-device-lib-path=/opt/rocm/amdgcn/bitcode
+ OBJ_PREF=gfx900
+ OBJ_FILE=gfx900_DummyKernel.hsaco
+ /opt/rocm/llvm/bin/clang -cl-std=CL2.0 -include /opt/rocm/llvm/lib/clang/12.0.0/include/opencl-c.h --hip-device-lib-path=/opt/rocm/amdgcn/bitcode -target amdgcn-amd-amdhsa -mcpu=gfx900 /root/ROCm-4.1/roctracer/test/hsa/test/dummy_kernel/dummy_kernel.cl -o /root/ROCm-4.1/roctracer/build/gfx900_DummyKernel.hsaco
'gfx900_DummyKernel.hsaco' generated
+ echo 'gfx900_DummyKernel.hsaco' generated
+ exit 0
+ /root/ROCm-4.1/roctracer/test/hsa/test/../script/build_kernel.sh /root/ROCm-4.1/roctracer/test/hsa/test/simple_convolution/simple_convolution /root/ROCm-4.1/roctracer/build /opt/rocm
+ SO_EXT=hsaco
+ TEST_NAME=/root/ROCm-4.1/roctracer/test/hsa/test/simple_convolution/simple_convolution
+ DST_DIR=/root/ROCm-4.1/roctracer/build
+ ROCM_DIR=/opt/rocm
+ TGT_LIST=
+ [ -z /root/ROCm-4.1/roctracer/test/hsa/test/simple_convolution/simple_convolution ]
+ sed -e+  s/_./\U&\E/g -e s/_//g
basename /root/ROCm-4.1/roctracer/test/hsa/test/simple_convolution/simple_convolution
+ echo _simple_convolution
+ OBJ_NAME=SimpleConvolution
+ [ -z /root/ROCm-4.1/roctracer/build ]
+ [ -z /opt/rocm ]
+ [ -z  ]
+ /opt/rocm/bin/rocminfo
+ grep amdgcn-amd-amdhsa--
+ head -n 1
+ sed -n s/^.*amdgcn-amd-amdhsa--\(\w*\).*$/\1/p
+ TGT_LIST=gfx900
+ [ -z gfx900 ]
+ OCL_VER=2.0
+ [ -e /opt/rocm/llvm ]
+ LLVM_DIR=/opt/rocm/llvm
+ LIB_DIR=/opt/rocm/lib
+ [ -e /opt/rocm/lib/bitcode/opencl.amdgcn.bc ]
+ [ -e /opt/rocm/lib/opencl.amdgcn.bc ]
+ [ -e /opt/rocm/amdgcn/bitcode/opencl.bc ]
+ BC_DIR=/opt/rocm/amdgcn/bitcode
+ CLANG_ROOT=/opt/rocm/llvm/lib/clang
+ ls -d /opt/rocm/llvm/lib/clang/12.0.0
+ head -n 1
+ CLANG_DIR=/opt/rocm/llvm/lib/clang/12.0.0
+ [ /opt/rocm/llvm/lib/clang/12.0.0 =  ]
+ BIN_DIR=/opt/rocm/llvm/bin
+ INC_DIR=/opt/rocm/llvm/lib/clang/12.0.0/include
+ [ -e /opt/rocm/amdgcn/bitcode/opencl.amdgcn.bc ]
+ BITCODE_OPTS=--hip-device-lib-path=/opt/rocm/amdgcn/bitcode
+ OBJ_PREF=gfx900
+ OBJ_FILE=gfx900_SimpleConvolution.hsaco
+ /opt/rocm/llvm/bin/clang -cl-std=CL2.0 -include /opt/rocm/llvm/lib/clang/12.0.0/include/opencl-c.h --hip-device-lib-path=/opt/rocm/amdgcn/bitcode -target amdgcn-amd-amdhsa -mcpu=gfx900 /root/ROCm-4.1/roctracer/test/hsa/test/simple_convolution/simple_convolution.cl -o /root/ROCm-4.1/roctracer/build/gfx900_SimpleConvolution.hsaco
'gfx900_SimpleConvolution.hsaco' generated
+ echo 'gfx900_SimpleConvolution.hsaco' generated
+ exit 0
+ cp /root/ROCm-4.1/roctracer/test/hsa/test/run.sh /root/ROCm-4.1/roctracer/build
+ cp /root/ROCm-4.1/roctracer/test/run.sh /root/ROCm-4.1/roctracer/build
+ ln -s run.sh /root/ROCm-4.1/roctracer/build/run_ci.sh
+ cp /root/ROCm-4.1/roctracer/script/check_trace.py /root/ROCm-4.1/roctracer/build/test/.
-----------Dest-name: roctracer
------Install-prefix: /opt/rocm
-----------CPACK-dir:
-- CPACK_PACKAGE_VERSION: 1.0.0
Using CPACK_DEBIAN_PACKAGE_RELEASE local
Using CPACK_RPM_PACKAGE_RELEASE local
RESULT_VARIABLE 0 OUTPUT_VARIABLE:
CPACK_RPM_PACKAGE_RELEASE: local
-- Configuring done
-- Generating done
-- Build files have been written to: /root/ROCm-4.1/roctracer/build
root@guest:~/ROCm-4.1/roctracer/build#
root@guest:~/ROCm-4.1/roctracer/build#
root@guest:~/ROCm-4.1/roctracer/build#
root@guest:~/ROCm-4.1/roctracer/build#
root@guest:~/ROCm-4.1/roctracer/build# make
/usr/local/bin/cmake -S/root/ROCm-4.1/roctracer -B/root/ROCm-4.1/roctracer/build --check-build-system CMakeFiles/Makefile.cmake 0
/usr/local/bin/cmake -E cmake_progress_start /root/ROCm-4.1/roctracer/build/CMakeFiles /root/ROCm-4.1/roctracer/build/CMakeFiles/progress.marks
make -f CMakeFiles/Makefile2 all
make[1]: Entering directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/so-major-link.dir/build.make CMakeFiles/so-major-link.dir/depend
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/CMakeFiles/so-major-link.dir/DependInfo.cmake --color=
Scanning dependencies of target so-major-link
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/so-major-link.dir/build.make CMakeFiles/so-major-link.dir/build
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
/usr/local/bin/cmake -E create_symlink ../roctracer/lib/libroctracer64.so.1 so-major-link
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
[  0%] Built target so-major-link
make -f CMakeFiles/so-link.dir/build.make CMakeFiles/so-link.dir/depend
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/CMakeFiles/so-link.dir/DependInfo.cmake --color=
Scanning dependencies of target so-link
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/so-link.dir/build.make CMakeFiles/so-link.dir/build
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
/usr/local/bin/cmake -E create_symlink ../roctracer/lib/libroctracer64.so so-link
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
[  0%] Built target so-link
make -f CMakeFiles/roctx64.dir/build.make CMakeFiles/roctx64.dir/depend
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/CMakeFiles/roctx64.dir/DependInfo.cmake --color=
Scanning dependencies of target roctx64
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/roctx64.dir/build.make CMakeFiles/roctx64.dir/build
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
[  4%] Building CXX object CMakeFiles/roctx64.dir/src/roctx/roctx.cpp.o
/usr/bin/c++  -DAMD_INTERNAL_BUILD -DHIP_PROF_HIP_API_STRING=1 -DHIP_VDI=0 -DHSA_DEPRECATED="" -DHSA_LARGE_MODEL="" -DLINUX -DLITTLEENDIAN_CPU=1 -DLOCAL_BUILD=1 -DUNIX_OS -D__AMD64__ -D__HIP_PLATFORM_HCC__=1 -D__linux__ -D__x86_64__ -Droctx64_EXPORTS -I/root/ROCm-4.1/roctracer/src -I/root/ROCm-4.1/roctracer -I/root/ROCm-4.1/roctracer/inc -I/opt/rocm/include/hsa -I/root/ROCm-4.1/roctracer/build/inc  -std=c++11 -Wall -Werror -Werror=return-type -fexceptions -fvisibility=hidden -fno-math-errno -fno-threadsafe-statics -fmerge-all-constants -fms-extensions -fmerge-all-constants -fPIC -m64  -msse -msse2 -O3 -DNDEBUG -fPIC   -o CMakeFiles/roctx64.dir/src/roctx/roctx.cpp.o -c /root/ROCm-4.1/roctracer/src/roctx/roctx.cpp
[  9%] Building CXX object CMakeFiles/roctx64.dir/src/roctx/roctx_intercept.cpp.o
/usr/bin/c++  -DAMD_INTERNAL_BUILD -DHIP_PROF_HIP_API_STRING=1 -DHIP_VDI=0 -DHSA_DEPRECATED="" -DHSA_LARGE_MODEL="" -DLINUX -DLITTLEENDIAN_CPU=1 -DLOCAL_BUILD=1 -DUNIX_OS -D__AMD64__ -D__HIP_PLATFORM_HCC__=1 -D__linux__ -D__x86_64__ -Droctx64_EXPORTS -I/root/ROCm-4.1/roctracer/src -I/root/ROCm-4.1/roctracer -I/root/ROCm-4.1/roctracer/inc -I/opt/rocm/include/hsa -I/root/ROCm-4.1/roctracer/build/inc  -std=c++11 -Wall -Werror -Werror=return-type -fexceptions -fvisibility=hidden -fno-math-errno -fno-threadsafe-statics -fmerge-all-constants -fms-extensions -fmerge-all-constants -fPIC -m64  -msse -msse2 -O3 -DNDEBUG -fPIC   -o CMakeFiles/roctx64.dir/src/roctx/roctx_intercept.cpp.o -c /root/ROCm-4.1/roctracer/src/roctx/roctx_intercept.cpp
[ 14%] Linking CXX shared library libroctx64.so
/usr/local/bin/cmake -E cmake_link_script CMakeFiles/roctx64.dir/link.txt --verbose=1
/usr/bin/c++ -fPIC -std=c++11 -Wall -Werror -Werror=return-type -fexceptions -fvisibility=hidden -fno-math-errno -fno-threadsafe-statics -fmerge-all-constants -fms-extensions -fmerge-all-constants -fPIC -m64  -msse -msse2 -O3 -DNDEBUG -Wl,-Bdynamic -Wl,-z,noexecstack -shared -Wl,-soname,libroctx64.so.1 -o libroctx64.so.1.0.0 CMakeFiles/roctx64.dir/src/roctx/roctx.cpp.o CMakeFiles/roctx64.dir/src/roctx/roctx_intercept.cpp.o  -lc -lstdc++
/usr/local/bin/cmake -E cmake_symlink_library libroctx64.so.1.0.0 libroctx64.so.1 libroctx64.so
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
[ 14%] Built target roctx64
make -f CMakeFiles/roctracer64.dir/build.make CMakeFiles/roctracer64.dir/depend
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/CMakeFiles/roctracer64.dir/DependInfo.cmake --color=
Scanning dependencies of target roctracer64
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/roctracer64.dir/build.make CMakeFiles/roctracer64.dir/build
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
[ 19%] Building CXX object CMakeFiles/roctracer64.dir/src/core/roctracer.cpp.o
/usr/bin/c++  -DAMD_INTERNAL_BUILD -DHIP_PROF_HIP_API_STRING=1 -DHIP_VDI=0 -DHSA_DEPRECATED="" -DHSA_LARGE_MODEL="" -DLINUX -DLITTLEENDIAN_CPU=1 -DLOCAL_BUILD=1 -DUNIX_OS -D__AMD64__ -D__HIP_PLATFORM_HCC__=1 -D__linux__ -D__x86_64__ -Droctracer64_EXPORTS -I/root/ROCm-4.1/roctracer/src -I/root/ROCm-4.1/roctracer -I/root/ROCm-4.1/roctracer/inc -I/opt/rocm/include/hsa -I/opt/rocm/hip/include -I/opt/rocm/lib/../include -I/root/ROCm-4.1/roctracer/build/inc  -std=c++11 -Wall -Werror -Werror=return-type -fexceptions -fvisibility=hidden -fno-math-errno -fno-threadsafe-statics -fmerge-all-constants -fms-extensions -fmerge-all-constants -fPIC -m64  -msse -msse2 -O3 -DNDEBUG -fPIC   -o CMakeFiles/roctracer64.dir/src/core/roctracer.cpp.o -c /root/ROCm-4.1/roctracer/src/core/roctracer.cpp
In file included from /root/ROCm-4.1/roctracer/src/core/roctracer.cpp:25:0:
/root/ROCm-4.1/roctracer/inc/roctracer_hip.h:40:10: fatal error: hip_ostream_ops.h: No such file or directory
 #include <hip_ostream_ops.h>
          ^~~~~~~~~~~~~~~~~~~
compilation terminated.
CMakeFiles/roctracer64.dir/build.make:65: recipe for target 'CMakeFiles/roctracer64.dir/src/core/roctracer.cpp.o' failed
make[2]: *** [CMakeFiles/roctracer64.dir/src/core/roctracer.cpp.o] Error 1
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
CMakeFiles/Makefile2:216: recipe for target 'CMakeFiles/roctracer64.dir/all' failed
make[1]: *** [CMakeFiles/roctracer64.dir/all] Error 2
make[1]: Leaving directory '/root/ROCm-4.1/roctracer/build'
Makefile:154: recipe for target 'all' failed
make: *** [all] Error 2


---

## 评论 (9 条)

### 评论 #1 — xuhuisheng (2021-04-13T01:32:09Z)

this header is generated by CppHeaderParser, we could install using pip
```
sudo apt install -y python3-pip
pip3 install cppheaderparser
```

---

### 评论 #2 — ROCmSupport (2021-04-19T09:03:54Z)

**import CppHeaderParser
ModuleNotFoundError: No module named 'CppHeaderParser'**

is the real issue.
Not sure why its missing in your machine. I have it in my machine.
I recommend you to install it explicitly and proceed.

And also I suggest you to share the exact steps while filing a ticket here. Thank you.

---

### 评论 #3 — ROCmSupport (2021-04-19T09:06:41Z)

Suggest to share the exact steps you followed from starting for better understanding so that we can help you out clearly.
Thank you.

---

### 评论 #4 — ROCmSupport (2021-05-07T07:27:33Z)

Got an update:
Able to reproduce this issue on a machine. Logged an internal ticket and assigned to developer.
Thank you.

---

### 评论 #5 — gggh000 (2021-05-12T22:02:35Z)

thanks any update? I installed the cppheaderparser  through pip3 as instructed and rebuilt but getting following error now: (previous error disappeared after pip3 installation):
oot@guest:~/ROCm-4.1/roctracer/build# make -j`nproc`
/usr/local/bin/cmake -S/root/ROCm-4.1/roctracer -B/root/ROCm-4.1/roctracer/build --check-build-system CMakeFiles/Makefile.cmake 0
/usr/local/bin/cmake -E cmake_progress_start /root/ROCm-4.1/roctracer/build/CMakeFiles /root/ROCm-4.1/roctracer/build/CMakeFiles/progress.marks
make -f CMakeFiles/Makefile2 all
make[1]: Entering directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/so-major-link.dir/build.make CMakeFiles/so-major-link.dir/depend
make -f CMakeFiles/so-link.dir/build.make CMakeFiles/so-link.dir/depend
make -f CMakeFiles/roctx64.dir/build.make CMakeFiles/roctx64.dir/depend
make -f CMakeFiles/roctracer64.dir/build.make CMakeFiles/roctracer64.dir/depend
make -f CMakeFiles/so-patch-link.dir/build.make CMakeFiles/so-patch-link.dir/depend
make -f CMakeFiles/kfdwrapper64.dir/build.make CMakeFiles/kfdwrapper64.dir/depend
make -f CMakeFiles/so-roctx-major-link.dir/build.make CMakeFiles/so-roctx-major-link.dir/depend
make -f CMakeFiles/so-roctx-patch-link.dir/build.make CMakeFiles/so-roctx-patch-link.dir/depend
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/CMakeFiles/so-link.dir/DependInfo.cmake --color=
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/CMakeFiles/so-major-link.dir/DependInfo.cmake --color=
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/CMakeFiles/so-patch-link.dir/DependInfo.cmake --color=
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/CMakeFiles/so-roctx-patch-link.dir/DependInfo.cmake --color=
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/CMakeFiles/roctracer64.dir/DependInfo.cmake --color=
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/CMakeFiles/kfdwrapper64.dir/DependInfo.cmake --color=
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/CMakeFiles/so-roctx-major-link.dir/DependInfo.cmake --color=
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/CMakeFiles/roctx64.dir/DependInfo.cmake --color=
Scanning dependencies of target kfdwrapper64
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/so-major-link.dir/build.make CMakeFiles/so-major-link.dir/build
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/so-patch-link.dir/build.make CMakeFiles/so-patch-link.dir/build
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/so-roctx-patch-link.dir/build.make CMakeFiles/so-roctx-patch-link.dir/build
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
/usr/local/bin/cmake -E create_symlink ../roctracer/lib/libroctracer64.so.1.0.0 so-patch-link
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
/usr/local/bin/cmake -E create_symlink ../roctracer/lib/libroctracer64.so.1 so-major-link
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
/usr/local/bin/cmake -E create_symlink ../roctracer/lib/libroctx64.so.1.0.0 so-roctx-patch-link
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/so-link.dir/build.make CMakeFiles/so-link.dir/build
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
Scanning dependencies of target roctracer64
make -f CMakeFiles/kfdwrapper64.dir/build.make CMakeFiles/kfdwrapper64.dir/build
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
/usr/local/bin/cmake -E create_symlink ../roctracer/lib/libroctracer64.so so-link
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/so-roctx-major-link.dir/build.make CMakeFiles/so-roctx-major-link.dir/build
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/roctx64.dir/build.make CMakeFiles/roctx64.dir/build
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
/usr/local/bin/cmake -E create_symlink ../roctracer/lib/libroctx64.so.1 so-roctx-major-link
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
make[2]: Nothing to be done for 'CMakeFiles/roctx64.dir/build'.
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
[  0%] Built target so-major-link
[  4%] Building CXX object CMakeFiles/kfdwrapper64.dir/src/kfd_wrapper.cpp.o
make -f CMakeFiles/so-roctx-link.dir/build.make CMakeFiles/so-roctx-link.dir/depend
[  4%] Built target so-patch-link
/usr/bin/c++  -DAMD_INTERNAL_BUILD -DHIP_PROF_HIP_API_STRING=1 -DHIP_VDI=0 -DHSA_DEPRECATED="" -DHSA_LARGE_MODEL="" -DLINUX -DLITTLEENDIAN_CPU=1 -DLOCAL_BUILD=1 -DUNIX_OS -D__AMD64__ -D__HIP_PLATFORM_HCC__=1 -D__linux__ -D__x86_64__ -Dkfdwrapper64_EXPORTS -I/root/ROCm-4.1/roctracer/src -I/root/ROCm-4.1/roctracer -I/root/ROCm-4.1/roctracer/inc -I/opt/rocm/include/hsa -I/opt/rocm/lib/../include -I/root/ROCm-4.1/roctracer/build/inc  -std=c++11 -Wall -Werror -Werror=return-type -fexceptions -fvisibility=hidden -fno-math-errno -fno-threadsafe-statics -fmerge-all-constants -fms-extensions -fmerge-all-constants -fPIC -m64  -msse -msse2 -O3 -DNDEBUG -fPIC   -o CMakeFiles/kfdwrapper64.dir/src/kfd_wrapper.cpp.o -c /root/ROCm-4.1/roctracer/build/src/kfd_wrapper.cpp
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/CMakeFiles/so-roctx-link.dir/DependInfo.cmake --color=
make -f test/hsa/CMakeFiles/ctrl.dir/build.make test/hsa/CMakeFiles/ctrl.dir/depend
[ 19%] Built target roctx64
[ 19%] Built target so-link
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
cd /root/ROCm-4.1/roctracer/build && /usr/local/bin/cmake -E cmake_depends "Unix Makefiles" /root/ROCm-4.1/roctracer /root/ROCm-4.1/roctracer/test/hsa/test /root/ROCm-4.1/roctracer/build /root/ROCm-4.1/roctracer/build/test/hsa /root/ROCm-4.1/roctracer/build/test/hsa/CMakeFiles/ctrl.dir/DependInfo.cmake --color=
[ 19%] Built target so-roctx-patch-link
[ 19%] Built target so-roctx-major-link
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/so-roctx-link.dir/build.make CMakeFiles/so-roctx-link.dir/build
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
/usr/local/bin/cmake -E create_symlink ../roctracer/lib/libroctx64.so so-roctx-link
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make -f test/hsa/CMakeFiles/ctrl.dir/build.make test/hsa/CMakeFiles/ctrl.dir/build
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
make[2]: Nothing to be done for 'test/hsa/CMakeFiles/ctrl.dir/build'.
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
[ 19%] Built target so-roctx-link
[ 47%] Built target ctrl
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
make -f CMakeFiles/roctracer64.dir/build.make CMakeFiles/roctracer64.dir/build
make[2]: Entering directory '/root/ROCm-4.1/roctracer/build'
[ 52%] Building CXX object CMakeFiles/roctracer64.dir/src/core/roctracer.cpp.o
/usr/bin/c++  -DAMD_INTERNAL_BUILD -DHIP_PROF_HIP_API_STRING=1 -DHIP_VDI=0 -DHSA_DEPRECATED="" -DHSA_LARGE_MODEL="" -DLINUX -DLITTLEENDIAN_CPU=1 -DLOCAL_BUILD=1 -DUNIX_OS -D__AMD64__ -D__HIP_PLATFORM_HCC__=1 -D__linux__ -D__x86_64__ -Droctracer64_EXPORTS -I/root/ROCm-4.1/roctracer/src -I/root/ROCm-4.1/roctracer -I/root/ROCm-4.1/roctracer/inc -I/opt/rocm/include/hsa -I/opt/rocm/hip/include -I/opt/rocm/lib/../include -I/root/ROCm-4.1/roctracer/build/inc  -std=c++11 -Wall -Werror -Werror=return-type -fexceptions -fvisibility=hidden -fno-math-errno -fno-threadsafe-statics -fmerge-all-constants -fms-extensions -fmerge-all-constants -fPIC -m64  -msse -msse2 -O3 -DNDEBUG -fPIC   -o CMakeFiles/roctracer64.dir/src/core/roctracer.cpp.o -c /root/ROCm-4.1/roctracer/src/core/roctracer.cpp
In file included from /root/ROCm-4.1/roctracer/src/core/roctracer.cpp:44:0:
/root/ROCm-4.1/roctracer/src/core/loader.h:314:2: error: #error HCC support dropped
 #error HCC support dropped
  ^~~~~
[ 57%] Linking CXX shared library libkfdwrapper64.so
/usr/local/bin/cmake -E cmake_link_script CMakeFiles/kfdwrapper64.dir/link.txt --verbose=1
/usr/bin/c++ -fPIC -std=c++11 -Wall -Werror -Werror=return-type -fexceptions -fvisibility=hidden -fno-math-errno -fno-threadsafe-statics -fmerge-all-constants -fms-extensions -fmerge-all-constants -fPIC -m64  -msse -msse2 -O3 -DNDEBUG -Wl,-Bdynamic -Wl,-z,noexecstack -shared -Wl,-soname,libkfdwrapper64.so -o libkfdwrapper64.so CMakeFiles/kfdwrapper64.dir/src/kfd_wrapper.cpp.o  -lc -lstdc++
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
[ 57%] Built target kfdwrapper64
/root/ROCm-4.1/roctracer/src/core/roctracer.cpp:660:21: error: expected constructor, destructor, or type conversion before ';' token
 LOADER_INSTANTIATE();
                     ^
CMakeFiles/roctracer64.dir/build.make:65: recipe for target 'CMakeFiles/roctracer64.dir/src/core/roctracer.cpp.o' failed
make[2]: *** [CMakeFiles/roctracer64.dir/src/core/roctracer.cpp.o] Error 1
make[2]: Leaving directory '/root/ROCm-4.1/roctracer/build'
CMakeFiles/Makefile2:216: recipe for target 'CMakeFiles/roctracer64.dir/all' failed
make[1]: *** [CMakeFiles/roctracer64.dir/all] Error 2
make[1]: Leaving directory '/root/ROCm-4.1/roctracer/build'
Makefile:154: recipe for target 'all' failed
make: *** [all] Error 2
root@guest:~/ROCm-4.1/roctracer/build#


---

### 评论 #6 — gggh000 (2021-05-12T22:03:37Z)

not sure why github is inserting crossed lines, please see if it can be ignored. 

---

### 评论 #7 — gggh000 (2021-06-04T18:45:31Z)

I had to install python module: "pip3 install CppHeaderParser" and it works. However cmake .. command additinoally throws gpu target not found error now: 

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

---

### 评论 #8 — gggh000 (2021-06-04T18:50:34Z)

I will close this one and open new  ticket. 

---

### 评论 #9 — ROCmSupport (2021-06-08T11:21:25Z)

Thanks @gggh000 for the closure.
I too verified and the issue is no more observed now.

---
