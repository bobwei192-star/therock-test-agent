# MIOpenGEMM make examples failing

> **Issue #1403**
> **状态**: closed
> **创建时间**: 2021-03-12T07:15:19Z
> **更新时间**: 2021-04-30T09:42:43Z
> **关闭时间**: 2021-04-30T09:42:43Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1403

## 描述

user libraru *so builds ok and test (smallgeometrytest) ran ok, however make examples seems to be failing
Ubuntu 2004 / ROCm4.0
:

root@Standard-PC-i440FX-PIIX-1996:~/ROCm/MIOpenGEMM/build# make examples
[ 58%] Built target miopengemm
Scanning dependencies of target apiexample1
[ 59%] Building CXX object examples/CMakeFiles/apiexample1.dir/apiexample1.cpp.o
In file included from /usr/local/include/CL/cl.h:32,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/platform.hpp:10,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/gemm.hpp:7,
                 from /root/ROCm/MIOpenGEMM/examples/apiexample1.cpp:8:
/usr/local/include/CL/cl_version.h:34:104: note: #pragma message: cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)
   34 | #pragma message("cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)")
      |                                                                                                        ^
[ 61%] Linking CXX executable apiexample1
[ 61%] Built target apiexample1
Scanning dependencies of target print
[ 62%] Building CXX object examples/CMakeFiles/print.dir/print.cpp.o
In file included from /usr/local/include/CL/cl.h:32,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/platform.hpp:10,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/hint.hpp:10,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/oclutil.hpp:9,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/tinytwo.hpp:12,
                 from /root/ROCm/MIOpenGEMM/examples/print.cpp:6:
/usr/local/include/CL/cl_version.h:34:104: note: #pragma message: cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)
   34 | #pragma message("cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)")
      |                                                                                                        ^
[ 63%] Linking CXX executable print
[ 63%] Built target print
Scanning dependencies of target multifindbase
[ 64%] Building CXX object examples/CMakeFiles/multifindbase.dir/multifindbase.cpp.o
In file included from /usr/local/include/CL/cl.h:32,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/platform.hpp:10,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/hint.hpp:10,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/oclutil.hpp:9,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/tinytwo.hpp:12,
                 from /root/ROCm/MIOpenGEMM/examples/multifindbase.cpp:7:
/usr/local/include/CL/cl_version.h:34:104: note: #pragma message: cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)
   34 | #pragma message("cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)")
      |                                                                                                        ^
[ 66%] Linking CXX executable multifindbase
[ 66%] Built target multifindbase
Scanning dependencies of target deepbench
[ 67%] Building CXX object examples/CMakeFiles/deepbench.dir/deepbench.cpp.o
In file included from /usr/local/include/CL/cl.h:32,
                 from /root/ROCm/MIOpenGEMM/examples/deepbench.cpp:14:
/usr/local/include/CL/cl_version.h:34:104: note: #pragma message: cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)
   34 | #pragma message("cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)")
      |                                                                                                        ^
[ 68%] Linking CXX executable deepbench
[ 68%] Built target deepbench
Scanning dependencies of target accu
[ 70%] Building CXX object examples/CMakeFiles/accu.dir/accu.cpp.o
In file included from /usr/local/include/CL/cl.h:32,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/platform.hpp:10,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/hint.hpp:10,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/oclutil.hpp:9,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/tinytwo.hpp:12,
                 from /root/ROCm/MIOpenGEMM/examples/accu.cpp:5:
/usr/local/include/CL/cl_version.h:34:104: note: #pragma message: cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)
   34 | #pragma message("cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)")
      |                                                                                                        ^
[ 71%] Linking CXX executable accu
[ 71%] Built target accu
Scanning dependencies of target find
[ 72%] Building CXX object examples/CMakeFiles/find.dir/find.cpp.o
In file included from /usr/local/include/CL/cl.h:32,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/platform.hpp:10,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/hint.hpp:10,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/oclutil.hpp:9,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/tinytwo.hpp:12,
                 from /root/ROCm/MIOpenGEMM/examples/find.cpp:5:
/usr/local/include/CL/cl_version.h:34:104: note: #pragma message: cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)
   34 | #pragma message("cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)")
      |                                                                                                        ^
[ 74%] Linking CXX executable find
[ 74%] Built target find
Scanning dependencies of target mergecaches
[ 75%] Building CXX object examples/CMakeFiles/mergecaches.dir/mergecaches.cpp.o
In file included from /usr/local/include/CL/cl.h:32,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/platform.hpp:10,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/hint.hpp:10,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/oclutil.hpp:9,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/hyperparams.hpp:13,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/derivedparams.hpp:14,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/kernelcache.hpp:9,
                 from /root/ROCm/MIOpenGEMM/miopengemm/include/miopengemm/kernelcachemerge.hpp:8,
                 from /root/ROCm/MIOpenGEMM/examples/mergecaches.cpp:6:
/usr/local/include/CL/cl_version.h:34:104: note: #pragma message: cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)
   34 | #pragma message("cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)")
      |                                                                                                        ^
[ 76%] Linking CXX executable mergecaches
[ 76%] Built target mergecaches
Scanning dependencies of target gemmbench
[ 77%] Building CXX object examples/CMakeFiles/gemmbench.dir/gemmbench.cpp.o
In file included from /usr/local/include/CL/cl.h:32,
                 from /root/ROCm/MIOpenGEMM/examples/gemmbench.cpp:15:
/usr/local/include/CL/cl_version.h:34:104: note: #pragma message: cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)
   34 | #pragma message("cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)")
      |                                                                                                        ^
/root/ROCm/MIOpenGEMM/examples/gemmbench.cpp: In function int main():
/root/ROCm/MIOpenGEMM/examples/gemmbench.cpp:118:52: error: ceil is not a member of std
  118 |       std::min<size_t>(1500, std::max<size_t>(std::ceil(1e11 / (2 * gg.m * gg.k * gg.n)), 2));
      |                                                    ^~~~
make[3]: *** [examples/CMakeFiles/gemmbench.dir/build.make:63: examples/CMakeFiles/gemmbench.dir/gemmbench.cpp.o] Error 1
make[2]: *** [CMakeFiles/Makefile2:439: examples/CMakeFiles/gemmbench.dir/all] Error 2
make[1]: *** [CMakeFiles/Makefile2:284: examples/CMakeFiles/examples.dir/rule] Error 2
make: *** [Makefile:212: examples] Error 2
root@Standard-PC-i440FX-PIIX-1996:~/ROCm/MIOpenGEMM/build# 

---

## 评论 (6 条)

### 评论 #1 — ROCmSupport (2021-03-12T07:37:31Z)

Hi @gggh000 
Thanks fr reaching out.
I am not sure why you have shared log as lines with strike-through.
Can you please share the steps to reproduce the problem and clear log.
Thank you. 

---

### 评论 #2 — ROCmSupport (2021-03-17T06:08:07Z)

Hi @gggh000 
Can you please share the steps to reproduce the problem and clear log.
Thank you.

---

### 评论 #3 — gggh000 (2021-03-23T17:18:28Z)

> Hi @gggh000
> Thanks fr reaching out.
> I am not sure why you have shared log as lines with strike-through.
> Can you please share the steps to reproduce the problem and clear log.
> Thank you.

not sure why it crossed out. I just pasted and github is converting the format. I will post the repro steps. 

---

### 评论 #4 — gggh000 (2021-03-24T06:29:01Z)

To repro, you just do a "make examples" from build directory:

root@guest:~/ROCm/MIOpenGEMM/build# cmake ..

There is an error however I tried with " 'cmake -DCMAKE_CXX_FLAGS=" -std=c++11 -Wall -Wextra -pedantic" but failed as well. 

*******************************************************************************
*----------------------------------- ERROR -----------------------------------*
* The variable 'CMAKE_CXX_FLAGS' should only be set by the cmake toolchain,
* either by calling 'cmake -DCMAKE_CXX_FLAGS=" -std=c++11 -Wall -Wextra -pedantic"' or
* set in a toolchain file and added with
* 'cmake -DCMAKE_TOOLCHAIN_FILE=<toolchain-file>'.
*-----------------------------------------------------------------------------*
*******************************************************************************

CMake Warning at /opt/rocm/share/rocm/cmake/ROCMChecks.cmake:37 (message):
  The toolchain variable 'CMAKE_CXX_FLAGS' is modified in the CMakeLists.txt.
Call Stack (most recent call first):
  examples/CMakeLists.txt:9999 (rocm_check_toolchain_var)
  examples/CMakeLists.txt:5 (SET)



*******************************************************************************
*----------------------------------- ERROR -----------------------------------*
* The variable 'CMAKE_CXX_FLAGS' should only be set by the cmake toolchain,
* either by calling 'cmake -DCMAKE_CXX_FLAGS=" -std=c++11 -Wall -Wextra -pedantic"' or
* set in a toolchain file and added with
* 'cmake -DCMAKE_TOOLCHAIN_FILE=<toolchain-file>'.
*-----------------------------------------------------------------------------*
*******************************************************************************

CMake Warning at /opt/rocm/share/rocm/cmake/ROCMChecks.cmake:37 (message):
  The toolchain variable 'CMAKE_CXX_FLAGS' is modified in the CMakeLists.txt.
Call Stack (most recent call first):
  tests/CMakeLists.txt:9999 (rocm_check_toolchain_var)
  tests/CMakeLists.txt:5 (SET)


-- Could NOT find LATEX (missing: LATEX_COMPILER)
Latex builder not found. To build PDF documentation run make in /root/ROCm/MIOpenGEMM/doc/pdf, once a latex builder is installed.
-- Configuring done
-- Generating done
-- Build files have been written to: /root/ROCm/MIOpenGEMM/build
root@guest:~/ROCm/MIOpenGEMM/build# make
[100%] Built target miopengemm
root@guest:~/ROCm/MIOpenGEMM/build# make examples
[ 58%] Built target miopengemm
[ 59%] Building CXX object examples/CMakeFiles/gemmbench.dir/gemmbench.cpp.o
In file included from /opt/rocm/opencl/include/CL/cl.h:32:0,
                 from /root/ROCm/MIOpenGEMM/examples/gemmbench.cpp:15:
/opt/rocm/opencl/include/CL/cl_version.h:34:104: note: #pragma message: cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)
 #pragma message("cl_version.h: CL_TARGET_OPENCL_VERSION is not defined. Defaulting to 220 (OpenCL 2.2)")
                                                                                                        ^
/root/ROCm/MIOpenGEMM/examples/gemmbench.cpp: In function 'int main()':
/root/ROCm/MIOpenGEMM/examples/gemmbench.cpp:118:52: error: 'ceil' is not a member of 'std'
       std::min<size_t>(1500, std::max<size_t>(std::ceil(1e11 / (2 * gg.m * gg.k * gg.n)), 2));
                                                    ^~~~
/root/ROCm/MIOpenGEMM/examples/gemmbench.cpp:118:52: note: suggested alternative: 'cerr'
       std::min<size_t>(1500, std::max<size_t>(std::ceil(1e11 / (2 * gg.m * gg.k * gg.n)), 2));
                                                    ^~~~
                                                    cerr
examples/CMakeFiles/gemmbench.dir/build.make:62: recipe for target 'examples/CMakeFiles/gemmbench.dir/gemmbench.cpp.o' failed
make[3]: *** [examples/CMakeFiles/gemmbench.dir/gemmbench.cpp.o] Error 1
CMakeFiles/Makefile2:679: recipe for target 'examples/CMakeFiles/gemmbench.dir/all' failed
make[2]: *** [examples/CMakeFiles/gemmbench.dir/all] Error 2
CMakeFiles/Makefile2:605: recipe for target 'examples/CMakeFiles/examples.dir/rule' failed
make[1]: *** [examples/CMakeFiles/examples.dir/rule] Error 2
Makefile:368: recipe for target 'examples' failed
make: *** [examples] Error 2


---

### 评论 #5 — ROCmSupport (2021-03-24T07:32:58Z)

Thanks @gggh000 
I am able to reproduce the problem.
I will try to help you or else I will reach MIOpen team for further help if needed.
Thank you.

---

### 评论 #6 — ROCmSupport (2021-04-30T09:42:43Z)

Hi @gggh000 
Got an update for you.
Issue is resolved with below steps now, can you please follow the same.

git clone https://github.com/ROCmSoftwarePlatform/MIOpenGEMM -b rocm-4.1.x && cd MIOpenGEMM/
mkdir build && cd build/
cmake ..
make miopengemm
sudo make install

Thank you.

---
