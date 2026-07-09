# MIOpenGEMM make examples failing

- **Issue #:** 1403
- **State:** closed
- **Created:** 2021-03-12T07:15:19Z
- **Updated:** 2021-04-30T09:42:43Z
- **URL:** https://github.com/ROCm/ROCm/issues/1403

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