# rocPRIM build failing due to requirement 'hcc' or 'clang' must be compiler

> **Issue #1450**
> **状态**: closed
> **创建时间**: 2021-04-10T08:37:49Z
> **更新时间**: 2021-04-16T10:41:23Z
> **关闭时间**: 2021-04-16T10:41:23Z
> **作者**: gggh000
> **标签**: 
> **URL**: https://github.com/ROCm/ROCm/issues/1450

## 描述

=~=~=~=~=~=~=~=~=~=~=~= MobaXterm log 2021.04.09 22:46:10 =~=~=~=~=~=~=~=~=~=~=~=
na[CXX=hipcc] cmake -DBUILD_BENCHMARK=ON ../.CXX=hipcc;..
root@guest:~/ROCm-4.1/rocPRIM# ehich       which hipcc
/usr/bin/hipcc
root@guest:~/ROCm-4.1/rocPRIM# which hipccCXX=`which hipcc`
root@guest:~/ROCm-4.1/rocPRIM# [CXX=hipcc] cmake -DBUILD_BENCHMARK=ON ../.Xccm
CMake Error: The source directory "/root/ROCm-4.1" does not appear to contain CMakeLists.txt.
Specify --help for usage, or press the help button on the CMake GUI.
root@guest:~/ROCm-4.1/rocPRIM# cd build
root@guest:~/ROCm-4.1/rocPRIM/build# rm -rf ./*
root@guest:~/ROCm-4.1/rocPRIM/build# rm -rf ./*cd buildmake -DBUILD_BENCHMARK=ON ../.
-- The CXX compiler identification is GNU 7.5.0
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Setting build type to 'Release' as none was specified.
CMake Error at cmake/VerifyCompiler.cmake:24 (find_package):
  Could not find a package configuration file provided by "hip" with any of
  the following names:

    hipConfig.cmake
    hip-config.cmake

  Add the installation prefix of "hip" to CMAKE_PREFIX_PATH or set "hip_DIR"
  to a directory containing one of the above files.  If "hip" provides a
  separate development package or SDK, be sure it has been installed.
Call Stack (most recent call first):
  CMakeLists.txt:67 (include)


-- Configuring incomplete, errors occurred!
See also "/root/ROCm-4.1/rocPRIM/build/CMakeFiles/CMakeOutput.log".
root@guest:~/ROCm-4.1/rocPRIM/build# find /opt -name hipConfig.cmake
root@guest:~/ROCm-4.1/rocPRIM/build# find ~/ROCm-4.1/ -name hipConfig.cmake
root@guest:~/ROCm-4.1/rocPRIM/build# find /opt -name HIP
root@guest:~/ROCm-4.1/rocPRIM/build# find /opt -name HIP   hip
/opt/rocm-4.1.0/include/hip
/opt/rocm-4.1.0/hip
/opt/rocm-4.1.0/hip/include/hip
/opt/rocm-4.1.0/hip/lib/cmake/hip
/opt/rocm-4.1.0/lib/cmake/hip
/opt/rocm/hip
root@guest:~/ROCm-4.1/rocPRIM/build# 

---

## 评论 (10 条)

### 评论 #1 — gggh000 (2021-04-11T14:37:00Z)

hip-config exists however apparently it is not finding it /opt/rocm-4.1.0/hip/lib/cmake/hip/hip-config.cmake

---

### 评论 #2 — gggh000 (2021-04-11T15:33:19Z)

I found this is due to disrepancy in path which I corrected and now, I see it is unable to find hipcc compiler and giving off following error:

cmake -DBUILD_BENCHMARK=ON CXX=/opt/rocm/bin/hipcc ../.
-- The CXX compiler identification is GNU 7.5.0
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Setting build type to 'Release' as none was specified.
-- Looking for C++ include pthread.h
-- Looking for C++ include pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
-- ROCclr at /opt/rocm/lib/cmake/rocclr
CMake Error at cmake/VerifyCompiler.cmake:29 (message):
  On ROCm platform 'hcc' or 'clang' must be used as C++ compiler.
Call Stack (most recent call first):
  CMakeLists.txt:67 (include)


-- Configuring incomplete, errors occurred!

I can see it is coming from 
../cmake/VerifyCompiler.cmake in rocPRIM: 

    if(NOT (CMAKE_CXX_COMPILER MATCHES ".*/hcc$" OR CMAKE_CXX_COMPILER MATCHES ".*/hipcc$"))
        message(FATAL_ERROR "On ROCm platform 'hcc' or 'clang' must be used as C++ compiler.")
    elseif(NOT CXX_VERSION_STRING MATCHES "clang")
        list(APPEND CMAKE_PREFIX_PATH /opt/rocm/hcc)
        set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -Wno-unused-command-line-argument")
    endif()

It is unclear why it is giving off this error even thou CXX is set to valid hipcc path and CXX_COMPILER_PATH is still set to c++ according to log.

---

### 评论 #3 — ROCmSupport (2021-04-12T08:10:18Z)

Thanks @gggh000 for reaching out.
Request you to modify the title for calling exact issue.
Request you to share the exact steps to reproduce the problem.
Thank you.

---

### 评论 #4 — ROCmSupport (2021-04-12T09:48:03Z)

Hi @gggh000 
I am not able to reproduce the problem when I followed below steps.

_taccuser@taccuser-X399-DESIGNARE-EX:~$ git clone https://github.com/rocmsoftwareplatform/rocprim -b rocm-4.1.x
Cloning into 'rocprim'...
remote: Enumerating objects: 1133, done.
remote: Counting objects: 100% (1133/1133), done.
remote: Compressing objects: 100% (463/463), done.
remote: Total 10231 (delta 699), reused 980 (delta 587), pack-reused 9098
Receiving objects: 100% (10231/10231), 3.19 MiB | 1.93 MiB/s, done.
Resolving deltas: 100% (7005/7005), done.
taccuser@taccuser-X399-DESIGNARE-EX:~$ cd rocprim/
taccuser@taccuser-X399-DESIGNARE-EX:~/rocprim$ mkdir build
taccuser@taccuser-X399-DESIGNARE-EX:~/rocprim$ cd build/
taccuser@taccuser-X399-DESIGNARE-EX:~/rocprim/build$ **CXX=/opt/rocm/hip/bin/hipcc cmake -DBUILD_BENCHMARK=ON ../.
-- The CXX compiler identification is Clang 12.0.0**
-- Check for working CXX compiler: /opt/rocm/hip/bin/hipcc
-- Check for working CXX compiler: /opt/rocm/hip/bin/hipcc -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Setting build type to 'Release' as none was specified.
-- Looking for C++ include pthread.h
-- Looking for C++ include pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Success
-- Found Threads: TRUE
-- ROCclr at /opt/rocm/lib/cmake/rocclr
-- Performing Test HIP_CLANG_SUPPORTS_PARALLEL_JOBS
-- Performing Test HIP_CLANG_SUPPORTS_PARALLEL_JOBS - Success
-- Found Git: /usr/bin/git (found version "2.25.1")
-- Downloading and building Google Benchmark.
-- Downloading/updating googlebenchmark
-- Configuring done
-- Generating done
-- Build files have been written to: /home/taccuser/rocprim/build/googlebenchmark-download
Scanning dependencies of target googlebenchmark-download
[ 11%] Creating directories for 'googlebenchmark-download'
[ 22%] Performing download step (git clone) for 'googlebenchmark-download'
-- googlebenchmark-download download command succeeded.  See also /home/taccuser/rocprim/build/googlebenchmark-download/googlebenchmark-download-prefix/src/googlebenchmark-download-stamp/googlebenchmark-download-download-*.log
[ 33%] No patch step for 'googlebenchmark-download'
[ 44%] Skipping update step for 'googlebenchmark-download'
[ 55%] Performing configure step for 'googlebenchmark-download'
-- googlebenchmark-download configure command succeeded.  See also /home/taccuser/rocprim/build/googlebenchmark-download/googlebenchmark-download-prefix/src/googlebenchmark-download-stamp/googlebenchmark-download-configure-*.log
[ 66%] Performing build step for 'googlebenchmark-download'
make -j
-- googlebenchmark-download build command succeeded.  See also /home/taccuser/rocprim/build/googlebenchmark-download/googlebenchmark-download-prefix/src/googlebenchmark-download-stamp/googlebenchmark-download-build-*.log
[ 77%] Performing install step for 'googlebenchmark-download'
-- googlebenchmark-download install command succeeded.  See also /home/taccuser/rocprim/build/googlebenchmark-download/googlebenchmark-download-prefix/src/googlebenchmark-download-stamp/googlebenchmark-download-install-*.log
[ 88%] No test step for 'googlebenchmark-download'
[100%] Completed 'googlebenchmark-download'
[100%] Built target googlebenchmark-download
--
-- ******** Summary ********
-- General:
--   System                : Linux
--   HIP ROOT              :
--   C++ compiler          : /opt/rocm/hip/bin/hipcc
--   C++ compiler version  : 12.0.0
--   CXX flags             : -Wno-unused-command-line-argument -Wall -Wextra
--   Build type            : Release
--   Install prefix        : /opt/rocm
--   Device targets        : gfx803;gfx900:xnack-;gfx906:xnack-;gfx908:xnack-
--
--   DISABLE_WERROR        : ON
--   ONLY_INSTALL          : OFF
--   BUILD_TEST            : OFF
--   BUILD_BENCHMARK       : ON
--   BUILD_EXAMPLE         : OFF
-- Configuring done
-- Generating done
-- Build files have been written to: /home/taccuser/rocprim/build
taccuser@taccuser-X399-DESIGNARE-EX:~/rocprim/build$ make -j
Scanning dependencies of target benchmark_device_merge_sort
Scanning dependencies of target benchmark_device_partition
Scanning dependencies of target benchmark_device_select
Scanning dependencies of target benchmark_warp_scan
Scanning dependencies of target benchmark_block_radix_sort
Scanning dependencies of target benchmark_device_merge
Scanning dependencies of target benchmark_block_scan
Scanning dependencies of target benchmark_block_histogram
Scanning dependencies of target benchmark_device_radix_sort
Scanning dependencies of target benchmark_device_binary_search
Scanning dependencies of target benchmark_block_reduce
Scanning dependencies of target benchmark_device_histogram
Scanning dependencies of target benchmark_device_scan
Scanning dependencies of target benchmark_block_exchange
Scanning dependencies of target benchmark_block_sort
Scanning dependencies of target benchmark_device_transform
Scanning dependencies of target benchmark_warp_reduce
Scanning dependencies of target benchmark_device_reduce_by_key
Scanning dependencies of target benchmark_block_discontinuity
Scanning dependencies of target benchmark_device_reduce
Scanning dependencies of target benchmark_device_run_length_encode
Scanning dependencies of target benchmark_warp_sort
Scanning dependencies of target benchmark_device_segmented_reduce
Scanning dependencies of target benchmark_device_segmented_radix_sort
Scanning dependencies of target benchmark_device_memory
[  6%] Building CXX object benchmark/CMakeFiles/benchmark_device_partition.dir/benchmark_device_partition.cpp.o
[  6%] Building CXX object benchmark/CMakeFiles/benchmark_block_radix_sort.dir/benchmark_block_radix_sort.cpp.o
[  6%] Building CXX object benchmark/CMakeFiles/benchmark_warp_scan.dir/benchmark_warp_scan.cpp.o
[  8%] Building CXX object benchmark/CMakeFiles/benchmark_block_histogram.dir/benchmark_block_histogram.cpp.o
[ 10%] Building CXX object benchmark/CMakeFiles/benchmark_device_binary_search.dir/benchmark_device_binary_search.cpp.o
[ 14%] Building CXX object benchmark/CMakeFiles/benchmark_device_merge.dir/benchmark_device_merge.cpp.o
[ 14%] Building CXX object benchmark/CMakeFiles/benchmark_device_histogram.dir/benchmark_device_histogram.cpp.o
[ 16%] Building CXX object benchmark/CMakeFiles/benchmark_block_scan.dir/benchmark_block_scan.cpp.o
[ 18%] Building CXX object benchmark/CMakeFiles/benchmark_device_radix_sort.dir/benchmark_device_radix_sort.cpp.o
[ 20%] Building CXX object benchmark/CMakeFiles/benchmark_device_merge_sort.dir/benchmark_device_merge_sort.cpp.o
[ 22%] Building CXX object benchmark/CMakeFiles/benchmark_block_reduce.dir/benchmark_block_reduce.cpp.o
[ 24%] Building CXX object benchmark/CMakeFiles/benchmark_device_select.dir/benchmark_device_select.cpp.o
[ 26%] Building CXX object benchmark/CMakeFiles/benchmark_device_scan.dir/benchmark_device_scan.cpp.o
[ 30%] Building CXX object benchmark/CMakeFiles/benchmark_block_discontinuity.dir/benchmark_block_discontinuity.cpp.o
[ 30%] Building CXX object benchmark/CMakeFiles/benchmark_device_run_length_encode.dir/benchmark_device_run_length_encode.cpp.o
[ 36%] Building CXX object benchmark/CMakeFiles/benchmark_block_exchange.dir/benchmark_block_exchange.cpp.o
[ 36%] Building CXX object benchmark/CMakeFiles/benchmark_warp_sort.dir/benchmark_warp_sort.cpp.o
[ 36%] Building CXX object benchmark/CMakeFiles/benchmark_device_transform.dir/benchmark_device_transform.cpp.o
[ 46%] Building CXX object benchmark/CMakeFiles/benchmark_device_reduce.dir/benchmark_device_reduce.cpp.o
[ 46%] Building CXX object benchmark/CMakeFiles/benchmark_block_sort.dir/benchmark_block_sort.cpp.o
[ 46%] Building CXX object benchmark/CMakeFiles/benchmark_device_reduce_by_key.dir/benchmark_device_reduce_by_key.cpp.o
[ 46%] Building CXX object benchmark/CMakeFiles/benchmark_device_segmented_reduce.dir/benchmark_device_segmented_reduce.cpp.o
[ 46%] Building CXX object benchmark/CMakeFiles/benchmark_device_segmented_radix_sort.dir/benchmark_device_segmented_radix_sort.cpp.o
[ 48%] Building CXX object benchmark/CMakeFiles/benchmark_warp_reduce.dir/benchmark_warp_reduce.cpp.o
[ 50%] Building CXX object benchmark/CMakeFiles/benchmark_device_memory.dir/benchmark_device_memory.cpp.o
ctest
[ 52%] Linking CXX executable benchmark_device_transform
[ 52%] Built target benchmark_device_transform
[ 54%] Linking CXX executable benchmark_device_binary_search
[ 54%] Built target benchmark_device_binary_search
[ 56%] Linking CXX executable benchmark_device_reduce
[ 56%] Built target benchmark_device_reduce
[ 58%] Linking CXX executable benchmark_device_segmented_reduce
[ 58%] Built target benchmark_device_segmented_reduce
[ 60%] Linking CXX executable benchmark_device_merge
[ 60%] Built target benchmark_device_merge
[ 62%] Linking CXX executable benchmark_warp_sort
[ 62%] Built target benchmark_warp_sort
[ 64%] Linking CXX executable benchmark_warp_reduce
[ 64%] Built target benchmark_warp_reduce
[ 66%] Linking CXX executable benchmark_block_histogram
[ 66%] Built target benchmark_block_histogram
[ 68%] Linking CXX executable benchmark_device_partition
[ 68%] Built target benchmark_device_partition
[ 70%] Linking CXX executable benchmark_warp_scan
[ 70%] Built target benchmark_warp_scan
[ 72%] Linking CXX executable benchmark_device_reduce_by_key
[ 72%] Built target benchmark_device_reduce_by_key
[ 74%] Linking CXX executable benchmark_block_discontinuity
[ 74%] Built target benchmark_block_discontinuity
[ 76%] Linking CXX executable benchmark_device_merge_sort
[ 76%] Built target benchmark_device_merge_sort
[ 78%] Linking CXX executable benchmark_device_histogram
[ 78%] Built target benchmark_device_histogram
[ 80%] Linking CXX executable benchmark_device_select
[ 80%] Built target benchmark_device_select
[ 82%] Linking CXX executable benchmark_device_run_length_encode
[ 82%] Built target benchmark_device_run_length_encode
[ 84%] Linking CXX executable benchmark_block_reduce
[ 84%] Built target benchmark_block_reduce
[ 86%] Linking CXX executable benchmark_device_scan
[ 86%] Built target benchmark_device_scan
[ 88%] Linking CXX executable benchmark_block_exchange
[ 88%] Built target benchmark_block_exchange
[ 90%] Linking CXX executable benchmark_device_segmented_radix_sort
[ 90%] Built target benchmark_device_segmented_radix_sort
[ 92%] Linking CXX executable benchmark_block_sort
[ 92%] Built target benchmark_block_sort
[ 94%] Linking CXX executable benchmark_device_memory
[ 94%] Built target benchmark_device_memory
[ 96%] Linking CXX executable benchmark_device_radix_sort
[ 96%] Built target benchmark_device_radix_sort
[ 98%] Linking CXX executable benchmark_block_radix_sort
[ 98%] Built target benchmark_block_radix_sort
[100%] Linking CXX executable benchmark_block_scan
[100%] Built target benchmark_block_scan
taccuser@taccuser-X399-DESIGNARE-EX:~_

---

### 评论 #5 — gggh000 (2021-04-12T18:28:27Z)

Can you let me know why cmake log printing /usr/bin/c++ as compiler even though i specified compiler to hipcc?
I tried several different ways all same: 

cmake -DBUILD_BENCHMARK=ON DCXX=/opt/rocm/bin/hipcc ../.
cmake -DBUILD_BENCHMARK=ON CXX=/opt/rocm/bin/hipcc ../.
cmake -DBUILD_BENCHMARK=ON DCMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc ../.
cmake -DBUILD_BENCHMARK=ON CMAKE_CXX_COMPILER=/opt/rocm/bin/hipcc ../.

root@guest:~/ROCm-4.1/rocPRIM# cd build
root@guest:~/ROCm-4.1/rocPRIM/build# rm -rf ./*
root@guest:~/ROCm-4.1/rocPRIM/build# !1965^C
root@guest:~/ROCm-4.1/rocPRIM/build# cmake -DBUILD_BENCHMARK=ON DCXX=/opt/rocm/bin/hipcc ../.
-- The CXX compiler identification is GNU 7.5.0
-- Check for working CXX compiler: /usr/bin/c++
-- Check for working CXX compiler: /usr/bin/c++ -- works
-- Detecting CXX compiler ABI info
-- Detecting CXX compiler ABI info - done
-- Detecting CXX compile features
-- Detecting CXX compile features - done
-- Setting build type to 'Release' as none was specified.
-- Looking for C++ include pthread.h
-- Looking for C++ include pthread.h - found
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD
-- Performing Test CMAKE_HAVE_LIBC_PTHREAD - Failed
-- Looking for pthread_create in pthreads
-- Looking for pthread_create in pthreads - not found
-- Looking for pthread_create in pthread
-- Looking for pthread_create in pthread - found
-- Found Threads: TRUE
-- ROCclr at /opt/rocm/lib/cmake/rocclr
CMake Error at cmake/VerifyCompiler.cmake:29 (message):
  On ROCm platform 'hcc' or 'clang' must be used as C++ compiler.
Call Stack (most recent call first):
  CMakeLists.txt:67 (include)


-- Configuring incomplete, errors occurred!
See also "/root/ROCm-4.1/rocPRIM/build/CMakeFiles/CMakeOutput.log".
See also "/root/ROCm-4.1/rocPRIM/build/CMakeFiles/CMakeError.log".
root@guest:~/ROCm-4.1/rocPRIM/build# cmake -DBUILD_BENCHMARK=ON CXX=/opt/rocm/bin/hipcc ../.
-- ROCclr at /opt/rocm/lib/cmake/rocclr
CMake Error at cmake/VerifyCompiler.cmake:29 (message):
  On ROCm platform 'hcc' or 'clang' must be used as C++ compiler.
Call Stack (most recent call first):
  CMakeLists.txt:67 (include)


-- Configuring incomplete, errors occurred!
See also "/root/ROCm-4.1/rocPRIM/build/CMakeFiles/CMakeOutput.log".
See also "/root/ROCm-4.1/rocPRIM/build/CMakeFiles/CMakeError.log".
root@guest:~/ROCm-4.1/rocPRIM/build#

For some other components i.e. rccl it works apparently, no compilation issue...
root@sriov:~/ROCm-4.1/rccl# ./install.sh -idt 
-- The CXX compiler identification is Clang 12.0.0
-- Check for working CXX compiler: /opt/rocm/bin/hipcc
-- Check for working CXX compiler: /opt/rocm/bin/hipcc -- works
...
[ 96%] Building CXX object CMakeFiles/rccl.dir/src/proxy.cc.o
[ 98%] Building CXX object CMakeFiles/rccl.dir/src/enqueue.cc.o
...



---

### 评论 #6 — gggh000 (2021-04-12T18:31:09Z)

On readme.md, it only says following about cxx compiler which does not work when followed:

# ! IMPORTANT !
# Set C++ compiler to HIP-clang. You can do it by adding 'CXX=<path-to-compiler>'
# before 'cmake' or setting cmake option 'CMAKE_CXX_COMPILER' to path to the compiler.
# Using HIP-clang:
[CXX=hipcc] cmake -DBUILD_BENCHMARK=ON ../.


---

### 评论 #7 — gggh000 (2021-04-12T18:32:06Z)

> CXX=/opt/rocm/hip/bin/hipcc cmake -DBUILD_BENCHMARK=ON ../.

I dont see which branch you are using.

---

### 评论 #8 — gggh000 (2021-04-12T18:33:48Z)

OK, following works as posted by you:
CXX=/opt/rocm/hip/bin/hipcc cmake -DBUILD_BENCHMARK=ON ../.

However, the readme.md does not convery this information correctly as mentioned above. 

---

### 评论 #9 — ROCmSupport (2021-04-16T10:41:11Z)

Thanks @gggh000 
You need to use exactly same as "CXX=/opt/rocm/hip/bin/hipcc cmake -DBUILD_BENCHMARK=ON ../.".
Changing the flags before and after do not work.

I followed documentation only. Doc says: [CXX=hipcc] cmake -DBUILD_BENCHMARK=ON ../., which is the same.
I just replaced CXX with full path.

---

### 评论 #10 — ROCmSupport (2021-04-16T10:41:23Z)

Thanks @gggh000  for following the above step exactly and confirming that issue is not reproduced.
Thank you.

---
